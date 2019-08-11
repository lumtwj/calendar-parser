import json
from shutil import copyfile


class Calendar:
    def __init__(self, raw, year, ):
        self.raw = raw
        self.year = year
        self.calendar_version = 1
        self.version = None
        self.calendar_name = None
        self.timezone = None
        self.events = []
        self.last_unique_index = 0

    def load_json(self, json_calendar):
        with open(json_calendar, 'r') as f:
            calendar = json.load(f)
            calendar_year = calendar['year']
            public_holidays = calendar['data']

            if self.year > calendar_year:
                file_name_index = json_calendar.rfind('.')
                copyfile(json_calendar, json_calendar[:file_name_index] + '_' + str(calendar_year) + '.json')
                for public_holiday in public_holidays:
                    date = public_holiday['date']

                    if calendar_year == int(date[0:4]):
                        print(public_holiday)
                        self.events.append(public_holiday)

                self.last_unique_index = public_holidays[len(public_holidays) - 1]['uid']
                self.calendar_version += 1

    def parse(self):
        name = None
        date = None

        for line in self.raw.splitlines():
            # print(line)

            if line.startswith("VERSION:"):
                self.version = line[line.index(':') + 1:]
            elif line.startswith("X-WR-CALNAME:"):
                self.calendar_name = line[line.index(':') + 1:]
            elif line.startswith("X-WR-TIMEZONE:"):
                self.timezone = line[line.index(':') + 1:]
            elif line.startswith("SUMMARY:"):
                name = line[line.index(':') + 1:]
            elif line.startswith("DTSTART;VALUE=DATE:"):
                date = line[line.index(':') + 1:]
            elif line == "END:VEVENT":
                self.last_unique_index += 1
                self.events.append({
                    "uid": self.last_unique_index,
                    "name": name,
                    "date": date
                })

        return json.dumps({
            "year": self.year,
            "version": self.calendar_version,
            "name": self.calendar_name,
            "timezone": self.timezone,
            "data": self.events
        })
