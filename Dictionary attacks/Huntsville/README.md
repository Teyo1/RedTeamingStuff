# Understanding Password Salts and /etc/shadow Fields

When encountering password hashes on a Linux machine, they are typically stored in the `/etc/shadow` file. This file secures user passwords using various hashing algorithms and includes additional information about password policies.

## Password Salts

A password salt is a random value added to the password before hashing to ensure that even if two users have the same password, their hash values will differ. This defeats precomputed hash attacks (rainbow tables) and adds complexity to brute-force attacks.

## /etc/shadow File Fields

The `/etc/shadow` file contains fields separated by dollar signs (`$`). Here are some common fields:

- **Username**: The username associated with the password hash.
- **Password Hash**: The hashed password itself.
- **Last Password Change**: Days since January 1, 1970, when the password was last changed.
- **Minimum Password Age**: Minimum days required before the password can be changed.
- **Maximum Password Age**: Maximum days the password is valid before it must be changed.
- **Password Warning Period**: Days before password expiration when the user is warned.
- **Password Inactivity Period**: Days after password expiration before the account is locked.
- **Account Expiry Date**: Days since January 1, 1970, when the account expires.
- **Reserved Field**: For future use.

For example, a hash starting with `$5$` indicates that the password has been hashed using SHA256.

For more details, refer to the [Linuxize guide on /etc/shadow file](https://linuxize.com/post/etc-shadow-file/).

---

This format provides a brief yet informative overview of password salts, the structure of `/etc/shadow` file fields, and where to find more detailed information. Adjustments can be made based on specific requirements or additional content.
