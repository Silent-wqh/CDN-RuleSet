# CDN Clash Rulesets

本项目自动同步 [mansourjabin/cdn-ip-database](https://github.com/mansourjabin/cdn-ip-database) 的官方 CDN IP 数据库，并将其转换为 Clash / Mihomo 兼容的 Rule Provider Rulesets 格式，以及 Sing-box 兼容的 `.srs` 格式。

数据每天由 GitHub Actions 自动构建更新。

## 规则订阅地址列表

| CDN 提供商 | 规则数 (IP / ASN) | `ipcidr` 类型 Ruleset (Clash) | `classical` 类型 Ruleset (Clash) | Sing-box `.srs` |
| :--- | :---: | :--- | :--- | :--- |
| Akamai | 9 / 39 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/akamai_ipcidr.yaml) | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/akamai_classical.yaml) | [akamai_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/akamai_ipcidr.srs) |
| ArvanCloud | 12 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/arvancloud_ipcidr.yaml) | - | [arvancloud_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/arvancloud_ipcidr.srs) |
| BelugaCDN | 17 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/belugacdn_ipcidr.yaml) | - | [belugacdn_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/belugacdn_ipcidr.srs) |
| Bunny | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/bunny_classical.yaml) | - |
| CDN77 | 35 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cdn77_ipcidr.yaml) | - | [cdn77_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cdn77_ipcidr.srs) |
| CDNetworks | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cdnetworks_classical.yaml) | - |
| CacheFly | 10 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cachefly_ipcidr.yaml) | - | [cachefly_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cachefly_ipcidr.srs) |
| CloudFront | 48 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cloudfront_ipcidr.yaml) | - | [cloudfront_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cloudfront_ipcidr.srs) |
| Cloudflare | 22 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cloudflare_ipcidr.yaml) | - | [cloudflare_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cloudflare_ipcidr.srs) |
| DDoS-Guard | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/ddos-guard_classical.yaml) | - |
| EdgeNext | 0 / 2 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/edgenext_classical.yaml) | - |
| Edgecast | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/edgecast_classical.yaml) | - |
| Edgio | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/edgio_classical.yaml) | - |
| Fastly | 21 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/fastly_ipcidr.yaml) | - | [fastly_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/fastly_ipcidr.srs) |
| Gcore | 1829 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/gcore_ipcidr.yaml) | - | [gcore_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/gcore_ipcidr.srs) |
| Google Cloud | 1045 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/google_cloud_ipcidr.yaml) | - | [google_cloud_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/google_cloud_ipcidr.srs) |
| Imperva | 12 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/imperva_ipcidr.yaml) | - | [imperva_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/imperva_ipcidr.srs) |
| IranServer | 17 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/iranserver_ipcidr.yaml) | - | [iranserver_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/iranserver_ipcidr.srs) |
| Limelight | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/limelight_classical.yaml) | - |
| Medianova | 62 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/medianova_ipcidr.yaml) | - | [medianova_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/medianova_ipcidr.srs) |
| ParsPack | 62 / 0 | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/parspack_ipcidr.yaml) | - | [parspack_ipcidr.srs](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/parspack_ipcidr.srs) |
| Qrator | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/qrator_classical.yaml) | - |
| StackPath | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/stackpath_classical.yaml) | - |
| StormWall | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/stormwall_classical.yaml) | - |
| Sucuri | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/sucuri_classical.yaml) | - |
| X4B | 0 / 1 | - | [订阅链接](https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/x4b_classical.yaml) | - |

## 使用方法

### Clash / Mihomo

在你的 Clash / Mihomo 配置文件中，像这样引用 Ruleset：

```yaml
rule-providers:
  cloudflare-ip:
    type: http
    behavior: ipcidr
    url: "https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cloudflare_ipcidr.yaml"
    path: ./ruleset/cloudflare_ipcidr.yaml
    interval: 86400

  cloudflare-classical:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cloudflare_classical.yaml"
    path: ./ruleset/cloudflare_classical.yaml
    interval: 86400

rules:
  # 使用 ipcidr 类型
  - RULE-SET,cloudflare-ip,DIRECT
  
  # 或者使用 classical 类型（支持 ASN 匹配，需客户端配置本地 GeoLite2-ASN 数据库）
  - RULE-SET,cloudflare-classical,DIRECT
```

### Sing-box

在你的 Sing-box 配置文件中，像这样引用 rule-set：

```json
{
  "route": {
    "rule_set": [
      {
        "tag": "cloudflare-ip",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/Silent-wqh/CDN-RuleSet/main/ruleset/cloudflare_ipcidr.srs",
        "download_detour": "proxy"
      }
    ],
    "rules": [
      {
        "rule_set": "cloudflare-ip",
        "outbound": "direct"
      }
    ]
  }
}
```
