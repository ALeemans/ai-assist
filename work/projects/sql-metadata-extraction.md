---
type: project
category: work
status: active
priority: high
created: 2026-02-02
feature_id: 139126
tags: [sql, metadata, python, query-validation, column-mapping]
---

# SQL Metadata Extraction & Query Validation

## Overview
Create a Python-based solution to extract metadata from SQL queries and validate query format. Multiple teams will send queries that need to be converted to views, and we need to extract column mapping metadata consistently.

## Goal
Build a system that:
- Validates SQL query format for consistency
- Extracts metadata (column mappings) from validated SQL queries
- Enables teams to submit queries that automatically generate views with proper metadata

## Feature Information
- **Feature ID**: 139126
- **Teams Involved**: Multiple teams submitting queries
- **Output**: SQL views with column metadata

## User Stories Created
- [x] User Story #145934: Python script voor het uitlezen van metadata uit SQL queries
- [x] User Story #145935: SQL query format validatie

**Links:**
- [User Story #145934](https://dev.azure.com/HogeschoolUtrecht/8b224685-8bd1-4a9a-9650-c62d60c23e77/_workitems/edit/145934) - Metadata extractie
- [User Story #145935](https://dev.azure.com/HogeschoolUtrecht/8b224685-8bd1-4a9a-9650-c62d60c23e77/_workitems/edit/145935) - Query validatie

## Notes
Teams submit SQL queries → System validates format → Extract metadata → Create view with column mapping

## Next Steps
- Define exact SQL query format requirements
- Determine what metadata fields are needed
- Build validation rules
- Implement extraction logic
