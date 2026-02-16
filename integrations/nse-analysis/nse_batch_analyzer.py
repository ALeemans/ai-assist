#!/usr/bin/env python3
"""
Author: Anne Leemans in collaboration with GitHub Copilot

NSE Analysis Tool - Batch Preparation & Processing
Prepares open answers in batches for AI analysis and helps organize outputs.
"""

import pandas as pd
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class NSEAnalyzer:
    def __init__(self, input_csv: str, output_template_csv: str, working_dir: str = None):
        """Initialize the NSE Analyzer."""
        self.input_csv = input_csv
        self.output_template_csv = output_template_csv
        self.working_dir = working_dir or Path(input_csv).parent
        Path(self.working_dir).mkdir(parents=True, exist_ok=True)
        
        # Load data
        self.df_input = pd.read_csv(input_csv, sep=";")
        self.df_template = pd.read_csv(output_template_csv, sep=";")
        
        # Clean data
        self.df_input['ANTWOORD'] = self.df_input['ANTWOORD'].fillna("").str.strip()
        
        print(f"✅ Loaded {len(self.df_input)} answers from input file")
        print(f"✅ Template loaded with {len(self.df_template)} rows")
        print()
    
    def get_unique_buckets(self) -> List[Tuple]:
        """Get all unique dimension combinations."""
        grouping_cols = ['D_JAAR_NSE_ID', 'D_CROHO_NSE_ID', 'D_INSTITUUT_NSE_ID', 'D_VORM_NSE_ID']
        buckets = self.df_input.groupby(grouping_cols).size().reset_index()
        buckets = buckets.drop(0, axis=1)  # Drop the count column
        return [tuple(row) for row in buckets.values]
    
    def get_answers_for_bucket(self, jaar: int, croho: int, instituut: int, vorm: int) -> List[str]:
        """Get all non-empty answers for a specific bucket."""
        mask = (
            (self.df_input['D_JAAR_NSE_ID'] == jaar) &
            (self.df_input['D_CROHO_NSE_ID'] == croho) &
            (self.df_input['D_INSTITUUT_NSE_ID'] == instituut) &
            (self.df_input['D_VORM_NSE_ID'] == vorm)
        )
        answers = self.df_input[mask]['ANTWOORD'].tolist()
        answers = [a for a in answers if a and len(a) > 0]  # Filter empty
        return answers
    
    def create_prompt(self, jaar: int, croho: int, instituut: int, vorm: int, 
                     answers: List[str]) -> str:
        """Create a prompt for analyzing a bucket of answers."""
        return f"""Je bent een expert in het analyseren van studentenfeedback.

Hieronder vind je {len(answers)} open antwoorden op de vraag:
"Wat zijn de top vijf meest gehoorde klachten over deze opleiding?"

Deze antwoorden zijn van studenten van:
- Jaar: {jaar}
- CROHO: {croho}
- Instituut: {instituut}
- Vorm: {vorm}

ANTWOORDEN:
{chr(10).join(f'{i+1}. {a}' for i, a in enumerate(answers))}

TAAK:
Analyseer deze antwoorden en identificeer de TOP 5 MEEST GEHOORDE KLACHTEN/THEMA'S.

OUTPUT FORMAT:
Geef je antwoord in deze exakte format (voor elk van de 5 klachten):
[KLACHT 1] <beschrijving van klacht 1>
[KLACHT 2] <beschrijving van klacht 2>
[KLACHT 3] <beschrijving van klacht 3>
[KLACHT 4] <beschrijving van klacht 4>
[KLACHT 5] <beschrijving van klacht 5>

Zorg dat elke klacht bondige, duidelijk, en gebaseerd op de gegeven antwoorden is."""
    
    def create_batch_file(self, output_file: str = None) -> str:
        """Create a JSON file with all batches ready for analysis."""
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.working_dir, f"nse_batches_{timestamp}.json")
        
        buckets = self.get_unique_buckets()
        batches = []
        
        print(f"📦 Creating {len(buckets)} batches...\n")
        
        for i, (jaar, croho, instituut, vorm) in enumerate(buckets, 1):
            answers = self.get_answers_for_bucket(jaar, croho, instituut, vorm)
            
            if len(answers) == 0:
                print(f"⏭️  Batch {i}: SKIPPED (no answers) - Y:{jaar}, C:{croho}, I:{instituut}, F:{vorm}")
                continue
            
            prompt = self.create_prompt(jaar, croho, instituut, vorm, answers)
            
            batch = {
                "batch_id": i,
                "dimensions": {
                    "jaar": int(jaar),
                    "croho": int(croho),
                    "instituut": int(instituut),
                    "vorm": int(vorm)
                },
                "answer_count": len(answers),
                "prompt": prompt,
                "status": "pending",
                "response": None
            }
            
            batches.append(batch)
            print(f"✅ Batch {i}: {len(answers):3d} answers - Y:{jaar}, C:{croho}, I:{instituut}, F:{vorm}")
        
        # Save batches
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(batches, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 Saved {len(batches)} batches to: {output_file}")
        return output_file
    
    def load_batch_file(self, batch_file: str) -> List[Dict]:
        """Load a batch file."""
        with open(batch_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_batch_file(self, batches: List[Dict], batch_file: str):
        """Save batches back to file."""
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batches, f, ensure_ascii=False, indent=2)
    
    def show_next_pending(self, batch_file: str) -> Dict:
        """Show the next pending batch."""
        batches = self.load_batch_file(batch_file)
        for batch in batches:
            if batch['status'] == 'pending':
                return batch
        return None
    
    def update_batch_response(self, batch_file: str, batch_id: int, response: str):
        """Update a batch with the response from the chat."""
        batches = self.load_batch_file(batch_file)
        for batch in batches:
            if batch['batch_id'] == batch_id:
                batch['response'] = response
                batch['status'] = 'completed'
                break
        self.save_batch_file(batches, batch_file)
        print(f"✅ Batch {batch_id} updated and marked as completed")
    
    def export_to_template(self, batch_file: str, output_excel: str):
        """Export completed batches to the NSE Copilot template."""
        batches = self.load_batch_file(batch_file)
        
        # Filter completed batches
        completed = [b for b in batches if b['status'] == 'completed' and b['response']]
        print(f"📊 Processing {len(completed)} completed batches...\n")
        
        rows = []
        for batch in completed:
            jaar = batch['dimensions']['jaar']
            croho = batch['dimensions']['croho']
            instituut = batch['dimensions']['instituut']
            vorm = batch['dimensions']['vorm']
            
            # Parse the response to extract 5 complaints
            response = batch['response']
            klachten = self._extract_complaints(response)
            
            row = {
                'D_JAAR_NSE_ID': jaar,
                'D_CROHO_NSE_ID': croho,
                'D_INSTITUUT_NSE_ID': instituut,
                'D_VORM_NSE_ID': vorm,
                'AWNSER_1': klachten[0] if len(klachten) > 0 else "",
                'AWNSER_2': klachten[1] if len(klachten) > 1 else "",
                'AWNSER_3': klachten[2] if len(klachten) > 2 else "",
                'AWNSER_4': klachten[3] if len(klachten) > 3 else "",
                'AWNSER_5': klachten[4] if len(klachten) > 4 else "",
            }
            rows.append(row)
            print(f"✅ Batch exported: Y:{jaar}, C:{croho}, I:{instituut}, F:{vorm}")
        
        # Create DataFrame and save
        df_output = pd.DataFrame(rows)
        df_output.to_csv(output_excel, sep=";", index=False, encoding='utf-8')
        print(f"\n💾 Exported {len(rows)} rows to: {output_excel}")
    
    def _extract_complaints(self, response: str) -> List[str]:
        """Extract the 5 complaints from the chat response."""
        lines = response.strip().split('\n')
        complaints = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('[KLACHT'):
                # Extract everything after "] "
                if '] ' in line:
                    complaint = line.split('] ', 1)[1]
                    complaints.append(complaint)
        
        return complaints[:5]  # Return max 5

def main():
    """Main function."""
    print("=" * 70)
    print("NSE Analysis Tool - Batch Preparation")
    print("=" * 70)
    print()
    
    # File paths
    input_csv = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd\nse.xlsx"
    template_csv = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd\NSE Copilot.xlsx"
    working_dir = r"C:\Users\AnneL\Stichting Hogeschool Utrecht\FCA-DA-P - Inleesbestanden\Domein Education Analytics\SEAA\NSE\Inleesbestanden dashboard\samengevoegd"
    
    # Initialize
    analyzer = NSEAnalyzer(input_csv, template_csv, working_dir)
    
    # Create batches
    batch_file = analyzer.create_batch_file()
    
    print("\n" + "=" * 70)
    print("NEXT STEPS:")
    print("=" * 70)
    print(f"""
1. Open the batch file: {batch_file}
2. For each pending batch:
   a) Copy the 'prompt' text
   b) Paste it into GitHub Copilot Chat
   c) Copy the response
   d) Run: analyzer.update_batch_response('{batch_file}', <batch_id>, '<response>')
3. Once all batches are completed, run:
   analyzer.export_to_template('{batch_file}', 'output_file.csv')
""")

if __name__ == "__main__":
    main()
