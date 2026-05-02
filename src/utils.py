import json

def save_report(report, filepath):
    with open(filepath, "w") as f:
        json.dump(report, f, indent=4)
