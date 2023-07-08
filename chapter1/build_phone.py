import numpy as np
import matplotlib.pyplot as plt


def discrete_model_build_phone(processes_dictionary, simulation_time):
    # Initiate variables
    time = 0
    supply_chain = 0

    time_all = np.array([[0],[0]])

    # Run model
    while (time < simulation_time):

        # Update the supply_chain number
        supply_chain += 1
        process_names = list(processes_dictionary.keys())

        for p in range(len(process_names)):

            process_name_p = process_names[p]

            # Add the process time to the time variable
            time += processes_dictionary[process_name_p]
            time_all = np.append(time_all,np.array([[time], [processes_dictionary[process_name_p]]]), axis=1)
            if (time + processes_dictionary[process_name_p] > simulation_time):
                return time_all

            print(f"Time = {time} days | Process Complete: {process_name_p}")

        print(f"COMPLETED: Supply-Chain cycle #{supply_chain} | Time = {time} days")

    return time_all


if __name__ == '__main__':
    processes = {"Sourcing raw material": 5, "Transport of raw material": 1, "Manufacturing parts": 3,
                 "Assembling parts": 2, "Selling products": 3, "Delivering products": 1.5}

    # Assign the simulation time
    simulation_time = 365

    # Run the model
    time_all = discrete_model_build_phone(processes, simulation_time)

    cumulative_time = time_all[0]
    individual_process_time = time_all[1]

    # Create 2D plot
    plt.plot(cumulative_time, individual_process_time,
             color='black', markerfacecolor='mediumvioletred',
             marker='o', markersize=6, linewidth=1.5)

    plt.xlabel("Cumulative duration (days)")
    plt.ylabel("Duration of each process (days)")
    plt.grid()
    plt.show()

    simulation_time = 365 * 5
    time_all = discrete_model_build_phone(processes, simulation_time)
    """Reducing the average duration of 'Delivering product' to 1 day would allow completing 121 cycles in 5 years. 
    This is an excellent example of how discrete-event models can support business decisions."""