import streamlit as st
import torch
import os
import random
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

# ===============================
# Task 1.1 – Environment Check
# ===============================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ===============================
# Task 1.4 – Mood Templates
# ===============================
MOOD_TEMPLATES = {
    "happy": "upbeat, cheerful, major key, bright instruments, positive vibes",
    "sad": "melancholic, slow tempo, minor key, emotional, piano and strings",
    "energetic": "high energy, fast-paced, driving beat, intense rhythm",
    "calm": "slow tempo, peaceful, ambient sounds, soft textures",
    "romantic": "warm, emotional, acoustic guitar, gentle rhythm",
    "mysterious": "dark, atmospheric, suspenseful, deep pads"
}

TEMPO_MAP = {
    "slow": "60-80 BPM",
    "medium": "90-110 BPM",
    "fast": "120-150 BPM"
}

# ===============================
# Task 1.3 – Input Processor
# ===============================
def process_input(user_text):
    text = user_text.lower()

    mood = "calm"
    if "happy" in text or "party" in text:
        mood = "happy"
    elif "sad" in text or "breakup" in text:
        mood = "sad"
    elif "energetic" in text or "workout" in text:
        mood = "energetic"
    elif "romantic" in text:
        mood = "romantic"
    elif "dark" in text or "mysterious" in text:
        mood = "mysterious"

    tempo = "medium"
    if "slow" in text:
        tempo = "slow"
    elif "fast" in text:
        tempo = "fast"

    instruments = "piano"
    if "guitar" in text:
        instruments = "guitar"
    elif "drums" in text:
        instruments = "drums"
    elif "synth" in text:
        instruments = "synthesizer"

    energy = random.randint(5, 9) if mood == "energetic" else random.randint(2, 6)

    return {
        "mood": mood,
        "tempo": tempo,
        "instruments": instruments,
        "energy": energy
    }

# ===============================
# Task 1.4 – Prompt Enhancer
# ===============================
def enhance_prompt(user_text, params):
    mood_desc = MOOD_TEMPLATES.get(params["mood"], "")
    tempo_desc = TEMPO_MAP.get(params["tempo"], "")

    prompt = f"""
    {mood_desc}.
    Tempo: {tempo_desc}.
    Energy level: {params['energy']}/10.
    Instruments: {params['instruments']}.
    High quality studio music.
    Music description: {user_text}
    """

    return prompt.strip()

# ===============================
# Task 1.2 – Load MusicGen
# ===============================
@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained("facebook/musicgen-small")
    model.set_generation_params(
        duration=10,
        temperature=1.0,
        top_k=250,
        top_p=0.0,
        cfg_coef=3.0
    )
    return model

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="AI Music Composer", layout="centered")
st.title("🎶 AI-Based Music Composition System")
st.caption("Tasks 1.1 – 1.4 (Complete Backend System)")

st.write(f"Device: {DEVICE}")

user_text = st.text_input(
    "Describe your music:",
    "Energetic music for workout"
)

if st.button("Generate Music 🎵"):
    st.info("Processing input...")

    params = process_input(user_text)
    enhanced_prompt = enhance_prompt(user_text, params)

    st.subheader("Extracted Parameters")
    st.json(params)

    st.subheader("Enhanced Prompt")
    st.code(enhanced_prompt)

    st.info("Generating music...")

    model = load_model()
    wav = model.generate([enhanced_prompt])

    os.makedirs("output", exist_ok=True)
    filename = f"output/music_{random.randint(1000,9999)}"

    audio_write(
        filename,
        wav[0].cpu(),
        model.sample_rate,
        strategy="loudness"
    )

    st.success("Music Generated Successfully!")
    st.audio(filename + ".wav")