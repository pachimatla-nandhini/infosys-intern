# AI-Based Music Composition System
# Infosys Virtual Internship – Milestone 1

# -------------------------------
# Environment Setup
# -------------------------------

python -m venv venv
venv\Scripts\activate

# -------------------------------
# Install Dependencies
# -------------------------------

pip install streamlit transformers torch torchaudio
pip install music21 mido pretty_midi pydub scipy
pip install openai anthropic accelerate
pip install audiocraft python-dotenv

# -------------------------------
# Project Structure
# -------------------------------

ai-music-composer/
│
├── app.py
├── test_gpu.py
├── requirements.txt
├── README.md
└── .env

# -------------------------------
# API Keys (.env)
# -------------------------------

OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
HUGGINGFACE_TOKEN=your_token_here

# -------------------------------
# GPU Test
# -------------------------------

python test_gpu.py

# -------------------------------
# Run Application
# -------------------------------

streamlit run app.py

# -------------------------------
# Milestone 1 Status
# -------------------------------

Environment Setup: DONE
Library Installation: DONE
Streamlit UI: DONE
GPU Test: DONE
