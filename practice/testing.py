

# def generate_daily_summary(weather_data):
#     # """Outputs a daily summary for the given weather data.

#     # Args:
#     #     weather_data: A list of lists, where each sublist represents a day of weather data.
#     # Returns:
#     #     A string containing the summary information.
#     # """
    
#     for date in weather_data:
#         iso_day = date[0]
#         converted_day = convert_date(iso_day)

#     for min in weather_data:
#         min_temp = min[1]
#         convert_min_to_C = convert_f_to_c(min_temp)
    
#     for max in weather_data:
#         max_temp = max[2]
#         convert_max_to_C = convert_f_to_c(max_temp)
    
daily_summary = f"---- converted_day ----" \
    f"  Minimum Temperature: convert_min_to_C°C" \
    f"  Maximum Temperature: convert_max_to_C°C" 

print(daily_summary)