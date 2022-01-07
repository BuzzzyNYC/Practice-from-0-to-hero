'''
Write a program displaying an Isosceles triangle with ASCII uppercase letters.
'''
try:
    n = int(input())
except:
    print("Invalid input")
    quit()

if n < 0:
    print("Please enter an integer")
else:
    # ASCII code of letter 'A'
    ASCII_char = 65
    for i in range(n):
        spaces = " "*((n - i)*2 - 1)
        print(spaces, end=" ")
    # Print characters on one line
        for j in range(2*i+1):
            # Convert ascii code to character
            letter = chr(ASCII_char)
            print(letter, end=" ")
            # Increment ascii code to get the next letter
            ASCII_char += 1
            # If the letter exceeds Z , we return to letter A
            if chr(ASCII_char) > 'Z':
                ASCII_char = 65
        print()