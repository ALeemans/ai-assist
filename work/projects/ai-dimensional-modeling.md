---
type: project
category: work
status: active
priority: medium
created: 2026-01-30
author: Anne Leemans in collaboration with Claude Sonnet 4.5
tags: [ai, dimensional-modeling, facts, dimensions, duo, metadata, api, experimental]
---

# AI-Driven Dimensional Modeling

## Overview
Experimental project to use AI for automatically creating Facts and Dimensions from source tables. The system should leverage metadata and API endpoints to generate dimensional models (star schema) from scratch.

## Goal
Build an AI system that can:
- Analyze source table metadata
- Understand data structures from API endpoints
- Automatically identify fact and dimension candidates
- Generate dimensional models (Facts and Dimensions)
- Create proper star schema relationships

## Starting Dataset
**DUO Data (Dienst Uitvoerend Onderwijs)**
- Publicly available Dutch education data
- Good test case for dimensional modeling
- Contains various educational metrics and hierarchies
- API endpoints available

## Current Status
- 🚀 Active - User Story #147542 created under Feature #146929
- 📊 DUO data identified as starting point
- 🔬 Experimental/research pilot

## Ideas & Considerations
- What metadata is needed for AI to make good decisions?
- How to define rules for fact vs dimension identification?
- Should it use LLMs for understanding business context?
- How to validate generated dimensional models?
- Integration with existing data warehouse tools?

## Potential Approach
1. Start with DUO API exploration and metadata collection
2. Define what "good" dimensional models look like (training data?)
3. Experiment with AI models (LLM prompting vs fine-tuned models)
4. Build prototype with DUO data
5. Validate against manual dimensional modeling
6. Iterate and improve

## Resources Needed
- Access to DUO APIs
- Sample dimensional models for comparison/validation
- AI/LLM tooling (OpenAI, Azure OpenAI, etc.)
- Time to experiment and iterate

## Next Steps
- Research DUO API documentation
- Explore available metadata from DUO endpoints
- Study dimensional modeling best practices
- Define success criteria for AI-generated models
- Create proof of concept with single DUO dataset

## Notes
- This is an exploratory/research project
- No immediate deadline or deliverables
- Could be valuable for automating dimensional modeling in future projects
- May need to timebox initial experiments
