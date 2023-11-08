import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):#It is
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt_object=datetime.fromisoformat(iso_string)
    formatted_string=dt_object.strftime("%A %d %B %Y")
    return formatted_string


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit_float=float(temp_in_farenheit)
    temp_in_celcius=(temp_in_farenheit_float-32)*5/9
    temp_in_celcius_rounded=round(temp_in_celcius,1)
    return temp_in_celcius_rounded


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data=[float(value) for value in weather_data]
    total=sum(weather_data)
    mean=total/len(weather_data)
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    
    with open(csv_file, mode='r', ) as file:
        csv_reader = csv.reader(file)
        headers=next(csv_reader)

        for row in csv_reader:
            if len(row) >= 2:
             converted_row = [row[0]] + [int(cell) for cell in row[1:]]
             data.append(converted_row)
    
    return data
   

   

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if not weather_data:
        return ()
    
    weather_data=[float(value) for value in weather_data]
    min_value=min(weather_data)
    min_index=len(weather_data) - 1 - weather_data[::-1].index(min_value)
    return min_value, min_index
    
  # min_index=weather_data.index(min_value)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if not weather_data:
        return ()
    
    weather_data=[float(value) for value in weather_data]
    max_value= max(weather_data)
    max_index=len(weather_data)-1-weather_data[::-1].index(max_value)
    return max_value, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    # """
    if not weather_data:
     return "No weather data available."
    
    length=len(weather_data)
    # This didnt work but I want to leave it for future reference
    # min_temp_list=[]
    # max_temp_list=[]
    # for value in weather_data:
    #     min_temp_list.append(value[1])
    #     max_temp_list.append(value[2])

    # min_value=[min(min_temp_list)]
    # max_value=[max(max_temp_list)]

    min_temp_list = [day[1] for day in weather_data]
    max_temp_list = [day[2] for day in weather_data]

    min_value = min(min_temp_list)
    max_value = max(max_temp_list)

    average_min_value=calculate_mean(min_temp_list)
    average_max_value=calculate_mean(max_temp_list)
   
    average_min_value_celcius=convert_f_to_c(average_min_value)
    average_max_value_celcius=convert_f_to_c(average_max_value)
    min_value_celcius=convert_f_to_c(min_value)
    max_value_celcius=convert_f_to_c(max_value)
    
    day_min_value = None
    for line in weather_data:
       if line[1] ==min_value:
           day_min_value=convert_date(line[0])

    day_max_value=None
    for line in weather_data:
       if line[2] ==max_value:
           day_max_value=convert_date(line[0])

    
    return f"""{length} Day Overview
  The lowest temperature will be {min_value_celcius}°C, and will occur on {day_min_value}.
  The highest temperature will be {max_value_celcius}°C, and will occur on {day_max_value}.
  The average low this week is {average_min_value_celcius}°C.
  The average high this week is {average_max_value_celcius}°C.
"""
  
 

    # return "8 Day Overview\n"+f"  The lowest temperature will be {min_value_celcius}°C, and will occur on {day_min_value}.\n"+f"  The highest temperature will be {max_value_celcius}°C, and will occur on {day_max_value}.\n"+f"  The average low this week is {average_min_value_celcius}°C.\n"+f"  The average high this week is {average_max_value_celcius}°C.\n"

    

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
      return "No weather data available."
   
    summary=""

    for day_data in weather_data:
        date = day_data[0]
        min_temp = day_data[1]
        max_temp = day_data[2]
        date_convert = convert_date(date)
        min_temp_celc = convert_f_to_c(min_temp)
        max_temp_celc = convert_f_to_c(max_temp)
        summary += f"---- {date_convert} ----\n  Minimum Temperature: {min_temp_celc}°C\n  Maximum Temperature: {max_temp_celc}°C\n\n"
        

    return summary
  