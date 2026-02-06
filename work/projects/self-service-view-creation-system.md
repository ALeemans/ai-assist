---
type: project
category: work
status: handed-off
priority: high
created: 2026-02-02
frontend_completed: 2026-02-05
author: Anne Leemans in collaboration with Claude Sonnet 4.5
feature_id: 139126
tags: [sql, metadata, python, query-validation, self-service, view-system, team-enablement, database-governance]
---

# Self-Service Database View Creation System

## Overview
Enable subteams (Finance, HR, Operations, IT, etc.) to create database views in their own schemas without direct database write permissions. This system provides a governed workflow where teams submit views via a repository, which are then validated, metadata-extracted, and deployed by the central Data & Analytics team.

## Context
**Central Team**: Data & Analytics (my team)
**Subteams**: Finance, HR, Operations, IT, etc. - each has their own database schema
**Current Capability**: Subteams only build Power BI semantic models and reports
**New Capability**: Subteams can create database views following a governed process

## Goal
Build a complete self-service workflow that:
- Empowers subteams to create views in their own schemas without database write permissions
- Validates SQL format for consistency and security
- Extracts and stores metadata from validated queries
- Automates the approval and deployment process
- Provides guardrails through formatting rules and AI-assisted documentation
- Maintains data governance and quality standards

## Feature Information
- **Feature ID**: 139126
- **Teams Involved**: Multiple teams submitting queries
- **Output**: SQL views with column metadata

## User Stories

### Completed ✅
- [x] User Story #145934: Python script voor het uitlezen van metadata uit SQL queries
- [x] User Story #145935: SQL query format validatie
  - SQL validator script completed (validates UNION, JOIN, WITH, comments)
  - Metadata extractor script completed (exports to CSV with semicolon separator)
  - Scripts tested and ready for production

**Completed Links:**
- [User Story #145934](https://dev.azure.com/HogeschoolUtrecht/8b224685-8bd1-4a9a-9650-c62d60c23e77/_workitems/edit/145934) - Metadata extractie
- [User Story #145935](https://dev.azure.com/HogeschoolUtrecht/8b224685-8bd1-4a9a-9650-c62d60c23e77/_workitems/edit/145935) - Query validatie ✅ DONE

### In Progress 🚧
- [ ] User Story #146271: Testen en documenteren SQL validator, metadata extractor en AI instructies
  - Test SQL validator with diverse test cases
  - Test metadata extractor with different view types
  - Validate AI instructions
  - Create user documentation

### Planned 📋
- [ ] User Story #146224: Proces documentatie en testen view-systeem met Dummy Verplichting
  - Document complete process from receipt to deployment
  - Test with views from 'Dummy_Verplichting_tbv_viewsysteem' repo
  - Create step-by-step guide for teams

**Active Links:**
- [User Story #146271](https://dev.azure.com/HogeschoolUtrecht/8b224685-8bd1-4a9a-9650-c62d60c23e77/_workitems/edit/146271) - Testing en documentatie (Doing)
- [User Story #146224](https://dev.azure.com/HogeschoolUtrecht/8b224685-8bd1-4a9a-9650-c62d60c23e77/_workitems/edit/146224) - Proces documentatie (Te Refinen)

## Deliverables

### Tools Developed
1. **sql_validator.py** - Validates SQL format
   - Checks for forbidden operations (UNION, JOIN, WITH)
   - Validates required comments
   - Exports validation results

2. **extract_metadata.py** - Extracts metadata
   - Column mappings (source → target)
   - CASE WHEN calculations
   - WHERE clause conditions
   - Exports to CSV (semicolon separated)

3. **SQL_BUILDER_INSTRUCTIONS.md** - AI instructions
   - Format rules for builders
   - Validation guidelines for AI
   - Examples and error handling

## Workflow
1. **Subteam writes view** - Team analyst creates SQL view definition
2. **Submit via repository** - Team pushes view to their repo
3. **Automated validation** - sql_validator.py checks format compliance
4. **Metadata extraction** - extract_metadata.py pulls column mappings and logic
5. **Metadata storage** - Metadata saved to central metadata database
6. **Review & approval** - Data & Analytics team reviews
7. **Deployment** - View is executed/created in team's schema

## My Role
- **Design & Pilot**: Create outline and small pilot implementation
- **Knowledge Transfer**: Backend team will implement full solution
- **Current Stage**: Testing phase (validation, extraction, and AI instructions complete)

## Current Progress
✅ **Completed Components:**
- SQL validation (format rules, forbidden operations)
- Metadata extraction (column mappings, calculations)
- AI instruction documentation for subteams

🧪 **Testing Phase:**
- Testing SQL validator with diverse test cases
- Testing metadata extractor with different view types
- Validating AI instructions effectiveness

📋 **Next Steps:**
- Complete testing and create user documentation
- Process documentation with Dummy Verplichting test cases
- Hand off to backend team for full implementation

## Notes
- Feature ID updated from 139126 to 145908
- Scripts use semicolon separator for CSV (Excel compatibility)
- Calculated columns marked as "(CALCULATED_COLUMN)" in source_column
- WHERE clauses include full statement with keyword
- Each team operates in isolated database schemas (finance, HR, operations, IT, etc.)
