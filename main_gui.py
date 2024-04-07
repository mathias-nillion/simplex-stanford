import streamlit as st

# Title of the web app
st.title('Simplex')

# Upload field
uploaded_file = st.file_uploader("Choose a file")

# Dropdown menu for countries
countries = ['United States', 'Canada', 'United Kingdom', 'Germany', 'France', 'Australia', 'Japan', 'China', 'India', 'Brazil']
selected_country = st.selectbox('Select a country', countries)

# Checkbox
report = st.checkbox('Report')

# Submit button
if st.button('Submit'):
    st.write('Submitted!')
    # Display uploaded file name (if file uploaded)
    if uploaded_file is not None:
        st.write('File uploaded:', uploaded_file.name)
    else:
        st.write('No file uploaded.')

    # Display selected country
    st.write('Selected country:', selected_country)

    # Display if report is checked
    if report:
        st.write('Report: Checked')
    else:
        st.write('Report: Not Checked')
