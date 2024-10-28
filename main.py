def caesar_cipher(text, shift, action):
    final_text = ""

    if action == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shifted_position = (ord(char.lower()) - ord('a') + shift) % 26 + ord('a')
            final_char = chr(shifted_position)
            final_text += final_char.upper() if char.isupper() else final_char
        else:
            final_text += char
    
    print(f"{action.capitalize()}ed message: {final_text}")

text = input("Enter the message: ")
shift = int(input("Enter the shift number: "))
action = input("Do you want to 'encrypt' or 'decrypt' the message? ").lower()
caesar_cipher(text, shift, action)