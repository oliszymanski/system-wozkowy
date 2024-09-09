from assign_helper import *
from models.schedule import Schedule
from models.publisher import Publisher
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
    
    marian = Publisher("Marian")
    marian.add_availability(1, time(7,0))
    marian.add_availability(1, time(8,0))
    marian.add_availability(4, time(7,0))
    marian.add_availability(4, time(8,0))
    marian.add_availability(4, time(17,0))
    marian.add_availability(4, time(18,0))

    karol = Publisher("Karol")
    karol.add_availability(1, time(7,0))
    karol.add_availability(1, time(8,0))
    karol.add_availability(4, time(7,0))
    karol.add_availability(4, time(8,0))

    marlena = Publisher("Marlena")
    marlena.add_availability(4, time(7,0))
    marlena.add_availability(4, time(8,0))
    marlena.add_availability(4, time(17,0))
    marlena.add_availability(4, time(18,0))

    irwina = Publisher("Irwina", "regular_pioneer")
    irwina.add_availability(1, time(7,0))
    irwina.add_availability(1, time(8,0))
    irwina.add_availability(4, time(7,0))
    irwina.add_availability(4, time(8,0))
    irwina.add_availability(4, time(17,0))
    irwina.add_availability(4, time(18,0))

    publishers = [marian, karol, marlena, irwina]

    priority_sum = sum(p.priority_global for p in publishers)
    Publisher.priority_cost = priority_sum / (len(s.entries) * 2)

    assign_shifts(s, publishers)

    for entry in s.entries:
        print(entry.start_time.strftime('%A %d.%m.%Y, %H:%M'), entry.place, list(x.name for x in entry.publishers))

    
