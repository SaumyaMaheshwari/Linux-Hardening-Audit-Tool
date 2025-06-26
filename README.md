# Linux Hardening Audit Tool

# Overview

This is a simple Python script to check basic Linux system hardening configurations.
This tool is designed to assist with identifying insecure settings and ensuring a baseline level of system security.

# What It Does

- Checks if root login via SSH is disabled
- Checks file permissions for `/etc/passwd` and `/etc/shadow`
- Checks if the UFW firewall is enabled

# Commands Used

mkdir linux-hardening-audit
cd linux-hardening-audit
nano audit_tool.py
sudo python3 audit_tool.py


