# weather.py
# author: Matthew Stevens

"""
This is a module containing various functions that will be used for
different computations and conditional checking on weather conditions.
"""

# This function takes a temperature in Kelvin and converts it to Fahrenheit.
def to_fahrenheit(temp):
	return ((temp * (9/5)) - 459.67)

# This function checks the weather conditions and determines if it is good
# snowboarding weather.
def snowboarding(temp, snow, cloud_cover):
	answer = True
	desired_snow = ["snow", "heavy snow", "heaver shower snow"]

	if snow not in desired_snow:
		answer = False
	if temp < 20 or temp > 45:
		answer = False
	if cloud_cover > 60:
		answer = False

	return answer
		
# This function checks the weather conditions and determines if it is good
# golfing weather.
def golfing(temp, condition, cloud_cover, humidity):
	answer = True
	desired_conditions = ["clear sky", "few clouds", "scattered clouds"]
	
	if temp	< 60 or temp > 75:
		answer = False
	if humidity > 75:
		answer = False
	if condition not in desired_conditions:
		answer = False
	if cloud_cover > 50:
		answer = False

	return answer

# This function checks the weather conditions and determines if it is going
# to be nice today.
def good_weather(temp, condition, humidity, cloud_cover):
	answer = True
	acceptable_conditions = ["clear sky", "few clouds"]

	if temp < 60 or temp > 75:
		answer = False
	if humidity >= 80:
		answer = False
	if cloud_cover > 50:
		answer = False
	if condition not in acceptable_conditions:
		answer = False

	return answer

# This function generates a list of suggested activites based on the weather
# conditions.
def suggested_activities(temp, condition, humidity):
	poss_activities = []

	if temp > 80 and humidity < 75 and "rain" not in condition.lower():
		poss_activities.append("relaxing")
	elif "rain" in condition.lower() or temp < 50:
		poss_activities.append("video games")
		poss_activities.append("movies")
	elif temp >= 60 and temp <= 75 and humidity <= 70:
		poss_activities.append("biking")
		poss_activities.append("hiking")
	else:
		poss_activities.append("No Suggestions")

	return poss_activities
		
