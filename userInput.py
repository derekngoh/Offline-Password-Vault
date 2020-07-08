from blackBox import BlackBox 

class User_Inputs:
  """
  Collects user input and sets format to facilitate usage by other methods
  """
  #sets server to default using default email and password.
  def __init__(self, email=BlackBox.def_email, passw=BlackBox.def_pass):
    self.email = email
    self.passw = passw
    
  #get login details if not using default server
  def login_details(self):
    self.email_input = input("Please enter your email account to login: \n")
    self.password_input = input("Please enter the password for login: \n")   
  
  #get subject heading and secret from user to encrypt then store in server
  def get_message_content(self):
    self.subject = "Subject: !~~" + input("Enter the subject header for " + 
      "retrieval of secret (This information is not encrypted.): \n") + "~~!\n"
    while True:
      self.message = input("\nEnter the secret (limits: minimum 2 and maximum" +
        " 200 characters): \n")
      if len(self.message) < 201 and len(self.message) > 1:
        break
      print("Please check message limits and try again.")

  #get encryption key from user to encrypt secret
  def get_enc_key(self):
    while True:
      self.enc_key = input("\nPlease enter a key for encrypting your message " + 
        "(limits: this key cannot be longer than your secret.): \n")
      if len(self.enc_key) > 1 and len(self.enc_key)<=len(self.message):
        break
      print("Please check message limits and try again.")
  
  #get decryption key from user to decrypt encrypted secret
  def get_dec_key(self):
    while True:
      self.dec_key = input("\nPlease enter your secret key for decryption: \n") 
      if len(self.dec_key) > 1:
        break

  #get destination email address if sending email
  def get_destination_email(self):
    self.recipient = input("Please enter email to send to: \n")

  #search for secret by using keywords to search subject headings
  def retrieve_user_inputs(self):
    self.keyword = input("Enter the precise subject keyword to locate your" +
      " secret (only the first most relevant result will be displayed.): \n")

  #ask user for permission to delete secret from server.
  def delete_message(self):
    self.delmsg = input("\nDelete message from server? If you choose to delete," + 
      "this would be your last chance to view the message. (Y/N): \n")

  #ask user to confirm deletion
  def delete_confirmation(self):
    self.del_conf = input("\nConfirm delete? (Y/N): ")

  #default main menu options
  def default_main_menu(self):
    self.def_menu = input("Select which function you would like to perform: " +
      "\n1. Encrypt and store secret.\n2. Decrypt stored secret. " + 
      "\nSelect option(1 or 2): ")

