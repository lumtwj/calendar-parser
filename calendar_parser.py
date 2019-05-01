import requests
from Calendar import Calendar

url = 'https://www.mom.gov.sg/~/media/mom/documents/employment-practices/public-holidays/public-holidays-sg-2019.ics'
calendar = Calendar(requests.get(url).text)

events = calendar.parse()
calendar_name = calendar.calendar_name.replace(' ', '_').lower()

f = open('./json/' + calendar_name + ".json", "w")
f.write(events)
f.close()
