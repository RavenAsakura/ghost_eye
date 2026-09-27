# Changelog

## Unreleased — Python 3.14 standard-library fork

This fork modernizes Ghost Eye so it can run without Python package
installation through `pip`, `pip3`, or `pipx`.

### Updated

- **`ghost_eye.py`**
  - Removed third-party imports: `beautifulsoup4`, `cloudscraper`,
    `python-nmap`, `requests`, `urllib3`, and `webtech`.
  - Replaced HTTP, cookie, HTML parsing, crawling, CMS detection, and
    certificate-transparency functionality with Python standard-library code.
  - Added graceful handling when optional Linux tools are unavailable.
  - Updated code for Python 3.14 compatibility.
- **`README.md`**
  - Replaced pip-based setup instructions with `apt` installation instructions.
  - Documented the fork, original project, license, system tools, and runtime
    instructions.
- **`requirements.txt`**
  - Removed because the project no longer has third-party Python dependencies.
- **`CHANGELOG.md`**
  - Added this fork's change summary.

### Runtime requirements

The Python code uses only the standard library. Optional menu features may
use Linux commands such as `nmap`, `dig`, `whois`, `http`, `mtr`, EtherApe,
and GNOME Terminal.
