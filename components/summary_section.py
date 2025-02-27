import streamlit as st

def summary_section():    
    st.markdown("""
    ## General Findings
    
    1. **Neighbourhood**: The majority of listings are concentrated in certain neighbourhoods.
    2. **Room Type**: Entire homes/apartments are the most common type of listing.
    3. **Price**: There is a wide range of prices, influenced by location and room type.
    4. **Minimum Nights**: Different listings have varying minimum night requirements.
    
    ### Specific Findings
    
    1. **Neighbourhood**: Listings in popular neighbourhoods tend to have higher prices. This reflects the desirability and demand for these locations.
    
    2. **Room Type**: Entire homes/apartments command higher prices compared to private or shared rooms. This is expected due to the increased space and privacy offered.
    
    3. **Price**: High-priced listings are generally associated with more luxurious accommodations and prime locations. However, there is also a significant number of budget-friendly options.
    
    4. **Minimum Nights**: Listings with higher minimum nights may indicate hosts preference for longer stays. This could be due to various factors such as location, price, and host strategy.
    
    The Tokyo Airbnb analysis provides insights into the market dynamics, helping hosts and guests make informed decisions.
    """)