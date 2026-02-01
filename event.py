class Event:
    def __init__(self, time_stamp, event_type, parameters = {}):
        self.time_stamp = time_stamp  # Time in seconds when the event should trigger
        self.event_type = event_type    # Type of event (e.g., 'flash', 'color_change')
        self.parameters = parameters    # Dictionary of parameters relevant to the event