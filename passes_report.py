import csv
from datetime import datetime

def generate_report(file_path, personnel_file="personnel_list.csv"):
    # Load personnel list
    with open(personnel_file, newline='') as f:
        personnel_reader = csv.DictReader(f)
        personnel = [row['Name of Personnel'] for row in personnel_reader]

    # Load passes data
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        records = list(reader)

    # Initialize report dictionary
    report = {name: {"Total Passes": 0, "Last Pass Date": None, "Compliance": "Compliant"} for name in personnel}

    # Process records
    for r in records:
        name = r['Name of Personnel']
        if name not in report:
            continue
        date = datetime.strptime(r['Date'], "%Y-%m-%d")
        if r['Remarks'] == "On Leave":
            report[name]["Total Passes"] += 1
            report[name]["Last Pass Date"] = date

    # Compliance check
    for name, data in report.items():
        if data["Total Passes"] > 4:  # more than 4 passes in a year
            data["Compliance"] = "Non-Compliant"

    # Print report
    print("=== Monitoring of Passes Report for CY 2026 ===")
    for name, data in report.items():
        last_pass = data["Last Pass Date"].strftime("%Y-%m-%d") if data["Last Pass Date"] else "None"
        status = data["Compliance"]
        if data["Total Passes"] == 0:
            status = "No Passes Availed Yet"
        print(f"{name}: {data['Total Passes']} passes, Last Pass: {last_pass}, Status: {status}")

if __name__ == "__main__":
    generate_report("passes_data.csv")
