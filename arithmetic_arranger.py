def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ["", "", "", ""]
    for problem in problems:
        parts = problem.split()

        # Check if the operator is valid
        operator = parts[1]
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are valid (only digits)
        operand1 = parts[0]
        operand2 = parts[2]
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the operands are within the limit of 4 digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Arrange the problem vertically
        width = max(len(operand1), len(operand2)) + 2
        arranged_problems[0] += operand1.rjust(width)
        arranged_problems[1] += operator + " " + operand2.rjust(width - 2)
        arranged_problems[2] += "-" * width
        if show_answers:
            answer = str(eval(problem))
            arranged_problems[3] += answer.rjust(width)

        # Add spacing between the problems
        if problem != problems[-1]:
            for i in range(4):
                arranged_problems[i] += "    "

    # Join the arranged problems and return as a string
    result = "\n".join(arranged_problems[:3])
    if show_answers:
        result += "\n" + arranged_problems[3]
    return result



