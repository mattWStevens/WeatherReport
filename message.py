# message.py
# author: Matthew Stevens

"""
This is a class representing a neatly formatted
message to be used for the body of an email.
"""
class EmailMessage:
	sent_from = ""
	to = ""
	subject = ""
	body = "" 

	# initializes the EmailMessage
	def __init__(self, sent_from, to, subject, body):
		self.sent_from = sent_from
		self.to = to
		self.subject = subject
		self.body = body
	
	# returns the EmailMessage
	def to_string(self):
		message = "Subject: {}\n\n{}".format(self.subject, self.body)

		return message

"""
Creates a neatly formatted email_body for use
in an email application.
"""
class EmailBody:
	first_line = ""
	weather_status = ""
	activities_message = ""
	current_temp = ""
	high = ""
	low = ""
	humidity = ""

	# initialize the EmailBody
	def __init__(self, first_line, weather_status, activities_message, current_temp, high, low, humidity):
		self.first_line = first_line
		self.weather_status = weather_status
		self.activities_message = activities_message
		self.current_temp = current_temp
		self.high = high
		self.low = low
		self.humidity = humidity

	# create neat email body
	def make_body(self):
		body = ""

		# add some numerical information regarding weather to beginning of body
		initial_message = "It is currently {} degrees Fahrenheit.".format(self.current_temp)
		highs_lows = "Todays high will be {} F and the low will be {} F".format(self.high, self.low)
		hum = "The humidity is {}".format(self.humidity)

		body += initial_message + highs_lows + hum + "\n\n"
		body += self.activities_message + "\n\n"
		body += "-your friendly Python program"
