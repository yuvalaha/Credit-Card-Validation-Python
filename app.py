# Get the credit card number from the user
credit_card = input("Hello and welcome to the credit card validation simulator\nPlease enter you credit card number: ")

# Collecting the odd numbers from the credit card
odd_numbers = credit_card[1::2]

# Sum the odd number
sum_odd_numbers = sum(int(num) for num in odd_numbers)

# Collecting the even numbers from the credit card
even_numbers = credit_card[::2]

# Multiplying by 2 the numbers in the even array 
even_numbers_multiplying = list(map (lambda num: int(num) *2, even_numbers))

# Sum the digits of number in the new even array if the number is greater or equal to 10 
for index in range(len(even_numbers_multiplying)):
    current_number = even_numbers_multiplying[index]
    if current_number > 9:
        even_numbers_multiplying[index] = current_number % 10 + int(current_number / 10)
        
# Sum the even number final array
sum_even_numbers = sum(int(num) for num in even_numbers_multiplying)

# Sum of odd and even 
final_sum = sum_even_numbers + sum_odd_numbers

# Lhun's Algorithm
print(f"Your Credit Card Is: {credit_card[0:4]}-{credit_card[4:8]}-{credit_card[8:12]}-{credit_card[12:16]}")
if final_sum % 10 == 0:
    print("Your Credit Card Is Valid!")
else:
    print("Your Credit Card Isn't Valid!")