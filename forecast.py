import pywapi
city = raw_input("Enter the city to check forecast:  ")
lookup = pywapi.get_location_ids(city)

for i in lookup:
	location_id = i

weather_com_result = pywapi.get_weather_from_weather_com(location_id)

print "Weather for %s is %s degree celcius " %(str(city), str(weather_com_result['current_conditions']['temperature']))