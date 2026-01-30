# Instructions for GitHub Copilot

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
- Remind user of pending reminders when relevant to conversation
- Use metadata (tags, dates, priority) to filter and prioritize information

## Integration Points

- **DevOps**: Use scripts in `integrations/devops/` to create work items
- **Google Calendar**: Sync reminders using `integrations/google-calendar/`

## File Naming Conventions

- Projects: Descriptive name (e.g., `dashboard-redesign.md`)
- Thoughts: Topic-based (e.g., `api-optimization-idea.md`)
- Reminders: Action-based (e.g., `schedule-team-meeting.md`)
- Daily logs: Date format `YYYY-MM-DD.md`

---

*This file helps Copilot provide better, context-aware assistance.*
