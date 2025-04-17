#
#
#
# import librarit
import os
import subprocess
import time

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Krijon 2000 file te ndryshem me tulifar file type
for i in range(2000):
    file_name = f"file_{i+1}.txt"
    file_path = os.path.join(desktop, file_name)
    with open(file_path, "w") as f:
        f.write(f"Kjo është skedari numër {i+1}.\n")

# Hap 1000  file prej tyne dhe i hap qata
for i in range(1000):
    file_name = f"file_{i+1}.txt"
    file_path = os.path.join(desktop, file_name)
    subprocess.Popen(['notepad.exe', file_path])
    time.sleep(0.1)  # vones per me qel sa tmun file

