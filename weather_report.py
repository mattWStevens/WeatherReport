# weather_report.py
# author: Matthew Stevens

import requests
from weather import *
import smtplib as st
from email.message import EmailMessage
from message import EmailMessage as em
import config
import sys

"""
This program utilizes an HTTP get request to access the API of OpenWeatherMap
in order to generate a daily email report of the weather and suggested activities
based upon this weather.
"""

# preps the body of the email message to be sent to EmailMessage object
def prep_body(body):
	message_body = ""

	for line in body:
		message_body += line + "\n\n"

	message_body += "-your friendly python program"

	return message_body

recipient = sys.argv[1]

# make HTTP request and convert response to json
try:
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=41.8&lon=-73.12&APPID=c68aeb8528331c33fe7fe2541f78f82a").json()

except:
	print("Unable to process API call")
	sys.exit() # stop executing script if cannot execute API call

# gather necessary variables
temp = r["main"]["temp"]

# convert Kelvin temperature to Fahrenheit
temp = to_fahrenheit(temp)

cloud_cover = r["clouds"]["all"]
condition = r["weather"][0]["description"]
humidity = r["main"]["humidity"]
first_line = ""
weather_status = ""

# check activities based on weather
if "snow" in condition.lower():
	snowboard = snowboarding(temp, snow, cloud_cover)
	message = "Today would be a perfect day for snowboarding!" if snowboard else ""

else:
	golf = golfing(temp, condition, cloud_cover, humidity)
	message = "Today would be a perfect dya for golfing!" if golf else ""

	weather = good_weather(temp, condition, humidity, cloud_cover)
	weather_status = "The weather is looking beautiful today!" if weather else "The weather is not looking so good."	

poss_activities = suggested_activities(temp, condition, humidity)

activities_message = "Some suggested activities are:\n"

# create list of suggested activities based on weather conditions
for act in poss_activities:
	activities_message += "\t" + act + "\n"

# build email with components for body that have been gathered
first_line = message

body = []
body.append(first_line)
body.append(weather_status)
body.append(activities_message)

# get message body ready
body = prep_body(body)

email = em(config.EMAIL_ADDRESS, recipient, "Your Weather Report", body)
msg = email.to_string()

# send email
try:
	server = st.SMTP("smtp.gmail.com", 587)

	server.connect("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()

	server.login(config.EMAIL_ADDRESS, config.PASSWORD)

	server.sendmail(config.EMAIL_ADDRESS, recipient, msg)
	server.quit()

except:
	print("Unable to send email")
