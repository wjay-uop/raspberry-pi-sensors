#!/usr/bin/env python
"""
Tool to read temperature, pressure and humidty measured by a SGP30 chip connected to a
Raspberry Pi

Author: William Jay (wjay)
"""

import argparse

from sgp30 import SGP30


def main(verbose=False):

    # Initialise sensor class
    sgp30 = SGP30()

    if verbose:
        print("Starting measurement")
        print("Should take between 15 and 20 seconds")
    sgp30.start_measurement()

    if verbose:
        print("Calculating air quality")
    # Take measurement
    result = sgp30.get_air_quality()

    # Get results
    eco2 = result.equivalent_co2
    tvoc = result.total_voc

    # Display results
    print(f"Equivalent CO2:\t\t\t\t{eco2} ppm")
    print(f"Total Volatile Organic Compounds\t{tvoc} ppb")


if __name__ == "__main__":

    helpstring = (
        "Read the CO2 equivalent and Total Volatile Organic Compounds measured by a "
        "SGP30 device."
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
