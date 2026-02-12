---
type: reminder
category: work
status: completed
priority: medium
created: 2026-01-30
due: 2026-02-10
tags: [integration, power-automate, email, teams, automation]
---

# Setup Power Automate Integration

## 📌 What

Set up Power Automate flows to integrate Microsoft Outlook and Teams with ai-assist project.

## ❓ Why

Enable automated capture of work tasks from email and Teams while staying within Microsoft's security boundaries (IT department approval friendly).

## ✅ Completion Criteria

- [ ] Create Power Automate flow for flagged/important emails
  - Watch for flagged emails in Outlook
  - Export to OneDrive/SharePoint folder as structured data
  - Script reads from that folder to create inbox items
- [ ] Create Power Automate flow for Teams messages
  - Capture starred/bookmarked messages
  - Extract action items from specific channels
  - Save to shared location
- [ ] Draft security justification document for IT approval
  - Emphasize: stays within Microsoft ecosystem
  - Read-only access to emails
  - No external API calls
  - Data never leaves tenant
- [ ] Test flows with sample data
- [ ] Document setup process in integrations/power-automate/

## 📝 Notes

**Security-friendly approach:**
- All processing stays within Microsoft tenant
- No external APIs or third-party services
- Only reads data, never sends
- Data export to controlled OneDrive location
- Python script only reads from OneDrive locally

**Potential flows:**
1. Flagged Email → JSON to OneDrive → Create inbox item
2. Teams bookmark → Text file to OneDrive → Create thought/note
3. Meeting recordings → Transcription (if allowed) → Meeting notes

**IT Approval Strategy:**
- Frame as "productivity automation within existing tools"
- Show it reduces manual copy-pasting
- Emphasize no data leaves Microsoft ecosystem
- Offer to demo in test environment first

## 🔗 Related

- `integrations/` folder (new subfolder needed)
- Similar pattern to google-calendar and devops integrations
