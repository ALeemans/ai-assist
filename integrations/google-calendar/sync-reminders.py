"""
Google Calendar Sync for AI-Assist Reminders

This script syncs reminder files with Google Calendar.
Reads YAML frontmatter from reminder markdown files and creates calendar events.
"""

import os
import yaml
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Google Calendar API imports (install: pip install google-auth google-auth-oauthlib google-api-python-client)
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False
    print("⚠️  Google Calendar libraries not installed. Run: pip install google-auth google-auth-oauthlib google-api-python-client")

# If modifying scopes, delete token.json
SCOPES = ['https://www.googleapis.com/auth/calendar']

def parse_reminder_file(file_path):
    """Parse a reminder markdown file and extract frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return frontmatter, body
    
    return None, content

def get_reminders(category=None):
    """Get all reminder files from work and/or private folders."""
    repo_root = Path(__file__).parent.parent.parent
    reminders = []
    
    categories = ['work', 'private'] if category is None else [category]
    
    for cat in categories:
        reminder_dir = repo_root / cat / 'reminders'
        if reminder_dir.exists():
            for file_path in reminder_dir.glob('*.md'):
                if file_path.name == 'README.md':
                    continue
                frontmatter, body = parse_reminder_file(file_path)
                if frontmatter and frontmatter.get('status') == 'pending':
                    reminders.append({
                        'path': file_path,
                        'frontmatter': frontmatter,
                        'body': body,
                        'category': cat
                    })
    
    return reminders

def authenticate_google():
    """Authenticate with Google Calendar API."""
    if not GOOGLE_AVAILABLE:
        return None
    
    creds = None
    token_path = Path(__file__).parent / 'token.json'
    credentials_path = Path(__file__).parent / 'credentials.json'
    
    # Load existing credentials
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    
    # Refresh or get new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not credentials_path.exists():
                print("❌ credentials.json not found. Please download from Google Cloud Console.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    return build('calendar', 'v3', credentials=creds)

def create_calendar_event(service, reminder):
    """Create a Google Calendar event from a reminder."""
    frontmatter = reminder['frontmatter']
    
    # Prepare event
    event = {
        'summary': frontmatter.get('type', 'Reminder') + ': ' + reminder['path'].stem.replace('-', ' ').title(),
        'description': reminder['body'][:500],  # First 500 chars
        'start': {
            'date': frontmatter.get('due', datetime.now().strftime('%Y-%m-%d')),
        },
        'end': {
            'date': frontmatter.get('due', datetime.now().strftime('%Y-%m-%d')),
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': get_reminder_minutes(frontmatter.get('priority', 'medium'))},
            ],
        },
    }
    
    # Create event
    event = service.events().insert(calendarId='primary', body=event).execute()
    return event

def get_reminder_minutes(priority):
    """Get reminder minutes before event based on priority."""
    priority_map = {
        'critical': 24 * 60,  # 1 day
        'high': 12 * 60,      # 12 hours
        'medium': 3 * 60,      # 3 hours
        'low': 60              # 1 hour
    }
    return priority_map.get(priority, 3 * 60)

def main():
    parser = argparse.ArgumentParser(description='Sync AI-Assist reminders to Google Calendar')
    parser.add_argument('--category', choices=['work', 'private'], help='Sync only specific category')
    parser.add_argument('--auth', action='store_true', help='Run authentication only')
    args = parser.parse_args()
    
    print("📅 AI-Assist Google Calendar Sync\n")
    
    # Authenticate
    service = authenticate_google()
    if not service:
        print("❌ Authentication failed.")
        return
    
    if args.auth:
        print("✅ Authentication successful! You can now sync reminders.")
        return
    
    # Get reminders
    reminders = get_reminders(args.category)
    print(f"📋 Found {len(reminders)} pending reminder(s)\n")
    
    # Sync each reminder
    for reminder in reminders:
        try:
            event = create_calendar_event(service, reminder)
            print(f"✅ Created: {reminder['path'].name}")
            print(f"   Link: {event.get('htmlLink')}\n")
        except Exception as e:
            print(f"❌ Failed: {reminder['path'].name}")
            print(f"   Error: {str(e)}\n")

if __name__ == '__main__':
    main()
