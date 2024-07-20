# Wordlist Modifier Script

## Information

This repository contains a script to modify a wordlist by appending sequences of numbers to each word. It is useful for generating lists with different combinations of words and numbers.

- **Script Name:** `create-wordlist.sh`
- **Purpose:** To read words from an input file and generate an output file with each word appended by numbers in various formats.
- **License:** MIT License

## Script

The `create-wordlist.sh` script reads a list of words from the specified input file and generates an output file where each word is appended with numbers in the following formats:
- Numbers from 0 to 99
- Numbers from 00 to 99 (with leading zeros)
- Numbers from 000 to 999 (with leading zeros)

### Script Code

```bash
#!/bin/bash

input_file="dictionary-list.txt"
output_file="modified_wordlist.txt"

# Clear the output file if it already exists
> "$output_file"

# Read each word from the input file
while IFS= read -r word; do
    # Append the word with numbers 0-99
    for i in $(seq 0 99); do
        echo "${word}${i}" >> "$output_file"
    done

    # Append the word with numbers 00-99
    for i in $(seq -w 0 99); do
        echo "${word}${i}" >> "$output_file"
    done

    # Append the word with numbers 000-999
    for i in $(seq -w 0 999); do
        echo "${word}${i}" >> "$output_file"
    done
done < "$input_file"

echo "Sequences have been appended to each word in '$input_file' and written to '$output_file'."
```

**Note:** In this script, the input file is hardcoded as `dictionary-list.txt` and the output file is hardcoded as `modified_wordlist.txt`. Ensure that the input file is named `dictionary-list.txt` or modify the script to reflect the actual input file name.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/teyo1/wordlist-expander.git
   ```

2. **Navigate to the directory**:
   ```bash
   cd wordlist-expander
   ```

3. **Make the script executable**:
   ```bash
   chmod +x create-wordlist.sh
   ```

4. **Prepare your input file**:
   - Ensure your input file is named `dictionary-list.txt` or adjust the script to use your actual file name.

5. **Run the script**:
   ```bash
   ./create-wordlist.sh
   ```

   This will use `dictionary-list.txt` as the input and produce an output file named `modified_wordlist.txt`.

### Example

If your `dictionary-list.txt` contains:
```
word1
word2
```

Running the script:
```bash
./create-wordlist.sh
```

Will produce an output file `modified_wordlist.txt` with content like:
```
word100
word101
...
word199
word200
word201
...
word299
word1000
word1001
...
word1999
```
