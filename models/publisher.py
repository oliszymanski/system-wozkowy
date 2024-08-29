class Publisher:
    priority_for_kind = {
        "default": 1,
        "regular_pioneer": 2
    }

    def __init__(self, name, kind, availability, related_publishers=[]):
        self.name = name
        self.kind = kind
        self.availability = availability
        self.priority_global = self.priority_for_kind[kind]
        self.priority_daily = [self.priority_global] * 31
        self.related_publishers = related_publishers

    def priority_for_shift(self, shift):
        # TODO: priority calculation
        return self.priority_global
