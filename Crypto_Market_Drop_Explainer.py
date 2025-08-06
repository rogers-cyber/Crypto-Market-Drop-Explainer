import streamlit as st
from gtts import gTTS
import os

# Title
st.title("🚨 Crypto Market Crash (Aug 4–6, 2025) Explainer")

# Scenes (text + narration)
scenes = [
    "🚨 Why Crypto Just Dropped (Aug 4–6, 2025) — and Why So Many Traders Lost 🚨",
    "The crypto market saw a sharp dip this week — and if you’re wondering why your gains vanished, this is for you.",
    "📉 What Happened?",
    "1️⃣ Big Options Expired. Over $7 billion in BTC & ETH options expired, triggering large sell-offs.",
    "2️⃣ Whale Sell-Offs. Large wallets dumped coins, especially on low-volume days. Price dropped fast.",
    "3️⃣ Leverage Liquidations. Many traders used high leverage. Over $1 billion in liquidations!",
    "4️⃣ Macro Fear. Interest rates, inflation, and tariffs scared investors. Risky assets were sold.",
    "5️⃣ ETF Outflows. Even Bitcoin ETFs saw huge withdrawals. Less demand = more selling.",
    "🧠 Why So Many Traders Lost? No stop-losses, too much leverage, chasing hype, panic selling.",
    "✅ What Smart Traders Did: Low/no leverage, took partial profits, set stop-losses, watched whales and ETFs.",
    "💬 Did you get caught or trade it right? Share your lessons below!"
]

# Show each scene with audio
for i, scene in enumerate(scenes):
    st.markdown(f"### Slide {i+1}")
    st.write(scene)

    # Generate TTS
    tts = gTTS(text=scene, lang='en')
    filename = f"scene_{i}.mp3"
    tts.save(filename)

    # Display audio player
    with open(filename, "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")

    # Clean up (optional in dev mode; Streamlit Cloud handles temp files)
    os.remove(filename)
