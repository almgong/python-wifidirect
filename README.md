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

##Testing
For testing on a virtual machine, you can use mac80211_hwsim. I followed the instructions (here)[https://github.com/wertarbyte/hostap/blob/master/tests/hwsim/example-setup.txt].

The gist of it is to install backports:

```shell
wget http://www.kernel.org/pub/linux/kernel/projects/backports/stable/v3.19-rc1/backports-3.19-rc1-1.tar.xz
tar xJf backports-3.19-rc1-1.tar.xz
cd backports-3.19-rc1-1

cat > defconfigs/mac80211_hwsim <<EOF
CPTCFG_CFG80211=m
CPTCFG_CFG80211_WEXT=y
CPTCFG_MAC80211=m
CPTCFG_MAC80211_LEDS=y
CPTCFG_MAC80211_MESH=y
CPTCFG_WLAN=y
CPTCFG_MAC80211_HWSIM=m
EOF

make defconfig-mac80211_hwsim
make
sudo make install
```

After installing, start the simulation software by running `sudo modprobe mac80211_hwsim radios=[#]`. Pass in the desired number of wireless radio interfaces as needed. 


Temp notes:
To start up wpa_supplicant, run: `sudo ./wpa_supplicant -Dnl80211 -iwlan0 -cwpa_supplicant.conf` in the wpa_supplicant build directory (this is assuming you did not run setup.sh)

To run wpa_cli: `sudo ./wpa_cli -i wlan0`
