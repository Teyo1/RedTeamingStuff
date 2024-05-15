# Removing Metasploitable's Internet Access

When setting up a vulnerable system like Metasploitable for testing or educational purposes, it's important to ensure that it doesn't have internet access to prevent unauthorized use by bad actors. This guide will walk you through the steps to remove internet access from Metasploitable.

## Checking Internet Access

Before proceeding with the steps, it's essential to verify whether Metasploitable currently has internet access. One way to do this is by pinging a public IP address like `google.com`.

![Ping Result](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/57902897-3431-4d40-90d1-0eb5c40bf5c2)

As shown in the image, if the ping to `google.com` is successful, it indicates that the system has internet access.

## Why Remove Internet Access?

Removing internet access from a vulnerable system like Metasploitable is crucial for several reasons:

1. **Prevention of Unauthorized Access:** By disconnecting Metasploitable from the internet, you reduce the risk of unauthorized users or malicious actors exploiting the vulnerabilities present in the system. Keeping it isolated ensures that only authorized users have access, limiting the potential for unauthorized exploitation.

2. **Protection of Other Systems:** Vulnerable systems like Metasploitable are often used for security testing and educational purposes. Allowing such a system to have internet access could potentially lead to unintended consequences, such as it being used as a launching point for attacks on other systems or networks. Removing internet access helps contain any potential damage within the isolated environment.

3. **Avoiding Legal and Ethical Issues:** Allowing a vulnerable system to connect to the internet opens up the possibility of it being used for illegal or unethical activities without your knowledge. By disconnecting it, you mitigate the risk of inadvertently participating in activities that could lead to legal consequences or reputational damage.

4. **Preservation of Integrity:** Vulnerable systems are often set up to simulate real-world scenarios and contain intentionally exploitable vulnerabilities. Allowing internet access could compromise the integrity of these vulnerabilities by exposing them to real-world attackers who could exploit them for malicious purposes. By keeping the system isolated, you ensure that it remains in a controlled environment for testing and learning purposes.

## Steps to Remove Internet Access

1. **Edit Virtual Machine Settings:**

   ![Edit Settings](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/e96f1ed5-1caf-4698-bd3a-f1de9f39056f)

2. **Disable Network Adapter:**

   Untick the option that allows the virtual machine to connect to the network.

   ![Disable Network Adapter](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/5df71568-cbdd-4e32-964c-1e322bfcb000)

3. **Confirmation:**

   Once the changes are applied, ensure that the virtual machine no longer has internet access.

   ![Ping Result](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/c54861ae-d288-4433-b8c7-c1485aeb47ce)

   As depicted in the image, attempting to ping a domain like `google.com` should result in an "unknown host" error, confirming the removal of internet access.

By following these steps, you can effectively isolate Metasploitable from the internet, reducing the risk of unauthorized usage and ensuring a safe testing environment.

Feel free to reach out if you have any questions or concerns!
