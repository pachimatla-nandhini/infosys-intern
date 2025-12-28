from transformers import MusicgenForConditionalGeneration, MusicgenProcessor

class MusicGenerator:
    def __init__(self):
        # Load processor
        self.processor = MusicgenProcessor.from_pretrained("facebook/musicgen-small")
        # Load model
        self.model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

    def generate(self, prompt):
        inputs = self.processor([prompt], return_tensors="pt")
        generated = self.model.generate(**inputs)
        return generated
