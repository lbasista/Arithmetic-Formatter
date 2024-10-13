def arithmetic_arranger(problems, show_answers=False):
    #Error 1 - too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #Error 2 - Wrong operator
    #Getting array with only operator signs
    operators = []
    for i in problems:
        single_problems = i.split()
        operators.append(single_problems[1])
    #If * or / return error
    for j in operators:
        if j in ['*','/']:
            return "Error: Operator must be '+' or '-'."

    #Error 3 - Not a digit
    digits = [] #Our array for only digits "around operators"
    for i in problems:
        single_parts = i.split()
        digits.append(single_parts[0])
        digits.append(single_parts[2])

    #If not a digit return error
    for j in digits:
        if not j.isdigit():
            return 'Error: Numbers must only contain digits.'

    #Error 4 - More than 4 digits
    for i in digits:
        if len(i) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    #Calculate
    results = []
    for i in range(0,len(digits),2):
        if operators[i//2] == "+":
            res = int(digits[i]) + int(digits[i+1])
        else:
            res = int(digits[i]) - int(digits[i+1])
        results.append(res)

        #Format output
    dig1 = ''
    dig2 = ''
    dash = ''
    ans = ''
    for i in range(0,len(digits),2):
        width = max(len(digits[i]),len(digits[i+1])) + 2

        dig1 += digits[i].rjust(width)
        dig2 += operators[i//2] + digits[i+1].rjust(width - 1)
        dash += '-' * width
        #Space between
        if i != len(digits) - 2:
            dig1 += ' ' * 4
            dig2 += ' ' * 4
            dash += ' ' * 4

    for i in range(len(results)):
        width = max(len(digits[2*i]),len(digits[2*i+1])) + 2
        ans += str(results[i]).rjust(width)
        if i != len(results) - 1:
            ans += ' ' * 4

    if show_answers:
        arranged_problems = '\n'.join((dig1, dig2, dash, ans))
    else:
        arranged_problems = '\n'.join((dig1, dig2, dash))


    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],1)}')