import streamlit as st
from gtts import gTTS
from moviepy.editor import *
import os
from datetime import datetime

# Title of the app
st.title("🚨 Crypto Market Crash (Aug 4–6, 2025) Explainer Video")

# Original script content (broken into segments for narration + scenes)
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

# Function to convert a text scene into a TTS audio clip
def generate_tts_clip(text, index):
    tts = gTTS(text, lang='en')
    filename = f"tts_clip_{index}.mp3"
    tts.save(filename)
    return filename

# Generate video from scenes and narration
def generate_video(scenes):
    clips = []
    for i, scene in enumerate(scenes):
        audio_file = generate_tts_clip(scene, i)
        audioclip = AudioFileClip(audio_file)
        duration = audioclip.duration

        txt_clip = TextClip(scene, fontsize=40, color='white', size=(1080, 720), method='caption', align='center')
        txt_clip = txt_clip.set_duration(duration).set_position('center').set_audio(audioclip)
        clips.append(txt_clip)

    final_video = concatenate_videoclips(clips, method="compose")
    output_path = f"crypto_drop_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    final_video.write_videofile(output_path, fps=24)

    # Cleanup temp audio files
    for i in range(len(scenes)):
        os.remove(f"tts_clip_{i}.mp3")

    return output_path

# Generate video button
if st.button("🎬 Generate Explainer Video"):
    with st.spinner("Generating video... this may take a minute ⏳"):
        video_file = generate_video(scenes)
        st.success("✅ Video generated!")

        # Display video
        st.video(video_file)
