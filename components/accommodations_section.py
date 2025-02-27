import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

from components.functions import (count_plot, bar_chart, pie_chart, violin_plot, box_plot, scatter_plot, count_plot_swapped)


def display_accommodations_section(normal: pd.DataFrame):
    
    # # Verificar si normal_data es una tupla y extraer el DataFrame correcto
    # if isinstance(normal_data, tuple):
    #     # Asumiendo que el DataFrame está en la primera posición de la tupla
    #     normal = normal_data[0]
    # else:
    #     # Si ya es un DataFrame, lo usamos directamente
    #     normal = normal_data
    
    st.subheader("📊 Tokyo in Numbers")
    
    # Verificar que normal es un DataFrame antes de continuar
    if not isinstance(normal, pd.DataFrame):
        st.error("Error: Los datos no tienen el formato esperado. Se esperaba un DataFrame.")
        return
    
    # Verificar que las columnas necesarias existen
    required_columns = ['neighbourhood', 'price_dollar', 'host_id', 'number_of_reviews', 'room_type', 'priceDisc']
    missing_columns = [col for col in required_columns if col not in normal.columns]
    
    if missing_columns:
        st.error(f"Error: Faltan las siguientes columnas en el DataFrame: {', '.join(missing_columns)}")
        st.write("Columnas disponibles:", normal.columns.tolist())
        return
    
    # Get the top N neighbourhoods by value counts
    top_neighbourhoods = normal['neighbourhood'].value_counts().nlargest(5).index
    filtered_df = normal[normal['neighbourhood'].isin(top_neighbourhoods)]
    
    
    tab1, tab2, tab3, tab4 = st.tabs(['🔎 Overview','🏡 Neighbourhood Analysis', '🛏️ Room Type Analysis', '💵 Price Analysis'])
    
    with tab1:
        
        # Usando columnas para mostrar métricas
        cols = st.columns(4)

        # Available Accommodations
        with cols[0]:
            st.markdown("### Accommodations")
            st.markdown(f"<h2 style='text-align: center;'>7399199)

        # Average Price/Night
        with cols[1]:
            st.markdown("### Price/Night")
            st.markdown(f"<h2 style='text-align: center;'>${normal['price_dollar'].mean():.2f}</h2>", unsafe_allow_html=True)

        # Unique Hosts
        with cols[2]:
            st.markdown("### Unique Hosts")
            st.markdown(f"<h2 style='text-align: center;'>{normal['host_id'].nunique():,}</h2>", unsafe_allow_html=True)

        # Average Reviews
        with cols[3]:
            st.markdown("### Average Reviews")
            st.markdown(f"<h2 style='text-align: center;'>{normal['number_of_reviews'].mean():.1f}</h2>", unsafe_allow_html=True)
        
        st.markdown("---")

        
        # Mapa de ejemplo mejorado con color según precio
        st.subheader("Sample Listings Map")
        st.markdown("Showing a sample of 100 random listings on the map...")
        try:
            # Usando sample para obtener una muestra aleatoria en lugar de head
            sample_size = min(100, len(normal))
            sample_df = normal.sample(sample_size, random_state=42) if sample_size > 0 else normal
        
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
                    
                    # Color del marcador basado en la categoría de precio
                    if row['priceDisc'] == 'Low':
                        color = 'green'
                    elif row['priceDisc'] == 'Medium':
                        color = 'blue'
                    elif row['priceDisc'] == 'High':
                        color = 'orange'
                    elif row['priceDisc'] == 'Very High':
                        color = 'red'
                    else:
                        color = 'gray'  # Default color for any undefined category
                    
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
    # Orden personalizado para categorías de precio
    custom_order = ['Low', 'Medium', 'High', 'Very High']
    
    # Orden personalizado para barrios
    neighbourhood_list = normal['neighbourhood'].unique().tolist()
    neighbourhood_order = sorted(neighbourhood_list)
    
    # Orden personalizado para tipos de habitaciones
    room_type_list = normal['room_type'].unique().tolist()
    room_type_order = sorted(room_type_list)
    
    with tab2:
        st.subheader('Listings Count by Neighbourhood')
        
        graph1 = count_plot_swapped(
        normal,
        x='neighbourhood',
        hue='neighbourhood', 
        title='Listings Count by Neighbourhood')
        st.pyplot(graph1)
        st.markdown("""
        - **Top 5 Neighbourhoods**: Shinjuku, Taito, Shibuya, Sumida, and Minato are the top 5 neighbourhoods with the most listings.
        - **Less Common Neighbourhoods**: Adachi, Katsushika, and Itabashi have fewer listings compared to other neighbourhoods.
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
            - **Shinjuku**: The most popular neighbourhood with the highest number of listings.
            - **Neighbourhoods**: Surprisingly, the top 5 most listed neighbourhoods include some neighbourhoods further away from the centre of Tokyo.
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
        - **Taito**: The neighbourhood with the widest range of prices, indicating a mix of budget and luxury listings.
        - **Shinjuku**: The neighbourhood with the highest median price, reflecting its popularity and desirability.
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
        - **Entire home/apt**: The most common room type, accounting for over 90% of listings.
        - **Shared room**: The least common room type, with less than 1% of listings.
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
        - **Entire home/apt**: The room type with the highest median price, reflecting the increased space and privacy offered.
        - **Shared room**: The room type with the lowest median price, suitable for budget-conscious travelers.
        """)
        
    with tab4:
        st.subheader('Box Plot Price Distribution by Neighbourhood - Price Disc')
        graph5 = box_plot(
            filtered_df,
            x='priceDisc',
            y='price_dollar',
            color='neighbourhood',
            hue='neighbourhood',
            title='Price Distribution by Neighbourhood',
            category_orders={'priceDisc': custom_order, 'neighbourhood': neighbourhood_order})
        st.plotly_chart(graph5)
        st.markdown("""
        - **Neighbourhoods**: The price distribution varies across neighbourhoods, with wide range of options for all neighbourhoods.
        """)
            
        st.subheader('Box Plot Price Distribution by Room Type - Price Disc')
        graph6 = box_plot(
            filtered_df,
            x='priceDisc',
            y='price_dollar',
            color='room_type',
            hue='room_type',
            title='Price Distribution by Room Type',
            category_orders={'priceDisc': custom_order, 'room_type': room_type_order})
        st.plotly_chart(graph6)
        st.markdown("""
        - **Room Types**: The price distribution varies by room type, there is variation in prices for all room types.
        - **Very High**: This price category only has Entire home/apt and Private Room listings.
        """)