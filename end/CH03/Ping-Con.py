#!




import platform
import os

print("Enter IP Address")
ip = input("")


ping_cmd = f"ping -n 1 -w 2 {ip}"
exit_code = os.system(ping_cmd)
print(exit_code)



