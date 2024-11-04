import os
import tempfile
import shutil
import subprocess

# Define the repositories and their respective paths for .yaml files
repos = [
    ("https://github.com/pikpikcu/nuclei-templates", ["basic-detections", "cves", "files", "panels", "payloads", "security-misconfiguration", "subdomain-takeover", "technologies", "tokens", "vulnerabilities"]),
    ("https://github.com/ARPSyndicate/kenzer-templates", ["nuclei"]),
    ("https://github.com/medbsq/ncl", ["templates"]),
    ("https://github.com/clarkvoss/Nuclei-Templates", ["."]),
    ("https://github.com/System00-Security/backflow", ["templates/wordpress"]),
    ("https://github.com/geeknik/the-nuclei-templates", ["."]),
    ("https://github.com/CharanRayudu/Custom-Nuclei-Templates", ["."]),
    ("https://github.com/daffainfo/my-nuclei-templates", ["."]),
    ("https://github.com/AshiqurEmon/nuclei_templates", ["."]),
    ("https://github.com/NitinYadav00/My-Nuclei-Templates", ["."]),
    ("https://github.com/meme-lord/Custom-Nuclei-Templates", ["."]),
    ("https://github.com/Akokonunes/Private-Nuclei-Templates", ["."]),
    ("https://github.com/test502git/log4j-fuzz-head-poc", ["."]),
    ("https://github.com/Str1am/my-nuclei-templates", ["new-tamp"]),
    ("https://github.com/dk4trin/templates-nuclei", ["."]),
    ("https://github.com/Elsfa7-110/mynuclei-templates", ["."]),
    ("https://github.com/justmumu/SpringShell", ["nuclei-templates"]),
    ("https://github.com/trickest/log4j", ["nuclei-templates"]),
    ("https://github.com/pentest-dev/Profesional-Nuclei-Templates", ["CVE", "LFI", "OpenRedirect", "RCE", "SSRF", "XSS"]),
    ("https://github.com/aels/CVE-2022-37042", ["."]),
    ("https://github.com/ExpLangcn/NucleiTP", ["CNVD", "CVES", "critical", "helpers", "high", "info", "low", "medium"]),
    ("https://github.com/Lopseg/nuclei-c-templates", ["."]),
    ("https://github.com/topscoder/nuclei-wordfence-cve", ["nuclei-templates"]),
    ("https://github.com/UltimateSec/ultimaste-nuclei-templates", ["."]),
    ("https://github.com/imhunterand/nuclei-custom-templates", ["."]),
    ("https://github.com/0xKayala/Custom-Nuclei-Templates", ["."]),
    ("https://github.com/Shakilll/my_nuclei_templates", ["."]),
    ("https://github.com/topscoder/nuclei-zero-day", ["nuclei-templates"]),
    ("https://github.com/madisec/nuclei-templates", ["CVEs", "RCE", "Redirect", "SQLi", "SSRF", "templates"])
]

# Create destination folder
dest_folder = os.path.expanduser("templates")
os.makedirs(dest_folder, exist_ok=True)

# Clone repositories and copy .yaml files
with tempfile.TemporaryDirectory() as temp_folder:
    for repo_url, folders in repos:
        repo_name = repo_url.split('/')[-1]
        repo_path = os.path.join(temp_folder, repo_name)
        subprocess.run(["git", "clone", repo_url, repo_path])

        for folder in folders:
            folder_path = os.path.join(repo_path, folder)
            for root, _, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".yaml"):
                        shutil.copy(os.path.join(root, file), dest_folder)

print(f"Templates copied to {dest_folder}")
