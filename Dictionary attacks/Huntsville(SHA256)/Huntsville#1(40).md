Let's continue with the cracking, as you read in the previous readme this time we are going to crack some SHA256 algorithm hashes.

hashcat -h gives us a help where we can read how we can build a command to crack SHA256s with the dictionary that was given to us at the beginning.
- [ Hash modes ] -

      # | Name                                                       | Category
  ======+============================================================+======================================
    900 | MD4                                                        | Raw Hash
      0 | MD5                                                        | Raw Hash
    100 | SHA1                                                       | Raw Hash
   1300 | SHA2-224                                                   | Raw Hash
   1400 | SHA2-256                                                   | Raw Hash
  10800 | SHA2-384                                                   | Raw Hash
   1700 | SHA2-512                                                   | Raw Hash
  17300 | SHA3-224                                                   | Raw Hash
  17400 | SHA3-256                                                   | Raw Hash
  17500 | SHA3-384                                                   | Raw Hash
  17600 | SHA3-512                                                   | Raw Hash

We have to use 1400 

Let's try it:
hashcat -m 1400 -a 0 '$5$JS4kTGQpJsuKAq7f$8yHlRHpl5IDzMbNttD3zfmxoBHSQZ7ENFkBGnzVXyI3' /usr/share/wordlists/dictionary-list.txt -w 4
hashcat (v6.2.6) starting

* Device #1: WARNING! Kernel exec timeout is not disabled.
             This may cause "CL_OUT_OF_RESOURCES" or related errors.
             To disable the timeout, see: https://hashcat.net/q/timeoutpatch
* Device #2: WARNING! Kernel exec timeout is not disabled.
             This may cause "CL_OUT_OF_RESOURCES" or related errors.
             To disable the timeout, see: https://hashcat.net/q/timeoutpatch
CUDA API (CUDA 12.2)
====================
* Device #1: NVIDIA GeForce RTX 2080 SUPER, 7006/7969 MB, 48MCU

OpenCL API (OpenCL 3.0 CUDA 12.2.148) - Platform #1 [NVIDIA Corporation]
========================================================================
* Device #2: NVIDIA GeForce RTX 2080 SUPER, skipped

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 17.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
============================================================================================================================================
* Device #3: cpu-skylake-avx512-AMD Ryzen 7 7800X3D 8-Core Processor, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hash '$5$JS4kTGQpJsuKAq7f$8yHlRHpl5IDzMbNttD3zfmxoBHSQZ7ENFkBGnzVXyI3': Token length exception

* Token length exception: 1/1 hashes
  This error happens if the wrong hash type is specified, if the hashes are
  malformed, or if input is otherwise not as expected (for example, if the
  --username option is used but no username is present)

No hashes loaded.

Started: Thu Jul 18 15:57:37 2024
Stopped: Thu Jul 18 15:57:38 2024

Looks like we are not getting the hash this time, lets see crackstation.
![Screenshot_2024-07-18_15-59-53](https://github.com/user-attachments/assets/db454d9b-c9a4-4b1a-8b17-e54ec612083d)

Yeah, let's try autodetect mode on hashcat: hashcat -a 0 '$5$JS4kTGQpJsuKAq7f$8yHlRHpl5IDzMbNttD3zfmxoBHSQZ7ENFkBGnzVXyI3' /usr/share/wordlists/dictionary-list.txt -w 4

hashcat -a 0 '$5$JS4kTGQpJsuKAq7f$8yHlRHpl5IDzMbNttD3zfmxoBHSQZ7ENFkBGnzVXyI3' /usr/share/wordlists/dictionary-list.txt -w 4 
hashcat (v6.2.6) starting in autodetect mode

* Device #1: WARNING! Kernel exec timeout is not disabled.
             This may cause "CL_OUT_OF_RESOURCES" or related errors.
             To disable the timeout, see: https://hashcat.net/q/timeoutpatch
* Device #2: WARNING! Kernel exec timeout is not disabled.
             This may cause "CL_OUT_OF_RESOURCES" or related errors.
             To disable the timeout, see: https://hashcat.net/q/timeoutpatch
CUDA API (CUDA 12.2)
====================
* Device #1: NVIDIA GeForce RTX 2080 SUPER, 7006/7969 MB, 48MCU

OpenCL API (OpenCL 3.0 CUDA 12.2.148) - Platform #1 [NVIDIA Corporation]
========================================================================
* Device #2: NVIDIA GeForce RTX 2080 SUPER, skipped

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 17.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
============================================================================================================================================
* Device #3: cpu-skylake-avx512-AMD Ryzen 7 7800X3D 8-Core Processor, skipped

Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

7400 | sha256crypt $5$, SHA256 (Unix) | Operating System

NOTE: Auto-detect is best effort. The correct hash-mode is NOT guaranteed!
Do NOT report auto-detect issues unless you are certain of the hash type.

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1396 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/dictionary-list.txt
* Passwords.: 87394
* Bytes.....: 832094
* Keyspace..: 87394

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.           

$5$JS4kTGQpJsuKAq7f$8yHlRHpl5IDzMbNttD3zfmxoBHSQZ7ENFkBGnzVXyI3:Abingdon
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 7400 (sha256crypt $5$, SHA256 (Unix))
Hash.Target......: $5$JS4kTGQpJsuKAq7f$8yHlRHpl5IDzMbNttD3zfmxoBHSQZ7E...zVXyI3
Time.Started.....: Thu Jul 18 15:57:27 2024 (1 sec)
Time.Estimated...: Thu Jul 18 15:57:28 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/dictionary-list.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    87586 H/s (24.71ms) @ Accel:64 Loops:512 Thr:256 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 21849/87394 (25.00%)
Rejected.........: 0/21849 (0.00%)
Restore.Point....: 0/87394 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4608-5000
Candidate.Engine.: Device Generator
Candidates.#1....: A-bomb -> cicala
Hardware.Mon.#1..: Temp: 53c Fan: 43% Util: 99% Core:2010MHz Mem:7500MHz Bus:16

Started: Thu Jul 18 15:57:13 2024
Stopped: Thu Jul 18 15:57:29 2024

Yeah, we should've used 7400, not 1400. Well, now we know.

![Screenshot_2024-07-18_16-02-48](https://github.com/user-attachments/assets/5330266e-aabf-4e41-a1c2-9e5287c55a20)
