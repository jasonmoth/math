from itertools import permutations

def compute_all_digit_rearrangements(n):
    digits = str(n)
    perm = permutations(digits)
    rearrangements = [int(''.join(p)) for p in perm]
    return rearrangements

three_digit_integers = [i for i in range(1, 1001)]
rearrangement_sums = []

for i in three_digit_integers:
    rearrangement_sums.append({
        "rootInteger": i,
        "summands": compute_all_digit_rearrangements(i),
        "sum": sum(compute_all_digit_rearrangements(i))
    })



print(rearrangement_sums)