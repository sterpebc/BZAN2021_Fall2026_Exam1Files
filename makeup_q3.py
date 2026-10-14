# Question 3

# Sample data to test with:

sample_customers = [
    ('Harbor Cafe',      (500.00, 750.00, 250.00, 750.00)),
    ('Pinewood Dental',  (1200.00, 499.75, 450.00, 400.00)),
    ('Summit Fitness',   (2100.00,)),
    ('Lakeside Books',   (900.00, 600.00, 499.50, 350.25)),
    ('Northgate Motors', (650.00, 820.50, 575.25, 300.00, 125.00)),
    ('Riverside Print',  (999.75, 1000.00, 80.00))
]

# Write your function below this line









# Test call -- do not change this
# Note that the order of the names in your returned list does not matter.
print(rebate_customers(sample_customers))   # should print ['Harbor Cafe', 'Summit Fitness', 'Northgate Motors']
