# 🚀 BGP Log Analyzer

A Python-based CLI tool to parse BGP logs, detect peer failures, and classify network incidents.

## 🔧 Features
- Log parsing using regex
- BGP peer state detection (down/up)
- Incident classification
- JSON report generation

## 📊 Sample Output

{
  "status": "High Severity Incident",
  "down_peers": ["10.2.2.2"]
}
