# sgCarParks2020
Project Goal: Return the nearest car park in Singapore given a pair of coordinates. Project Admin: Bryan.

## Tasks:

The file `hdb-carpark-information.csv` contains a comma-separated list of HDB carparks in Singapore.

### Task 1.1

In `main.py`, write program code to read in the carpark details from `hdb-carpark-information.csv`, and store them in an appropriate data structure with the variable name `carpark_data`.

### Task 1.2

Calculate the total number of each **car_park_type**:
- surface carparks
- multi-storey carparks

Display the total number of each **car_park_type**.

### Task 1.3

Write a function, `sortByDistance()`, that takes in carpark data, an x-coordinate, and a y-coordinate as arguments, and returns carpark data sorted in **ascending order** of distance from the given point `x0`, `y0`.

The function should use the insertion sort algorithm to sort the carpark data.

`distance` is defined as the square root of `x1 - x0` and `y1 - y0`, where `x1`, `y1` are the x- and y-coordinates of each carpark.

### Task 1.4

Write a function, `nearestCarpark(x_coord, y_coord)` that takes in two float variables `x_coord` and `y_coord` representing a map coordinate, and returns the **car_park_no** that is nearest to this coordinate.

The nearest carpark is the one with the shortest `distance`.

Use this function to find the carpark nearest Nanyang Junior College. The `x_coord, y_coord` of Nanyang Junior College is `31630.2870, 36953.6515`.

### Task 1.5

Create a webpage that:

1. Displays an HTML form asking the user to enter a pair of coordinates, `x_coord` and `y_coord`,
2. Displays the input coordinates, and the **car_park_no** of the nearest car park.
