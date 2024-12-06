import streamlit as st
import os

# Center-align the title
st.markdown("<h1 style='text-align: center;'>🐾 WildLens</h1>", unsafe_allow_html=True)

# Center-align the subtitle
st.markdown("<h3 style='text-align: center;'>A Citizen Science Project for Wildlife</h3>", unsafe_allow_html=True)

# Image section
st.image("assets/wildlife_banner.jpg", use_container_width=True)
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; margin-top: -10px;">
        <a href="https://www.vecteezy.com/free-vector/wildlife-banner" target="_blank">
        Wildlife Banner Vectors by Vecteezy
        </a>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("<h4 style='text-align: center;'><i>Capture the Unseen, Protect the Wild 🌿</i></h4>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 🌍 **Help Us Record, Save, and Celebrate Wildlife**")

# Directory to save uploaded images
upload_directory = "uploaded_images"

# Ensure the directory exists
if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)

# Upload a Picture
uploaded_file = st.file_uploader("Upload a picture of roadkill or wildlife", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Save the uploaded file to the specified directory
    file_path = os.path.join(upload_directory, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"Image saved successfully to {file_path}!")
    st.image(file_path, caption="Uploaded Image", use_container_width=True)


# Location and Details
location = st.text_input("Enter the location where the picture was taken")
notes = st.text_area("Additional details (e.g., species, time, weather)")

# Submit Button
if st.button("Submit"):
    if uploaded_file and location:
        # Save the file and data (implement this part)
        st.success("Thank you for your submission, We obtained your image!")
    else:
        st.error("Please provide all required information.")

