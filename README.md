BBB-Telit
=========

A collection of utilities that can be used to connect a BeagleBone Black (rev. C)
to a Point-to-Point network through a Telit GL865 GSM/GPRS module.

Tested on Debian Wheezy.

#### Tools
* [BeagleBone Black rev. C with Debian Wheezy](http://beagleboard.org/black)
* [Telit GL865-QUAD module](http://www.telit.com/products/product-service-selector/product-service-selector/show/product/gl865-quad/)
* [Adafruit BBIO Library](https://github.com/adafruit/adafruit-beaglebone-io-python)
* [Sakis3G](https://github.com/RadiusNetworks/sakis3g)

#### GPIO setup
Connect pin **P9\_24 (UART1\_TXD)** of the BBB to the **RX** channel of the Telit.  
Connect pin **P9\_26 (UART1\_RXD)** of the BBB to the **TX** channel of the Telit.

#### Usage
Install the Adafruit BBIO library (complete guide [here](https://github.com/adafruit/adafruit-beaglebone-io-python)):
  ```
  sudo ntpdate pool.ntp.org
  sudo apt-get update
  sudo apt-get install build-essential python-dev python-pip -y
  easy_install -U distribute
  sudo pip install Adafruit_BBIO
  ```

Download Sakis3G from [here](https://github.com/RadiusNetworks/sakis3g), extract
the zip and put the content in `/usr/bin`

Install ppp:  
  ```
  sudo apt-get install ppp
  ```

Use tinit.py to open the serial connection towards the Telit and check the
communication. If you connected the Telit to the UART1 pins of the BBB you don't
have to edit anything. Launch the script with root privileges:  
  ```
  sudo python tinit.py
  ```

In tconnect.sh, update the lines  
  ```
  apn
  apn_user
  apn_pass
  dial
  ```  
  with your APN data.  
  Then, launch the script with root privileges to instaurate the
connection:  
  ```
  sudo ./tconnect.sh
  ```

To close the Point-to-Point connection, launch tdisconnect.sh with root privileges:  
  ```
  sudo ./tdisconnect.sh
  ```
