# Exercise 8: Cracking MD5 Hash with Hashcat

## Description

In this exercise, we'll demonstrate how to crack the MD5 hash `563e276e8d7450d264eefd297a368233` using Hashcat on an RTX 2080 SUPER graphics card.

### Hash Information

- **Hash**: `563e276e8d7450d264eefd297a368233`

### Command Used

```sh
hashcat -m 0 -a 0 563e276e8d7450d264eefd297a368233 /usr/share/wordlists/dictionary-list.txt
```

### Hashcat Output

```plaintext
hashcat (v6.2.6) starting

CUDA API (CUDA 12.2)
====================
* Device #1: NVIDIA GeForce RTX 2080 SUPER, 7008/7969 MB, 48MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

Host memory required for this attack: 843 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/dictionary-list.txt
* Passwords.: 87394
* Bytes.....: 832094
* Keyspace..: 87394

Approaching final keyspace - workload adjusted.           

563e276e8d7450d264eefd297a368233: quinquagenarians         
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: 563e276e8d7450d264eefd297a368233
Time.Started.....: Thu Jul 18 15:12:06 2024 (0 secs)
Time.Estimated...: Thu Jul 18 15:12:06 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/dictionary-list.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  6986.0 kH/s (0.06ms) @ Accel:2048 Loops:1 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 87394/87394 (100.00%)
Rejected.........: 0/87394 (0.00%)
Restore.Point....: 43697/87394 (50.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: homecomings -> zymurgy
Hardware.Mon.#1..: Temp: 39c Fan: 28% Util:  9% Core:1650MHz Mem:7500MHz Bus:16

Started: Thu Jul 18 15:12:05 2024
Stopped: Thu Jul 18 15:12:07 2024
```

### Explanation

- **Hashcat Command**: We used `-m 0 -a 0` for MD5 hash type and dictionary attack, respectively.
- **Output**: Hashcat successfully cracked the hash to the password `quinquagenarians`.

## Verification on CrackStation

For verification, the cracked password `quinquagenarians` was checked on CrackStation.

![CrackStation Screenshot](https://github.com/user-attachments/assets/0f6ac30e-4462-44ef-908e-ebc2296d1d38)

### Conclusion

This exercise demonstrates the effectiveness of Hashcat in quickly cracking MD5 hashes using dictionary attacks. With appropriate hardware and a well-prepared wordlist, such tasks can be efficiently accomplished.

---

This Markdown file provides a structured walkthrough of the exercise, including commands used, output from Hashcat, and verification on CrackStation. Adjust paths and additional details as needed for your specific setup.
