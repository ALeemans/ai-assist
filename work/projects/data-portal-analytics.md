---
type: project
category: work
status: planned
priority: medium
created: 2026-01-30
author: Anne Leemans in collaboration with Claude Sonnet 4.5
tags: [ckan, data-portal, google-analytics, analytics, usage-tracking, hu]
feature_id: 142557
feature_url: https://dev.azure.com/HogeschoolUtrecht/DevOps%20DenA/_boards/board/t/Team%20Data%20Analytics/Backlog%20items?workitem=142557
---

# Data Portal Usage Analytics (CKAN + Google Analytics)

## Overview
Implement usage tracking and analytics for the HU Data Portal (built on CKAN) using Google Analytics. This will provide insights into how the portal is being used, which datasets are popular, user behavior patterns, and overall portal effectiveness.

## Current Status
- 📋 Planning phase - preparing email to CKAN beheerders
- 🎯 Goal: Set up Google Analytics for CKAN data portal
- 📊 No existing analytics implementation
- 🔰 Team has no prior Google Analytics experience
- ✉️ Email draft created (2026-02-16) - ready to send to beheerders

## Goals
- Track portal usage metrics (visits, users, sessions)
- Understand which datasets are most accessed
- Analyze user navigation patterns
- Identify popular search terms
- Monitor user engagement and retention
- Track data downloads and API usage

## Technology Stack
- **Platform**: CKAN (data portal software)
- **Analytics Tool**: Google Analytics (GA4)
- **Integration**: Need to research CKAN + GA integration methods

## Key Questions to Answer
1. How to integrate Google Analytics with CKAN?
2. What events/metrics should we track?
3. How to set up custom tracking for dataset views/downloads?
4. What dashboards/reports are most useful for data portal analytics?
5. Privacy considerations (GDPR compliance)?

## Research Needed
- [x] Google Analytics setup basics (GA4) - researched 2026-02-16
- [x] CKAN documentation on analytics integration - researched 2026-02-16
- [ ] Best practices for data portal analytics
- [x] Custom event tracking for CKAN actions - covered by ckanext-googleanalytics plugin
- [ ] Privacy/GDPR requirements for analytics
- [ ] Alternative analytics tools (comparison)

## Key Findings (2026-02-16)
- **Official Plugin:** `ckanext-googleanalytics` is the standard CKAN extension for GA integration
- **Setup Requirements:**
  - Plugin installation on CKAN server
  - Configuration in development.ini/production.ini
  - Google Cloud Service Account with JSON credentials
  - GA4 property with Read access for service account
- **Features:**
  - Automatic tracking code insertion
  - Event tracking for downloads, API calls, dataset views
  - Statistics stored in CKAN database
  - GDPR compliance options

## Implementation Steps (Draft)
1. **Learn Google Analytics basics**
   - Create Google Analytics account/property
   - Understand GA4 vs Universal Analytics
   - Learn about events, dimensions, and metrics
   
2. **Plan tracking strategy**
   - Define what to track (page views, downloads, searches, etc.)
   - Design custom events for CKAN-specific actions
   - Plan data structure and reporting needs
   
3. **Technical integration**
   - Add GA tracking code to CKAN
   - Implement custom event tracking
   - Test tracking implementation
   
4. **Configure dashboards**
   - Set up useful reports in GA
   - Create custom dashboards for stakeholders
   - Schedule automated reports
   
5. **Validate and optimize**
   - Verify data accuracy
   - Refine tracking based on insights
   - Train team on using analytics

## Resources Needed
- Google Analytics account (GA4)
- Access to CKAN portal code/configuration
- Time for learning and experimentation
- Possibly: CKAN plugins for analytics integration

## Success Criteria
- Google Analytics successfully integrated with CKAN portal
- Key metrics being tracked (views, downloads, searches, users)
- Dashboards provide actionable insights
- Team can interpret and use analytics data
- Privacy compliance verified

## Notes
- Feature ID: 142557
- Team: Data Analytics
- Starting from scratch - learning opportunity
- Consider documenting process for future reference

## Action Items
- [ ] Review and send email to CKAN beheerders (draft in temp/email-draft-ckan-google-analytics.md)
- [ ] Create Google Cloud Service Account and credentials JSON
- [ ] Set up GA4 property for dataportal
- [ ] Coordinate with beheerders on plugin installation timeline
- [ ] Plan testing session after installation

## Email Draft Location
`temp/email-draft-ckan-google-analytics.md` (created 2026-02-16)
