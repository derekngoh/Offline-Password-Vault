General Introduction
The Password Vault(PV) is designed to be an offline vault for passwords and secrets. To mitigate attacks on the vault, all passwords and secrets and encrypted before being stored on the server. Therefore, any unauthorised retrieval of the secret or password cannot be read or deciphered without the decryption key set by the user. Upon retrieval of the secret or password, the decryption can be done offline. Therefore, the user can disconnect from the internet prior to decryption to prevent cyber-eavesdropping.

Configuration instructions
For the trial version, a default server and a default encryption text will be used. There is no further configuration needed and PV can be used immediately after installation. Because you are using a shared default server, the encrypted secrets may be viewed by the server administrators. However, without your decryption key, the secret cannot be decrypted and viewed.

- Actual Secret
-- Subject Heading: "Example Header"
-- Secret(before encryption): "This is a top secret message"

- Secret on Server
-- Subject Heading: "Example Header"
-- Secret(after encryption): 0010011100001101000010100000000101000101000111010001011101000001000100100101010000011100000010100101001001000010000000010000-110000000111000101010000000001010110010000110000001000010000000000010000000000000100000000010000101001011100

- Decrypted secret with INCORRECT keys
-- Subject Heading: "Example Header"
-- Secret(after encryption): "Your secret is: nCINONT<koa.`x}rQt utsolf5"

- Decrypted secret with CORRECT keys
-- Subject Heading: "Example Header"
-- Secret(after encryption): "Your secret is: This is a top secret message"

Installation instructions
Double-click on the Password_Vault.exe file to install. Select the desired folder. Once installation is complete, you should see the files stated in the file manifest below.

Operating instructions
1. Double-click on passwordVault.exe file to start
2. Follow instruction on screen to complete the selected operations.

File manifest
After installation, the following files should appear in the folder:
- README
- keytext
- binaryConvert
- blackBox
- emailServer
- userInput
- passwordVault

Copyright and licensing information
All rights reserved.

Contact information for the distributor or programmer

