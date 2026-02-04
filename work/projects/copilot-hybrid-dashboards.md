---
type: project
category: work
status: planning
priority: high
created: 2026-02-04
author: Anne Leemans in samenwerking met Claude Sonnet 4.5
feature_id: 142267
feature_url: https://dev.azure.com/HogeschoolUtrecht/DevOps%20DenA/_boards/board/t/Team%20Data%20Analytics/Backlog%20items?workitem=142267
tags: [copilot, ai, dashboards, hybrid, filtering, prompts, user-stories]
---

# Copilot Hybrid Dashboards

## Overzicht
Hybride aanpak voor het beschikbaar stellen van Copilot-gegenereerde resultaten via gefilterde dashboards. Eerste versie presenteert vooraf gegenereerde resultaten met prompts als filtervensters, toekomstige versies stellen eindgebruikers in staat zelf te prompen.

## Strategie
**Fase 1 (Huidige Focus): Gefilterde Resultaten Dashboard**
- Copilot genereert vooraf resultaten
- 5 goed gedefinieerde prompts als filtervensters
- Dashboard toont resultaten gefilterd op prompts
- Optioneel per opleiding uitgesplitst
- Basis voor evaluatie met stakeholders

**Fase 2 (Toekomstig): Self-Service Prompting**
- Gebruikers kunnen zelf prompts indienen
- Diepere analyse mogelijkheden
- Iteratieve verbetering van resultaten

## Workflow
1. **Stakeholder Workshop** - Definieer 5 kernprompts met kleine groep stakeholders
2. **Copilot Processing** - Genereer resultaten voor de gedefinieerde prompts
3. **Dashboard Development** - Bouw dashboard met filter- en weergavefunctionaliteit
4. **Presentatie** - Toon resultaten aan stakeholders voor evaluatie
5. **Iteratie** - Verfijn op basis van feedback

## User Stories

### In Progress 🚧
- [ ] User Story #146351: Hybride Copilot Dashboards v1 - Gefilterde Resultaten
  - Dashboard development met gefilterde prompts
  - Resultaten opslag en weergave
  - Optioneel per opleiding splitsen
  - Performance optimalisatie
  - Stakeholder-ready presentatie

**Active Links:**
- [User Story #146351](https://dev.azure.com/HogeschoolUtrecht/8b224685-8bd1-4a9a-9650-c62d60c23e77/_workitems/edit/146351) - Gefilterde Resultaten Dashboard (Te Refinen)
- [Feature 142267](https://dev.azure.com/HogeschoolUtrecht/DevOps%20DenA/_boards/board/t/Team%20Data%20Analytics/Backlog%20items?workitem=142267) - Copilot Dashboards

## Key Features
- **Prompt als Filter**: Gebruikers selecteren prompts om resultaten te zien
- **Vooraf Gegenereerde Resultaten**: Copilot levert al verwerkte content
- **Dashboard Visualisatie**: Duidelijke weergave van Copilot output
- **Optioneel per Opleiding**: Gesplitste weergave per educatief domein
- **Performance**: Snelle laadtijden (<3 seconden)

## De 5 Kernprompts

### Prompt 1: [Naam/Categorie]
**Vraag aan Copilot:**
- [Definieer de prompt]

**Verwachte Output:**
- [Wat voor resultaten levert dit op?]

**Data Bronnen:**
- [Welke data is nodig?]

**Relevantie voor Stakeholders:**
- [Waarom is dit belangrijk?]

---

### Prompt 2: [Naam/Categorie]
**Vraag aan Copilot:**
- [Definieer de prompt]

**Verwachte Output:**
- [Wat voor resultaten levert dit op?]

**Data Bronnen:**
- [Welke data is nodig?]

**Relevantie voor Stakeholders:**
- [Waarom is dit belangrijk?]

---

### Prompt 3: [Naam/Categorie]
**Vraag aan Copilot:**
- [Definieer de prompt]

**Verwachte Output:**
- [Wat voor resultaten levert dit op?]

**Data Bronnen:**
- [Welke data is nodig?]

**Relevantie voor Stakeholders:**
- [Waarom is dit belangrijk?]

---

### Prompt 4: [Naam/Categorie]
**Vraag aan Copilot:**
- [Definieer de prompt]

**Verwachte Output:**
- [Wat voor resultaten levert dit op?]

**Data Bronnen:**
- [Welke data is nodig?]

**Relevantie voor Stakeholders:**
- [Waarom is dit belangrijk?]

---

### Prompt 5: [Naam/Categorie]
**Vraag aan Copilot:**
- [Definieer de prompt]

**Verwachte Output:**
- [Wat voor resultaten levert dit op?]

**Data Bronnen:**
- [Welke data is nodig?]

**Relevantie voor Stakeholders:**
- [Waarom is dit belangrijk?]

---

## Dashboard Mockup Overwegingen
- **Filter Interface**: Hoe selecteren gebruikers prompts? (dropdown, knoppen, etc.)
- **Results Display**: Tabellen, visualisaties, tekst?
- **Opleiding Filter**: Hoe implementeren we de optionele opleiding-filter?
- **Performance**: Caching strategie voor pre-generated resultaten

## Volgende Stappen
- [x] Template voor prompt definitie aangemaakt (2026-02-04)
- [ ] 5 kernprompts definiëren met stakeholder perspectief
- [ ] Bijeenkomst met stakeholders plannen om prompts te valideren
- [ ] Copilot resultaten generen voor gedefinieerde prompts
- [ ] Dashboard prototype bouwen
- [ ] Feedback verzamelen en itereren

## Notities
- Beginjaar is 2026
- Deze aanpak schept basis voor toekomstige versie met self-service prompting
- Focus op gebruiksvriendelijkheid en duidelijke relatie prompt ↔ resultaten
- Denk aan: Welke vragen stellen stakeholders nu al regelmatig?
- Prompts moeten breed genoeg zijn voor hergebruik, maar specifiek genoeg voor waardevolle resultaten
