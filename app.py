import streamlit as st

# Page configuration with emoji
st.set_page_config(page_title="Project Growth Mindset", page_icon="🌱")

st.title("🚀 Growth Mindset Challenge")
st.header("🌻 Welcome to the Journey of Growth!")

# Description with emojis
st.write("""
💪 Embrace Challenges | 🧠 Learn from Mistakes | 🏋️ Persist Through Difficulties
🎉 Celebrate Effort 

This app helps you develop a growth mindset with:
🔍 Reflection | 🧗 Challenge | 🏆 Achievements
""")

# Quote section with emoji
st.header("✨ Today's Quote on Growth Mindset!")
st.write("“Be not afraid of growing slowly; be afraid only of standing still.” - Chinese Proverb 🌱")

# Challenge Section
st.header("🧗 What's Your Challenge Today?")
user_input = st.text_input("📝 Tell us about your challenge:")

if user_input:
    st.success(f"🎯 You're facing: {user_input}. Keep pushing forward toward your goals! 💪")
else:
    st.warning("⏳ Tell us about your challenge to get started")

# Reflection Section
st.header("🤔 Reflect on Your Learning")
reflection = st.text_area("📖 Write your reflection here:")

if reflection:
    st.success(f"🌟 Great insight! Your reflection: {reflection}")
else:
    st.info("🔍 Learning from past experiences helps you grow! Share your challenges. 🌱")

# Achievement Section
st.header("🏆 Celebrate Your Win")
achievement = st.text_area("🎉 Tell us about something you achieved recently!:")

if achievement:
    st.success(f"🥳 Amazing! You achieved: {achievement}")
else:
    st.info("🌈 Every achievement matters, big or small,share one now! ⭐️")

# Footer with emojis
st.write("---")
st.write("🚀 “People who are crazy enough to think they can change the world are the ones who do.” - Rob Siltanen")
st.write("Made with ❤️ by Tahirzee.")




    

