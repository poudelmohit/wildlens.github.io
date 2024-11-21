import streamlit as st

# App Title
st.title("WildLens: Citizen Science for Wildlife")

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
