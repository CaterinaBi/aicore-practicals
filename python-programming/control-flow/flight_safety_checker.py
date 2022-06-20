# Given 2 parameters, altitude (ft) and airspeed (knots)
altitude_in_feet = 0
airspeed_in_knots = 0

# Write a program that categorises entries into 'safe flying' and 'unsafe flying' based on the following criteria:
# An altitude below 100ft or above 50000ft is considered unsafe flying.
# An airspeed below 60 knots or above 500 knots is considered unsafe flying.
# If altitude and airspeed are outside these ranges, the flight is considered as safe.
# CLUE: You will have to figure out the syntax for using and/or keywords in if statements
if altitude_in_feet < 100 or altitude_in_feet > 50000:
        print('Unsafe flying!')
elif airspeed_in_knots < 60 or airspeed_in_knots > 500:
    print('Unsafe flying!')
else:
    print('Safe flying!')

# Try to write this as cleanly as possible and test your code with the following by substituting in again:
# Altitude: 25000ft, Airspeed: 300 knots  # safe
# Altitude: 50001ft, Airspeed: 250 knots  # unsafe
# Altitude: 90ft, Airspeed: 125 knots     # unsafe
