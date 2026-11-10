import pandas as pd
import zipfile

## Explore content of the zip file 
zip_path = 'RawData/logistics-operations-database.zip'

data_tabels = [
    'drivers.csv', 'trucks.csv', 'routes.csv', 'loads.csv', 
    'trips.csv', 'fuel_purchases.csv', 'maintenance_records.csv', 
    'delivery_events.csv', 'safety_incidents.csv'
]

#Read the CSV files from the zip file into pandas DataFrames
with zipfile.ZipFile(zip_path, "r") as z:
    for tab in data_tabels:
        if tab in z.namelist():
            print(f"Reading {tab} from the zip file...")
            dfs = pd.read_csv(z.open(tab))
            print(f"DataFrame for {tab} created with shape: {df.shape}")
        else:
            print(f"{tab} not found in the zip file.")

# Extract Variable Namess
drivers =dfs.get('drivers.csv')
trucks = dfs.get('trucks.csv')
routes = dfs.get('routes.csv')
loads = dfs.get('loads.csv')
trips = dfs.get('trips.csv')
fuel_purchases = dfs.get('fuel_purchases.csv')
maintenance_records = dfs.get('maintenance_records.csv')
delivery_events = dfs.get('delivery_events.csv')
incidents = dfs.get('safety_incidents.csv')

# Relation: trips -> loads (1:1) and loads -> routes (M:1)
df_base = trips.merge(loads, on='load_id', how='left') # Merge trips with loads on load_id
df_base = df_base.merge(routes, on='route_id', how='left') # Merge the resulting DataFrame with routes on route_id

if 'trip_start_date' in df_base.columns:
    df_base['trip_start_date'] = pd.to_datetime(df_base['trip_start_date']) # Convert trip_start_date to datetime format





