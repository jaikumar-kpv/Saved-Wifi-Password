import subprocess

def get_wifi_password(ssid):
  """Retrieves the Wi-Fi password for a given SSID on Windows.

  Args:
    ssid: The name of the Wi-Fi network (SSID).

  Returns:
    The Wi-Fi password, or None if the network is not found or an error occurs.
  """
  try:
    command = f'netsh wlan show profile name="{ssid}" key=clear'
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    output = result.stdout

    if "Security settings" in output:
        for line in output.splitlines():
            if "Content" in line:
                password = line.split(":")[1].strip()
                return password
    else:
        return None  # Profile not found or no password

  except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")
    return None
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return None
def get_all_wifi_passwords():
    """Retrieves all stored wifi passwords."""
    try:
        command_profile = "netsh wlan show profiles"
        result_profile = subprocess.run(command_profile, capture_output=True, text=True, check=True)
        profiles_output = result_profile.stdout
        wifi_names = []
        for line in profiles_output.splitlines():
            if "All User Profile" in line:
                ssid = line.split(":")[1].strip().strip('"')
                wifi_names.append(ssid)

        wifi_passwords = {}
        for ssid in wifi_names:
            password = get_wifi_password(ssid)
            if password:
                wifi_passwords[ssid] = password
        return wifi_passwords

    except subprocess.CalledProcessError as e:
        print(f"Error retrieving all wifi passwords: {e}")
        return None
    except Exception as e:
         print(f"An unexpected error occurred: {e}")
         return None

# Example usage:
ssid_to_find = "Your_WiFi_SSID" # Replace with the actual SSID.
password = get_wifi_password(ssid_to_find)

if password:
  print(f"Password for {ssid_to_find}: {password}")
else:
  print(f"Password for {ssid_to_find} not found.")

all_passwords = get_all_wifi_passwords()

if all_passwords:
  print("\nAll stored Wi-Fi passwords:")
  for ssid, password in all_passwords.items():
    print(f"{ssid}: {password}")