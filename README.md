# Linux WiFi Direct

Toy project to see if I can get devices running on Linux to connect
via WiFiDirect. The most important thing is to see if I can do this in Python
(and later to use Docker containers for portability). Currently this is in the
form of a command line program.

##Setup
Run `setup.sh`. Make any additional configuration as needed.

##wpa_supplicant
Currently using (wpa_supplicant)[https://wiki.archlinux.org/index.php/WPA_supplicant]
to bootstrap.

##Known issues
Sometimes the .config file will need to be recopied (will look into this later) to wpa/wpa_supplicant.../wpa_supplicant/ directory in order to build the executables. 


