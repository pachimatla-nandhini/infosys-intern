from backend.audio_processor import AudioProcessor

processor = AudioProcessor()

processor.enhance_audio(
    input_file="input.wav",
    output_file="output_enhanced.wav"
)

print("✅ Audio processing completed successfully")
