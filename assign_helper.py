import random

def choose_publisher_for_shift(entry, publishers):
    '''
    Randomly chooses publisher with priority bias
    '''
    priorities = []
    for pub in publishers:
        priorities.append(pub.priority_for_shift(entry))
    return random.choices(publishers, priorities)[0]

def assign_shifts(schedule, publishers):
    entries = schedule.get_entries()
    for entry in entries:
        while not entry.is_full():
            assignee = choose_publisher_for_shift(entry, publishers)
            entry.add_publisher(assignee)
