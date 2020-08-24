


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

Add another field, `distance`, to `carpark_data` for each entry. The value of this field is a float representing the straight-line distance between that carpark and Nanyang Junior College. Calculate the `distance` value for each **car_park_no**.

Write a function, `sortByDistance()`, that takes in `carpark_data` as an argument and returns the data sorted by `distance`.