import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("traffic_data (1).csv")

# Create Total Vehicles column
df["Total_Vehicles"] = df["Cars_Count"] + df["Bikes_Count"] + df["Buses_Count"]




def total_vehicles_per_junction(data):
    return data.groupby("Junction_ID")["Total_Vehicles"].sum()

total_vehicles = total_vehicles_per_junction(df)
print(total_vehicles)
===================================

def busiest_junction(data):
    totals = total_vehicles_per_junction(data)
    return totals.idxmax(), totals.max()

busiest = busiest_junction(df)
print("Busiest Junction:", busiest)


====================================

def least_busy_junction(data):
    totals = total_vehicles_per_junction(data)
    return totals.idxmin(), totals.min()

least_busy = least_busy_junction(df)
print("Least Busy Junction:", least_busy)


=================================

def average_waiting_time(data):
    return data["Avg_Wait_Time"].mean()

print("Average Waiting Time:", average_waiting_time(df))

def average_waiting_time_per_junction(data):
    return data.groupby("Junction_ID")["Avg_Wait_Time"].mean()

print(average_waiting_time_per_junction(df))


===============================

def peak_traffic_time(data):
    time_totals = data.groupby("Time_of_Day")["Total_Vehicles"].sum()
    return time_totals.idxmax(), time_totals.max()

peak_time = peak_traffic_time(df)
print("Peak Traffic Time:", peak_time)
==================================


def convert_to_numpy_arrays(data):
    cars = data["Cars_Count"].to_numpy()
    bikes = data["Bikes_Count"].to_numpy()
    buses = data["Buses_Count"].to_numpy()
    total = data["Total_Vehicles"].to_numpy()
    wait_time = data["Avg_Wait_Time"].to_numpy()
    
    return cars, bikes, buses, total, wait_time

cars_np, bikes_np, buses_np, total_np, wait_np = convert_to_numpy_arrays(df)

print("Cars array:", cars_np)
print("Total vehicles array:", total_np)

===========================================================================================













import pandas as pd

# 1. Load the dataset
df = pd.read_csv('traffic_data.csv')

# 1. Add column: Total_Vehicles
# This sums up Cars, Bikes, and Buses for each row
df['Total_Vehicles'] = df['Cars_Count'] + df['Bikes_Count'] + df['Buses_Count']

# 3and4. Group data by Time_of_Day and Find average vehicles per time slot
avg_vehicles = df.groupby('Time_of_Day')['Total_Vehicles'].mean().reset_index()
print("Average Vehicles per Time Slot:\n", avg_vehicles)

# 2. Sort junctions by congestion (Total Vehicles)
# We'll group by Junction_ID to see which junction is busiest overall
junction_congestion = df.groupby('Junction_ID')['Total_Vehicles'].sum().sort_values(ascending=False).reset_index()
print("\nJunctions Sorted by Congestion:\n", junction_congestion)

# 5. Detect high congestion zones
# Let's define "High Congestion" as any junction/time where Total_Vehicles is 
# above the 75th percentile of the data.
threshold = df['Total_Vehicles'].quantile(0.75)
high_congestion_zones = df[df['Total_Vehicles'] > threshold]

print(f"\nHigh Congestion Zones (Total Vehicles > {threshold}):")
print(high_congestion_zones[['Junction_ID', 'Time_of_Day', 'Total_Vehicles']])

=============================================================================================================














import matplotlib.pyplot as plt
import pandas as pd

# --- RE-ESTABLISH DATA (To ensure shapes are correct) ---
df = pd.read_csv('traffic_data.csv')
df['Total_Vehicles'] = df['Cars_Count'] + df['Bikes_Count'] + df['Buses_Count']

# 1. Bar Chart – Junction vs Total Vehicles
# We use .reset_index() to make sure we have a clean table to plot from
junction_data = df.groupby('Junction_ID')['Total_Vehicles'].sum().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(junction_data['Junction_ID'].astype(str), 
        junction_data['Total_Vehicles'], 
        color='skyblue', edgecolor='black')

plt.title('Total Vehicles per Junction')
plt.xlabel('Junction ID')
plt.ylabel('Vehicle Count')
plt.show()

# 2. Line Chart – Time of Day vs Average Traffic
avg_time = df.groupby('Time_of_Day')['Total_Vehicles'].mean().reindex(['Morning', 'Afternoon', 'Evening', 'Night']).reset_index()

plt.figure(figsize=(8, 5))
plt.plot(avg_time['Time_of_Day'], avg_time['Total_Vehicles'], 
         marker='o', linestyle='-', color='red')
plt.title('Average Traffic per Time Slot')
plt.grid(True, alpha=0.3)
plt.show()

# 3. Stacked Bar Chart – Vehicle Types per Junction
types_data = df.groupby('Junction_ID')[['Cars_Count', 'Bikes_Count', 'Buses_Count']].sum()
types_data.plot(kind='bar', stacked=True, figsize=(8, 5), edgecolor='black')
plt.title('Vehicle Types per Junction')
plt.xticks(rotation=0)
plt.show()

# 4. Histogram – Waiting Time Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Avg_Wait_Time'], bins=6, color='purple', edgecolor='black', alpha=0.7)
plt.title('Waiting Time Distribution')
plt.xlabel('Seconds')
plt.ylabel('Frequency')
plt.show()













=====================================================================================================================================




report_content = """
TRAFFIC ANALYSIS SUMMARY REPORT
... Based on the data extracted from your screenshots and the analysis performed, here is the content for your Traffic_Analysis_Report.txt.

Traffic_Analysis_Report.txt
TRAFFIC ANALYSIS SUMMARY REPORT Date: 15-01-2026 Data Source: traffic_data.csv

1. Busiest Junction

Junction ID: J2

Analysis: J2 consistently recorded the highest total vehicle counts across all time slots, with a peak of 360 vehicles during the Evening.

2. Peak Traffic Time

Peak Time Slot: Evening

Analysis: Average traffic across all junctions is highest during the Evening hours, followed closely by the Morning rush.

3. Average Waiting Time

Overall Average: Approximately 43.75 seconds

Maximum Recorded: 85 seconds (J2 during Evening)

Minimum Recorded: 10 seconds (J3 during Night)

4. Congested Zones (High Traffic Detectors) The following slots were identified as "High Congestion" (Total Vehicles > 250):

Junction J2 - Morning: 315 Vehicles

Junction J2 - Afternoon: 248 Vehicles

Junction J2 - Evening: 360 Vehicles

Junction J1 - Evening: 250 Vehicles

5. Improvement Suggestions

Dynamic Signal Timing at J2: Since J2 handles the highest volume, implementing AI-controlled traffic lights that extend green-light duration during the Morning and Evening peaks could reduce the 85-second wait times.

Evening Shift Management: Traffic volume increases by nearly 200% from Night to Evening. Public transit (Buses) should be incentivized or increased in frequency during this window to reduce the number of private Cars.

Bicycle Lane Infrastructure: There is a significant number of "Bikes" recorded (up to 110 at J2). Dedicated bike lanes at J1 and J2 would separate slow-moving traffic from fast-moving cars, improving the overall flow.

Night-time Maintenance: Since traffic is lowest at Night (minimum 54 vehicles), any road repairs or infrastructure upgrades should be strictly scheduled during this window to avoid city-wide gridlock.(paste the text above here) ...
"""


with open('Traffic_Analysis_Report.txt', 'w') as f:
    f.write(report_content)

print("Report generated: Traffic_Analysis_Report.txt")
