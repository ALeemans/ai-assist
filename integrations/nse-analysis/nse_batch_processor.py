#!/usr/bin/env python3
"""
Author: Anne Leemans in collaboration with GitHub Copilot

NSE Batch Processor - Interactive helper for processing batches
"""

import json
import os
import pyperclip
from pathlib import Path
from nse_batch_analyzer import NSEAnalyzer

class BatchProcessor:
    def __init__(self, batch_file: str):
        """Initialize the batch processor."""
        self.batch_file = batch_file
        self.batches = None
        self.current_batch_index = 0
        self.load_batches()
    
    def load_batches(self):
        """Load batches from file."""
        with open(self.batch_file, 'r', encoding='utf-8') as f:
            self.batches = json.load(f)
        print(f"✅ Loaded {len(self.batches)} batches")
    
    def save_batches(self):
        """Save batches to file."""
        with open(self.batch_file, 'w', encoding='utf-8') as f:
            json.dump(self.batches, f, ensure_ascii=False, indent=2)
    
    def find_next_pending(self) -> int:
        """Find the index of the next pending batch."""
        for i, batch in enumerate(self.batches):
            if batch['status'] == 'pending':
                return i
        return -1
    
    def show_current_batch(self):
        """Show the current batch details."""
        idx = self.find_next_pending()
        if idx == -1:
            print("✅ All batches completed!")
            return None
        
        batch = self.batches[idx]
        print("\n" + "=" * 80)
        print(f"📦 BATCH {batch['batch_id']} (Progress: {idx + 1}/{len(self.batches)})")
        print("=" * 80)
        print(f"Dimensions:")
        print(f"  - Jaar: {batch['dimensions']['jaar']}")
        print(f"  - CROHO: {batch['dimensions']['croho']}")
        print(f"  - Instituut: {batch['dimensions']['instituut']}")
        print(f"  - Vorm: {batch['dimensions']['vorm']}")
        print(f"  - Aantal antwoorden: {batch['answer_count']}")
        print("\n" + "-" * 80)
        print("PROMPT TO SEND TO GITHUB COPILOT:")
        print("-" * 80)
        print(batch['prompt'])
        print("\n" + "=" * 80)
        return idx
    
    def copy_prompt_to_clipboard(self):
        """Copy current batch prompt to clipboard."""
        idx = self.find_next_pending()
        if idx == -1:
            print("✅ All batches completed!")
            return
        
        batch = self.batches[idx]
        pyperclip.copy(batch['prompt'])
        print(f"✅ Prompt from batch {batch['batch_id']} copied to clipboard!")
    
    def submit_response(self, response: str):
        """Submit a response for the current batch."""
        idx = self.find_next_pending()
        if idx == -1:
            print("✅ All batches completed!")
            return
        
        batch = self.batches[idx]
        batch['response'] = response
        batch['status'] = 'completed'
        self.save_batches()
        
        print(f"✅ Response received for batch {batch['batch_id']}")
        print(f"   Status: {batch['status']}")
        
        # Show next batch
        self.show_current_batch()
    
    def show_stats(self):
        """Show processing statistics."""
        completed = sum(1 for b in self.batches if b['status'] == 'completed')
        pending = sum(1 for b in self.batches if b['status'] == 'pending')
        
        print("\n" + "=" * 80)
        print("STATISTICS")
        print("=" * 80)
        print(f"Total batches: {len(self.batches)}")
        print(f"Completed: {completed} ({100*completed//len(self.batches)}%)")
        print(f"Pending: {pending}")
        print("=" * 80 + "\n")
    
    def start_interactive(self):
        """Start interactive batch processing."""
        print("\n" + "=" * 80)
        print("NSE BATCH PROCESSOR - Interactive Mode")
        print("=" * 80)
        print("\nCommands:")
        print("  'show'   - Show next pending batch")
        print("  'copy'   - Copy batch prompt to clipboard")
        print("  'submit' - Submit response for current batch")
        print("  'stats'  - Show processing statistics")
        print("  'exit'   - Exit")
        print("=" * 80 + "\n")
        
        while True:
            cmd = input("Command: ").strip().lower()
            
            if cmd == 'show':
                self.show_current_batch()
            elif cmd == 'copy':
                self.copy_prompt_to_clipboard()
            elif cmd == 'submit':
                print("\nPaste the response from GitHub Copilot (press Enter twice to finish):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        if lines and lines[-1] == "":
                            break
                    lines.append(line)
                response = "\n".join(lines[:-1])
                self.submit_response(response)
            elif cmd == 'stats':
                self.show_stats()
            elif cmd == 'exit':
                print("Goodbye!")
                break
            else:
                print("Unknown command. Try again.")

def main():
    """Main function."""
    # Find the most recent batch file
    work_dir = Path(r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd")
    
    batch_files = sorted(work_dir.glob("nse_batches_*.json"), reverse=True)
    
    if not batch_files:
        print("❌ No batch files found. Run nse_batch_analyzer.py first.")
        return
    
    batch_file = str(batch_files[0])
    print(f"Using batch file: {batch_file}\n")
    
    processor = BatchProcessor(batch_file)
    processor.show_stats()
    processor.show_current_batch()
    processor.start_interactive()

if __name__ == "__main__":
    main()
