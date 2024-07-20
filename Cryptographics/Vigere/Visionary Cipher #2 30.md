# What if the Key is Unknown?

Here's the ciphertext:

```
Dvrl olm uah fcl mwl hf vijfphx avzk qlgjskl? Hysx doj lll grei rsp A yzsu ls lbtjcwh kzmz avkwhuv. TXD, ww s qlgjskl wj wrjfphxlr rfh kstjcwhvv aphy lll grei rsp, llhh zk ghzcwh zmdeiafzu iuqiqtawff.
```

Have fun? Yeah, let's see...

## Using CyberChef

Let's open [CyberChef](https://gchq.github.io/CyberChef/) and try a few keys as guesses.

- **KEY**, **SECRET**, **PASSWORD** do not work.

## Using dCode

Let's see if [dCode Vigenère Cipher](https://www.dcode.fr/vigenere-cipher) can solve this.

![Screenshot of dCode Vigenère Cipher](https://github.com/user-attachments/assets/c9415735-279c-44a5-9096-aaf7948a218a)

Seems like a 5-letter key might be the right approach.

Let's put the 5-letter option in the box instead of 3.

![Screenshot of dCode with 5-letter option](https://github.com/user-attachments/assets/3e1fe7a1-0bf7-4471-8001-d7ef6f0994a3)

Ah yes, the answer is **horse**. That's the flag.

![Screenshot showing the flag](https://github.com/user-attachments/assets/2755e451-84e7-4f2e-9fa9-35b09e4d56c3)
```
