from models.schedule import Schedule
from datetime import datetime,time

if ( __name__ == '__main__' ):
    weektimetable=[{
        "place":"OKIS",
        "weekday_polish": "wtorek",
        "shifts": [time(7,0), time(8,0)]
    },
    {
        "place":"Park",
        "weekday_polish": "Piątek",
        "shifts": [time(7,0), time(8,0)]
    },
    {
        "place":"API",
        "weekday_polish": "piątek",
        "shifts": [time(17,0), time(18,0)]
    }]

    s = Schedule(2024, 9)
    s.create_entries(weektimetable)
    for entry in s.entries:
        print(entry.start_time.strftime('%A %d.%m.%Y, %H:%M'), entry.place)