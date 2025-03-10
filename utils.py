import numpy as np

def euclidean_distance(city_1,city_2):
    """
    Calculates the euclidean distance between city_1 and city_2

    Parameters:
    city_1,city_2:np.array
        (x,y) coordinates of both cities

    Returns:
        float 
            The euclidean distance.
    """

    return np.sqrt(np.sum((city_2-city_1)**2))

def total_tour_distance(cities_coordinates,tour):
    """
    Calculates the total distance for a particular tour sequence.

    Parameter:
        cities_coordinates:2d-array consisting of coordinates of the cities
        tour:Contains a particular tour sequence (example  -->[0,1,5,4])

    Returns:
        Total distance to visit all cities exactly once and return back to starting point.
    """
    total_cities=len(cities_coordinates)
    total_distance=0
    for i in range(total_cities-1):
        total_distance+=euclidean_distance(cities_coordinates[tour[i]],cities_coordinates[tour[i+1]])

    # Total returning distance from last distance to the starting point 
    total_distance+=euclidean_distance(cities_coordinates[tour[-1]],cities_coordinates[tour[0]])

    return total_distance
