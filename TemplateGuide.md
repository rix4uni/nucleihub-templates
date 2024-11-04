# Guide to Nuclei Templating

![Static Badge](https://img.shields.io/badge/Nuclei-Templating%20Guide-green)

Welcome to the comprehensive guide on Nuclei templating! Here, we'll walk through the fundamentals of creating custom templates for the [Nuclei](https://github.com/projectdiscovery/nuclei) engine, best practices, and some handy tips and tricks.

---

## Table of Contents
1. [Introduction to Nuclei Templates](#introduction)
2. [Template Structure](#structure)
3. [Matchers and Extractors](#matchers)
4. [Advanced Features](#advanced)
5. [Best Practices](#best-practices)
6. [Conclusion](#conclusion)

---

<a name="introduction"></a>
## 📘 Introduction to Nuclei Templates

Nuclei templates are essentially YAML formatted scripts that instruct the Nuclei engine on what to look for when scanning targets. They are pivotal in identifying vulnerabilities, misconfigurations, or informational insights about a target.

---

<a name="structure"></a>
## 🏗️ Template Structure

A basic Nuclei template consists of:

```yaml
id: unique-id-for-template

info:
  name: Template Name
  author: Your Name
  severity: low|medium|high|critical|info
  description: Short description about the template.

requests:
  - raw:
      - |
        GET /path HTTP/1.1
        Host: {{Hostname}}

    matchers:
      - type: word
        words:
          - "specific-string-to-look-for"
```

---

<a name="matchers"></a>
## 🎯 Matchers and Extractors

**Matchers**:
Matchers are conditions that must be satisfied for a request to be considered a match.

- **Word Matcher**: Matches if a word or set of words are found in the HTTP response body.
- **Regex Matcher**: Uses regular expressions to identify matches.
- **Status Matcher**: Matches based on the HTTP response status code.
  
**Extractors**:
Extractors are used to extract and display specific information from the HTTP response.

- **Regex Extractor**: Pulls out specific pieces of data using regular expressions.

---

<a name="advanced"></a>
## 🚀 Advanced Features

1. **Parallelism**: Nuclei can run multiple requests in parallel. 
2. **Workflows**: Combining multiple templates to be executed in a particular order.

---

<a name="best-practices"></a>
## ⚙️ Best Practices

- **Always test your templates** on environments where you have permission to scan.
- **Keep the template simple**. Complexity can lead to false positives/negatives.
- **Stay updated** with the latest vulnerabilities and techniques.
  
---

<a name="conclusion"></a>
## 📝 Conclusion

Nuclei templating is an empowering feature, enabling the community to share, reuse, and benefit from each other's knowledge. Always strive to improve, refine, and expand your templates. Happy scanning!

---

Remember, this is a concise guide. Depending on your knowledge and the intricacies you'd like to cover, you can expand on the sections or even add new ones.