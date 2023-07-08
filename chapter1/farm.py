def discrete_model_farm(process_dict, simulation_time):
    # Initiate variables
    time = 0
    supply_chain = 0

    # Define ending condition
    while time < simulation_time:

        supply_chain += 1
        process_names = list(process_dict.keys())

        for p in range(len(process_names)):
            event_duration = process_dict[process_names[p]]

            # Add the process duration
            time += event_duration
            print(f"{process_names[p]}  (completed): time = {time}")

        print(f"COMPLETED: Production cycle #{supply_chain} | Time = {time} days")


if __name__ == '__main__':
    # Create dictionary
    process_dict = {
        "Compost": 5,
        "Amendment": 3,
        "Weeding": 4,
        "Planting": 2,
        "Watering and growing": 60,
        "Harvesting": 7,
        "Delivery": 2
    }

    # Simulatiom time (days)
    simulation_time = 365

    # Run the model
    discrete_model_farm(process_dict, simulation_time)