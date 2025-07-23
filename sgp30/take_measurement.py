"""
Tool to read temperature, pressure and humidty measured by a BME280 chip connected to a
Raspberry Pi

Author: William Jay (wjay)
"""

import time

from sgp30 import SGP30


def main():

    # Initialise sensor class
    sgp30 = SGP30()

    # Connect to sensor
    sgp30.start_measurement()

    # Take measurement
    result = sgp30.get_air_quality()

    print(result)


if __name__ == "__main__":

   main() 
