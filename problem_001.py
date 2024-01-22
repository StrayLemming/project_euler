'''

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
Find the sum of all the multiples of 3 or 5 below N. 


'''


def find_sequence_sum(n, factor):
    # sequence of multiples of 3: 3,6,9,..
    # sequence of multiples of 5: 5,10,15,..
    # Arithmetic sequence formula: n/2(first_term + last_term)

    first_term = factor
    last_term = ((n-1) // factor) * factor
    num_terms = ((last_term - first_term) // factor) + 1
    total = ((num_terms)*(first_term + last_term)) // 2
    return total


tc = int(input().strip())

for _ in range(tc):
    n = int(input().strip())
    # Need to minus 15 as this is common in a sequence of 3 AND 5, therefore only want to add once
    result = find_sequence_sum(
        n, 3) + find_sequence_sum(n, 5) - find_sequence_sum(n, 15)

    print(result)
