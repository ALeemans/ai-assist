# NSE Analysis Tool - Manual Hybrid Workflow

This tool helps you analyze NSE (Nationale Studenten Enquête) open answers using GitHub Copilot Chat.

## Overview

The workflow is **manual-hybrid**: Python prepares batches, you feed them to the chat, then the tool collects responses.

```
Input: nse.xlsx
  ↓
[Python] Group by dimensions, create batches
  ↓
[You] Send prompts to GitHub Copilot Chat
  ↓
[Python] Collect responses, fill NSE Copilot.xlsx
```

## Setup

### 1. Install Dependencies

```powershell
& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe -m pip install -r integrations/nse-analysis/requirements.txt
```

### 2. Update File Paths

Edit both scripts and update these paths to match your setup:

**In `nse_batch_analyzer.py` (line ~170):**
```python
input_csv = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\...\nse.xlsx"
template_csv = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\...\NSE Copilot.xlsx"
working_dir = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\...\samengevoegd"
```

**In `nse_batch_processor.py` (line ~130):**
```python
work_dir = Path(r"C:\Users\AnneL\Stichting Hogeschool Utrecht\...\samengevoegd")
```

## Workflow

### Step 1: Create Batches

```powershell
& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe integrations/nse-analysis/nse_batch_analyzer.py
```

**Output:**
- Creates `nse_batches_YYYYMMDD_HHMMSS.json` file
- Shows how many batches were created
- Lists all batches with answer counts

**Example output:**
```
✅ Batch 1: 12 answers - Y:2025, C:12, I:106, F:1
✅ Batch 2:  8 answers - Y:2025, C:23, I:211, F:1
...
💾 Saved 47 batches to: nse_batches_20260212_143022.json
```

### Step 2: Process Batches Interactively

```powershell
& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe integrations/nse-analysis/nse_batch_processor.py
```

**Interactive commands:**

| Command | Description |
|---------|-------------|
| `show` | Display the next pending batch and its prompt |
| `copy` | Copy the batch prompt to your clipboard |
| `submit` | Paste the response from the chat (paste, then Enter twice) |
| `stats` | Show progress statistics |
| `exit` | Quit the processor |

### Step 3: For Each Batch

1. **Show** → Get the prompt displayed
2. **Copy** → Prompt goes to clipboard
3. **Paste** in GitHub Copilot Chat → Get AI analysis
4. **Copy** response from chat
5. **Submit** → Paste response in processor
6. Processor validates and marks as complete
7. Automatically shows next batch

**Example interaction:**

```
Command: show
📦 BATCH 1 (Progress: 1/47)
Dimensions:
  - Jaar: 2025
  - CROHO: 12
  - Instituut: 106
  - Vorm: 1
  - Aantal antwoorden: 12

PROMPT TO SEND TO GITHUB COPILOT:
[Je krijgt hier de prompt...]

Command: copy
✅ Prompt from batch 1 copied to clipboard!

[Open GitHub Copilot Chat, paste, get response...]

Command: submit
[Paste the response, press Enter twice]
✅ Response received for batch 1
   Status: completed

📦 BATCH 2 (Progress: 2/47)
[Next batch appears...]
```

## Response Format

When you submit responses, the tool expects this format from the chat:

```
[KLACHT 1] Beschrijving van eerste klacht
[KLACHT 2] Beschrijving van tweede klacht
[KLACHT 3] Beschrijving van derde klacht
[KLACHT 4] Beschrijving van vierde klacht
[KLACHT 5] Beschrijving van vijfde klacht
```

The tool automatically extracts these and fills the output template.

## Step 4: Export Results

Once all batches are completed:

```powershell
# In Python or IPython:
from integrations.nse_analysis.nse_batch_analyzer import NSEAnalyzer

analyzer = NSEAnalyzer(
    r"C:\path\to\nse.xlsx",
    r"C:\path\to\NSE Copilot.xlsx"
)

batch_file = r"C:\path\to\nse_batches_20260212_143022.json"
analyzer.export_to_template(batch_file, r"C:\path\to\output\NSE_Results.csv")
```

**Output:**
- Creates `NSE_Results.csv` with all 5 complaint columns filled
- Ready to import into Power BI or other tools

## File Structure

```
integrations/nse-analysis/
├── nse_batch_analyzer.py      # Creates batches from input data
├── nse_batch_processor.py      # Interactive batch processor
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

## Tips & Best Practices

### For Better AI Responses

1. **Be consistent** - Keep answers in Dutch as sent to the chat
2. **Review responses** - The chat might need refinement
3. **Copy the exact format** - Use `[KLACHT 1]` format exactly

### If Processing Takes Long

- You can close the processor and resume later - batches are saved in JSON
- Processor automatically finds where you left off
- No progress is lost

### Troubleshooting

**Q: "No batch files found"**
- Run `nse_batch_analyzer.py` first to create batches

**Q: Files not found errors**
- Check file paths in the scripts match your actual locations
- Use raw strings: `r"C:\path\..."`

**Q: Response didn't parse correctly**
- Ensure response starts with `[KLACHT 1]` format
- Submit again with corrected format

## Output Template Structure

Updated `NSE Copilot.xlsx` will have:

| Column | Description |
|--------|-------------|
| D_JAAR_NSE_ID | Year |
| D_CROHO_NSE_ID | CROHO code |
| D_INSTITUUT_NSE_ID | Institute ID |
| D_VORM_NSE_ID | Form ID |
| AWNSER_1 | Top complaint 1 |
| AWNSER_2 | Top complaint 2 |
| AWNSER_3 | Top complaint 3 |
| AWNSER_4 | Top complaint 4 |
| AWNSER_5 | Top complaint 5 |

---

**Questions?** Check the Python docstrings in the scripts for more details.
