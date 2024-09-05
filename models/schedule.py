from datetime import datetime, date, time, timedelta
from .schedule_entry import Schedule_entry

polish_weekdays=[
    "poniedziałek",
    "wtorek",
    "środa",
    "czwartek",
    "piątek",
    "sobota",
    "niedziela"
]

class Schedule:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.entries = []
    
    def create_entries(self, weektimetable):
        '''
            Initally creates the entries.
            Params:  weektimetable - collection of dictionaries with keys: 
                    place - string
                    weekday_polish - string in Polish
                    shifts - collection of time objects, describing starting times of the shifts
        '''

        # Reorganise entries into lookup table for each weekday
        weekly_shifts = [[] for _ in range(7)] # 7 element array of arrays
        for shift_data in weektimetable:
            weekday_polish = shift_data["weekday_polish"].lower()
            weekday = polish_weekdays.index(weekday_polish)
            weekly_shifts[weekday].append(shift_data)

        current_date = date(self.year, self.month, 1)
        while current_date.month == self.month:
            weekday = current_date.weekday()
            for place_shifts in weekly_shifts[weekday]:
                place = place_shifts["place"]
                for shift_time in place_shifts["shifts"]:
                    shift_start_time=datetime.combine(current_date, shift_time)
                    entry = Schedule_entry(shift_start_time, place)
                    self.entries.append(entry)
            current_date = current_date + timedelta(days=1)
    
    def get_entries(self):
        '''
        Returns entries
        '''
        return self.entries