import streamlit as st

def summary_section():    
    st.markdown("""
   ## General Summary
    
    - **Neighbourhood Distribution**: The distribution of listings across neighbourhoods is not uniform. Surprisingly the most popular neighbourhoods are not only at the Cernter of Tokyo, there are also some neighbourhoods that are not at the center of Tokyo but have a lot of listings.
    - **Room Type Distribution**: Entire homes/apartments are the most common type of listing, followed by private rooms, hotel rooms and shared rooms.
    - **Price Distribution**: Prices vary widely, with a significant number of listings at both the lower and higher ends of the spectrum.
    - **February**: Is the least month with listings. Becuase of the cold weather in Tokyo. And some temples and sanctuaries are closed.
    - **Minimum and Maximum Nights**: The minimum and maximum nights required for bookings vary across listings.
    
    
    ### Accommodations Findings
    
    - **Taito**: Taito has the chepest listings as well as the more expensive listings.
    - **Shinjuku**: Shinjuku has the most listings.
    - **Shared Rooms**: Shared rooms are the cheapest option, in general.
    - **Entire Homes/Apartments**: Entire homes/apartments are the most common type of listing (>90%).
    - **More expensive listings**: There are more expensive rooms are Entire Homes/Apartments and Private Rooms. Located at the Sumida and Shibuja neighbourhoods.
    
    
    ### Luxury Accommodations Findings
    
    - **Outliers**: Luxury listings are characterized by their high prices. There were two outliers with extremely high prices, which may be due to unique features or premium services that I excluded from the analysis.
    - **Average Price**: The average price of luxury listings is significantly higher than that of normal listings, more then 1500%.
    - **Shinjuku**: Shinjuku has the most luxury listings.
    - **Taito**: Taito has the highest mean price for luxury listings.
    - **Entire Homes/Apartments**: Entire homes/apartments are the most common type of luxury listing.
    """)
