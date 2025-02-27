import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown('<hr style="border:5px solid #FF5A5F">', unsafe_allow_html=True)
    st.markdown("""
                <div style='text-align: center; color: #666;'>
            <p>Developed by Clàudia Ondategui, Data Analyst.</p>
            <p>Visit my 
               <a href="https://github.com/condategui">GitHub.</a> to discover more projects or check my
                <a href="https://www.linkedin.com/in/claudia-ondategui/">LinkedIn</a>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )