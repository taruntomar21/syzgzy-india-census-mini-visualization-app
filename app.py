import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.header('India Census Analysis by Maping')

final_df = pd.read_csv('india-census.csv')

list_of_states = list(final_df['State'].unique())
list_of_states.insert(0,'Overall India')
list_of_districts = list(final_df['District'].sort_values())

st.sidebar.title('India Census Analysis')

select_state = st.sidebar.selectbox('Select State',list_of_states)
# select_district = st.sidebar.selectbox('Select District',list_of_districts)

primary = st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[5:]))

plot = st.sidebar.button('Plot Map')

if plot:
    st.text('primary parameter represent size')
    st.text('secondary parameter represent color')

    if select_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=3.5, size_max=35
                                ,mapbox_style='open-street-map', width=1300, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        state_df = final_df[final_df['State'] == select_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=5,
                                size_max=35,mapbox_style="carto-positron", width=1400, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)