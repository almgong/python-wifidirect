# Linux WiFi Direct

Toy project to see if I can get devices running on Linux to connect
via WiFiDirect. The most important thing is to see if I can do this in Python
(and later to use Docker containers for portability). Currently this is in the
form of a command line program.

##Setup
Run `setup.sh`. Make any additional configuration as needed.

##Commands
Define user commands in `commands.json`. See `main.py` for example linking
of commands.

##wpa_supplicant
Currently using (wpa_supplicant)[https://wiki.archlinux.org/index.php/WPA_supplicant]
to bootstrap.


