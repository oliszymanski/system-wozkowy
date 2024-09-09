class Publisher:
    priority_for_kind = {
        "default": 1,
        "regular_pioneer": 2
    }
    priority_cost=0

    def __init__(self, name, kind="default"):
        self.name = name
        self.kind = kind
        self.priority_global = self.priority_for_kind[kind]
        self.priority_daily = [self.priority_global] * 31
        self.related_publishers = []
        self.availability = {
            0:[],1:[],2:[],3:[],4:[],5:[],6:[]
        }# 0 - Monday, 1 - Tuesday ... 6 - Sunday
        # calendar.day_name
        self.shifts = set()

    def add_availability(self, weekday, shift_time):
        self.availability[weekday].append(shift_time)

    def priority_for_shift(self, shift):
        # TODO: priority calculation
        if not self.is_available(shift.start_time):
            return 0
        
        priority = self.priority_global
        priority -= (len(self.shifts) * self.priority_cost)
        return max(priority, 0.05)

    def is_available(self, start_time):
        weekday = start_time.weekday()
        available_times = self.availability[weekday]
        time = start_time.time()
        return time in available_times