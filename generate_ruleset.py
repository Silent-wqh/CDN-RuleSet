import json
import urllib.request
import os
import re

# Directory for output
output_dir = "ruleset"
if os.path.exists(output_dir):
    import shutil
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Read repository info for link generation
github_repo = os.environ.get("GITHUB_REPOSITORY", "Silent-wqh/CDN-RuleSet")

source_url = "https://raw.githubusercontent.com/mansourjabin/cdn-ip-database/main/data/resolved_ips.json"

print(f"Fetching data from {source_url}...")
req = urllib.request.Request(
    source_url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name).strip('_').lower()

generated_files = []

for cdn_name, info in data.items():
    safe_name = sanitize_filename(cdn_name)
    ips = info.get("ips", [])
    asns = info.get("asns", [])
    
    ipcidr_path = None
    classical_path = None
    
    if ips:
        filename = f"{safe_name}_ipcidr.yaml"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("payload:\n")
            for ip in ips:
                f.write(f"  - '{ip}'\n")
        ipcidr_path = f"ruleset/{filename}"

    classical_rules = []
    has_asn = False
    for asn in asns:
        asn_num = asn.upper().replace("AS", "").strip()
        if asn_num.isdigit():
            classical_rules.append(f"IP-ASN,{asn_num}")
            has_asn = True
            
    if has_asn:
        for ip in ips:
            classical_rules.append(f"IP-CIDR,{ip}")
            
        filename = f"{safe_name}_classical.yaml"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("payload:\n")
            for rule in classical_rules:
                f.write(f"  - '{rule}'\n")
        classical_path = f"ruleset/{filename}"
        
    if ipcidr_path or classical_path:
        generated_files.append({
            "cdn": cdn_name,
            "ipcidr": ipcidr_path,
            "classical": classical_path,
            "ips_count": len(ips),
            "asns_count": len(asns)
        })

readme_content = f"""# CDN Clash Rulesets

本项目自动同步 [mansourjabin/cdn-ip-database](https://github.com/mansourjabin/cdn-ip-database) 的官方 CDN IP 数据库，并将其转换为 Clash / Mihomo 兼容的 Rule Provider Rulesets 格式。

数据每天由 GitHub Actions 自动构建更新。

## 规则订阅地址列表

| CDN 提供商 | 规则数 (IP / ASN) | `ipcidr` 类型 Ruleset | `classical` 类型 Ruleset |
| :--- | :---: | :--- | :--- |
"""

for item in sorted(generated_files, key=lambda x: x["cdn"]):
    cdn = item["cdn"]
    counts = f"{item['ips_count']} / {item['asns_count']}"
    
    if item["ipcidr"]:
        ipcidr_url = f"https://raw.githubusercontent.com/{github_repo}/main/{item['ipcidr']}"
        ipcidr_link = f"[订阅链接]({ipcidr_url})"
    else:
        ipcidr_link = "-"
        
    if item["classical"]:
        classical_url = f"https://raw.githubusercontent.com/{github_repo}/main/{item['classical']}"
        classical_link = f"[订阅链接]({classical_url})"
    else:
        classical_link = "-"
        
    readme_content += f"| {cdn} | {counts} | {ipcidr_link} | {classical_link} |\n"

readme_content += """
## 使用方法

在你的 Clash / Mihomo 配置文件中，像这样引用 Ruleset：

```yaml
rule-providers:
  cloudflare-ip:
    type: http
    behavior: ipcidr
    url: "https://raw.githubusercontent.com/{github_repo}/main/ruleset/cloudflare_ipcidr.yaml"
    path: ./ruleset/cloudflare_ipcidr.yaml
    interval: 86400

  cloudflare-classical:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/{github_repo}/main/ruleset/cloudflare_classical.yaml"
    path: ./ruleset/cloudflare_classical.yaml
    interval: 86400

rules:
  # 使用 ipcidr 类型
  - RULE-SET,cloudflare-ip,DIRECT
  
  # 或者使用 classical 类型（支持 ASN 匹配，需客户端配置本地 GeoLite2-ASN 数据库）
  - RULE-SET,cloudflare-classical,DIRECT
```
""".replace("{github_repo}", github_repo)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Rulesets and README.md generated successfully!")
