# Data Recovery from a Windows Shared Drive Using Foremost on Kali Linux

This guide covers the steps to recover data from a **Windows shared C drive** using **Foremost** on **Kali Linux**. The data will be saved directly to the Kali machine.

## Prerequisites

- A Windows machine with the shared C drive.
- Kali Linux with `cifs-utils` and `foremost` installed.
- Access to the Windows machine via SMB (you need the username and password).

---

## Steps

### 1. Install Required Tools

First, ensure that the necessary tools are installed on your Kali machine.

```bash
sudo apt update
sudo apt install cifs-utils foremost \
```

2. Mount the Windows Shared C Drive

You need to mount the Windows shared C drive on your Kali Linux system. Replace 192.168.1.102 with the IP of your Windows machine and AA with your Windows username.

bash

sudo mkdir /mnt/windows_share
sudo mount.cifs //192.168.1.102/C /mnt/windows_share -o username=AA

Enter the password for the AA account when prompted. The Windows C drive should now be accessible under /mnt/windows_share.
3. Create a Directory for Recovered Data

Create a local directory on your Kali machine where Foremost can store the recovered data.

bash

mkdir ~/foremost_output

4. Run Foremost to Scan and Recover Data

Use Foremost to scan the entire mounted Windows C drive and recover all known file types.

bash

sudo foremost -i /mnt/windows_share -o ~/foremost_output -T

    -i: Input directory (the mounted Windows share).
    -o: Output directory for the recovered files.
    -T: Option to recover all known file types.

5. Verify Recovered Files

Once Foremost completes the recovery process, check the output directory for the recovered files:

bash

ls ~/foremost_output

6. Unmount the Windows Share (Optional)

If you are finished working with the Windows share, you can unmount it:

bash

sudo umount /mnt/windows_share
