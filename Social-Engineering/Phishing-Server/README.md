# QR Code Credential Harvest

## Poster with QR Code

- **Effectiveness**: A well-designed poster with a QR code can be highly effective in collecting credentials. This approach leverages a physical medium (the poster) to direct individuals to a malicious link.
- **Target Audience**: This tactic is effective for any group of individuals who might be susceptible to phishing attempts. Placing the poster in settings where people are concerned about their security or where LinkedIn is commonly used (e.g., office spaces, tech conferences) increases the likelihood of success.

## Scenario for Usage

- **Scenario**: The phishing attempt is framed as a security alert from LinkedIn, urging the target to act quickly to secure their account. This creates a sense of urgency and fear, which can lead people to act impulsively and enter their credentials without scrutinizing the legitimacy of the request.
- **Specific Group**: This is effective for professionals who use LinkedIn regularly and are concerned about account security. It preys on the natural anxiety people feel about potential security breaches.

## Harvesting Tool

- **Website**: The website used, set up using the `zphisher` tool, mimics a LinkedIn login page to collect user credentials. The use of a tool like `zphisher` simplifies the creation of phishing pages.
- **Testing**: The QR code and website were tested thoroughly, confirming that the tool is working as expected.

## Outcome

- **Phishing Success**: If the target enters their LinkedIn login credentials on the fake page, the attacker gains access to the victim’s LinkedIn account. This could lead to unauthorized activities and potential damage, such as identity theft or financial loss.

## QR Code Creation

- **Link Shortener**: Using a link shortener (`t.ly` in this case) makes the URL more manageable and helps obscure the destination, making it less obvious that the link is malicious.
- **Poster Design**: Canva was used to design the poster, which is a user-friendly tool for creating visually appealing and convincing materials.

## Results

- **Data Collection**: Test credentials were successfully collected using the phishing page, as demonstrated by the screenshots.

## Recommendations and Considerations

1. **Ethical Use**: Ensure that such techniques are used ethically and legally. Always have explicit permission from the target group if conducting security awareness tests or penetration tests.
2. **Awareness Training**: Consider using this experience to educate others about phishing risks and how to recognize and avoid them.

---

## Phishing Server - Planning

### Alibi

- **LinkedIn Site**: The phishing attempt is framed as a security alert from LinkedIn.
- **Security Alert**: The email claims that unauthorized login attempts have been detected.
- **Scenario/Plan**: Created with the help of ChatGPT.

### Scenario

- **Email Content**: The target receives an email from LinkedIn warning them of suspicious activity on their account, urging immediate action to secure their account.

### Tactics

- **Call to Action**: The poster instructs the target to scan the QR code.
- **Urgency**: The message implies that immediate action is required.
- **Financial**: The phishing scenario involves enticing targets with a potential financial benefit.

## The Website in the Making

- **Downloading the Tool**:
  ```bash
  git clone --depth=1 https://github.com/htr-tech/zphisher.git
  ```
- **Screenshots**: 
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/b2f1feda-e5c6-43e4-b3b2-68b2a0397952)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/7d820b29-5445-41da-a8c2-6bbb97f3cf4d)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/db6ba531-83ba-4f64-b257-6ecac9f110c3)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/f89cd6d7-7f63-4208-9201-83758bf0522d)

- **Selecting the Phishing Template**:
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/7bdfea9d-6b4a-4b59-8d3f-391cfc971dc5)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/b2caa277-635e-46ee-80f9-3cc7ef773264)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/52596ec3-c6e1-40c7-9ca3-d6eb2e5c253c)

- **Copying the Link**:
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/2723ce05-96da-4530-804a-088fb2aa7c71)

- **Testing**:
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/1dd5db9f-2331-4716-881e-19170c399734)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/4da5b0ce-a7a2-488f-8cb2-d0479ecd550d)

- **Success**:
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/bc5ee8a7-66ca-4cda-a87f-249fc4d418bc)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/6ae60a3d-5806-4350-94fb-3c813b936755)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/56e7982e-4c54-409a-bb16-321565ddda53)

## The QR Code

- **Link**: [https://el-express-benjamin-serial.trycloudflare.com/login.html](https://el-express-benjamin-serial.trycloudflare.com/login.html)
- **Link Shortener**: 
  [https://t.ly](https://t.ly)

  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/e64df0a8-88e2-4dfb-ab1f-bb37bead590e)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/26aeefcb-e194-4aff-b0aa-8f6b7b04dc12)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/ac8e3aa8-a43f-4bc8-a84d-0cf93efb3fcc)
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/39710387-d546-4525-af44-a3e53612349d)

- **QR Code on Phone**:
  ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/83deba22-aade-4fb3-a00c-be922a6b87f8)

## Poster Design

- **Creating the Poster**: 
  - Opened Canva: ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/2ca446a3-b3b3-4b24-8c45-4b65da4b8ecb)
  - Final Poster: ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/5473c226-3b59-4ee0-aeee-492785e9afb8)
  - Scanned QR Code: [YouTube Video](https://www.youtube.com/shorts/KNU2SQD_HGc) ![image](https://github.com/PrivacyAndSocialEngineering/privacy-social-returns-Teyo1/assets/131766045/301d9c29-8e3d-4929-9b01-e7f36a18304d)

## Summary

- **Harvesting Data**: Managed to collect information as demonstrated by the screenshots.

**Note**: It's important to use such techniques responsibly and legally. Ensure explicit permission if conducting security awareness tests or penetration tests.
```

This Markdown format provides a structured overview of the phishing campaign setup, including the poster creation, scenario, and results.
