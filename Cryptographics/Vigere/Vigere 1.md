## Decoding the Vigenère Cipher

The **Vigenère cipher** is a method of encrypting alphabetic text by using a series of Caesar ciphers based on the letters of a keyword. Each letter in the plaintext is shifted along the alphabet by a number of positions determined by the corresponding letter in the keyword.

### Task

**Visionary Cipher #1 25**

Standard ROT ciphers simply do not have enough permutations (25, to be exact). This next form of encryption interweaves multiple ROTs based on a key.

**Encrypted Message:**

```
Dlc ppyq mq fmeorcbi
```

### Decoding Process

1. **Open CyberChef**:
   Go to [CyberChef](https://gchq.github.io/CyberChef/).

   ![Screenshot showing CyberChef interface](https://github.com/user-attachments/assets/96828771-eccf-4d14-b72c-ba580de09a77)

2. **Enter the Information**:
   - Input the encrypted message into CyberChef.
   - Select the Vigenère cipher operation.

   ![Screenshot showing Vigenère cipher operation in CyberChef](https://github.com/user-attachments/assets/de41a712-415d-48de-ac61-d290878fb188)

3. **Determine the Key**:
   Based on the clue "This next form of encryption interwove multiple ROTs based on a key," we use the key **KEY**.

   ![Screenshot showing decryption result with the key](https://github.com/user-attachments/assets/dfc1c2b1-3fb1-4565-af66-8fc993f1d970)

4. **Decryption Result**:
   The flag decoded from the message is **vigenere**.

   It took some time to understand the key.

### Summary

The Vigenère cipher uses a keyword to shift letters in the plaintext, making it more complex than standard ROT ciphers. In this case, the keyword "KEY" was used to decode the message, revealing the flag.

---
