# Question 4

# Sample data to test with:

sample_questions = ["Wait time", "Staff courtesy", "Cleanliness", "Value for money", "Likely to return"]

sample_ratings = [
    [4, 5, 4, 3, 4],
    [2, 4, 5, 2, 3],
    [3, 5, 4, 3, 4],
    [2, 4, 5, 3, 5],
    [3, 5, 3, 2, 4],
    [4, 4, 4, 3, 3],
]


# Write your function below this line









# Test call -- do not change this
# Depending on how you do the math, your last digit may differ.
print(experience(sample_questions, sample_ratings))   # should print ('Value for money', 2.6666666666666665)
