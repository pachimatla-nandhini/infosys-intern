from backend.quality_scorer import AudioQualityScorer

scorer = AudioQualityScorer()

audio_path = "C:\Users\DELL\Desktop\milestone 3\audio_wav_sample-30s.wav"  # put your audio file here
stats, final_score = scorer.score(audio_path)

print("\n--- Audio Quality Results ---")
for key, value in stats.items():
    print(f"{key}: {value}")

print("\nFinal Score:", final_score)
