from arithmetic_arranger import arithmetic_arranger

# Test cases
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))

problems_with_answers = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems_with_answers, True))

invalid_problems = ["32 / 8", "1 - 3801", "9999 + 9999", "523 - 49", "12345 + 6789"]
print(arithmetic_arranger(invalid_problems))

# Output:
#    32         3801      45         123
# + 698      -    2    + 43       +  49
# -----      ------    ----       -----
#
#   32          1      9999        523
# +  8      -3801    +9999      -  49
# ----     ------    ------      -----
#   40      -3800     19998        474
#
# Error: Operator must be '+' or '-'
#
# Error: Too many problems.
