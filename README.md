## nucleihub-templates

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-automated-blue)
![Update Frequency](https://img.shields.io/badge/update-every_6_hours-brightgreen)
![Nuclei Version](https://img.shields.io/badge/nuclei-v3.3.7-orange)
![Template Sources](https://img.shields.io/badge/sources-600%2B_repos-lightgrey)

A continuously updated repository of Nuclei templates collected from 600+ GitHub repositories, automatically refreshed every 6 hours using GitHub Actions.

## 🚀 Overview

This repository serves as a centralized, up-to-date collection of security testing templates for [Nuclei](https://github.com/projectdiscovery/nuclei), the fast and customizable vulnerability scanner. By aggregating templates from numerous sources, it provides security researchers and penetration testers with comprehensive coverage for their security assessments.

## ⚙️ How It Works

### Automated Collection Pipeline

```yaml
Schedule: Runs every 6 hours
Trigger: Also on push to main branch
Process:
1. 📥 Downloads templates from 600+ repositories
2. 🔄 Checks for updates using nucleihub
3. 🗑️ Removes duplicate templates
4. ✅ Commits and pushes new templates
```

### Tools Used

- **nucleihub**: For repository management and template collection
- **nuclei**: Latest version (v3.3.7) for template validation
- **GitHub Actions**: For automation and scheduling

## 📂 Repository Structure

```
nuclei-templates-collector/
├── .github/workflows/
│   └── collect-templates.yml  # Automation workflow
├── nucleihub-templates/       # Collected templates (auto-generated)
│   ├── cves/
│   ├── vulnerabilities/
│   ├── exposures/
│   └── ...other categories
└── README.md
```

## 🛠️ Usage

### Using with Nuclei

```bash
# Clone this repository
git clone https://github.com/your-username/nuclei-templates-collector.git

# Run nuclei with the collected templates
nuclei -u https://target.com -t nucleihub-templates/

# Run specific template categories
nuclei -u https://target.com -t nucleihub-templates/cves/
nuclei -u https://target.com -t nucleihub-templates/vulnerabilities/
```

### Integration in Existing Workflows

```bash
# Add as a template directory in your nuclei config
nuclei -u https://target.com -t nucleihub-templates/ -t ~/nuclei-templates/
```

## 🔄 Automation Details

- **Schedule**: Runs every 6 hours (0 */6 * * *)
- **Update Check**: Uses `nucleihub updatecheck` to detect new templates
- **Duplicate Removal**: Automatically removes large content duplicates
- **Commit**: Automatically commits changes with IST timestamp

## 📊 Template Sources

This repository collects templates from **600+ curated GitHub repositories** including:

### Major Sources
- **[projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)** - Official Nuclei templates
- **[projectdiscovery/fuzzing-templates](https://github.com/projectdiscovery/fuzzing-templates)** - Fuzzing templates
- **[ARPSyndicate/kenzer-templates](https://github.com/ARPSyndicate/kenzer-templates)** - Kenzer security templates
- **[optiv/mobile-nuclei-templates](https://github.com/optiv/mobile-nuclei-templates)** - Mobile application testing
- **[rix4uni/collected-templates-other-sources](https://github.com/rix4uni/collected-templates-other-sources)** - Additional template collections

### Community Contributors
- **[daffainfo/my-nuclei-templates](https://github.com/daffainfo/my-nuclei-templates)**
- **[pikpikcu/my-nuclei-templates](https://github.com/pikpikcu/my-nuclei-templates)**
- **[geeknik/the-nuclei-templates](https://github.com/geeknik/the-nuclei-templates)**
- **[0xSojalSec/nuclei-templates](https://github.com/0xSojalSec/nuclei-templates)**
- **[sudouday/nuclei-templates](https://github.com/sudouday/nuclei-templates)**

### Specialized Collections
- **CVE-specific templates** (Log4Shell, Spring4Shell, various CVEs)
- **Technology-specific templates** (WordPress, Drupal, Joomla, etc.)
- **API security templates**
- **Cloud security templates**
- **Mobile application templates**
- **Network device templates**

### Complete Source List
The complete list of 600+ source repositories is collected from:
```
https://raw.githubusercontent.com/rix4uni/nucleihub/main/reponames.txt
```

This includes repositories from security researchers, bug bounty hunters, and security teams worldwide, ensuring comprehensive coverage of the latest vulnerabilities and security checks.

## 🤝 Contributing

While this repository is automatically generated, you can contribute by:

1. **Suggesting new template sources** by opening an issue
2. **Reporting problematic templates** that may cause false positives
3. **Improving the collection process** via pull requests

## ⚠️ Disclaimer

This repository aggregates templates from various public sources. Users should:

- Validate templates before use in production environments
- Understand that some templates may generate false positives
- Use responsibly and only on authorized targets
- Comply with all applicable laws and regulations

## 📄 License

The automation code in this repository is licensed under MIT. However, individual templates may have their own respective licenses from their original sources.

## 🔗 Related Projects

- [Nuclei](https://github.com/projectdiscovery/nuclei) - The core vulnerability scanner
- [nucleihub](https://github.com/rix4uni/nucleihub) - Template repository management tool
- [Nuclei Templates](https://github.com/projectdiscovery/nuclei-templates) - Official templates
