## Question 1

The file `contactlist.csv` contains a comma-separated list of names, emails, and contact details.

These are to be stored in an appropriate Hash Table for quick lookup.

### Task 1.1

In `main.py`, write program code to read in the contact details from `contactlist.csv`, and store them in an appropriate data structure.

### Task 1.2

Implement `ContactList`, a class that uses a Hash Table to store the contact details, with the name as the key. This class is to be defined in `classes.py` and imported into `main.py`.

Names are to be hashed using the following algorithm:

```
for char in name
    cnum = ascii code of char
    pnum = <index of char in name (1st char has index 1)>
    add cnum*pnum to total
return total
```

Use an appropriate method to generate an index from the hashed name. Store **all the fields** under this index.

If two names have the same index, their contact details are to be stored together under that index. The name will be used to retrieve the correct set of contact details.

### Task 1.3

In `main.py`, write program code to store all the contact details from **Task 1.1**.

By using appropriate test values, write print statements to show that `ContactList` is able to retrieve the correct contact details (returns `True` only if the contact details match).

Also print out the data stored internally in the Hash Table.