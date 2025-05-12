import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    location_totals_df = violations_df.pivot_table(index='location', values='amount', aggfunc='sum').sort_values(by='amount', ascending=False)
    location_totals_df['location'] = location_totals_df.index
    location_totals_df.reset_index(drop=True, inplace=True)
    return location_totals_df[location_totals_df['amount'] >= threshold]


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locs_df = top_locations(violations_df, threshold)
    unique_coords_df = violations_df[['location', 'lat', 'lon']].drop_duplicates(subset=['location'])
    mapped_df = pd.merge(top_locs_df, unique_coords_df, on='location')
    return mapped_df.drop_duplicates()


def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000)  -> pd.DataFrame:
    top_locs_only_df = top_locations(violations_df)
    filtered_tickets_df = pd.merge(top_locs_only_df[['location']], violations_df, on='location')
    return filtered_tickets_df


print("Running ETL job...")
print("Loading parking violations data from ./cache/final_cuse_parking_violations.csv")
violations_data_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    
top_locs_data = top_locations(violations_data_df)
print("Saving top locations to ./cache/top_locations.csv")
top_locs_data.to_csv('./cache/top_locations.csv', index=False)
    
mappable_locs_data = top_locations_mappable(violations_data_df)
print("Saving mappable top locations to ./cache/top_locations_mappable.csv")
mappable_locs_data.to_csv('./cache/top_locations_mappable.csv', index=False)

tickets_data = tickets_in_top_locations(violations_data_df, top_locs_data)
print("Saving tickets from top locations to ./cache/tickets_in_top_locations.csv")
tickets_data.to_csv('./cache/tickets_in_top_locations.csv', index=False)
