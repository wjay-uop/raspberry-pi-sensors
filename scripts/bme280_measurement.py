#!/usr/bin/env python
"""
Tool to read temperature, pressure and humidty measured by a BME280 chip connected to a
Raspberry Pi

Author: William Jay (wjay)
"""

import argparse
import smbus2
import bme280


def main(address: int = 0x76):

    bus = smbus2.SMBus(1)
    
    calibration_params = bme280.load_calibration_params(bus, address)

    data = bme280.sample(bus, address, calibration_params)

    temperature_celcius = data.temperature
    pressure = data.pressure
    humidity = data.humidity
    
    print(f"Temperature:\t{temperature_celcius} °C")
    print(f"Pressure:\t{pressure} hPa")
    print(f"Humidity:\t{humidity} %" )


if __name__ == "__main__":

    helpstring = (
        "Read the temperature, pressure and humidty measured by a BME280 sevice."
    )
    parser = argparse.ArgumentParser(
        description=helpstring, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # FIXME: Handling hex input as integer doesn't work
    parser.add_argument(
        "--address",
        type=int,
        default=0x76,
        help=(
            "Base 16 (hexidecimal) registry address for the BME280 chip. Should be "
            "found using `i2cdetect -y 1` and prefixing with `0x`"
        ),
    )
    args = parser.parse_args()

    # Run function
    main(args.address)
