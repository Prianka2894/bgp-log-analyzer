import argparse
from src.parser import parse_line, extract_ip
from src.analyzer import analyze_logs, classify_incident
from src.utils import save_report

def main():
    parser = argparse.ArgumentParser(description="BGP Log Analyzer")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--peers", required=True, help="Comma-separated peer IPs")

    args = parser.parse_args()

    peers = args.peers.split(",")
    parsed_logs = []

    with open(args.file, "r") as file:
        for line in file:
            log = parse_line(line)
            if not log:
                continue

            ip = extract_ip(log["message"])
            log["ip"] = ip
            parsed_logs.append(log)

    down_peers, recovered_peers, error_count = analyze_logs(parsed_logs, peers)
    status = classify_incident(down_peers, peers)

    report = {
        "status": status,
        "down_peers": list(down_peers),
        "recovered_peers": list(recovered_peers),
        "error_count_per_ip": error_count,
    }

    print("=== INCIDENT REPORT ===")
    print(report)

    save_report(report, "output/report.json")


if __name__ == "__main__":
    main()
