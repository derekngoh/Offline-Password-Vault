import sys
import smtplib
import imapclient
import re

class Eserver:
  """
  Logs in and out of email server account. Sends / drafts / reads / deletes 
  messages in selected folder. Search messages via 'subject' headings. 
  """
  #exstablish connection with IMAP / SMTP servers
  def __init__(self, smtp='smtp.gmail.com', imap='imap.gmail.com', port=587):
    self.smtp = smtp
    self.imap = imap
    self.port = port
   
    self.imapObj = imapclient.IMAPClient(imap, ssl=True)

    #start Transport Layer Security (TLS) or SSL encryption
    try:
      print("Activating TLS encryption\n")
      self.smtpObj = smtplib.SMTP(self.smtp, self.port)
      #establish connection with ehlo
      self.smtpObj.ehlo()
      self.smtpObj.starttls()

    except:
      print(sys.exc_info())
      print("Activating SSL encryption\n")
      self.smtpObj = smtplib.SMTP_SSL(self.smtp, 465)
      #establish connection with ehlo
      self.smtpObj.ehlo()


  #send email with SMTP
  def send_login(self, email, passw):
    self.smtpObj.login(email, passw)

  def send(self, email, recipient, subject, message):
    self.smtpObj.sendmail(email, recipient, subject + message)

  def quit(self):
    self.smtpObj.quit()
    self.imapObj.logout()

  #retrieve emails for reading or deleting using IMAP
  def view_login(self, email, passw):
    #login into email account with all the provided details
    self.imapObj.login(email, passw)

  #saving draft using IMAP
  def save_as_draft(self, subject, message):
    folder = self.view_identify_folder()
    self.imapObj.select_folder(folder)
    self.imapObj.append(folder, subject + message)

  #select folder for viewing
  def view_identify_folder(self, folder="[Gmail]/Drafts"):
    return folder


  #Select message to show. 
  def view_select_message(self, keyword, delete=False, readonly=True, viewNum=0):
    folder = self.view_identify_folder()
    self.imapObj.select_folder(folder, readonly)

    try:
      allUniqueIDs = self.imapObj.search(['ALL'])
      allUniqueIDs[0] #to raise exception if list is empty
      selectedUIDs = []
      for uid in allUniqueIDs:
        uidFullMsg = self.imapObj.fetch(uid,['BODY[]'])
        uidEncodedSubj = uidFullMsg[uid][bytes('BODY[]', 'ascii')]
        slice_pos1 = uidEncodedSubj.find(bytes("!~~", "ascii"))
        slice_pos2 = uidEncodedSubj.find(bytes("~~!", "ascii"))
        subject = uidEncodedSubj[slice_pos1+3:slice_pos2] 
        pattern = re.compile('.*' + keyword + '.*', re.IGNORECASE)
        if pattern.match(subject.decode("ascii")):
          selectedUIDs += [uid]

    except IndexError:
      print("\nNo secret stored in vault. Please store a secret first.")
      return True

    try:
      full_encoded_body = self.imapObj.fetch(selectedUIDs[viewNum],['BODY[]'])

    except IndexError:
      print("\nNo matches found. Please re-search with other keyword.")
      return True
    
    encoded_body = full_encoded_body[selectedUIDs[viewNum]][bytes('BODY[]', 'ascii')]
    slice_pos1 = encoded_body.find(bytes("{**", "ascii"))
    slice_pos2 = encoded_body.find(bytes("**}", "ascii"))
    body = encoded_body[slice_pos1+3:slice_pos2]

    self.delete = False

    if delete:
      self.delete = True
      self.deleteID = [selectedUIDs[viewNum]]
    
    return body
  
  def delete_msg(self):
    if self.delete:
      try:
        self.imapObj.delete_messages(self.deleteID[0])
        self.imapObj.expunge()
        print("\nMessage deleted")

      except:
        print(sys.exc_info())
        print("\nError in deletion. Please try again.")
        return False
    


