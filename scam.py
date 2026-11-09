
import streamlit as st
import re

st.set_page_config(
    page_title="Scam Message Investigator",
    page_icon="🔍",
    layout="centered"
)

def analyze_message(message):
    patterns = {
        "Suspicious Links": r"https?://|www\.|bit\.ly",
        "OTP / Password Request": r"otp|password|pin|கடவுச்சொல்|ரகசிய எண்|ஓடிபி",
        "Urgent Warning": r"urgent|immediately|act now|account blocked|அவசரம்|உடனே|முடக்கப்படும்",
        "Prize / Lottery": r"winner|lottery|prize|reward|பரிசு|லாட்டரி|வெற்றி",
        "Payment Request": r"pay now|registration fee|processing fee|send money|பணம் அனுப்பு|கட்டணம்|முன்பணம்",
        "Fake Job Indicators": r"work from home|earn daily|guaranteed income|job offer|வேலை வாய்ப்பு|பதிவு கட்டணம்|தினமும் சம்பாதிக்க"
    }

    detected = []

    for name, pattern in patterns.items():
        if re.search(pattern, message, re.IGNORECASE):
            detected.append(name)

    return detected


st.title("🔍 Scam Message Investigator")
st.subheader("Fast Tamil & English Scam Screening")

st.write(
    "Check suspicious SMS, emails, job offers and online messages."
)

message_type = st.selectbox(
    "Select Message Type",
    ["SMS Message", "Email", "Job Offer", "Online Message"]
)

message = st.text_area(
    "Enter your message",
    placeholder="Enter Tamil or English message here...",
    height=180
)

if st.button("Investigate Message", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message.")

    else:
        warnings = analyze_message(message)

        st.divider()
        st.subheader("Investigation Report")
        st.write("Message Type:", message_type)

        if warnings:
            st.error("Suspicious Indicators Detected")

            for warning in warnings:
                st.warning("⚠️ " + warning)

            st.write(
                "Be careful. Verify the sender before taking action."
            )

        else:
            st.success("No listed suspicious indicators detected.")

            st.info(
                "This does not guarantee that the message is genuine."
            )

        st.subheader("Safety Recommendations")

        st.write("1. Never share OTP or passwords.")
        st.write("2. Avoid unexpected payment requests.")
        st.write("3. Do not open unknown links.")
        st.write("4. Verify messages through official sources.")

st.divider()

st.caption(
    "Scam Message Investigator | Python | Streamlit"
)

st.caption(
    "Educational screening tool. It does not guarantee scam detection."
)
