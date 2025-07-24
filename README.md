# Collecting environmental data with Raspberry Pi #

This repository contains instructions and programmes to interact with simple sensors designed for setting up "smart home" devices.

These have been tested on a Raspberry Pi 4 Model B running Raspberry Pi OS 6.12.


## Getting Started  ##


### The Raspberry Pi ###


The Raspberry Pi is a mini computer. It was origionally created as an educational tool for getting students into computer science but has been a huge sucess in enabling a huge range of projects, from building cube satellites to hobbyist weather stations.


### Raspberry Pi Installation ###

This assumes that you have access to a Raspberry Pi with an operating system installed - these are availible from LabPlus.

If you have a brand new Raspberry Pi that needs the operating system installed, this is an easy process on the Raspberry Pi which you can follow [here](https://www.raspberrypi.com/software/).


### The Linux Command Line ###

Some basic knowlage of the Linux command line is required to run the following tool. Don't be scared.

[Here](docs/command_line.md) is a basic guide of the command line tools you 


## Clone this Repository ##


Using `git` in a terminal on a Raspberry Pi, you can clone all the code in this repository with the following command:
```bash
git clone https://github.com/wjay-uop/raspberry-pi-sensors.git
```

This will create a new directory called `raspberry-pi-sensors` containing this repository.


## Sensors ##

Follow the links below for instructions for specific sensors.


### BME280 ###

The BME280 measures temperature, pressure and humidity.

[Instructions](docs/bme280.md)


### BME688  ###

The BME688 measures temperature, pressure, humidity and air quality.

[Instructions](docs/bme688.md)


### SGP30 ###

The SGP30 measures total volitile compounds (TVOC) and equivilent CO2 (eCO2).

[Instructions](docs/sgp30.md)

