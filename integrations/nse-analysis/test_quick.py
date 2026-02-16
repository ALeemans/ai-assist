#!/usr/bin/env python3
"""
Author: Anne Leemans in collaboration with GitHub Copilot

Quick Test - NSE Batch Analyzer with local test files
"""

import sys
from pathlib import Path

# Add the parent directory to path so we can import nse_batch_analyzer
sys.path.insert(0, str(Path(__file__).parent))

from nse_batch_analyzer import NSEAnalyzer

def main():
    """Run quick test with the local CSV files."""
    print("=" * 80)
    print("NSE ANALYSIS - QUICK TEST")
    print("=" * 80)
    print()
    
    # Use the test CSV files
    workspace_root = Path(__file__).parents[2]  # ai-assist root
    test_dir = workspace_root / "test"
    
    input_csv = str(test_dir / "nse.csv")
    template_csv = str(test_dir / "NSE Copilot.csv")
    output_dir = str(test_dir)
    
    print(f"Input file: {input_csv}")
    print(f"Template file: {template_csv}")
    print(f"Output directory: {output_dir}")
    print()
    
    # Check files exist
    if not Path(input_csv).exists():
        print(f"❌ Input file not found: {input_csv}")
        return
    
    if not Path(template_csv).exists():
        print(f"❌ Template file not found: {template_csv}")
        return
    
    # Initialize
    print("Loading data...")
    analyzer = NSEAnalyzer(input_csv, template_csv, output_dir)
    
    # Create batches
    print("\nCreating batches...")
    batch_file = analyzer.create_batch_file()
    
    print("\n" + "=" * 80)
    print("✅ TEST COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print(f"""
Batch file created: {batch_file}

NEXT STEPS:
1. Review the batch file contents
2. Process each batch using:
   & D:/HogeschoolUtrecht/GithubRepos/ai-assist/.venv/Scripts/python.exe integrations/nse-analysis/nse_batch_processor.py
""")

if __name__ == "__main__":
    main()
