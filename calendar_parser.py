from ics_calendar import Calendar
import datetime
from zoneinfo import ZoneInfo

now = datetime.datetime.now(ZoneInfo('Asia/Singapore'))
year = now.year
print('Current year:', year)

public_holiday_json = './json/public_holidays_sg.json'

calendar = Calendar(year)
calendar.load_json(public_holiday_json)
events = calendar.parse()

f = open(public_holiday_json, "w")
f.write(events)
f.close()
