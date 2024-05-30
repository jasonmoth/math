two_digit_integers = [i for i in range(1, 101)]
digit_rearrangement_sums = []

for i in two_digit_integers:
    if len(str(i)) == 1:
        digit_rearrangement_sums.append(i*2)
    elif len(str(i)) == 2: 
        digit_rearrangement_sums.append(i + int((str(i))[::-1]))

print(digit_rearrangement_sums)

# OEIS 
# A056964
# https://mathworld.wolfram.com/Reverse-Then-AddSequence.html
# https://mathworld.wolfram.com/196-Algorithm.html