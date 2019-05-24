import json


class Calendar:
    def __init__(self, raw, year):
        self.raw = raw
        self.year = year
        self.version = None
        self.calendar_name = None
        self.timezone = None
        self.events = []

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
                self.events.append({
                    "name": name,
                    "date": date
                })

        return json.dumps({
            "year": self.year,
            "calendar_name": self.calendar_name,
            "calendar_timezone": self.timezone,
            "json": self.events
        })
