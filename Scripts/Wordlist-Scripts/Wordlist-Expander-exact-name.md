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
