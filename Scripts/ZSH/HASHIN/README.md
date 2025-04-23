
# 🔍 Hash Type Aggregator with Hashcat Mode Support

Tired of manually identifying hundreds of hashes with `hashid`?  
This script helps you **identify, count, and sort hash types**, including their Hashcat modes if available — fast and automated.

---

## 📦 Features

- Scans a file of hashes (`madness.txt`)
- Identifies possible hash types using `hashid`
- Aggregates and **counts all detected types**
- Shows **Hashcat mode** if available
- Outputs a **sorted table** from most to least common

---

## 💡 Example Output

```
====== Hash Type Counts ======

Hash Type                                     Count   Mode
---------                                     -----   ----
SHA-256 [Hashcat Mode: 1400]                  590     1400
NTLM [Hashcat Mode: 1000]                     61      1000
MD5 [Hashcat Mode: 0]                         61      0
Snefru-256                                    590     —
...
```

---

## 🧰 Requirements

- [`hashid`](https://github.com/psypanda/hashID)

Install it with:

```bash
pip install hashid
```

---

## 🚀 Usage

1. Place your hashes in a file called `madness.txt` (one per line)
2. Save the script as `typechecker.sh`
3. Make it executable:

```bash
chmod +x typechecker.sh
./typechecker.sh
```

---

## 📜 Script: `typechecker.sh`

```bash
#!/bin/bash

declare -A hash_types
declare -A hash_modes

echo -e "Scanning hashes from: hashes.txt\n"

while read -r line; do
    echo "Checking hash: $line"
    while IFS= read -r type; do
        echo "  Found type: $type"
        ((hash_types["$type"]++))
        if [[ "$type" =~ \[Hashcat\ Mode:\ ([0-9]+)\] ]]; then
            hash_modes["$type"]="${BASH_REMATCH[1]}"
        else
            hash_modes["$type"]="—"
        fi
    done < <(hashid -m "$line" 2>/dev/null | sed -n 's/^\[+\] //p')
done < path/to/the/hashes.txt

echo -e "\n====== Hash Type Counts ======\n"
printf "%-45s %-7s %s\n" "Hash Type" "Count" "Mode"
printf "%-45s %-7s %s\n" "---------" "-----" "----"

for key in "${!hash_types[@]}"; do
    printf "%-45s %-7d %s\n" "$key" "${hash_types[$key]}" "${hash_modes[$key]}"
done | sort -k2 -nr
```

---

## 🧪 Tip

Pipe results into a file for reports or further processing:

```bash
./typechecker.sh > hash_summary.txt
```

---

## 🧙 About

This tool is made for pentesters, CTF players, and anyone with way too many hashes and not enough time.

Contributions welcome!
