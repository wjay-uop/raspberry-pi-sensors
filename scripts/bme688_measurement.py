#!/usr/bin/env python
"""
Tool to interact with the BME668 sensor with a Raspberry Pi

Requires the bme680 module by pimoroni:
    https://github.com/pimoroni/bme680-python

Based on examples provided by Pimoroni:
    https://github.com/pimoroni/bme680-python/tree/main/examples

Author William Jay (wjay)
"""

import argparse
import time

import bme680


def main(verbose=False):
    """

    """
    
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    #except (RuntimeError, IOError):
    #sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    
    # These calibration data can safely be commented
    # out, if desired.

    if verbose:
        # Iterate through the attributes within the calibration_data object
        for name in dir(sensor.calibration_data):
    
            # Ignore internal attributes
            if not name.startswith('_'):
                value = getattr(sensor.calibration_data, name)
    
                # Assume that all other atrributes are calibration gains if they are
                # integers
                if isinstance(value, int):
                    print(f"{name}: {value}")

    # TODO: No calibration gains are applied here, this assumes that it is handled
    # within the bme688-python

    # These oversampling settings can be tweaked to change the balance between accuracy
    # and noise in the data
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

    if verbose:
        # Iterate through data attributes
        for name in dir(sensor.data):
            value = getattr(sensor.data, name)
        
            # If the attribute is not internal, then print its name and value
            if not name.startswith('_'):
                print(f"{name}: {value}")

    # TODO: What is this? 
    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)
    sensor.select_gas_heater_profile(0)

    # TODO: What is this?
    # Up to 10 heater profiles can be configured, each
    # with their own temperature and duration.
    # sensor.set_gas_heater_profile(200, 150, nb_profile=1)
    # sensor.select_gas_heater_profile(1)
    
    print("Taking environment measurments...")
    while not sensor.get_sensor_data():
        time.sleep(0.1)

    temperature = sensor.data.temperature
    pressure = sensor.data.pressure
    humidity = sensor.data.humidity

    print(f"Temperature:\t{temperature} °C")
    print(f"Pressure:\t{pressure} hPa")
    print(f"Humidity:\t{humidity} %")

    # TODO: I haven't seen this become True yet...
    print("Taking gas measurements...")
    while not sensor.data.heat_stable:
        gas_resistance = sensor.data.gas_resistance
        time.sleep(0.1)

    print(f"Gas Resistance:\t{gas_resistance} °C")

    
if __name__ == "__main__":

    helpstring = (
        "Read the temperature, pressure and humidty measured by a BME280 sevice."
    )
    parser = argparse.ArgumentParser(
        description=helpstring, formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print more information"
    )

    args = parser.parse_args()

    # Run function
    main(args.verbose)
