import json
import csv

def generate_report():
    results = [
        {"search_type": "Google Dork", "result": "Example result 1"},
        {"search_type": "GitHub Leak", "result": "Example result 2"},
        {"search_type": "Dark Web", "result": "Example result 3"}
    ]

    # Generate JSON report
    with open("report.json", "w") as json_file:
        json.dump(results, json_file, indent=4)

    # Generate CSV report
    with open("report.csv", "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["search_type", "result"])
        writer.writeheader()
        writer.writerows(results)

    print("Report generated: report.json, report.csv")
