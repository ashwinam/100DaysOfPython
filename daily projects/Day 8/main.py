import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)




# def encrypt(text, shift):  
#   cipher_text = ""
#   for each_letter in text:
#     get_index = alphabet.index(each_letter)
#     cipher_text += alphabet[get_index + shift]

#   print(f"the encode text is {cipher_text}")



# def decrypt(decrypt_text, decrypt_shift):
#   decode_text = ""
#   for each_letter in decrypt_text:
#     get_index = alphabet.index(each_letter)
#     decode_text += alphabet[get_index - decrypt_shift]

#   print(f"the decode text is {decode_text}")


# if direction == "encode":
#   encrypt(text = text, shift = shift)
# else:
#   decrypt(decrypt_text=text, decrypt_shift=shift)


# My way
def caesar(u_text, u_shift):
  encode_text = ""
  decode_text = ""
  for each_letter in u_text:
    if each_letter in alphabet:
      get_index = alphabet.index(each_letter)
      if direction == "encode":
        encode_text += alphabet[get_index + u_shift]
      else:
        decode_text += alphabet[get_index - u_shift]
    else:
      if direction == "encode":
        encode_text += each_letter
      else:
        decode_text += each_letter

      
  if direction == "encode":
      print(f"the encoded text is {encode_text}")
  else:
    print(f"the encoded text is {decode_text}")


# Angela Way
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  caesar(u_text=text, u_shift=shift)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    should_continue = False
    print("Goodbye.")