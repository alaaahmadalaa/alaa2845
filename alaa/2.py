def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        if digit == '1':
            decimal = decimal * 2 + 1
        elif digit == '0':
            decimal = decimal * 2
        else:
            return None
    return decimal


binary_number = input("Enter a binary number: ")
if not all(char.isdigit() and char in ['0', '1'] for char in binary_number):
    print("Invalid input. Please enter a binary number (0s and 1s only).")
else:
    decimal_number = binary_to_decimal(binary_number)
    if decimal_number is not None:
        print(
            f"The decimal equivalent of {binary_number} is: {decimal_number}")
    else:
        print("Invalid input. Please enter a binary number (0s and 1s only).")
