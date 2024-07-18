# Cracking SHA1 Hash with Hashcat and `-w 4` Option

In this writeup, we will demonstrate how to crack a SHA1 hash using Hashcat with the `-w 4` option. The command used is:

```sh
hashcat -m 100 -a 0 dc5f634ff5098b1e190fa6eaf9368c1282f8e84f /usr/share/wordlists/dictionary-list.txt -w 4
```

The `-m 100` parameter specifies SHA1 hashes, and `-w 4` specifies the workload profile (4). This option affects how much workload is given to the GPU.

## Understanding `-w 4`

The `-w` option in Hashcat adjusts the workload profile:

- `-w 1`: Low workload, best for slower GPUs or when running other tasks concurrently.
- `-w 2`: Moderate workload, balanced for typical use.
- `-w 3`: High workload, suitable for high-performance GPUs or systems with dedicated GPUs.
- `-w 4`: Very high workload, for systems with multiple powerful GPUs or when maximum performance is needed.

## Running the Command

```plaintext
hashcat (v6.2.6) starting...

CUDA API (CUDA 12.2)
====================
* Device #1: NVIDIA GeForce RTX 2080 SUPER, 7025/7969 MB, 48MCU

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

**dc5f634ff5098b1e190fa6eaf9368c1282f8e84f: Carolinian**

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 100 (SHA1)
Hash.Target......: dc5f634ff5098b1e190fa6eaf9368c1282f8e84f
Time.Started.....: Thu Jul 18 15:43:17 2024 (0 secs)
Time.Estimated...: Thu Jul 18 15:43:17 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/dictionary-list.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 39785.9 kH/s (0.08ms) @ Accel:2048 Loops:1 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 43697/87394 (50.00%)
Rejected.........: 0/43697 (0.00%)
Restore.Point....: 0/87394 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: A-bomb -> homecoming
Hardware.Mon.#1..: Temp: 40c Fan: 29% Util:  1% Core:1650MHz Mem:7500MHz Bus:16

Started: Thu Jul 18 15:43:17 2024
Stopped: Thu Jul 18 15:43:18 2024
```

This output demonstrates Hashcat successfully cracked the SHA1 hash `dc5f634ff5098b1e190fa6eaf9368c1282f8e84f` to the password `Carolinian` using the specified dictionary file and `-w 4` workload option.

---

![Screenshot_2024-07-18_15-45-09](https://github.com/user-attachments/assets/7e882d54-c414-4c1f-92e1-87a2d24a027a)


