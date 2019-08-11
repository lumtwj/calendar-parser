import requests
from Calendar import Calendar

url = 'https://www.mom.gov.sg/~/media/mom/documents/employment-practices/public-holidays/public-holidays-sg-2020.ics'
calendar = Calendar(requests.get(url).text, 2020)

calendar.load_json('./json/public_holidays_sg.json')
events = calendar.parse()

f = open('./json/public_holidays_sg.json', "w")
f.write(events)
f.close()
