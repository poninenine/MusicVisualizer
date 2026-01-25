import event

def generate_demo_events(duration):
    """
    Generates a list of demo events for testing purposes.
    
    Parameters:
        duration (float): Duration of the audio in seconds.
        
    Returns:
        List[Event]: A list of Event objects representing demo lightshow events.
    """
    demo_events = []
    interval = 1.0  # 1 second intervals
    
    for t in range(0, int(duration), int(interval)):
        # Alternate between 'flash' and 'color_change' events
        demo_events.append(event.Event(time_stamp=t*interval, event_type='kick', parameters={'intensity': 1.0}))
    
    return demo_events