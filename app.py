import streamlit as st


# Center-align the title
st.markdown("<h1 style='text-align: center;'>🐾 WildLens</h1>", unsafe_allow_html=True)

# Center-align the subtitle
st.markdown("<h3 style='text-align: center;'>A Citizen Science Project for Wildlife</h3>", unsafe_allow_html=True)

# Image section:

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


# Upload a Picture
uploaded_file = st.file_uploader("Upload a picture of roadkill or wildlife", type=["png", "jpg", "jpeg"])

# Location and Details
location = st.text_input("Enter the location where the picture was taken")
notes = st.text_area("Additional details (e.g., species, time, weather)")

# Submit Button
if st.button("Submit"):
    if uploaded_file and location:
        # Save the file and data (implement this part)
        st.success("Thank you for your submission!")
    else:
        st.error("Please provide all required information.")
