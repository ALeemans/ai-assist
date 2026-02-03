---
type: project
category: work
status: active
priority: high
created: 2026-02-02
feature_id: 145908
tags: [sql, metadata, python, query-validation, column-mapping, view-system]
---

# SQL Metadata Extraction & Query Validation

## Overview
Create a Python-based solution to extract metadata from SQL queries and validate query format. Multiple teams will send queries that need to be converted to views, and we need to extract column mapping metadata consistently.

## Goal
Build a system that:
- Validates SQL query format for consistency
- Extracts metadata (column mappings) from validated SQL queries
- Enables teams to submit queries that automatically generate views with proper metadata
- Document and test the complete process from receipt to deployment

## Feature Information
- **Feature ID**: 145908
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

## Process Flow
1. Teams submit SQL queries
2. Validate format using sql_validator.py
3. Extract metadata using extract_metadata.py
4. Review and approve
5. Deploy views to database
6. Document in metadata repository

## Notes
- Feature ID updated from 139126 to 145908
- Scripts use semicolon separator for CSV (Excel compatibility)
- Calculated columns marked as "(CALCULATED_COLUMN)" in source_column
- WHERE clauses include full statement with keyword
