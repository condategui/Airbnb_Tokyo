import streamlit as st
import pandas as pd
import warnings

from components.header import render_header
from components.footer import render_footer
from components.accommodations_section import display_accommodations_section
from components.luxury_accommodations_section import display_luxury_accommodations_section
from components.introduction_section import introduction_section
from components.summary_section import summary_section


warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="🏯 Discover Tokyo through Airbnb",
    page_icon="🏯",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    try:
        luxury = pd.read_csv('data/luxury_dataframe.csv')
        normal = pd.read_csv('data/normal_dataframe.csv')
        return luxury, normal
    except FileNotFoundError as e:
        st.error(f"Error: {e}")
        return None, None
    except pd.errors.EmptyDataError as e:
        st.error(f"Error: {e}")
        return None, None
    except pd.errors.ParserError as e:
        st.error(f"Error: {e}")
        return None, None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None, None


def main():
    render_header()
    luxury, normal = load_data() # Unpack the tuple returned by load_data
    
    if normal is not None and luxury is not None:
        st.sidebar.title("Menu")
        
        # Define the pages with their icons and functions
        pages = {
            "🗾 Introduction": introduction_section,
            "🏡 Accommodations": display_accommodations_section,
            "💵 Luxury Accommodations": display_luxury_accommodations_section,
            "📒 Summary": summary_section
        }
        
        # Store the current page in session state if it doesn't exist yet
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "🗾 Introduction"
        
        # Create a button for each page
        for page_name in pages.keys():
            if st.sidebar.button(page_name, key=page_name):
                st.session_state.current_page = page_name
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("### Tokyo at a Glance:")
        st.sidebar.markdown("""
        🗼 **Why Tokyo?**
        - Ancient traditions meet futuristic technology
        - World-renowned sushi and ramen
        - Anime and manga culture
        - Cherry blossom seasons
        """)
        
        # Display the selected page
        if st.session_state.current_page == "🗾 Introduction":
            pages[st.session_state.current_page]()
        elif st.session_state.current_page == "📒 Summary":
            pages[st.session_state.current_page]()
        else:
            if st.session_state.current_page == "🏡 Accommodations":
                pages[st.session_state.current_page](normal)
            elif st.session_state.current_page == "💵 Luxury Accommodations":
                pages[st.session_state.current_page](luxury)
            
        render_footer()
    else:
        st.error("Failed to load data. Please check the data files.")


if __name__ == "__main__":
    main()