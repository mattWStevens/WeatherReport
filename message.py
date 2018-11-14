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
