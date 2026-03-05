# Monitoring of Passes for CY 2026

This repository tracks employee leave (termed "Passes") for compliance with the rule:
**Each personnel can only avail one pass every 3 months.**

## Files
- `passes_data.csv` → Raw log of passes
- `personnel_list.csv` → Master list of personnel
- `passes_monitoring.py` → Script to check eligibility and update records
- `passes_report.py` → Reporting script for compliance summaries

## Columns
- Month
- Date
- Name of Personnel
- Duration
- Remarks → "On Leave", "Can Avail for Passes", "Not yet Available to Avail"

## Usage

### Add a New Pass
```bash
python passes_monitoring.py
