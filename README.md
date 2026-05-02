# BGP Log Analyzer

## Overview
A Python-based CLI tool to parse BGP logs, detect peer failures, and classify network incidents.
## Features
- Log parsing using regex
- Extracts IP addresses and log metadata
- BGP peer state detection (down/up)
- Incident classification(No Issue / High Severity / Outage)
- Tracks error count per peer
- JSON report generation
- CLI support

## Tech Stack
- Python (Core)
- Regex

## Usage
```bash
python main.py --file logs/sample.log --peers 10.1.1.1,10.2.2.2

##  Sample Output

{
  "status": "High Severity Incident",
  "down_peers": ["10.2.2.2"]
}
