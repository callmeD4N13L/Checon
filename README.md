# 🕵️‍♂️ **Checon — OSINT Subdomain & Email Enumerator**

![alt text](Assets/logo.png)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Build-Stable-brightgreen)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)]()

Checon is a lightweight OSINT tool designed for **subdomain checking**, **web crawling**, **link extraction**, and **email harvesting**, supporting multi-layer recursive scanning and JSON exports.

---

# 📚 **Table of Contents**

* [✨ Features](#-features)
* [📁 Project Structure](#-project-structure)
* [⚙️ Installation](#️-installation)
* [🚀 Usage](#-usage)
* [📝 Example Files](#-example-files)

  * `targets.txt`
  * `config.json`
* [📤 Output Samples](#-output-samples)
* [🧠 How It Works](#-how-it-works)
* [💻 Code Examples](#-code-examples)
* [🛡 Legal Disclaimer](#-legal-disclaimer)
* [🤝 Contributing](#-contributing)
* [⭐ Support](#-support)

---

# ✨ **Features**

Checon provides:

* Automatic subdomain checking
* Multi-depth web crawling (configurable)
* Link extraction (`<a href>`)
* Email harvesting (regex-based)
* JSON export with timestamps
* Threaded execution for speed
* Clean modular structure
* Easy configuration using `config.json`

---

# 📁 **Project Structure**

```
checon/
│
├── core/
│   ├── checker.py
│   ├── mail_crawler.py
│   ├── concurrent_runner.py
│   └── logger.py
│
├── config/
│   ├── config_loader.py
│   └── config.json
│
├── data/
│   └── exporters/
│       ├── json_exporter.py
│
├── utils/
│   ├── crawler_utils.py
│   └── http_utils.py
│
├── Checon.py
├── requirements.txt
└── README.md
```

---

# ⚙️ **Installation**

### Clone the repo:

```
git clone https://github.com/YourUser/Checon.git
cd Checon
```

### Install dependencies:

```
pip install -r requirements.txt
```

Or manually:

```
pip install requests beautifulsoup4 urllib3 tld
```

---

# 🚀 **Usage**

Run Checon with:

```
python main.py -c ./config/config.json -t ./targets.txt
```

### Arguments:

| Argument          | Description          |
| ----------------- | -------------------- |
| `-c` / `--conf`   | Path to config file  |
| `-t` / `--target` | Path to targets list |

---

# 📝 **Example Files**

## `targets.txt`

```
example.com
api.example.com
sub.domain.net
```

## `config.json`

```json
{
    "level": 2,
    "export": true
}
```

---

# 📤 **Output Samples**

### Checker output:

```json
{
    "0": {
        "subdomain_address": "https://example.com/",
        "status_code": 200,
        "subdomain_title": "Example Domain"
    }
}
```

### Email export:

```
emails_20250215_181020.json
```

---

# 🧠 **How It Works**

### `checker.py`

* Sends HTTP requests
* Fetches status code and title

### `mail_crawler.py`

* Multi-layer crawling (L1, L2, L3…)
* Extracts internal/external links
* Finds emails using regex

### `main.py`

* Loads configuration
* Manages threading
* Handles output export

---

# 💻 **Code Examples**

### Example: Importing and using the crawler inside another script

```python
from core.mail_crawler import crawler
from core.checker import checker
from core.utilities import export_json

session = requests.Session()

targets = ["https://example.com"]

# Run checker
results = checker(targets, session)

# Run crawler for 2 layers
emails = crawler(results, session, LEVEL=2)

print("Emails found:", emails)
```

---

# 🛡 **Legal Disclaimer**

This tool is intended **only for lawful security testing and OSINT research**.
The user assumes full responsibility for any misuse.

---

# 🤝 **Contributing**

Pull requests and feature suggestions are welcome.
Feel free to open issues or fork the project.

---

# ⭐ **Support**

If you find Checon useful, please consider giving it a **star ⭐ on GitHub** — it motivates further development.
---
# Our Plans

- Data Intelligence & Analytics
- Support more exporting formats
- DB Tables
- Regex Configurations for favorite patterns
- Improve logging
