Certainly! Here's the provided information formatted in Markdown:

---

# Cracking SHA1 Hash with Hashcat

In this writeup, we will demonstrate how to crack SHA1 hashes using Hashcat. We are using the command:

```sh
hashcat -m 100 -a 0 afafb738461b35f1eb36194c21cb463113dfced4 /usr/share/wordlists/dictionary-list.txt
```

The `-m 100` parameter specifies SHA1 hashes.

## Running the Command

```plaintext
hashcat (v6.2.6) starting...

CUDA API (CUDA 12.2)
====================
* Device #1: NVIDIA GeForce RTX 2080 SUPER, 7012/7969 MB, 48MCU

OpenCL API (OpenCL 3.0 CUDA 12.2.148) - Platform #1 [NVIDIA Corporation]
========================================================================
* Device #2: NVIDIA GeForce RTX 2080 SUPER, skipped

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 17.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
============================================================================================================================================
* Device #3: cpu-skylake-avx512-AMD Ryzen 7 7800X3D 8-Core Processor, skipped

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

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 843 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/dictionary-list.txt
* Passwords.: 87394
* Bytes.....: 832094
* Keyspace..: 87394

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: [Hashcat FAQ on More Work](https://hashcat.net/faq/morework)

Approaching final keyspace - workload adjusted.           

**afafb738461b35f1eb36194c21cb463113dfced4: Aaron**

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 100 (SHA1)
Hash.Target......: afafb738461b35f1eb36194c21cb463113dfced4
Time.Started.....: Thu Jul 18 15:29:13 2024 (0 secs)
Time.Estimated...: Thu Jul 18 15:29:13 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/dictionary-list.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 40337.1 kH/s (0.08ms) @ Accel:2048 Loops:1 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 43697/87394 (50.00%)
Rejected.........: 0/43697 (0.00%)
Restore.Point....: 0/87394 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: A-bomb -> homecoming
Hardware.Mon.#1..: Temp: 41c Fan: 28% Util:  0% Core:1650MHz Mem:7500MHz Bus:16

Started: Thu Jul 18 15:29:10 2024
Stopped: Thu Jul 18 15:29:15 2024
```

This output shows Hashcat successfully cracked the SHA1 hash `afafb738461b35f1eb36194c21cb463113dfced4` to the password `Aaron` using the specified dictionary file.

---
![Screenshot_2024-07-18_15-38-40](https://github.com/user-attachments/assets/1d79022e-0fd9-466e-b22f-39a38c95e849)

