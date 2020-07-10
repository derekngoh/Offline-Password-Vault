
""" 
Converts messages to unicode or ascii encodings and then further converts 
the encodings to binary strings for encryption.
"""

#convert number to binary
def conv_num_to_binary(num, bits=8):
  binary = []
  while num > 0:
    binary = [str(0)] + binary if num%2 == 0 else [str(1)] + binary
    num = num//2
  
  binary = int(''.join(binary))
  binary = ('%0' + str(self.bits) + 'd') % binary
  return binary

#converts text to unicode/ ascii encodings, then to binary strings
def conv_text_to_binary(text):
  binary = []
  for i in text:
    binary = binary + [str(self.conv_num_to_binary(ord(i)))]

  binary = ''.join(binary)

  return binary

#converts binary strings to unicode or ascii texts
def conv_binary_to_text(text, bits=8):
  str_text = ''
  while True:
    if not text[:bits]:
      return str_text
    char = chr(int(text[:bits], 2))
    text = text[bits:]  
    return str_text + char + self.conv_binary_to_text()  


