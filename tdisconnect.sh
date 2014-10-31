#!/bin/bash

# Close Point-to-Point connection using the Sakis3G script.
# Must be executed as root.

# Sakis3G script location
sakis_path="/usr/bin/"

cd sakis_path
./sakis3g --interactive disconnect
