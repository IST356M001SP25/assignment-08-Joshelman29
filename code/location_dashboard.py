'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")


def render_location_dashboard():
    ticket_data = pd.read_csv('./cache/tickets_in_top_locations.csv')

    st.title('High-Violation Parking Locations in Syracuse')
    st.caption('Displays data for locations with $1,000+ in parking ticket fines.')

    unique_locations = ticket_data['location'].unique()
    selected_location = st.selectbox('Choose a location:', unique_locations)

    if selected_location:
        location_data = ticket_data[ticket_data['location'] == selected_location]

        col_left, col_right = st.columns(2)

        with col_left:
            st.metric("Number of Tickets", location_data.shape[0])
            fig_hour, ax_hour = plt.subplots()
            ax_hour.set_title('Ticket Counts by Hour')
            sns.barplot(data=location_data, x="hourofday", y="count", estimator="sum", hue="hourofday", ax=ax_hour)
            st.pyplot(fig_hour)

        with col_right:
            total_fines = location_data['amount'].sum()
            st.metric("Total Fines", f"$ {total_fines}")
            fig_day, ax_day = plt.subplots()
            ax_day.set_title('Ticket Counts by Day')
            sns.barplot(data=location_data, x="dayofweek", y="count", estimator="sum", hue="dayofweek", ax=ax_day)
            st.pyplot(fig_day)

        st.map(location_data[['lat', 'lon']])



render_location_dashboard()
