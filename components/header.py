import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.title("🗼 Airbnb Tokyo Analysis")
        st.markdown("""
        Explore Tokyo's accommodation market through real data.
        Discover trends, prices, and property features across different neighborhoods.
        
        This is a representative sample of accommodation data.
        """)
    st.markdown("---")