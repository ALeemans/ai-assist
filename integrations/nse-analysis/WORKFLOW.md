# NSE Analysis - Complete Workflow Summary

## ✅ What We've Built

A **manual-hybrid solution** for analyzing NSE open answers using GitHub Copilot Chat:

1. **Python batch creator** - Groups answers by dimensions, creates prompts
2. **Interactive batch processor** - Feeds prompts to chat, collects responses
3. **Auto-filler** - Saves results to output template

## 📊 How It Works (4 Steps)

### Step 1: Create Batches
```powershell
& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe integrations/nse-analysis/nse_batch_analyzer.py
```

**Output:** Creates JSON file with 455 batches (from your test data)
- Each batch = 1 combination of (Jaar, CROHO, Instituut, Vorm)
- Each batch contains all open answers for that group
- Includes Dutch prompt ready for GitHub Copilot

### Step 2: Process Interactively
```powershell
& D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe integrations/nse-analysis/nse_batch_processor.py
```

**Interactive interface lets you:**
- `show` → Display next batch prompt
- `copy` → Copy prompt to clipboard
- `submit` → Paste response from chat
- Stats tracking

### Step 3: For Each Batch
```
PROMPT: 
"Je bent een expert in het analyseren van studentenfeedback.
Hieronder vind je 176 open antwoorden op de vraag:
'Wat zijn de top vijf meest gehoorde klachten over deze opleiding?'

Deze antwoorden zijn van studenten van:
- Jaar: 2023
- CROHO: 1
- Instituut: 1
- Vorm: 1

[176 answers listed...]

TAAK: Analyseer en identificeer TOP 5 MEEST GEHOORDE KLACHTEN"
```

You paste this into **GitHub Copilot Chat** → Get top 5 complaints → Paste response back

### Step 4: Export Results
```powershell
from integrations.nse_analysis.nse_batch_analyzer import NSEAnalyzer

analyzer = NSEAnalyzer("nse.xlsx", "NSE Copilot.xlsx")
analyzer.export_to_template("nse_batches_YYYYMMDD_HHMMSS.json", "output.csv")
```

**Output:** `NSE_Results.csv` with all 5 complaint columns filled

---

## 📁 File Structure

```
integrations/nse-analysis/
├── nse_batch_analyzer.py      # Main: Creates batches
├── nse_batch_processor.py      # Interactive: Processes batches
├── test_quick.py              # Test with sample CSVs
├── requirements.txt           # Dependencies
└── README.md                  # Full documentation
```

---

## ⚙️ Configuration for Your Real Files

**Edit these 2 files with your actual paths:**

### File 1: nse_batch_analyzer.py (line ~170)
```python
input_csv = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd\nse.xlsx"
template_csv = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd\NSE Copilot.xlsx"
working_dir = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd"
```

### File 2: nse_batch_processor.py (line ~130)
```python
work_dir = Path(r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd")
```

---

## 🚀 Next Steps

1. **Update file paths** in both scripts
2. **Run batch creator** to generate all batches
3. **Start processor** and work through batches interactively
4. **Export results** when done

## 📊 Test Results

Your test data produced:
- **455 batches** (459 groups detected, ~4 empty)
- **40,865 total answers** analyzed
- Batches created in seconds

---

## 💡 Key Features

✅ Automatic grouping by all 4 dimensions  
✅ Dutch prompts optimized for Copilot Chat  
✅ Copy-paste interface - no manual prompt writing  
✅ Progress tracking built-in  
✅ All results saved automatically  
✅ Works with Excel files  

---

## ❓ Questions?

See the detailed README:
[integrations/nse-analysis/README.md](integrations/nse-analysis/README.md)

