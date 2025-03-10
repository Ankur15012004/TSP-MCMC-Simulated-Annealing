import numpy as np 
import matplotlib.pyplot as plt
from utils import total_tour_distance



def propose_new_tour(tour):
    """
    Propose the new tour by swapping randomly selected two cities.

    Parameters:
        tour: Current tour state in our markov chain.

    Returns:
        New tour state by randomly swapping two selected cities.
    
    """
    new_tour=tour.copy()
    i,j=np.random.choice(len(tour),size=2,replace=False)

    # Swapping them
    new_tour[i],new_tour[j]=new_tour[j],new_tour[i]

    return new_tour

def metropolis_hastings_accept(old_distance,new_distance,temperature):
    """
        Decides whether to accept the new proposal according to metropolis hasting rule.

        Parameters:
            old_distance: Total minimum distance of the current state in markov chain.
            new_distance: Total distance of the new proposed state in the markov chain.
            temperature: A parameter for simulated annealing.

        Return:
            A bool value whether to accept the new proposal or to reject the new proposal.
    
    """
    if new_distance<old_distance:
        return True
    
    acceptance_probability=np.exp((old_distance-new_distance)/temperature)

    return np.random.rand()<acceptance_probability

def simulated_annealing_mcmc(cities,initial_temperature,cooling_rate,iterations):

    """
        Solves the Travelling Salesman Problem (TSP) using Markov Chain Monte Carlo(MCMC) using simulated annealing.

        Parameters:
            -cities: 2d-array containing the corrdinates of the various cities.
            -temperature: Initial temperature for simulated annealing.
            -cooling_rate: decay factor for temperature.
            -iterations: Number of iteration until the stationary distribution is obtained for the markov chain.

        Returns:
            -best_tour: An array that contain best tours value(Approximation).
            -best_distance: Value corresponding the best tour

            
    """

    # Initializing the inital state of the Markov Chain

    num_cities=len(cities)
    current_tour=np.random.permutation(num_cities)
    current_distance=total_tour_distance(cities,current_tour)

    # Tracking the best tour distance

    best_tour=current_tour.copy()
    best_distance=current_distance

    temperature=initial_temperature

    # Start the MCMC loop

    for i in range(iterations):
        # Propose a new tour from our proposal Markov Chain
        new_tour=propose_new_tour(current_tour)
        new_distance=total_tour_distance(cities,new_tour)

        # Using Metropolis-Hastings rule to accept or reject the new proposal
        if metropolis_hastings_accept(current_distance,new_distance,temperature):
            current_tour=new_tour
            current_distance=new_distance

            # Tracking the best tour and distance
            if new_distance<best_distance:
                best_tour=new_tour.copy()
                best_distance=new_distance

        # Decreasing the temperature(simulated annealing)

        temperature*=cooling_rate

        if i % 100 == 0:
            print(f"Iteration {i}: Best Distance = {best_distance:.2f}, Temperature = {temperature:.4f}")

    return best_tour,best_distance

def plot_tour(cities,tour,title="TSP Tour"):
    """
        Plots the given approximate solution in 2d graph

        Parameters:
            cities: 2-d array consisting of (x,y) coordinates of various cities.
            tour: Contains the optimal tour sequence.

        Returns:
            2-d Plots.
    
    """
    plt.figure(figsize=(8,6))

    # Reorder the cities according to the best tour values 
    ordered_cities=cities[tour]

    # Plotting edges 
    plt.plot(ordered_cities[:, 0], ordered_cities[:, 1], 'bo-', label="Tour Path")
    
    # Connect the last city back to the first
    plt.plot([ordered_cities[-1, 0], ordered_cities[0, 0]], 
             [ordered_cities[-1, 1], ordered_cities[0, 1]], 'bo-')

    # Mark the cities
    for i, (x, y) in enumerate(cities):
        plt.text(x, y, str(i), fontsize=12, ha='right', color='red')  # City labels

    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Step 1: Generate random cities
    np.random.seed(42)  # For reproducibility
    num_cities = 15
    cities = np.random.rand(num_cities, 2) * 100  # Random coordinates in [0,100] x [0,100]

    # Step 2: Run MCMC Simulated Annealing for TSP
    initial_T = 1000  # Initial temperature
    cooling_rate = 0.999  # Cooling factor
    iterations = 5000  # Total iterations

    best_tour, best_distance = simulated_annealing_mcmc(cities, initial_T, cooling_rate, iterations)

    # Step 3: Plot the results
    plot_tour(cities, best_tour, title=f"Optimized TSP Tour (Distance: {best_distance:.2f})")
    print("\nBest Tour Sequence (City Indices):")
    print(best_tour)









