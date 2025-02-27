import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

from components.functions import (count_plot, bar_chart, pie_chart, violin_plot, box_plot, scatter_plot, count_plot_swapped)


def display_luxury_accommodations_section(luxury : pd.DataFrame):
    
    # # Verificar si luxury_data es una tupla y extraer el DataFrame correcto
    # if isinstance(luxury_data, tuple):
    #     # Asumiendo que el DataFrame está en la primera posición de la tupla
    #     luxury = luxury_data[0]
    # else:
    #     # Si ya es un DataFrame, lo usamos directamente
    #     luxury = luxury_data
    
    st.subheader("📊 Luxury Tokyo in Numbers")
    
    # Verificar que luxury es un DataFrame antes de continuar
    if not isinstance(luxury, pd.DataFrame):
        st.error("Error: Los datos no tienen el formato esperado. Se esperaba un DataFrame.")
        return
    
    # Verificar que las columnas necesarias existen
    required_columns = ['neighbourhood', 'price_dollar', 'host_id', 'number_of_reviews', 'room_type']
    missing_columns = [col for col in required_columns if col not in luxury.columns]
    
    if missing_columns:
        st.error(f"Error: Faltan las siguientes columnas en el DataFrame: {', '.join(missing_columns)}")
        st.write("Columnas disponibles:", luxury.columns.tolist())
        return
    
    # Get the top N neighbourhoods by value counts
    top_neighbourhoods = luxury['neighbourhood'].value_counts().nlargest(5).index
    filtered_df = luxury[luxury['neighbourhood'].isin(top_neighbourhoods)]
    
    
    tab1, tab2, tab3, = st.tabs(['🔎 Overview','🏡 Neighbourhood Analysis', '🛏️ Room Type Analysis'])
    
    with tab1:
        
        # Usando columnas para mostrar métricas
        cols = st.columns(4)

        # Available Accommodations
        with cols[0]:
            
            st.markdown("### Accommodations")
            st.markdown(f"<h2 style='text-align: center;'>{len(luxury):,}</h2>", unsafe_allow_html=True)

        # Average Price/Night
        with cols[1]:
            st.markdown("### Price/Night")
            st.markdown(f"<h2 style='text-align: center;'>${luxury['price_dollar'].mean():.2f}</h2>", unsafe_allow_html=True)

        # Unique Hosts
        with cols[2]:
            st.markdown("### Unique Hosts")
            st.markdown(f"<h2 style='text-align: center;'>{luxury['host_id'].nunique():,}</h2>", unsafe_allow_html=True)

        # Average Reviews
        with cols[3]:
            st.markdown("### Average Reviews")
            st.markdown(f"<h2 style='text-align: center;'>{luxury['number_of_reviews'].mean():.1f}</h2>", unsafe_allow_html=True)
        
        st.markdown("---")

        
        # Mapa de ejemplo mejorado con color según precio
        st.subheader("Sample Listings Map")
        st.markdown("Showing a sample of 100 random listings on the map...")
        try:
            # Usando sample para obtener una muestra aleatoria en lugar de head
            sample_size = min(100, len(luxury))
            sample_df = luxury.sample(sample_size, random_state=42) if sample_size > 0 else luxury
        
            # Verificar que las columnas necesarias para el mapa existen
            map_columns = ['latitude', 'longitude', 'host_name', 'priceDisc', 'room_type']
            missing_map_columns = [col for col in map_columns if col not in sample_df.columns]
            
            if missing_map_columns:
                st.warning(f"No se pueden mostrar algunos elementos del mapa porque faltan las columnas: {', '.join(missing_map_columns)}")
            else:
                # Creando un mapa centrado en la ubicación promedio
                m = folium.Map(location=[sample_df['latitude'].mean(), sample_df['longitude'].mean()], 
                              zoom_start=12, 
                              tiles="CartoDB positron")  # Usando un estilo más limpio
                
                # Añadiendo marcadores con información más detallada
                for idx, row in sample_df.iterrows():
                    popup_text = f"""
                    <b>{row['host_name']}</b>

                    Price: ${row['price_dollar']:.2f}

                    Room Type: {row['room_type']}
                    """
                    
                    color= 'green'
                    
                    folium.Marker(
                        location=[row['latitude'], row['longitude']],
                        popup=folium.Popup(popup_text, max_width=200),
                        icon=folium.Icon(color=color)
                    ).add_to(m)
                    
                # Añadiendo leyenda al mapa - actualizada para reflejar categorías de priceDisc
                legend_html = """
                <div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background-color: white; padding: 10px; border: 2px solid grey; border-radius: 5px;">
                    <p><i class="fa fa-circle" style="color:green"></i> Low</p>
                    <p><i class="fa fa-circle" style="color:blue"></i> Medium</p>
                    <p><i class="fa fa-circle" style="color:orange"></i> High</p>
                    <p><i class="fa fa-circle" style="color:red"></i> Very High</p>
                </div>
                """
                m.get_root().html.add_child(folium.Element(legend_html))
                
                folium_static(m)
        except Exception as e:
            st.error(f"Error al mostrar el mapa: {str(e)}")
    
    # Definiendo las órdenes personalizadas
    
    # Orden personalizado para barrios
    neighbourhood_list = luxury['neighbourhood'].unique().tolist()
    neighbourhood_order = sorted(neighbourhood_list)
    
    # Orden personalizado para tipos de habitaciones
    room_type_list = luxury['room_type'].unique().tolist()
    room_type_order = sorted(room_type_list)
    
    with tab2:
        st.subheader('Listings Count by Neighbourhood')
        
        graph1 = count_plot_swapped(
        luxury,
        x='neighbourhood',
        hue='neighbourhood', 
        title='Listings Count by Neighbourhood')
        st.pyplot(graph1)
        st.markdown("""
        - **Taito**: The most popular neighbourhood with the highest number of listings.
        - **Shinjuku**: The neighbourhood with the highest listings count, reflecting its popularity.
        - **Luxury Listings**: Luxury accommodattions are consideres based on price, >720 dollars per night.
        """)
        
        st.subheader("""
                    Since there are many neighbourhoods, we will focus on the top 5 neighbourhoods.                     
                    """)
        
        graph1_1 = count_plot(
        filtered_df,
        x='neighbourhood',
        hue='neighbourhood', 
        title='Listings Count by Neighbourhood')
        st.pyplot(graph1_1)
        st.markdown("""
        - **Shinjuku**: The most popular neighbourhood with the highest number of listings on normal and luxury accommodations.
        - **Shibuya**: Surprisingly, Shibuya is not in the top 5 luxury neighbourhoods by listings count.
        """)
        
        st.subheader('Price Distribution by Neighbourhood')
        graph2 = box_plot(
        filtered_df,
        x='neighbourhood',
        y='price_dollar',
        color='neighbourhood',
        hue='neighbourhood',
        title='Price Distribution by Neighbourhood')       
        st.plotly_chart(graph2)
        st.markdown("""
        - **Shinjuku**: The luxury neighbourhood with the lowest median price.
        - **Taito**: The neighbourhood with the widest range of prices, having in mind all of them are considered luxury listings.
        """)
        
    with tab3:
        
        st.subheader('Room Type Distribution')
        graph3 = pie_chart(
        filtered_df,
        names='room_type',
        values='id',
        title='Listings Count by Room Type') 
        st.plotly_chart(graph3)
        st.markdown("""
        - **Entire home/apt**: The most common room type among outliers, reflecting the luxury listings.
        - **Private Rooms**: The second most common room type among outliers.
        - **Hotel Rooms**: The least common room type among outliers. Less than 1% of listings.
        - **Shared Rooms**: No shared rooms among outliers. All listings are luxury accommodations.
        """)
        
        st.subheader('Room Type Price Distribution')
        graph4 = box_plot(
        filtered_df,
        x='room_type',
        y='price_dollar',
        color='room_type',
        hue='room_type',
        title='Room Type Price Distribution')
        st.plotly_chart(graph4)
        st.markdown("""
        - **Private Room**: This room type has a ditribution of prices with the highest median price among luxury accommodations.
        - **Entire Home/Apt**: The room type with the lowest median price among luxury accommodations. 
        - **Per night price**: The highest price among the outliers listing is 6.600 dollars. Excluding the two outliers of 10.000 dollars and 40.000 dollars per night.
        """)
        