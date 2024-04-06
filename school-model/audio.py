import numpy as np
from scipy.io import wavfile
from phone import call
from database import add_call
from dotenv import load_dotenv

load_dotenv()


def calculate_decibels(wav_file):
    # Read the .wav file
    sample_rate, data = wavfile.read(wav_file)

    # Calculate the root mean square (RMS) of the audio data
    rms = np.sqrt(np.mean(data**2))

    # Convert RMS to decibels (assuming 16-bit audio, i.e., 32767 is the maximum amplitude)
    decibels = 20 * np.log10(rms / 32767)

    return abs(decibels)

# Replace 'your_audio_file.wav' with the path to your .wav file
file_path = 'audio/gun1.wav'

decibels = calculate_decibels(file_path)

if (decibels > 60):
    print(f"Loud gun detected, calling cops!")
    add_call(file_path, "Gunshot audio detected!")
    call()