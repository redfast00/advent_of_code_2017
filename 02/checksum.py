with open("input_2.txt") as spreadsheet:
    total = 0
    for line in spreadsheet.readlines():
        numbers = line.split('\t')
        numbers = [int(number) for number in numbers]
        difference = max(numbers) - min(numbers)
        total += difference
    print(total)

def find_divisor(numbers):
    for number in numbers:
        for second in numbers:
            if number % second == 0 and number != second:
                print(f'{number},{second}')
                return number / second
with open("input_2.txt") as spreadsheet:
    total = 0
    for line in spreadsheet.readlines():
        numbers = line.split('\t')
        numbers = [int(number) for number in numbers]
        total += find_divisor(numbers)
    print(total)
