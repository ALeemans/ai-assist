---
applyTo: '**'
---
# Instructions for GitHub Copilot ai Assist Repository

## Purpose of This Repository

This repository serves as a personal knowledge base and task management system. When the user asks questions or needs help, use the content here as context to provide personalized assistance.

## How to Use This Context

1. **Check daily-logs** for recent activities and current focus
2. **Review work/projects** and **private/projects** for active projects
3. **Check reminders** to understand priorities and deadlines
4. **Reference thoughts** for past ideas that might be relevant

## Key Behaviors

- When user mentions a project, search `work/projects/` or `private/projects/` for context
- Suggest moving items from `inbox/` to proper folders when appropriate
- Help create user stories in DevOps based on project notes
- **Link projects to DevOps features** - When a project has an associated DevOps feature, always add the feature number and/or link to the project markdown file in the frontmatter (using `feature_id` and `feature_url` fields)
- Remind user of pending reminders when relevant to conversation
- Use metadata (tags, dates, priority) to filter and prioritize information
- **Always ask to clean up redundant files after completing functionality** - This repo involves testing and can get cluttered. After finishing any new feature or integration, proactively ask the user if they want to remove test files, unused scripts, or obsolete documentation
- **Always use virtual environment for Python scripts** - Before running any Python script, ALWAYS use the virtual environment Python interpreter: `& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe <script-path>`
- **Automatically sync reminders to Google Calendar** - When creating reminder files in `private/reminders/` or `work/reminders/`, ALWAYS automatically run the sync script immediately after creation using: `& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe D:/HogeschoolUtrecht/GithubRepos/ai-assist/integrations/google-calendar/sync-reminders-to-calendar.py`
- **Schedule work reminders on weekdays only** - When creating work reminders, ensure the due date falls on a weekday (Monday-Friday). If a date falls on a weekend, move it to the next Monday
- **Archive completed reminders** - When a reminder is completed, change its status to `status: completed` and run `& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe D:/HogeschoolUtrecht/GithubRepos/ai-assist/integrations/reminders/archive_completed.py` to automatically move it to the archive folder. This keeps active reminder folders clean while preserving history. 

## Integration Points

- **DevOps**: Use scripts in `integrations/devops/` to create work items
  - **IMPORTANT**: All DevOps user stories MUST be written in Dutch
  - **REQUIRED**: Always include acceptance criteria (Acceptatiecriteria) for every user story
  - Use the `--acceptance-criteria` argument when creating user stories
- **Google Calendar**: Sync reminders using `integrations/google-calendar/`

## File Naming Conventions

- Projects: Descriptive name (e.g., `dashboard-redesign.md`)
- Thoughts: Topic-based (e.g., `api-optimization-idea.md`)
- Reminders: Action-based (e.g., `schedule-team-meeting.md`)
- Daily logs: Date format `YYYY-MM-DD.md`

---

*This file helps Copilot provide better, context-aware assistance.*
