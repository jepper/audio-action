import sounddevice as sd
import numpy as np
import os

def check_sound_level(input_data, threshold):
    rms = np.sqrt(np.mean(np.square(input_data)))
    print(rms)
    return rms > threshold

def main():
    # Configurable threshold for sound level (adjust this value as per your requirements)
    threshold = 0.01

    # Set the sampling frequency and duration for audio recording
    fs = 44100  # 44.1 kHz (standard for audio)
    duration = 1  # Record audio for 5 seconds

    try:
        while True:
            print("Listening...")

            # Record audio from the default microphone
            audio_data = sd.rec(int(fs * duration), samplerate=fs, channels=1)
            sd.wait()

            # Check if the sound level exceeds the threshold
            if check_sound_level(audio_data, threshold):
                print("Sound level exceeded the threshold! Shutting down the PC...")
#                os.system("shutdown /s /t 0")  # Shutdown the PC immediately
                break  # End the loop and terminate the script

    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")

if __name__ == "__main__":
    main()

