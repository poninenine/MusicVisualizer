import event

def generate_demo_events(duration, bpm = 120):
    """
    Generates a list of demo events for testing purposes.
    
    Parameters:
        duration (float): Duration of the audio in seconds.
        
    Returns:
        List[Event]: A list of Event objects representing demo lightshow events.
    """
    demo_events = []
    interval = 60.0 / bpm  # Calculate interval based on BPM
    
    for t in range(0, int(duration / interval)):
        # Alternate between 'flash' and 'color_change' events
        demo_events.append(event.Event(time_stamp=t*interval, event_type='kick', parameters={'intensity': 1.0}))
    
    return demo_events