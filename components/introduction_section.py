import streamlit as st

def introduction_section():
    st.subheader('🇯🇵 Introduction to Tokyo Airbnb Analysis')
    
    
    tab1, tab2 = st.tabs(['🗾 AIRBNB IN TOKYO', '🏡 ABOUT AIRBNB'])
    
    with tab1: 
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
    ## Insights
    - **7.39M+ Listings**: There are more than 7.39 million registrations in Airbnb from Tokyo, Japan. Since December 2024 to March 2026.
    - **4K+ Hosts**: There are more than 4.000 hosts offering their rooms in Tokyo.
    - **Central Neighbourhoods**: At the central area of Tokyo you can find these neighbourhoods
        - Chiyoda
        - Chuo
        - Minato
        - Shinjuku
        - Bunkyo
        - Shibuya
    - **Room Types**: The most common room types are Entire home/apt, but there are also Private Rooms and some Shared Rooms and Hotels.
    - **Price**: To better understand the pricing (Yens) I've converted the prices to USD (exchange rate 0.0066 USD/Yen - 19th February 2025).
    - **Average Price by Room Type**:
        - Entire home/apt    258.08$
        - Hotel room          83.73$
        - Private room       135.46$
        - Shared room         49.87$
    - **Luxury**: There are some listings with luxury prices, that have been analyzed separately.
    """) 
            
        with col2:
            
            st.image("img/greater-tokyo-area.png", caption='Japan', width=500)

    
    with tab2:
        st.markdown("""
    ## What is Airbnb? 
    Airbnb is an online marketplace that connects people who want to rent out their homes with people who are looking for accommodations. Founded in 2008, Airbnb has grown to become a major player in the travel and hospitality industry, offering a wide variety of lodging options in destinations around the world.
    
    ### Key Facts:
    - **Founded**: August 2008
    - **Headquarters**: San Francisco, California, USA
    - **Listings**: Over 7 million
    - **Countries**: Available in 220+ countries and regions
    
    ## Airbnb's History
    
    Airbnb was founded in August 2008 by Brian Chesky, Joe Gebbia, and Nathan Blecharczyk. The idea for the company came about when Chesky and Gebbia, struggling to pay rent for their San Francisco loft, decided to turn their living room into a bed and breakfast for conference attendees. They rented out air mattresses on their floor and provided homemade breakfast, thus the name "Air Bed & Breakfast" was born.
    
    The company quickly expanded, and by 2009, it had secured its first round of funding from Y Combinator. Over the years, Airbnb has grown exponentially, expanding into new markets and adding various types of accommodations, including entire homes, unique stays (like treehouses and castles), and boutique hotels.
    
    Today, Airbnb is a global phenomenon, with millions of hosts and guests using the platform to arrange stays in over 220 countries and regions. The company's growth has not been without challenges, including regulatory issues and competition from traditional hotel chains, but Airbnb continues to innovate and adapt, offering new services such as "Experiences" and "Airbnb Plus" to enhance the travel experience.
    """)
    
        st.image('img/Airbnb_Logo_Bélo.svg.png', caption='Airbnb', width=500)
