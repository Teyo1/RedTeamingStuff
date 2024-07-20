# Define the mapping function
def number_to_letter(number):
    # Convert number to corresponding letter (1 -> A, 2 -> B, ..., 26 -> Z)
    return chr(number + 64)

# List of numbers
numbers = [20, 8, 5, 6, 12, 1, 7, 20, 15, 20, 8, 9, 19, 3, 8, 1, 12, 12, 5, 14, 7, 5, 9, 19, 26, 5, 2, 18, 1]

# Convert numbers to letters
decoded_message = ''.join(number_to_letter(num) for num in numbers)

print(f"Decoded message: {decoded_message}")
