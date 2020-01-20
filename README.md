This project was used to understand how encryptions work with the 
goal of creating a text-based encryption that would be extremely
difficult to break without a key. A one-time pad was chosen for the
project because a one-time pad is considered to be unbreakable if the 
random key is kept unshared. This being said the encryption is made by 
taking the local system time and using it as a seed for random number
generation. This creates a regenerable set of random numbers since it is 
impossible to create an entirely random number on a computer.

Definition of Encryption:
In cryptography, encryption is the process of encoding a message 
or information in such a way that only authorized parties can 
access it and those who are not authorized cannot. Encryption 
does not itself prevent interference but denies the intelligible 
content to a would-be interceptor.

Definition of one-time pad:
In cryptography, the one-time pad (OTP) is an encryption 
technique that cannot be cracked, but requires the use of a 
one-time pre-shared key the same size as, or longer than, the 
message being sent. In this technique, a plaintext is paired with
a random secret key (also referred to as a one-time pad).

Instructions for use:

Try to print in command line/Terminal:

pip install pypng
pip install pillow

To test the “test.png” image insert the following inputs:

Welcome to the one-time pad Encryption Program!
Would you like to Encrypt(E) or Decrypt(D) a message?
E or D? D
Enter Image File Name, Exclude extention: test
Enter Secret Key: 1579563593
Enter Length: 143
Enter Size: 255


If you have any questions feel free to contact me. 
Thanks!
Jason Van Bladel
