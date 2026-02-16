#!/usr/bin/env python3
"""
Author: Anne Leemans in collaboration with GitHub Copilot

Diagnostic script to check Microsoft 365 Copilot API access availability.
Tests authentication and connectivity to various Microsoft 365 Copilot endpoints.
"""

import sys
import json
from azure.identity import InteractiveBrowserCredential
from azure.core.exceptions import ClientAuthenticationError
import requests

# Configuration
TENANT_ID = "98932909-9a5a-4d18-ace4-7236b5b5e11d"
GRAPH_SCOPE = "https://graph.microsoft.com/.default"
GRAPH_ENDPOINT = "https://graph.microsoft.com/v1.0"

def authenticate():
    """Authenticate using Entra ID with interactive browser login."""
    print("🔐 Authenticating with Azure Entra ID...")
    print(f"   Tenant ID: {TENANT_ID}")
    print("   A browser window will open for you to log in.\n")
    
    try:
        credential = InteractiveBrowserCredential(tenant_id=TENANT_ID)
        token = credential.get_token(GRAPH_SCOPE)
        print("✅ Authentication successful!\n")
        return token.token
    except ClientAuthenticationError as e:
        print(f"❌ Authentication failed: {str(e)}\n")
        return None

def test_graph_api(token):
    """Test basic Microsoft Graph API access."""
    print("📊 Testing Microsoft Graph API access...")
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{GRAPH_ENDPOINT}/me", headers=headers, timeout=10)
        if response.status_code == 200:
            user_data = response.json()
            print(f"✅ Graph API: SUCCESS")
            print(f"   User: {user_data.get('displayName', 'Unknown')}")
            print(f"   Email: {user_data.get('mail', 'Unknown')}\n")
            return True
        else:
            print(f"❌ Graph API: FAILED ({response.status_code})")
            print(f"   {response.text}\n")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Graph API: ERROR - {str(e)}\n")
        return False

def test_copilot_endpoints(token):
    """Test potential Microsoft 365 Copilot API endpoints."""
    print("🤖 Testing Microsoft 365 Copilot endpoints...\n")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    endpoints = [
        # Microsoft Copilot endpoints
        ("Copilot Chat API", "https://api.copilot.microsoft.com/v1/chat/completions"),
        ("Graph Copilot", f"{GRAPH_ENDPOINT}/me/copilot"),
        ("Semantic Search", f"{GRAPH_ENDPOINT}/me/semanticSearch"),
        ("AI Services Chat", "https://api.microsoft.com/v1/openai/chat/completions"),
    ]
    
    results = {}
    for name, endpoint in endpoints:
        try:
            response = requests.head(endpoint, headers=headers, timeout=10)
            # HEAD request might return 405, but if we can reach it, it's available
            if response.status_code in [200, 204, 405]:
                print(f"✅ {name}: REACHABLE (HTTP {response.status_code})")
                results[name] = "reachable"
            elif response.status_code == 401:
                print(f"⚠️  {name}: UNAUTHORIZED (might need special permissions)")
                results[name] = "unauthorized"
            elif response.status_code == 404:
                print(f"❌ {name}: NOT FOUND")
                results[name] = "not_found"
            else:
                print(f"⚠️  {name}: HTTP {response.status_code}")
                results[name] = f"http_{response.status_code}"
        except requests.exceptions.RequestException as e:
            if "certificate_verify_failed" in str(e):
                print(f"⚠️  {name}: SSL ERROR (check corporate firewall/proxy)")
                results[name] = "ssl_error"
            else:
                print(f"❌ {name}: UNREACHABLE ({str(e)})")
                results[name] = "unreachable"
    
    print()
    return results

def check_organization_settings(token):
    """Check organization settings for Copilot enablement."""
    print("🏢 Checking organization settings...\n")
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        # Check tenant details
        response = requests.get(
            f"{GRAPH_ENDPOINT}/organization",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            org_data = response.json()
            if org_data.get('value'):
                org = org_data['value'][0]
                print(f"✅ Organization: {org.get('displayName', 'Unknown')}")
                print(f"   ID: {org.get('id', 'Unknown')}\n")
    except Exception as e:
        print(f"⚠️  Could not retrieve org settings: {str(e)}\n")

def generate_report(auth_success, graph_success, copilot_results):
    """Generate final diagnostic report."""
    print("=" * 60)
    print("📋 DIAGNOSTIC REPORT")
    print("=" * 60 + "\n")
    
    print("Authentication: ✅" if auth_success else "Authentication: ❌")
    print("Microsoft Graph API: ✅" if graph_success else "Microsoft Graph API: ❌")
    
    print("\nCopilot Endpoints:")
    for endpoint, status in copilot_results.items():
        icon = "✅" if status == "reachable" else "⚠️ " if status in ["unauthorized", "ssl_error"] else "❌"
        print(f"  {icon} {endpoint}: {status}")
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    
    reachable_endpoints = [k for k, v in copilot_results.items() if v == "reachable"]
    
    if not auth_success:
        print("❌ Authentication failed. Contact your IT department to verify:")
        print("   - Your Entra ID account is active")
        print("   - Your tenant ID is correct")
        return
    
    if not graph_success:
        print("❌ Microsoft Graph API access denied. Contact your IT to verify permissions.")
        return
    
    if not reachable_endpoints:
        print("⚠️  No Copilot endpoints are directly accessible.")
        print("\nRecommended alternatives:")
        print("   1. Check if GitHub Copilot Chat API is available in your GitHub settings")
        print("   2. Check if Azure OpenAI is deployed in your organization")
        print("   3. Contact IT to enable Microsoft 365 Copilot for your tenant")
        return
    
    if "Copilot Chat API" in reachable_endpoints:
        print("✅ Microsoft 365 Copilot Chat API is available!")
        print("\n   You can build a Python script to:")
        print("   - Authenticate with your Entra ID token")
        print("   - Call the Copilot Chat API directly")
        print("   - Analyze NSE responses automatically")
        return
    
    print("\n⚠️  Limited Copilot endpoint access detected.")
    print("Contact your IT department to:")
    print("   - Enable Microsoft 365 Copilot Chat API")
    print("   - Verify your account permissions")

def main():
    """Main diagnostic flow."""
    print("\n" + "=" * 60)
    print("Microsoft 365 Copilot Access Diagnostics")
    print("=" * 60 + "\n")
    
    # Authenticate
    token = authenticate()
    if not token:
        print("❌ Cannot proceed without authentication.")
        sys.exit(1)
    
    # Test Graph API
    graph_success = test_graph_api(token)
    
    # Check org settings
    check_organization_settings(token)
    
    # Test Copilot endpoints
    copilot_results = test_copilot_endpoints(token)
    
    # Generate report
    generate_report(token is not None, graph_success, copilot_results)
    
    print("\n")

if __name__ == "__main__":
    main()
