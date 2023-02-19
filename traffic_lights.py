import time

# Define the lanes and their corresponding traffic flow rates
lanes = {
    'north': 50,
    'east': 40,
    'south': 30,
    'west': 20
}

# Set the duration of the green light for each lane
green_light_duration = {
    'north': 20,
    'east': 20,
    'south': 20,
    'west': 20
}

# Set the duration of the yellow light
yellow_light_duration = 5

# Set the total duration of the light cycle
cycle_duration = sum(green_light_duration.values()) + yellow_light_duration

# Start the loop for the traffic lights
while True:
    # Determine which lane has the most traffic
    max_traffic_lane = max(lanes, key=lanes.get)
    
    # Set the green light duration for the max traffic lane
    green_light_duration[max_traffic_lane] += 5
    
    # Set the green light durations for the other lanes based on their traffic flow rates
    for lane in lanes:
        if lane != max_traffic_lane:
            green_light_duration[lane] = int(lanes[lane] / lanes[max_traffic_lane] * green_light_duration[max_traffic_lane])
    
    # Start the green light for each lane
    for lane in green_light_duration:
        print(f"{lane.capitalize()} lane: Green light for {green_light_duration[lane]} seconds")
        time.sleep(green_light_duration[lane])
        
        # Start the yellow light for each lane
        print(f"{lane.capitalize()} lane: Yellow light for {yellow_light_duration} seconds")
        time.sleep(yellow_light_duration)
    
    # Reset the green light durations for the next cycle
    green_light_duration = {
        'north': 20,
        'east': 20,
        'south': 20,
        'west': 20
    }
