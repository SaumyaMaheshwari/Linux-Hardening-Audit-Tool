import os

def check_root_login_disabled():
    try:
        with open('/etc/ssh/sshd_config', 'r') as file:
            for line in file:
                if line.strip().startswith("PermitRootLogin"):
                    return "Root login is disabled" if "no" in line else "Root login is enabled"
        return "Could not find 'PermitRootLogin' setting"
    except Exception as e:
        return f"Error reading sshd_config: {e}"

def check_password_file_permissions():
    try:
        passwd_perm = oct(os.stat('/etc/passwd').st_mode)[-3:]
        shadow_perm = oct(os.stat('/etc/shadow').st_mode)[-3:]
        return {
            "passwd": "/etc/passwd permissions are OK" if passwd_perm == "644" else f"/etc/passwd has wrong permissions: {passwd_perm}",
            "shadow": "/etc/shadow permissions are OK" if shadow_perm == "640" else f"/etc/shadow has wrong permissions: {shadow_perm}"
        }
    except Exception as e:
        return {"passwd": f"Error: {e}", "shadow": f"Error: {e}"}

def check_firewall_status():
    try:
        status = os.popen("sudo ufw status").read()
        return "Firewall is enabled" if "active" in status else "Firewall is not enabled"
    except Exception as e:
        return f"Error checking firewall: {e}"

def run_audit():
    print("Running Linux Hardening Audit...\n")
    print(check_root_login_disabled())
    perms = check_password_file_permissions()
    print(perms['passwd'])
    print(perms['shadow'])
    print(check_firewall_status())

if __name__ == "__main__":
    run_audit()
