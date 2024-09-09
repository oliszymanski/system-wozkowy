class Schedule_entry:
    max_count = 2
    def __init__(self, start_time, place):
        self.start_time = start_time
        self.place = place
        self.publishers = set()

    def is_full(self):
        return len(self.publishers) >= self.max_count

    def add_publisher(self, pub):
        self.publishers.add(pub)
        pub.shifts.add(self)

    def csv_results(self):
        # Return results for csv
        csv_line=[]
        # TODO add relevant info
        return csv_line
        