import itertools

def generate_password_list(words):
    password_list = []
    total_permutations = sum([len(list(itertools.permutations(words, r))) for r in range(1, len(words) + 1)])
    current_permutations = 0
    
    # Generate permutations of input words
    for r in range(1, len(words) + 1):
        for combination in itertools.permutations(words, r):
            password_list.append(''.join(combination))
            current_permutations += 1
            percentage_complete = (current_permutations / total_permutations) * 100
            print(f"Generating passwords: {percentage_complete:.2f}% complete", end='\r')
    
    return password_list

# Get input from user for input_words
input_words = input("Enter a list of words separated by spaces: ").split()

result = generate_password_list(input_words)

# Save passwords to a file on local storage
file_path = 'passwords.txt'  # Update this path
with open(file_path, 'w') as file:
    for password in result:
        file.write(password + '\n')

print(f"\nPasswords saved to '{file_path}'")