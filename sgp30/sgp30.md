# Interacting with the SGP30 Sensor #

This document outlines how to set up the SGP30 sensor to communicate with the Raspberry Pi.

## Set up ##

### Connect to Raspberry Pi ###

Connect the following BME280 pins to the corresponding Raspberry Pi pins:

| **SGP30** | **Raspberry Pi** | **Pin Number** |
| --------- | ---------------- | -------------- |
| 2-6V      | 3v3 Power        | 1              |
| SDA       | GPIO 2           | 3              |
| SCL       | GPIO 3           | 5              |
| GND       | Ground           | 11             |

See the diagram of the Raspberry Pi pins [here](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio).




### Installation ###

```
python3 -m pip install pimoroni-sgp30
```

If you get an error about the environment being externally managed, then try the below command:

```
python3 -m pip install pimoroni-sgp30 --break-system-packages
```
