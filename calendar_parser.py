import requests
from ics_calendar import Calendar

url = 'https://www.mom.gov.sg/~/media/mom/documents/employment-practices/public-holidays/public-holidays-sg-2021.ics'
calendar = Calendar(requests.get(url).text, 2021)

calendar.load_json('./json/public_holidays_sg.json')
events = calendar.parse()

f = open('./json/public_holidays_sg.json', "w")
f.write(events)
f.close()
