# 🚀 Frappe Bench Ultimate Setup Guide

📚 This comprehensive guide provides everything you need to master Frappe Bench setup and deployment.


## ⭐ Prerequisites

Before diving in, ensure your system meets these essential requirements:


| Component | Version | Purpose |
|-----------|---------|---------|
| **Python 3** | Latest | Core runtime environment |
| **MariaDB** | ≥ 10.3 | Robust database solution |
| **Redis**   | ≥ 5.0  | High-performance caching |
| **Supervisor** | Latest | Process orchestration |
| **git**     | ≥ 2.0  | Version control system |

## 📝 Installation Steps

### 1️⃣ Install Dependencies

First, update your package index and install essential dependencies:

```bash
sudo apt update && sudo apt install -y python3-dev python3-pip mariadb-server redis supervisor
```

> [!NOTE] Make sure your system has sufficient disk space (> 5GB recommended)

### 2️⃣ Install Frappe Bench

Install Frappe Bench globally using pip:

```bash
pip install frappe-bench
```

> [!TIP] Use a virtual environment for better dependency management

### 3️⃣ Initialize Frappe Bench

Set up your Frappe Bench environment with version-14:

```bash
bench init frappe-bench --frappe-branch version-14
cd frappe-bench
```

> [!IMPORTANT] This step creates the foundation for your Frappe ecosystem

### 4️⃣ Create a New Site

Establish your site (replace `mysite.local` with your desired domain):

```bash
bench new-site mysite.local
```

> [!WARNING] Secure your database credentials carefully

### 5️⃣ Create Custom App

Develop your custom app (customize `myapp` to your needs):

```bash
bench new-app myapp
```

> [!CAUTION] Follow naming conventions for maintainability

### 6️⃣ Install App on Site

Deploy your app to the site:

```bash
bench --site mysite.local install-app myapp
```

> [!TIP] Test thoroughly before production deployment

## 🚀 Additional Configuration

### Development Server Setup

Launch the development server:

```bash
bench start
```

Access your site at [http://mysite.local](http://mysite.local)

> [!NOTE] Ensure hosts file maps to 127.0.0.1

## 🎯 Troubleshooting Guide

If you encounter issues, verify these critical points:

1. ⚙️ Dependency Verification
   - All prerequisites installed
   - Correct versions confirmed
   - No conflicts present

2. 🔄 Service Status
   - MariaDB running: `sudo service mariadb status`
   - Redis active: `redis-cli ping`
   - Supervisor operational: `supervisorctl status`

3. 🛡️ Security Checks
   - Strong passwords configured
   - Firewall settings verified
   - Backup strategy implemented

4. 🌐 Network Configuration
   - Hosts file properly configured
   - Port availability confirmed
   - DNS resolution working

## 🏆 Best Practices

🔹 Regular backups
🔹 Monitor logs frequently
🔹 Keep dependencies updated
🔹 Document customizations
🔹 Test thoroughly before deployment

## 📋 Hostname Configuration Guide

### For Linux/Ubuntu Systems

1. Open your hosts file:
```bash
sudo nano /etc/hosts
```

2. Add this line at the end:
```bash
127.0.0.1 mysite.local
```

3. Save and exit (Ctrl+X, then Y, then Enter)

4. Verify the configuration:
```bash
ping mysite.local
```

### For Windows/WSL Systems

1. Create or edit the WSL configuration file:
```bash
sudo nano /etc/wsl.conf
```

2. Add these lines:
```ini
[network]
hostname = mysite.local
generateHosts = false
```

3. Update the hosts file:
```bash
sudo nano /etc/hosts
```

4. Add:
```bash
127.0.0.1 mysite.local
127.0.0.1 localhost
```

5. Restart WSL:
```bash
wsl --shutdown
```

Then relaunch your WSL distribution.

### For macOS Systems

1. Open the hosts file:
```bash
sudo nano /etc/hosts
```

2. Add:
```bash
127.0.0.1 mysite.local
```

3. Save and exit (Ctrl+X, then Y, then Enter)

4. Flush DNS cache:
```bash
sudo killall -HUP mDNSResponder
```

---

Need help? Create an issue in our repository for dedicated support!

[![Open Issues](https://img.shields.io/github/issues/DavidWells/advanced-markdown)](https://github.com/DavidWells/advanced-markdown/issues)
[![Stars](https://img.shields.io/github/stars/DavidWells/advanced-markdown)](https://github.com/DavidWells/advanced-markdown/stargazers)
[![License](https://img.shields.io/github/license/DavidWells/advanced-markdown)](https://github.com/DavidWells/advanced-markdown/blob/master/LICENSE)

[^1]: [Create an issue here](https://github.com/DavidWells/advanced-markdown/issues/new)
