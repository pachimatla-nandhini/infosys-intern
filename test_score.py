# test_score.py

# Import libraries
import librosa

# Use raw string (r"") to avoid unicode errors with backslashes
audio_path = r"C:\Users\DELL\Desktop\milestone 3\audio_wav_sample-30s.wav"  # change this to your audio file

# Load the audio file
y, sr = librosa.load(audio_path, sr=None)

# Print some basic info
print(f"Audio loaded successfully!")
print(f"Sample rate: {sr}")
print(f"Audio duration: {len(y)/sr:.2f} seconds")


