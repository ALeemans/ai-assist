---
type: email-draft
created: 2026-02-16
author: Anne Leemans in collaboration with Claude Sonnet 4.5
project: data-portal-analytics
feature_id: 142557
recipients: CKAN Dataportal Beheerders
subject: Verzoek Google Analytics Integratie CKAN Dataportal
---

# Email Draft: Google Analytics Integratie CKAN Dataportal

**Aan:** CKAN Dataportal Beheerders
**Van:** Anne Leemans (Team Data & Analytics)
**Onderwerp:** Verzoek Google Analytics Integratie CKAN Dataportal
**Prioriteit:** Normaal

---

Beste beheerders,

Vanuit het team Data & Analytics willen we graag gebruiksstatistieken verzamelen van het HU Dataportal (CKAN). Hiervoor hebben we jullie hulp nodig om de Google Analytics integratie in te richten.

## Wat we nodig hebben van jullie

### 1. Installatie van de Google Analytics Plugin

We hebben de officiële CKAN Google Analytics extensie nodig:
- **Plugin:** `ckanext-googleanalytics` (officiële CKAN extensie)
- **GitHub:** https://github.com/ckan/ckanext-googleanalytics
- **Installatie:** `pip install -e git+https://github.com/ckan/ckanext-googleanalytics.git#egg=ckanext-googleanalytics`

### 2. Configuratie in CKAN

De plugin moet worden geactiveerd en geconfigureerd in het CKAN configuratiebestand (development.ini of production.ini). De volgende instellingen zijn nodig:

```ini
# Google Analytics Plugin activeren
ckan.plugins = ... googleanalytics

# Google Analytics configuratie
googleanalytics.id = [GA4 Measurement ID van Google Analytics property]
googleanalytics.account = [Google Analytics Account naam]
```

### 3. Service Account voor API Toegang

Voor het ophalen van statistieken uit Google Analytics hebben we een Google Cloud Service Account nodig:

**Optie A - Jullie maken het service account aan:**
1. Creëer een Service Account in Google Cloud Console
2. Genereer een JSON sleutelbestand (credentials.json)
3. Geef het service account "Read" toegang tot de Google Analytics property
4. Deel het JSON bestand veilig met mij

**Optie B - Ik maak het service account aan:**
1. Ik creëer zelf het service account en deel de credentials met jullie
2. Jullie configureren deze credentials in CKAN
3. Jullie voegen het service account email adres toe aan de Google Analytics property

### 4. Database Toegang voor Data Export

Voor het bouwen van Power BI dashboards heb ik toegang nodig tot de CKAN database waar de analytics data wordt opgeslagen:
- **Toegang:** Read-only toegang tot de analytics tabellen in de CKAN database
- **Doel:** Data exporteren naar Power BI voor custom dashboards
- **Alternatief:** Als directe database toegang niet mogelijk is, kunnen we ook de Google Analytics Property ID gebruiken om data via API op te halen

## Wat deze integratie oplevert

✅ Automatische tracking van alle pagina views op het dataportal
✅ Statistieken over dataset downloads en populariteit
✅ Inzicht in zoekgedrag en gebruikersnavigatie
✅ Rapportages over API gebruik
✅ Data beschikbaar in CKAN database voor Power BI dashboards
✅ Custom dashboards met gebruiksmetrieken voor stakeholders (in Power BI)

## Technische Details

De plugin werkt als volgt:
- **Tracking code:** Automatisch ingevoegd in alle CKAN pagina's
- **Event tracking:** Dataset views, downloads en API calls worden gelogd naar Google Analytics
- **Data opslag:** Statistieken worden opgehaald via Google Analytics API en opgeslagen in CKAN database tabellen
- **Power BI integratie:** Data uit CKAN database kan direct worden gebruikt voor custom Power BI dashboards
- **Privacy:** GDPR-compliant tracking (IP anonimisering indien gewenst)

## Vervolgstappen

1. **Jullie actie:** Installatie en configuratie van de plugin
2. **Mijn actie:** Setup van Google Analytics property en dashboards
3. **Gezamenlijk:** Testen van de tracking en valideren van data
4. **Oplevering:** Werkende analytics met toegang tot rapportages

## Vragen of onduidelijkheden?

Ik help graag mee met de technische setup als dat nodig is. We kunnen ook een korte call inplannen om dit door te nemen.

**Mijn voorkeur voor vervolgstap:**
- Optie B (ik maak service account aan) lijkt me het meest efficiënt
- Dan heb ik alleen van jullie nodig: plugin installatie + configuratie met de credentials die ik aanlever

Laat me weten wat jullie voorkeur heeft en wanneer we dit kunnen oppakken!

Met vriendelijke groet,

Anne Leemans
Data Analist | Team Data & Analytics
Hogeschool Utrecht

---

## Bijlagen / Referenties

- [CKAN Google Analytics Plugin - GitHub](https://github.com/ckan/ckanext-googleanalytics)
- [CKAN Extensions Documentatie](https://extensions.ckan.org/extension/googleanalytics/)
- [Setup Guide - HackMD](https://hackmd.io/@datopian-ed-team/B1LoIsJD5)
- Feature ID: #142557 (Azure DevOps)
