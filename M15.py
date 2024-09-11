def convert_length(value, from_unit, to_unit):
    length_units = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34,
        'nautical mile': 1852.0  # Added key to induce error
    }
    
    # Convert from source unit to meters
    value_in_meters = value * length_units[from_unit]  # This line will cause a KeyError if 'from_unit' is 'nautical mile'
    # Convert from meters to target unit
    converted_value = value_in_meters / length_units[to_unit]
    return converted_value

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilogram': 1.0,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495
    }
    
    # Convert from source unit to kilograms
    value_in_kilograms = value * weight_units[from_unit]
    # Convert from kilograms to target unit
    converted_value = value_in_kilograms / weight_units[to_unit]
    return converted_value

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32

    return None

# Example Usage with Mutation
try:
    length = convert_length(10, 'nautical mile', 'kilometer')
    print(f"10 nautical miles is {length} kilometers.")
except KeyError as e:
    print(f"Error: {e}")

weight = convert_weight(5, 'kilogram', 'pound')
print(f"5 kilograms is {weight} pounds.")

temperature_result_c_to_f = convert_temperature(25, 'celsius', 'fahrenheit')
print(f"25 Celsius in Fahrenheit: {temperature_result_c_to_f}")

temperature_result_f_to_k = convert_temperature(32, 'fahrenheit', 'kelvin')
print(f"32 Fahrenheit in Kelvin: {temperature_result_f_to_k}")

temperature_result_c_to_k = convert_temperature(25, 'celsius', 'kelvin')
print(f"25 Celsius in Kelvin: {temperature_result_c_to_k}")
