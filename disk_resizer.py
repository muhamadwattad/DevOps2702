from os import getenv


def disk_resizer(disk_name, machine_name, target_gb):
    print(f"Disk details: DN: {disk_name} , MN: {machine_name} to {target_gb}")
    print("connecting to vSphere")
    print("location machine")
    print("resizing disk")
    print("sshing ext4")


disk_name = getenv("DISK_NAME")
machine_name = getenv("MACHINE_NAME")
target_gb = getenv("TARGET_GB")

disk_resizer(disk_name, machine_name, target_gb)
