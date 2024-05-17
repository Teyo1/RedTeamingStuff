To enhance the readability of your content when displayed on GitHub, you can utilize Markdown formatting to organize and present the information more effectively. Here's how you can structure and format your text:

```markdown
# Chapter: Initial Access

In this chapter, we'll explore different methods to gain access to the system. First, we need to identify potential attack vectors.

As discussed in the previous enumeration chapter, multiple ports are open on the target system. Now, our aim is to establish initial access through these ports.

## Nmap Scan Results

Below are the results of the Nmap scan conducted:

```plaintext
Nmap scan report for 192.168.1.15
Host is up, received syn-ack (0.00020s latency).
Scanned at 2024-05-17 21:05:30 EEST for 11s
...

```

Some of the services hint the version, which helps us identify potential vulnerabilities.

## Exploiting Port 21/FTP

We'll focus on exploiting the FTP service running on port 21.

1. Open Metasploit in the terminal using the command `sudo msfconsole`.
2. Search for the exploit targeting vsftpd.
   ![Search vsftpd](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/638dca1e-c6a0-4178-a5ad-a9c1b8258522)
3. Select the exploit and show available options.
   ![Show options](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/73eeaa72-06ff-4275-9351-09c0b66d811b)
4. Set the required options, including the target IP and port.
   ![Set options](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/2505dc51-f0d4-48a0-873b-b5b57b630631)
5. Exploit the vulnerability.
   ![Exploit](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/03b38f26-1118-4cc8-a89c-4aaaca655a55)

## Post-Exploitation

After successfully exploiting the vulnerability, we have gained root access to the target machine.
   ![Root Access](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/9e3ebd78-0453-4540-9810-1eaadb485eaa)

Now, we have complete control over the Linux machine, allowing us to perform various actions, such as creating files.

## Viewing Created File

To demonstrate our control, let's create a file on the compromised machine.
   ![Create File](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/6db0c3d6-87ef-4429-af1b-b43924dd906d)

We can confirm the creation of the file using another shell on our virtual machine.
   ![View File](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/ce3c806a-705c-461b-a7f3-c5f96587d83a)
