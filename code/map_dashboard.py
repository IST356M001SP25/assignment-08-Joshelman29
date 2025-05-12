
'''
map_dashboard.py
'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd

# Map display constants
SYRACUSE_CENTER = (43.0481, -76.1474)
DEFAULT_ZOOM = 14
COLOR_SCALE_MIN = 1000
COLOR_SCALE_MAX = 5000


def render_parking_map_dashboard():
    location_data = pd.read_csv('./cache/top_locations_mappable.csv')

    st.title('High-Fine Parking Violation Locations in Syracuse')
    st.caption('Displays Syracuse locations with over $1,000 in accumulated parking fines on an interactive map.')

    geo_df = gpd.GeoDataFrame(location_data, geometry=gpd.points_from_xy(location_data.lon, location_data.lat))

    base_map = folium.Map(location=SYRACUSE_CENTER, zoom_start=DEFAULT_ZOOM)
    mapped_layer = geo_df.explore(
        column='amount',
        m=base_map,
        cmap="magma",
        vmin=COLOR_SCALE_MIN,
        vmax=COLOR_SCALE_MAX,
        legend=True,
        legend_name='Total Fine Amount ($)',
        marker_type="circle",
        marker_kwds={"radius": 10, "fill": True},
    )

    sf.folium_static(mapped_layer, width=800, height=600)


if __name__ == '__main__':
    render_parking_map_dashboard()
