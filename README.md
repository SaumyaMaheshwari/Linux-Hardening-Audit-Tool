# Linux Hardening Audit Tool

## Overview

This is a simple Python script that checks basic Linux system hardening configurations.  
It helps identify insecure settings and ensures a baseline level of system security.

## What It Does

- Checks if root login via SSH is disabled  
- Checks file permissions for `/etc/passwd` and `/etc/shadow`  
- Checks if the UFW firewall is enabled  

## Commands Used

```bash
mkdir linux-hardening-audit
cd linux-hardening-audit
nano audit_tool.py
sudo python3 audit_tool.py



