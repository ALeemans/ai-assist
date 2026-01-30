import requests
import argparse
import yaml
from pathlib import Path
from azure.identity import DefaultAzureCredential

# Load configuration
def load_config():
    """Load configuration from config.yaml"""
    config_path = Path(__file__).parent / "config.yaml"
    if not config_path.exists():
        print("⚠️  config.yaml not found. Using hardcoded defaults.")
        return None
    
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

# Get authentication token
print("🔐 Authenticating with Azure DevOps...")
credential = DefaultAzureCredential()
token = credential.get_token("499b84ac-1321-427f-aa17-267ca6975798/.default")
print("✅ Authentication successful!\n")

### CREATE NEW USER STORY
def create_user_story(title, description, organization, project, api_version, 
                      feature_id, iteration_path, tag, state, assigned_to):
        """Create a user story in Azure DevOps with specified properties"""
        
        url = f"{organization}/{project}/_apis/wit/workitems/$Product Backlog Item?api-version={api_version}"
        
        # Build the patch document according to JSON Patch specification
        data = [
            {"op": "add", "path": "/fields/System.Title", "value": title},
            {"op": "add", "path": "/fields/System.Description", "vastate},
            {"op": "add", "path": "/fields/System.IterationPath", "value": iteration_path},
            {"op": "add", "path": "/fields/System.Tags", "value": tag},
            {"op": "add", "path": "/fields/System.AssignedTo", "value": assigned_to},
        ]
        
        # Add parent link to Feature
        if feature_id:
            parent_url = f"{organization}/_apis/wit/workItems/{feature_id
            parent_url = f"{ORGANIZATION}/_apis/wit/workItems/{FEATURE_ID}"
            data.append({
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": parent_url
                }
            })
        
        response = requests.post(url, headers=HEADERS, json=data)


        
        if response.status_code in [200, 201]:
            work_item = response.json()
            print(f"✅ Successfully created User Story: {title}")
            print(f"🔹 Work Item ID: {work_item['id']}")
            print(f"🔹 URL: {work_item['_links']['html']['href']}")
            print(f"🔹 State: {state}")
            print(f"🔹 Iteration: {iteration_path}")
            print(f"🔹 Tag: {tag}")
            if feature_id:
                print(f"🔹 Linked to Feature: {feature_id}")
            return work_item
        else:
            error_msg = f"Error creating User Story.\nStatus Code: {response.status_code}\nResponse: {response.text}"
            print(f"❌ {error_msg}")
            return None

# Headers
HEADERS = {
    "Content-Type": "application/json-patch+json",
    "Authorization": f"Bearer {token.token}"
}

# Main execution
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Create Azure DevOps User Story",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (prompts for title and description)
  python create_user_story.py
  
  # Provide title and description via arguments
  python create_user_story.py --title "Fix login bug" --description "Users can't login with email"
  
  # Override specific config values
  python create_user_story.py --feature 12345 --tag "BugFix" --priority high
  
  # Assign to different person
  python create_user_story.py --assigned-to "John Doe" --title "New feature"
        """
    )
    
    # Work item content
    parser.add_argument('--title', '-t', help='Title of the user story')
    parser.add_argument('--description', '-d', help='Description of the user story')
    
    # Configuration overrides
    parser.add_argument('--feature', type=int, help='Feature ID to link to (overrides config)')
    parser.add_argument('--iteration', help='Iteration path (overrides config)')
    parser.add_argument('--tag', help='Tag for the work item (overrides config)')
    parser.add_argument('--state', help='Initial state (overrides config)')
    parser.add_argument('--assigned-to', help='Person to assign to (overrides config)')
    parser.add_argument('--project', help='Project name (overrides config)')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config()
    
    # Set defaults from config or fallback to hardcoded values
    if config:
        organization = config['devops']['organization']
        project = args.project or config['devops']['project']
        api_version = config['devops']['api_version']
        feature_id = args.feature if args.feature is not None else config['defaults']['feature_id']
        iteration_path = args.iteration or config['defaults']['iteration_path']
        tag = args.tag or config['defaults']['tag']
        state = args.state or config['defaults']['state']
        assigned_to = args.assigned_to or config['defaults']['assigned_to']
    else:
        # Fallback to hardcoded defaults if no config file
        organization = "https://dev.azure.com/HogeschoolUtrecht"
        project = args.project or "DevOps DenA"
        api_version = "7.1"
        feature_id = args.feature if args.feature is not None else 130948
        iteration_path = args.iteration or "DevOps DenA\\Data Analytics"
        tag = args.tag or "ME"
        state = args.state or "Domeinteam Verzoek To Do"
        assigned_to = args.assigned_to or "Anne Leemans"
    
    print("📋 Azure DevOps User Story Creator")
    print(f"   Organization: {organization}")
    print(f"   Project: {project}")
    print(f"   Feature ID: {feature_id or 'None (no parent)'}")
    print(f"   Iteration: {iteration_path}")
    print(f"   State: {state}")
    print(f"   Tag: {tag}")
    print(f"   Assigned To: {assigned_to}\n")
    
    try:
        # Get title and description (from args or interactive input)
        title = args.title
        description = args.description
        
        if not title:
            title = input("Enter the title of the user story: ")
        if not description:
            description = input("Enter the description of the user story: ")
        
        if title and description:
            # Create the user story
            work_item = create_user_story(
                title, description, organization, project, api_version,
                feature_id, iteration_path, tag, state, assigned_to
            )
            if work_item:
                print(f"\n✅ User Story created successfully!")
        else:   
            print("❌ User Story creation cancelled - title and description are required.")
            
    except Exception as e:
        error_msg = f"Error creating User Story: {str(e)}"
        print(f"❌ {error_msg}")
