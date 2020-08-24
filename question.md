


https://repl.it/@mrjsng/ExamPractice1

## Question 1

The file `hdb-carpark-information.csv` contains a comma-separated list of HDB carparks in Singapore.

### Task 1.1

In `main.py`, write program code to read in the contact details from `hdb-carpark-information.csv`, and store them in an appropriate data structure with the variable name `carpark_data`.

### Task 1.2

1. Calculate the total number of each **car_park_type**:
   - surface carparks
   - multi-storey carparks
2. Return the **car_park_no** with the highest number of total carparks.


### Task 1.3

The `x_coord, y_coord` of Nanyang Junior College is `31630.2870, 36953.6515`.

Write a function, `sortByDistance()`, that takes in `carpark_data` as an argument and returns the data sorted by `distance` **in ascending order**.

`distance` is defined as the square root of `x_coord` and `y_coord`.

### Task 1.4

Write a function, `nearestCarpark(x_coord, y_coord)` that takes in two float variables `x_coord` and `y_coord` representing a map coordinate, and returns the **car_park_no** that is nearest to this coordinate.

The nearest carpark is the one with the shortest `distance`.

### Task 1.5

Create a webpage that:

1. Displays an HTML form asking the user to enter a pair of coordinates, `x_coord` and `y_coord`,
2. Displays the input coordinates, and the **car_park_no** of the nearest car park.