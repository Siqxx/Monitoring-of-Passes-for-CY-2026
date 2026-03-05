import csv
from datetime import datetime

def load_personnel(file_path="personnel_list.csv"):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        return [row['Name of Personnel'] for row in reader]

def check_eligibility(records, name, new_date):
    employee_records = [r for r in records if r['Name of Personnel'] == name and r['Remarks'] == "On Leave"]
    dates = [datetime.strptime(r['Date'], "%Y-%m-%d") for r in employee_records]
    for d in dates:
        if abs((new_date - d).days) < 90:
            return "Not yet Available to Avail"
    return "Can Avail for Passes"

def update_passes(file_path, month, date_str, name, duration):
    personnel = load_personnel()
    if name not in personnel:
        print(f"Error: {name} is not in personnel list.")
        return

    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        records = list(reader)

    new_date = datetime.strptime(date_str, "%Y-%m-%d")
    remarks = check_eligibility(records, name, new_date)
    final_remarks = "On Leave" if remarks == "Can Avail for Passes" else remarks

    new_entry = {
        "Month": month,
        "Date": date_str,
        "Name of Personnel": name,
        "Duration": duration,
        "Remarks": final_remarks
    }

    with open(file_path, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writerow(new_entry)

    print(f"Entry added: {new_entry}")

# Example usage:
# update_passes("passes_data.csv", "March", "2026-03-10", "Juan Dela Cruz", "1 day")
