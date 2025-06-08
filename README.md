# Saved Wi-Fi Password Viewer (Windows)

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A Python script that retrieves and displays the passwords of all Wi-Fi networks saved on a Windows machine.

---

## ⚠️ Disclaimer: For Educational & Ethical Use Only

This tool is intended for educational purposes and for individuals to recover their own lost Wi-Fi passwords from devices they have legitimate access to.

-   **Do not use this script on any computer you do not own or have explicit permission to access.**
-   Accessing saved passwords on a device without authorization is a breach of privacy and may be illegal in your jurisdiction.
-   The author is not responsible for any misuse or damage caused by this script. **Use it responsibly.**


---

## Description

Have you ever forgotten the password to a Wi-Fi network that your computer automatically connects to? This script solves that problem. It uses Python's `subprocess` module to interact with the Windows `netsh` command-line tool, which can reveal details about saved wireless network profiles, including their security keys (passwords).

The script can retrieve the password for a specific network or list the passwords for all saved networks on the system.

---

## Platform Compatibility

This script is designed to work **only on Windows operating systems**. It relies on the `netsh.exe` utility, which is specific to Windows and not available on macOS or Linux.

---

## Requirements

1.  **Windows OS**: Vista, 7, 8, 10, or 11.
2.  **Python 3.6** or newer.
3.  **Administrator Privileges**: The script must be run from a terminal with administrative rights to access the security keys of the Wi-Fi profiles.

---

## How to Use

1.  Clone the repository or download the `wifi_passwords.py` script.
2.  **Open Command Prompt or PowerShell as an Administrator.**
    -   Click the Start menu.
    -   Type `cmd` or `powershell`.
    -   Right-click on the result and select **"Run as administrator"**.
3.  Navigate to the directory where you saved the script.
    ```powershell
    cd C:\path\to\your\script
    ```
4.  Run the Python script:
    ```powershell
    python wifi_passwords.py
    ```

**Example Output:**

When you run the script, it will first attempt to find a password for the hardcoded example SSID and then list all other saved network passwords.
