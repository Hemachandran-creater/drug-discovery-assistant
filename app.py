import streamlit as st
import random
import os

st.set_page_config(page_title="Drug Discovery Assistant", layout="centered")
st.title("🧬 Drug Discovery Assistant")
st.subheader("Powered by Generative AI")
st.markdown("An AI-powered assistant to simulate **drug molecule generation** and provide **predictions** for safety and binding affinity.")

target = st.text_input("🔍 Enter Target Protein or Disease", "COVID-19")
desired_property = st.selectbox("⚙️ Desired Property", ["Low Toxicity", "High Affinity", "Anti-viral", "Anti-inflammatory"])

molecule_images = [
    "images/mol1.png",
    "images/mol2.png",
    "images/mol3.png",
    "images/mol4.png",
    "images/mol5.png"
]

if st.button("🚀 Generate Drug Molecule"):
    image_path = random.choice(molecule_images)
    safety_score = round(random.uniform(75, 99), 2)
    affinity_score = round(random.uniform(-13, -6), 2)
    
    st.markdown("## 🧪 Simulation Results")
    col1, col2 = st.columns(2)

    with col1:
        if os.path.exists(image_path):
            st.image(image_path, caption="Generated Molecule", use_column_width=True)
        else:
            st.warning("Image not found. Please check image path.")

    with col2:
        st.metric("🛡️ Safety Score", f"{safety_score}%", delta="+High")
        st.metric("🎯 Binding Affinity", f"{affinity_score} kcal/mol", delta="-Good")

    st.markdown("---")
    st.markdown("### 📘 Explanation")
    st.markdown(f"""
    - Target: **{target}**  
    - Desired Property: **{desired_property}**
    - Molecule visuals are simulated.
    - Scores are generated to mimic AI predictions.
    - This demo shows how AI could assist researchers.
    """)

else:
    st.info("👉 Fill the inputs and click 'Generate Drug Molecule' to simulate.")
