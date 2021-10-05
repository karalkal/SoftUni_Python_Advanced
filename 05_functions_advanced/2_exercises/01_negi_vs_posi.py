def calculate_posi_and_negi_sums(numbers_list):
    negi_sum, posi_sum, stronger, weaker = 0, 0, "", ""
    for number in numbers_list:
        if number < 0:
            negi_sum += number
        else:
            posi_sum += number

    if abs(negi_sum) > posi_sum:
        stronger, weaker = "negatives", "positives"
    else:
        stronger, weaker = "positives", "negatives"

    return negi_sum, posi_sum, stronger, weaker


numbers_list = [int(x) for x in input().split()]
posi_and_negi_sums = calculate_posi_and_negi_sums(numbers_list)
print(posi_and_negi_sums[0])
print(posi_and_negi_sums[1])
print(f"The {posi_and_negi_sums[2]} are stronger than the {posi_and_negi_sums[3]}")
