import random

def generate_random_list(n):
    random_list = [random.randint(1, 100) for _ in range(n)]  # Change the range as needed
    return random_list

list_10 = generate_random_list(10)
list_40 = generate_random_list(40)
list_80 = generate_random_list(80)

# Save lists to text files
with open('random_list_10.txt', 'w') as file:
    file.write(str(list_10))

with open('random_list_40.txt', 'w') as file:
    file.write(str(list_40))

with open('random_list_80.txt', 'w') as file:
    file.write(str(list_80))