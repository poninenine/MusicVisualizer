import subprocess
import sounddevice as sd


# individual samples approach




# ffmpeg approach

def play_audio(file_path):
    return subprocess.Popen(
            ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", file_path],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

def stop_audio(player_process):
    if player_process:
        player_process.terminate()
        try:
            player_process.wait(timeout=0.5)
        except subprocess.TimeoutExpired:
            player_process.kill()
    
    return None