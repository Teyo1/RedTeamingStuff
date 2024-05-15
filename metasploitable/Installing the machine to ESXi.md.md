# Converting VMDK to ESXi Format

## Introduction

This guide will walk you through the process of converting a VMDK file to the format compatible with ESXi, VMware's hypervisor.

## Steps

1. **Upload the VMDK File to Datastore:**
   - Navigate to your datastore and upload the `metasploitable.vmdk` file.

2. **Create New Virtual Machine (VM) Without Disk:**
   - Create a new VM without assigning any disk.

3. **Attach Existing Disk to the VM:**
   - Attach the existing disk to the VM. Select the `metasploitable.vmdk` file from the datastore.

4. **SSH into ESXi:**
   - Log on to your ESXi host via SSH.

5. **Run the Conversion Command:**
   - Execute the following command:
     ```bash
     vmkfstools -i /vmfs/volumes/blah/<source-vmdk-file-you-uploaded>.vmdk -d thin /vmfs/volumes/blah/vm/<destination>.vmdk
     ```
     Replace `<source-vmdk-file-you-uploaded>` and `<destination>` with the appropriate paths.

   - **Bonus:** This command also converts the disk to thin provision.

6. **Detach Disk from VM:**
   - Detach the disk from the VM.

7. **Attach Newly Created Disk to VM:**
   - Attach the newly created disk (in ESXi format) to the VM.

8. **Boot the Vulnerable OS and Hack:**
   - Boot the VM with the vulnerable OS and proceed with your intended activities.

9. **Set Adapter Type to "E1000":**
   - Before booting, ensure the adapter type of the VM is set to "E1000" as "VMXNET3" will not be supported.
If done orrectly you should see following
![image](https://github.com/Teyo1/RedTeamingStuff/assets/131766045/bb72d797-f796-4ab0-8f68-ae16bdc146ad)



# and login info wasn't admin:admin (has to be secure!!)


## Example

```bash
[root@localhost:~] ssh root@192.168.1.3
[root@localhost:~] vmkfstools -i /vmfs/volumes/Virtual\ Machines/Metasploitable.vmdk -d thin /vmfs/volumes/SSD/Metasploitable.vm
dk
Destination disk format: VMFS thin-provisioned
Cloning disk '/vmfs/volumes/Virtual Machines/Metasploitable.vmdk'...
Clone: 100% done.
