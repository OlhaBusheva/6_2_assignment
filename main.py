import convertor

import csv


def clean_temperature(temp_str: str):
    return ''.join(filter(str.isdigit, temp_str))


def format_temperature(temp: float, unit: str):
    if unit == 'F':
        return f"{temp}°F"
    elif unit == 'C':
        return f"{temp}°C"


def convert_temperature(target_temp):
    # output_filename = 'converted_temperature.csv'
    with open('temperature.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        with open('converted_temperature.csv', 'w', newline='',
                  encoding='utf-8') as output_file:
            fieldnames = ['Date', 'Reading']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                original_temp_str = row['Reading'].strip()
                original_temp_cleaned = clean_temperature(original_temp_str)
                original_temp = int(original_temp_cleaned)
                unit = original_temp_str[-2:]

                if target_temp == 'C':
                    if unit == '°F':
                        converted_temp = (
                            convertor.temperature.conv_fahrenheit_to_celsius(
                                original_temp)
                        )
                    else:
                        converted_temp = original_temp
                elif target_temp == 'F':
                    if unit == '°C':
                        converted_temp = (
                            convertor.temperature.conv_celsius_to_fahrenheit(
                                original_temp)
                        )
                    else:
                        converted_temp = original_temp

                formatted_temp = format_temperature(int(converted_temp),
                                                    target_temp)
                writer.writerow({'Date': row['Date'], 'Reading':
                                 formatted_temp})


select_format = input("Print 'C' or 'F': ")
convert_temperature(select_format)
