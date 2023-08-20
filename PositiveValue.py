
def positive_identifiers(a, b, c):
    positive_nums = [num for num in [a, b, c] if num > 0]
    return f'Value is {True}' if  len(positive_nums)  == 2 else f'Value is {False}'

count = 1
value_list = []
while count < 4:
    try:
        value = int(input(f"input 3 numbers to check. Num {count}: "))
        value_list.append(value)
        count += 1
    except ValueError:
        print("Value Must Be An Integer.")
a, b, c = value_list
print(a,b,c)

print(positive_identifiers(a,b,c))