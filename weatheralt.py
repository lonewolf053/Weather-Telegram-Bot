import requests, json

def getweather(cityname):

	api_key = "15db601059d063a234dc0e5a084d744e"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	
	city_name = cityname
	
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	
	response = requests.get(complete_url)
	
	x = response.json()
	if x["cod"] != "404":
	    y = x["main"]
	    current_temperature = y["temp"]
	    current_pressure = y["pressure"]
	    current_humidity = y["humidity"]
	    z = x["weather"]
	    weather_description = z[0]["description"]
	
	    return(" Temperature (in celsius) = " +
	                    str(current_temperature-273.15) +
	          "\n atmospheric pressure (in hPa unit) = " +
	                    str(current_pressure) +
	          "\n humidity (in percentage) = " +
	                    str(current_humidity) +
	          "\n description = " +
	                    str(weather_description))


