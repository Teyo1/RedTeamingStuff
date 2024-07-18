Certainly! Here's how you can format the `README.md` file for the first exercise using Markdown:

---

# Exercise 1: Cracking a Hash with Hashcat

In this exercise, we'll be cracking the MD5 hash `c9af96c05921d8a3ad9d033367c0c873` using Hashcat on an RTX 2080 graphics card. Alternatively, you can use CrackStation for the same purpose.

## Using Hashcat

First, ensure you have a dictionary list available. I've moved mine to `/usr/share/wordlists/` for convenience, where popular lists like `rockyou.txt` can also be found.

### Step-by-Step Instructions

1. **Command to Crack the Hash**:
   
   ```sh
   hashcat -m 0 -a 0 c9af96c05921d8a3ad9d033367c0c873 /usr/share/wordlists/dictionary-list.txt --show
   ```

   This command uses `-m 0` for MD5 hash type, `-a 0` for a dictionary attack, and `/usr/share/wordlists/dictionary-list.txt` as the wordlist.

2. **Expected Output**:
   
   After running the command, Hashcat will output the cracked password:
   
   ```
   c9af96c05921d8a3ad9d033367c0c873: Abraham
   ```

## Using CrackStation

For comparison, here's how the same hash appears on CrackStation:

![Screenshot from CrackStation](https://github.com/user-attachments/assets/7ff4240e-8e04-4a8a-9172-2f3022278cac)

As seen, CrackStation also successfully cracks the hash to "Abraham".

### Additional Details

- **Hash Strength**: MD5 hashes are known to be weak against modern cracking techniques due to their vulnerability to precomputed tables and dictionary attacks.
- **Exercise Completion**: This exercise demonstrates the basic usage of Hashcat for hash cracking, using a predefined dictionary list.

![Screenshot from CrackStation](https://github.com/user-attachments/assets/344310b7-88ef-4c88-ab8c-287cb7f516ec)

This concludes Exercise 1, where we successfully cracked the MD5 hash `c9af96c05921d8a3ad9d033367c0c873` using Hashcat.

---

Feel free to adjust the paths, commands, and additional details as needed for your specific setup or preferences.
