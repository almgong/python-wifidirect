#!/bin/bash

###
# This setup script needs some testing, but should be enough to get things 
# downloaded and installed.
###
WPA_VERSION=2.6
cwd=$(pwd)

echo "Installing some dependencies..."
sudo apt-get update
sudo apt-get install -y libcurl4-openssl-dev libnl-3-dev libnl-genl-3-dev

echo "Downloading wpa_supplicant binaries package..."
wget http://w1.fi/releases/wpa_supplicant-$WPA_VERSION.tar.gz
mkdir wpa
tar -zxvf wpa_supplicant-$WPA_VERSION.tar.gz -C wpa/

echo "Building executables..."
cp $cwd/src/.wpa_config $cwd/wpa/wpa_supplicant-$WPA_VERSION/wpa_supplicant/.config
cp $cwd/src/.wpa_supplicant.conf $cwd/wpa/wpa_supplicant-$WPA_VERSION/wpa_supplicant/wpa_supplicant.conf
cd $cwd/wpa/wpa_supplicant-$WPA_VERSION/src && make
cd $cwd/wpa/wpa_supplicant-$WPA_VERSION/wpa_supplicant && make BINDIR=/sbin LIBDIR=/lib
cd $cwd

echo WPA_EXEC_PATH=$cwd/wpa/wpa_supplicant-$WPA_VERSION/wpa_supplicant > .WPA_PATH

echo "cleaning up..."
rm wpa_supplicant-$WPA_VERSION.tar.gz

echo "Completed."

echo \n\n
echo "Would you like to start wpa_supplicant now?"
select yn in "Yes" "No"; do
	case $yn in
		Yes ) echo "it worked well."; break;;
		No ) break;;
	esac
done