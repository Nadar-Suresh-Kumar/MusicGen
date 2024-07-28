import os
import replicate
import streamlit as st

# Streamlit app
st.title("Music Generation with Replicate API")

# Input box for the Replicate API token
api_token = st.text_input("Enter your Replicate API Token", type="password")

if api_token:
    # Set the Replicate API token
    os.environ["REPLICATE_API_TOKEN"] = api_token
    api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
    # Input fields for the parameters
    prompt = st.text_input("Prompt", value="Edo25 major g melodies that sound triumphant and cinematic. Leading up to a crescendo that resolves in a 9th harmonic")
    duration = st.number_input("Duration (seconds)", value=8)
    top_k = st.number_input("Top K", value=250)
    top_p = st.number_input("Top P", value=0)
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=1.0)
    continuation = st.checkbox("Continuation", value=False)
    model_version = st.selectbox("Model Version", ["stereo-large"])
    output_format = st.selectbox("Output Format", ["mp3"])
    continuation_start = st.number_input("Continuation Start", value=0)
    multi_band_diffusion = st.checkbox("Multi Band Diffusion", value=False)
    normalization_strategy = st.selectbox("Normalization Strategy", ["peak"])
    classifier_free_guidance = st.number_input("Classifier Free Guidance", value=3.0)

    if st.button("Generate Music"):
        # Define the input for the Replicate API
        input_data = {
            "top_k": top_k,
            "top_p": top_p,
            "prompt": prompt,
            "duration": duration,
            "temperature": temperature,
            "continuation": continuation,
            "model_version": model_version,
            "output_format": output_format,
            "continuation_start": continuation_start,
            "multi_band_diffusion": multi_band_diffusion,
            "normalization_strategy": normalization_strategy,
            "classifier_free_guidance": classifier_free_guidance
        }

        # Run the replicate model
        output = replicate.run(
            "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
            input=input_data
        )

        # Display the generated music
        st.write("Generated Music:")
        for music_url in output:
            st.audio(music_url)

# Note: Make sure you have all necessary imports and dependencies installed
