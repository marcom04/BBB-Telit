#!/bin/bash

# Establish a Point-to-Point connection from BeagleBone Black (rev. C), using
# - Telit GL865-QUAD GSM/GPRS module (http://www.telit.com/products/product-service-selector/product-service-selector/show/product/gl865-quad/)
# - Sakis3G script (https://github.com/RadiusNetworks/sakis3g).
# Must be executed as root.

# Access Point Name information
apn="ibox.tim.it"
apn_user="blank"	# leave "blank" unless your ISP requires specific credentials
apn_pass="blank"        # leave "blank" unless your ISP requires specific credentials
dial=*99#

# Telit module information
custom_tty="ttyO1"
baud=115200             # max baud rate for the Telit

# Sakis3G script location
sakis_path="/usr/bin/"

#   --pppd          use directly pppd instead of calling wvdial
#   --interactive   enable user interaction during script execution
cd $sakis_path
./sakis3g connect --pppd --interactive \
	APN=$apn \
	APN_USER=$apn_user \
	APN_PASS=$apn_pass \
	MODEM="OTHER" \
	OTHER="CUSTOM_TTY" \
	CUSTOM_TTY=$custom_tty \
	DIAL=$dial \
	BAUD=$baud
