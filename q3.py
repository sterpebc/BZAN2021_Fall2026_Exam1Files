# Question 3

# Sample data to test with:

sample_drivers = [
    ('Maria',  ('On time', 'Late', 'On time', 'On time', 'Late', 'On time', 'On time', 'On time', 'Late')),
    ('Devon',  ('On time', 'On time', 'Late', 'On time', 'On time', 'On time')),
    ('Priya',  ('Late', 'On time', 'On time', 'Late', 'On time', 'On time', 'On time', 'On time')),
    ('Tom',    ('Late', 'Late', 'On time', 'Late', 'Late')),
    ('Keisha', ('On time', 'On time', 'On time', 'On time', 'On time', 'On time', 'On time'))
]

# Write your function below this line









# Test call -- do not change this
# Note that the order of the names in your returned list does not matter.
print(needs_coaching(sample_drivers))   # should print ['Maria', 'Tom']
