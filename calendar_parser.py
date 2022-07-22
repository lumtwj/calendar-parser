from ics_calendar import Calendar

public_holiday_json = './json/public_holidays_sg.json'

calendar = Calendar(2023)
calendar.load_json(public_holiday_json)
events = calendar.parse()

f = open(public_holiday_json, "w")
f.write(events)
f.close()
