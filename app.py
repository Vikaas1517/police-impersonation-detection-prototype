import json
import streamlit as st
from features.name_similarity import compute_name_similarity
from features.image_similarity import compute_image_similarity
from features.metadata_anomaly import compute_metadata_anomaly
from scorer import compute_risk_score

st.set_page_config(
    page_title="Police Impersonation Detection",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='text-align:center;'>🚨 Police Impersonation Detection</h1>
    <p style='text-align:center; color:gray;'>
    AI-assisted decision support for Cybercrime Units
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------- PROFILE SELECTION ----------
profile_choice = st.selectbox(
    "Select profile to analyze",
    ["suspicious_profile.json", "genuine_profile.json"]
)

with open(f"data/{profile_choice}", "r") as f:
    profile = json.load(f)

REFERENCE_NAME = "Rajesh Kumar IPS"
REFERENCE_IMAGE = "images/real_officer.jpeg"

# ---------- FEATURE COMPUTATION ----------
name_similarity = compute_name_similarity(
    profile["display_name"], REFERENCE_NAME
)

image_similarity = compute_image_similarity(
    profile["profile_image"], REFERENCE_IMAGE
)

metadata_anomaly = compute_metadata_anomaly(
    profile["account_age_days"], profile["total_posts"]
)

features = {
    "name_similarity": name_similarity,
    "image_similarity": image_similarity,
    "metadata_anomaly": metadata_anomaly
}

risk_score = compute_risk_score(features)

# ---------- RISK STATUS ----------
st.subheader("📊 Risk Assessment")

if risk_score >= 80:
    st.error(f"🔴 HIGH RISK IMPERSONATION — {risk_score}")
elif risk_score >= 50:
    st.warning(f"🟠 SUSPICIOUS PROFILE — {risk_score}")
else:
    st.success(f"🟢 LIKELY GENUINE — {risk_score}")

# ---------- IMAGE EVIDENCE ----------
st.subheader("🖼️ Image Evidence")

col1, col2 = st.columns(2)
with col1:
    st.image(profile["profile_image"], caption="Profile Image", width=200)
with col2:
    st.image(REFERENCE_IMAGE, caption="Reference Image", width=200)

# ---------- EVIDENCE BREAKDOWN ----------
st.subheader("🔍 Evidence Breakdown")

st.markdown(
    f"""
    - **Name Similarity:** `{round(name_similarity*100, 1)}%`
    - **Image Reuse Similarity:** `{round(image_similarity*100, 1)}%`
    - **Activity Anomaly Score:** `{metadata_anomaly}`
    """
)

# ---------- WHY FLAGGED ----------
st.subheader("❓ Why this profile was flagged")

reasons = []
if name_similarity > 0.85:
    reasons.append("Name closely matches verified police identity")
if image_similarity > 0.75:
    reasons.append("Profile image reused or visually similar to reference")
if metadata_anomaly > 0.6:
    reasons.append("Unnatural posting activity for account age")

if reasons:
    for r in reasons:
        st.write(f"• {r}")
else:
    st.write("• No strong impersonation indicators detected")

# ---------- OFFICER RECOMMENDATION ----------
st.subheader("📝 Officer Recommendation")

if risk_score >= 80:
    st.write("➡️ **Immediate takedown request & active monitoring recommended**")
elif risk_score >= 50:
    st.write("➡️ **Manual verification by cyber officer advised**")
else:
    st.write("➡️ **No action required at this stage**")

st.divider()

st.caption(
    "⚠️ This system provides decision support only. "
    "Final action remains with law enforcement officers."
)
