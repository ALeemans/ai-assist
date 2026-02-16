# Microsoft 365 Copilot Integration

This folder contains tools for connecting to Microsoft 365 Copilot APIs.

## Diagnostic Script

The `diagnostic_copilot_access.py` script checks if you have access to Microsoft 365 Copilot APIs.

### How to Run

1. **Install dependencies**:
   ```powershell
   & D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe -m pip install -r integrations/m365-copilot/requirements.txt
   ```

2. **Run the diagnostic**:
   ```powershell
   & D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe integrations/m365-copilot/diagnostic_copilot_access.py
   ```

3. **What happens**:
   - A browser window will open for you to log in with your Hogeschool Utrecht credentials
   - The script will test connectivity to various Microsoft 365 Copilot endpoints
   - It will generate a report showing what's available

### Expected Outcomes

- ✅ **All green**: Microsoft 365 Copilot Chat API is available
- ⚠️ **Some warnings**: Limited access, may need IT approval
- ❌ **All red**: Copilot not available yet, need alternative solution

### Next Steps Based on Results

**If Copilot Chat API is available**:
- We can build an automated Python script to analyze NSE responses
- Script will authenticate with your Entra ID token
- Call Copilot API to process answers in batches

**If APIs are not available**:
- Check if Azure OpenAI is deployed in your tenant
- Contact IT to enable Microsoft 365 Copilot APIs
