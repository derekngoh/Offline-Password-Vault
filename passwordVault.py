from emailServer import Eserver
from userInput import User_Inputs
from blackBox import BlackBox

class PasswordVault:
  """
  Runs the programme. Sets default method to store and retrieve secrets.
  """
  def __init__(self):
    self.server = Eserver()
    self.user = User_Inputs()
    self.cryptobox = BlackBox()

  #calls methods to login, get needed user inputs to store secret, encrypts and 
  #save encrypted secret on server
  def default_draft_storage(self):

    #login to generic email server
    self.server.view_login(self.user.email, self.user.passw)

    #get content from user and save
    self.user.get_message_content()
    self.user.get_enc_key()
    ciphertext = self.cryptobox.encrypt(self.user.message, self.user.enc_key)
    self.server.save_as_draft(self.user.subject, "{**" + ciphertext + "**}")

    self.server.quit()

    print("\nMessage saved. Logged out.")

  #calls method to get inputs from user, retrieve encrypted secret, decrypt and 
  #delete secret
  def default_draft_retrieval(self):

    #login to generic email server
    self.server.view_login(self.user.email, self.user.passw)

    while True:
      #get keyword of subject
      self.user.retrieve_user_inputs()
      self.user.delete_message()

      if self.user.delmsg.lower() == 'y':
        delete = True 
        readonly = False

      else:
        delete = False
        readonly = True
      
      if self.server.view_select_message(self.user.keyword, delete, readonly) != True:
        break

    ciphertext = self.server.view_select_message(self.user.keyword, delete, readonly)
    self.user.get_dec_key()
    try:
      secret = self.cryptobox.decrypt(ciphertext, self.user.dec_key)
    except:
      secret = "#$%^#FSEGqwD*#poLYP"
    print("\nYour secret is: ", secret)

    if secret != "#$%^#FSEGqwD*#poLYP":
      self.user.delete_confirmation()
      if self.user.del_conf.lower() == 'y': 
        self.server.delete_msg()
 
    self.server.quit()

  #calls the default start menu
  def start_menu(self):
    self.user.default_main_menu()
    print("")
    
    if self.user.def_menu == '1':
      new.default_draft_storage()

    elif self.user.def_menu == '2':
      new.default_draft_retrieval()

    else: 
      print("\nOption not valid. Please enter one of the above options. \n")
      new.start_menu()


#Runs programme
new = PasswordVault()
new.start_menu()



