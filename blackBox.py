from binaryConvert import BinaryConvert

class BlackBox:
  """ 
  Stores encryption and decryption codes as well as default server login 
  email and password.
  """

  f = open(".keytext.txt", 'r')
  keytext = f.read()
  f.close()
  a = keytext
  def_email = a[195]+a[8]+a[3]+a[2]+a[27]+a[27]+a[2]+a[42]+a[1]+a[17]+a[23]+"@gmail.com"
  def_pass = a[195]+a[8]+a[3]+a[2]+a[27]+a[42].upper()+a[8]+a[3]+a[3]

  #makes the length of key same as the message.  
  def pad_key_to_msg_length(self, key, klen, mlen):
    kmix = ord(key[0])+ord(key[1])+ord(key[-1])
    pad = self.keytext[klen+kmix:mlen+kmix]
    padded_key = key + pad

    return padded_key

  #encrypts message with same-length key and converts encrypted message into
  #binary string. Returns binary string of encrypted text.
  def encrypt(self, msg, key):
    mlen = len(msg)
    klen = len(key)
    padded_key = self.pad_key_to_msg_length(key, klen, mlen)
    binary_padded_key = BinaryConvert(padded_key).conv_text_to_binary()
    binary_message = BinaryConvert(msg).conv_text_to_binary()
    if len(binary_padded_key) != len(binary_message):
      raise Exception("Key & message length not equal!")
    non_padded_ciphertext = bin(int(binary_padded_key, 2)^int(binary_message, 2))
    ciphertext = ('%0' + str(len(binary_padded_key)) + 'd') % int(non_padded_ciphertext[2:])
    
    return ciphertext
    
  #decrypts binary string message using key provided and converts binary into
  #text. If key is correct, decryption is correct. 
  def decrypt(self, enc_message, key, bits=8):
    klen = len(key)
    encmlen = int(len(enc_message)/bits)
    padded_key = self.pad_key_to_msg_length(key, klen, encmlen)
    binary_padded_key = BinaryConvert(padded_key).conv_text_to_binary()
    binary_enc = enc_message
    if len(binary_padded_key) != len(enc_message):
      raise Exception("Key & message length not equal!")
    non_padded_decoded_text = bin(int(binary_padded_key, 2)^int(enc_message, 2))
    decoded_binary = ('%0' + str(len(binary_padded_key)) + 'd') % int(non_padded_decoded_text[2:])
    decoded_text = BinaryConvert(decoded_binary).conv_binary_to_text()

    return decoded_text


