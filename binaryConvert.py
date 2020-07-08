
class BinaryConvert:
  """ 
  Converts messages to unicode or ascii encodings and then further converts 
  the encodings to binary strings for encryption.
  """
  def __init__(self, text_or_binary, bits=8):
    self.text = text_or_binary
    self.bits = bits

  #convert number to binary
  def conv_num_to_binary(self, num):
    binary = []
    while num > 0:
      binary = [str(0)] + binary if num%2 == 0 else [str(1)] + binary
      num = num//2
    
    binary = int(''.join(binary))
    binary = ('%0' + str(self.bits) + 'd') % binary
    return binary

  #converts text to unicode/ ascii encodings, then to binary strings
  def conv_text_to_binary(self):
    binary = []
    for i in self.text:
      binary = binary + [str(self.conv_num_to_binary(ord(i)))]

    binary = ''.join(binary)

    return binary

  #converts binary strings to unicode or ascii texts
  def conv_binary_to_text(self):
    text = ''
    while True:
      if not self.text[:self.bits]:
        return text
      char = chr(int(self.text[:self.bits], 2))
      self.text = self.text[self.bits:]  
      return text + char + self.conv_binary_to_text()  


