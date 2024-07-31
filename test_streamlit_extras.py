import streamlit as st

try:
    from streamlit_extras.add_vertical_space import add_vertical_space
    st.write("streamlit-extras imported successfully!")
    add_vertical_space(5)
    st.write("Vertical space added above")
except ImportError as e:
    st.write(f"ImportError: {e}")