"""
File: escape_velocity.py
Author: Seth Leslie
Date: 09/09/2024
Description: This program calculates the escape velocity based on the user input.
"""

launch_body = input("Which body are you launching from?" )
launch_mass = float(input("Enter the mass of the planet in scientific notation with the floating number first:"))
launch_power = int(input("What power of 10 is this?"))
launch_radius = float(input("Enter the coefficient of the scientific notation of the radius from the center of your lau\
nch body."))
launch_power_2 = int(input("What power of 10 is this?"))

print("The escape velocity required for", launch_body, "is", round(((2*((6.67*(10**-11))*launch_mass *
                                                                        (10 **launch_power)))/launch_radius *
                                                                    (10 **launch_power_2))**(1/2), 3), "m/s")
