# Google Calendar Integration

Scripts to sync reminders with Google Calendar.

## Setup

1. Install required packages:
   ```powershell
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

2. Set up Google Calendar API credentials:
   - Go to https://console.cloud.google.com/
   - Create a project and enable Google Calendar API
   - Download credentials.json and place in this folder

3. Run initial authentication:
   ```powershell
   python sync-reminders.py --auth
   ```

## Usage

```powershell
# Sync all pending reminders to Google Calendar
python sync-reminders.py

# Sync specific category only
python sync-reminders.py --category work
```

## Features

- Creates calendar events from reminder files
- Uses due dates from frontmatter
- Sets reminders based on priority
- Two-way sync (optional)
