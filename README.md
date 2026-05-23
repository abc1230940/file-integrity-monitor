<a name="top"></a>

<p align="center"> 
  <a href="https://www.linkedin.com/in/clarence-fong" target="_blank">
    <img width="50" height="50" alt="LinkedIn" src="https://github.com/user-attachments/assets/7ab6e12b-ca8a-4aa6-8f10-79ba89d485b5" />
  </a>
  <a href="mailto:abc1230940@gmail.com">
    <img width="50" height="50" alt="Gmail" src="https://github.com/user-attachments/assets/4e0491ce-239c-413c-b433-74a5ff48f231" />
  </a>
  <a href="https://www.instagram.com/cyberbrexel?igsh=MXNxeWJid2VxZWxxaw%3D%3D&utm_source=qr" target="_blank">
    <img width="50" height="50" alt="Instagram Old" src="https://github.com/user-attachments/assets/62e4672b-d424-4489-a204-c301040905a3" />
  </a>
  <a href="https://discordapp.com/users/cyberbrexel" target="_blank">
    <img width="50" height="50" alt="Discord" src="https://github.com/user-attachments/assets/f76173ca-fad3-4390-bca1-5c2305bc748e" />
  </a>
  <a href="https://www.reddit.com/user/abc1230940/" target="_blank">
    <img width="50" height="50" alt="Reddit" src="https://github.com/user-attachments/assets/6e9bd985-dfa3-4349-b966-4cf49362bd61" />
  </a>
</p> <br>


<h3 id="web-server-port-alerter "align="center"> 
  <strong> File Integrity Monitor </strong>
</h3>
<p align="center">
  <img width="200" height="200" alt="—Pngtree—files vector icon_3743117" src="https://github.com/user-attachments/assets/f1a14567-bde2-488d-9d1d-06a8e884b964" />
</p>


<p align="center">
  An automated python tool that scans the sensitive files /etc/passwd and /etc/shadow containing user information in the unix system to monitor the file integrity
</p> <br>


<details>
  <summary>🔎 Table of Content</summary>
  <ol>
    <li> <a href="#about-the-project"> About The Project </a> </li>
    <ul>
    <li> <a href="#built-with"> Built With </a></li>
      <ul>
        <li> <a href="#language"> Language </a> </li>
        <li> <a href="#libraries-and-dependancies"> Libraries & Dependancies </a> </li>
      </ul>
    </ul>
    <li> <a href="#getting-started"> Getting Started </a> </li>
    <ul>
      <li> <a href="#prerequisites"> Prerequisites </a> </li>
      <li> <a href="#installation"> Installation </a> </li>
    </ul>
    <li> <a href="#usage"> Usage </a> </li>
    <li> <a href="#acknowledgement"> Acknowledgement </a> </li>
  </ol>
</details>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="about-the-project"> About the Project </h2>
<img width="681" height="145" alt="Screenshot 2026-05-23 165801" src="https://github.com/user-attachments/assets/937d330f-a8be-4a9b-957d-26f053f79862" />
<p> When an enterprise Linux server is compromised, one of the immediate actions taken by the attacker is to create a backdoor user to achieve persistence. Once a new user is created, /etc/passwd and /etc/shadow (which contain all user information in the system) will be modified. </p>
<p> This lightweight Python tool is designed to check the integrity of these sensitive files by comparing them with their initial SHA-256 hash values every hour. Alerts will be sent to a SOC Webhook server if discrepancies are detected, allowing incident responders to take immediate remediation action. </p
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h3 id="built-with"> Built With </h3>
<h4 id="language"> Language </h4>
<img src="https://img.shields.io/badge/Python-14354C?style=plastic&logo=python&logoColor=white" />
<h4 id="libraries-and-dependancies"> Libraries & Dependancies </h4>
<ul>
 <li> certifi (v2.7.0) </li>
 <li> charset-normalizer (v3.4.7) </li>
 <li> idna (v3.15) </li>
 <li> requests (v2.34.2) </li>
 <li> urllib3 (v2.7.0) </li>
</ul>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="getting-started"> Getting Started </h2>
The File Integrity Monitor is designed to use on the unix system, please make sure the system is updated and python with virtual environment is installed. Moreover, A Discord Webhook server is required to install to receive alert notifications.
<h3 id="prerequisites"> Prerequisites </h3>
<p> 1. System Update and Installation of Python </p>
<pre> <code lang="bash"> sudo apt update && sudo apt install -y python3.12-venv </code> </pre>
<p> 2. Configure a Discord Webhook Server </p>
<p> 2-1. Navigate to <a href="https://discord.com"> Discord</a> and Login </p>
<img width="1851" height="965" alt="2" src="https://github.com/user-attachments/assets/4ffcb751-461d-4d9d-bd9b-f5c570db63de" /><br>
<p> 2-2. Scroll down the navbar on the left and press "Add a Server" </p>
<img width="467" height="208" alt="2 0" src="https://github.com/user-attachments/assets/373f25c0-33a6-4195-b7ff-2d6040171e8c" /><br>
<p> 2-3. Create Your Server</p>
<p> choose "Create My Own" </p>
<img width="550" height="700" alt="2 1" src="https://github.com/user-attachments/assets/5d991dc8-1d4a-4fd8-94f0-02ec7c844cfd" /><br>
<p> 2-4. Tell Us About Your Server </p>
<p> choose "For me and my friends" </p>
<img width="548" height="465" alt="2 2" src="https://github.com/user-attachments/assets/fc8fe3bc-c7be-47f6-915d-33f621b0f742" /><br>
<p> 2-5. Customize Your Server </p>
<p> Give a name to your server and i named "File Integrity Monitor" </p>
<img width="547" height="517" alt="Screenshot 2026-05-23 154718" src="https://github.com/user-attachments/assets/37ce406a-ab72-4d6d-81ad-c8b2b2adf3bc" />
<p> 2-6. A server is installed </p>
<p> Click the Gear icon next to # general </p>
<img width="1503" height="821" alt="2 4" src="https://github.com/user-attachments/assets/8aeef7c3-6660-4663-9679-96c88d535915" /><br>
<p> 2-7. Click "Integrations" </p>
<img width="322" height="293" alt="2 6" src="https://github.com/user-attachments/assets/9cbf5013-aa5a-4589-a794-bdf07ec93482" /><br>
<p> 2-8. Click "Create Webhook" button </p>
<img width="963" height="497" alt="2 7" src="https://github.com/user-attachments/assets/8696f10d-5717-45e7-9812-c900793bab44" /><br>
<img width="970" height="606" alt="2 8" src="https://github.com/user-attachments/assets/975b1735-aeb7-45d1-9b55-864bd0d8daf7" /><br>
<p> 2.9. Click "Copy Webhook URL" button and paste it to your clipboard </p>
<img width="873" height="523" alt="2 9" src="https://github.com/user-attachments/assets/fad75ac0-ec8d-470b-b27a-f9b459e27489" /><br>
<img width="1252" height="105" alt="Screenshot 2026-05-23 154908" src="https://github.com/user-attachments/assets/59c4cedb-4497-4183-a408-6b592eb33e9e" />
<p> 2.10. Great! The Webhook server is created! </p>


<h3 id="installation"> Installation </h3>
<p> 1. Clone the Repo </p>
<pre> <code lang="bash">git clone https://github.com/abc1230940/file-integrity-monitor.git</code> </pre>
<p> 2. Navigate into the folder </p>
<pre> <code lang="bash">cd file-integrity-monitor</code> </pre> 
<p> 3. Set up the virtual environment </p>
<pre> <code lang="bash">python3 -m venv env</code> </pre>
<p> 4. Activate the virtual environment </p>
<pre> <code lang="bash">source env/bin/activate</code> </pre>
<p> 5. Install the required dependancies </p>
<pre> <code lang="bash">pip install -r requirements.txt</code> </pre>
<p> 6. Deactivate the virtual environment when finished </p>
<pre> <code lang="bash">deactivate </code> </pre>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="usage"> Usage </h2>
<p> 1. Edit the python script and then save</p>
<pre> <code lang="bash">nano file_integrity_monitor.py</code> </pre>
<img width="687" height="115" alt="Screenshot 2026-05-23 161220" src="https://github.com/user-attachments/assets/0fa77db0-b1c6-4a99-8314-e3f0f9136a2b" />
<p> ❗The monitor is designed to scan the sensitive files (/etc/passwd and /etc/shadow), but you can edit to scan targeted file paths
<p> ❗Paste your <strong>Webhook URL</strong> from the clipboard you have done before</p>
<p> 2. Launch the file integrity monitor script to begin monitoring </p>
<pre> <code lang="bash">sudo python3 file_integrity_monitor.py</code> </pre>
<img width="1118" height="133" alt="Screenshot 2026-05-23 161923" src="https://github.com/user-attachments/assets/912ecde6-c0f3-4193-87a6-c6860cf8106f" />
<p> 3. If the attacker created a backdoor user on the system upon compromise
<pre> <code lang="bash">useradd hacker</code> </pre>
<pre> <code lang="bash">passwd hacker</code> </pre>
<img width="408" height="26" alt="Screenshot 2026-05-23 164214" src="https://github.com/user-attachments/assets/e00c2fe1-9fb1-495c-9ca8-17f9d0c6e0a8" />
<p> A backdoor user "hacker" was added into /etc/passwd and /etc/shadow </p>
<p> 4. After an hour the script ran automatically and detected the files were edited, the following alert was shown </p>
<img width="681" height="145" alt="Screenshot 2026-05-23 165801" src="https://github.com/user-attachments/assets/5339fa67-f81a-43c1-9dc0-7b518b60979d" />
<p> 5. And the alert was also sent to your webhook server, so you can be alerted immediately on your workstation</p>
<img width="553" height="138" alt="Screenshot 2026-05-23 165817" src="https://github.com/user-attachments/assets/0a22dee6-6f96-48bc-9e3a-ef7ad26518bd" />
<p> 6. The monitor run automatically for every hour (3600 seconds) to keep checking file integrity </p>
<p align="right">(<a href="#top">Back to Top</a>)</p>


<h2 id="acknowledgement"> Acknowledgement </h2>
<p> </p><a href="https://app.letsdefend.io/training/lessons/python-for-blue-team"> LetsDefend - Python for Blue Team </a> </p>
<p> </p><a href="https://discord.com"> Discord </a> </p> 
<img width="1506" height="786" alt="2 14" src="https://github.com/user-attachments/assets/0013778a-8ff6-4bcb-8bd2-e2789f523c59" />
<p align="right">(<a href="#top">Back to Top</a>)</p>
