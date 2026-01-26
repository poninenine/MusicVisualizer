import Utilities.demoFunctions as demo_util
import librosa
import event

def process_audio(file_path):
    # Turns an audio file into an array of events for the lightshow
    # Currently just creates an event on beat
    y, sr = librosa.load(file_path, sr=None)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_timestamps = librosa.frames_to_time(beats, sr=sr)

    event_array = []

    for timestamp in beat_timestamps:
        event_array.append(event.Event(time_stamp=timestamp, event_type='beat', parameters={}))
    return event_array


    # print(f"Audio tempo: {tempo} bpm")
    # duration = librosa.get_duration(y=y, sr=sr)
    # print(f"Audio duration: {duration} seconds")


    # Currently just a placeholder that generates demo events
    # return demo_util.generate_demo_events(duration=duration, bpm=tempo)  # Assuming a fixed duration for demo purposes
    
    # return demo_util.generate_demo_events(duration=45.0, bpm=131)  # Assuming a fixed duration for demo purposes

# Testing function
# process_audio("C:/Users/Johannes/Downloads/No Broke Boys - Disco Lines.mp3")