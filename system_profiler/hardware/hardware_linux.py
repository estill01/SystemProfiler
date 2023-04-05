import os
import subprocess
import pwd
import re

# PLATFORM: LINUX
#
# 1 Hardware Info
#
# 1.1 Processor
# 1.2 Memory
# 1.3 Storage Devices
# 1.4 Network Interfaces
# 1.5 Graphics Card
# 1.6 Sound Devices
# 1.7 Input Devices
# 1.8 USB Devices
# 1.9 Battery
# 1.10 Cooling System
# 1.11 BIOS/UEFI
# 1.12 Device Tree
# 1.13 Secure Boot
# 1.14 Trusted Platform Module (TPM)
# 1.15 Hardware Security Modle (HSM)
# 1.16 Hardware Root of Trust (RoT)

def is_root():
    return os.geteuid() == 0

def get_hardware_info():
    hardware_info = {
        "processor": get_processor_info(),
        "memory": get_memory_info(),
        "storage_devices": get_storage_devices(),
        "network_interfaces": get_network_interfaces(),
        "graphics_card": get_graphics_card_info(),
        "sound_devices": get_sound_devices(),
        "input_devices": get_input_devices(),
        "usb_devices": get_usb_devices(),
        "battery": get_battery_info(),
        "cooling_system": get_cooling_system_info(),
        "bios_uefi": get_bios_uefi_info(),
        "hardware_security": get_hardware_security(),
        "device_tree_data": get_device_tree_data(),
        "secure_boot": get_secure_boot(),
        "tpm": get_tpm_info(),
        "hsm": get_hsm_info(),
        "hardware_root_of_trust": get_hardware_root_of_trust(),
    }
    return hardware_info


# 1.1 Processor
def get_processor_info():
    processor_info = {}

    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
            if "model name" in line:
                processor_info["model_name"] = line.split(":")[1].strip()
            elif "cpu cores" in line:
                processor_info["cpu_cores"] = int(line.split(":")[1].strip())
            elif "siblings" in line:
                processor_info["siblings"] = int(line.split(":")[1].strip())
            elif "flags" in line:
                processor_info["flags"] = line.split(":")[1].strip().split()

    return processor_info

# 1.2 Memory
def get_memory_info():
    memory_info = {}

    with open('/proc/meminfo') as f:
        for line in f:
            if "MemTotal" in line:
                memory_info["ram"] = line.split(": ")[1].strip()  # 1.2.1 RAM
            elif "SwapTotal" in line:
                memory_info["swap_space"] = line.split(": ")[1].strip()  # 1.2.2 Swap Space

    return memory_info

# 1.3 Storage Devices
def get_storage_devices():
    storage_devices = []

    output = subprocess.run(['lsblk', '-d', '-o', 'NAME,MODEL,SIZE,TYPE'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n')[1:]:
        if line:
            name, model, size, device_type = line.strip().split()
            if device_type in ['disk', 'rom']:
                device_info = {
def is_root():
    return os.geteuid() == 0

def get_hardware_info():
    hardware_info = {
        "processor": get_processor_info(),
        "memory": get_memory_info(),
        "storage_devices": get_storage_devices(),
        "network_interfaces": get_network_interfaces(),
        "graphics_card": get_graphics_card_info(),
        "sound_devices": get_sound_devices(),
        "input_devices": get_input_devices(),
        "usb_devices": get_usb_devices(),
        "battery": get_battery_info(),
        "cooling_system": get_cooling_system_info(),
        "bios_uefi": get_bios_uefi_info(),
        "hardware_security": get_hardware_security(),
        "device_tree_data": get_device_tree_data(),
    }
    return hardware_info

# 1.1 Processor
def get_processor_info():
    processor_info = {}

    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
            if "model name" in line:
                processor_info["model_name"] = line.split(":")[1].strip()
            elif "cpu cores" in line:
                processor_info["cpu_cores"] = int(line.split(":")[1].strip())
            elif "siblings" in line:
                processor_info["siblings"] = int(line.split(":")[1].strip())
            elif "flags" in line:
                processor_info["flags"] = line.split(":")[1].strip().split()

    return processor_info

# 1.2 Memory
def get_memory_info():
    memory_info = {}

    with open('/proc/meminfo') as f:
        for line in f:
            if "MemTotal" in line:
                memory_info["ram"] = line.split(": ")[1].strip()  # 1.2.1 RAM
            elif "SwapTotal" in line:
                memory_info["swap_space"] = line.split(": ")[1].strip()  # 1.2.2 Swap Space

    return memory_info

# 1.3 Storage Devices
def get_storage_devices():
    storage_devices = []

    output = subprocess.run(['lsblk', '-d', '-o', 'NAME,MODEL,SIZE,TYPE'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n')[1:]:
        if line:
            name, model, size, device_type = line.strip().split()
            if device_type in ['disk', 'rom']:
                device_info = {
                    "name": name,
                    "model": model,
                    "size": size,
                    "type": device_type,
                    "partitions": get_device_partitions(name),
                }
                storage_devices.append(device_info)

    return storage_devices

def get_device_partitions(device_name):
    partitions = []

    output = subprocess.run(['lsblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n')[1:]:
        if line:
            name, size, device_type, *mountpoint = line.strip().split()
            mountpoint = mountpoint[0] if mountpoint else None
            if device_type == 'part' and device_name in name:
                partition_info = {
                    "name": name,
                    "size": size,
                    "mountpoint": mountpoint,
                }
                partitions.append(partition_info)

    return partitions

# 1.4 Network Interfaces
def get_network_interfaces():
    network_interfaces = []

    output = subprocess.run(['ip', 'link'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n'):
        if line.startswith(' '):
            continue
        if ':' in line:
            index, name = line.split(':', 1)
            name = name.strip()
            interface_info = {
                "name": name,
                "mac_address": get_mac_address(name),
                "ip_address": get_ip_address(name),
                "statistics": get_interface_statistics(name),
            }
            network_interfaces.append(interface_info)

    return network_interfaces

# TODO Do we need this here?
def get_interface_statistics(interface_name):
    statistics = {}

    stats_path = f"/sys/class/net/{interface_name}/statistics"
    if os.path.exists(stats_path):
        for stat in os.listdir(stats_path):
            with open(os.path.join(stats_path, stat), 'r') as f:
                statistics[stat] = int(f.read().strip())

    return statistics


# 1.5 Graphics Card
def get_graphics_card_info():
    # Combined collectors for 1.5.1 and 1.5.2
    graphics_cards = []

    output = subprocess.run(['lspci'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n'):
        if "VGA" in line or "Display" in line:
            graphics_cards.append(line)

    return graphics_cards

# 1.6 Sound Devices
def get_sound_devices():
    sound_devices = []

    output = subprocess.run(['lspci'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n'):
        if "Audio" in line:
            sound_devices.append(line)

    return sound_devices

# 1.7 Input Devices
def get_input_devices():
    input_devices = {
        "keyboard": [],  # 1.7.1 Keyboard
        "mouse": [],  # 1.7.2 Mouse
        "touchpad": []  # 1.7.3 Touchpad
    }

    output = subprocess.run(['xinput', '--list'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n'):
        if "keyboard" in line.lower():
            input_devices["keyboard"].append(line.strip())
        elif "mouse" in line.lower():
            input_devices["mouse"].append(line.strip())
        elif "touchpad" in line.lower():
            input_devices["touchpad"].append(line.strip())

    return input_devices

# 1.8 USB Devices
def get_usb_devices():
    usb_info = {
        "controllers": [],  # 1.8.1 USB Controllers
        "connected_devices": []  # 1.8.2 Connected USB Devices
    }

    output = subprocess.run(['lsusb'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n'):
        if "Hub" in line or "Host Controller" in line:
            usb_info["controllers"].append(line.strip())
        else:
            usb_info["connected_devices"].append(line.strip())

    return usb_info

# 1.9 Battery
def get_battery_info():
    battery_info = {}

    if not is_root():
        return "Requires root access"

    if os.path.exists('/sys/class/power_supply/BAT0'):
        with open('/sys/class/power_supply/BAT0/uevent', 'r') as f:
            for line in f:
                if "POWER_SUPPLY_STATUS" in line:
                    battery_info["status"] = line.split("=")[1].strip()
                elif "POWER_SUPPLY_CAPACITY" in line:
                    battery_info["capacity"] = int(line.split("=")[1].strip())
                elif "POWER_SUPPLY_VOLTAGE_NOW" in line:
                    battery_info["voltage_now"] = int(line.split("=")[1].strip())

    return battery_info


# 1.10 Cooling System
def get_cooling_system_info():
    cooling_info = []

    thermal_zones = os.listdir('/sys/class/thermal')
    for zone in thermal_zones:
        zone_info = {"name": zone}
        with open(f'/sys/class/thermal/{zone}/temp', 'r') as f:
            zone_info["temperature"] = int(f.read().strip()) / 1000
        cooling_info.append(zone_info)

    return cooling_info

# 1.11 BIOS/UEFI Information
def get_bios_uefi_info():
    bios_info = {}

    if not is_root():
        return "Requires root access"

    output = subprocess.run(['dmidecode', '-t', 'bios'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode()
    for line in output.split('\n'):
        if "Vendor" in line:
            bios_info["vendor"] = line.split(": ")[1].strip()
        elif "Version" in line:
            bios_info["version"] = line.split(": ")[1].strip()
        elif "Release Date" in line:
            bios_info["release_date"] = line.split(": ")[1].strip()

    return bios_info

# 1.12 Device Tree
def get_device_tree_data():
    if not is_root():
        return "Requires root access"

    device_tree_data = {}

    output = subprocess.run(['lspci', '-tv'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode()
    device_tree_data["lspci_tree"] = output

    return device_tree_data


# 1.13 Secure Boot
def get_secure_boot():
    if not is_root():
        return "Requires root access"

    secure_boot = None
    try:
        output = subprocess.run(['mokutil', '--sb-state'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode()
        if "SecureBoot enabled" in output:
            secure_boot = True
        elif "SecureBoot disabled" in output:
            secure_boot = False
    except FileNotFoundError:
        return "mokutil not found"

    return secure_boot

# 1.14 Trusted Platform Module (TPM)
def get_tpm_info():
    if not is_root():
        return "Requires root access"

    tpm_info = {}

    output = subprocess.run(['ls', '/sys/class/tpm'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout.decode()
    if output:
        tpm_devices = output.split()
        tpm_info["devices"] = tpm_devices

    return tpm_info

# 1.15 Hardware Security Module (HSM)
def get_hsm_info():
    if not is_root():
        return "Requires root access"

    hsm_info = []

    output = subprocess.run(['lspci'], stdout=subprocess.PIPE).stdout.decode()
    for line in output.split('\n'):
        if "Security devices" in line or "Cryptographic" in line or "Encryption" in line:
            hsm_info.append(line.strip())

    return hsm_info

# 1.16 Hardware Root of Trust
def get_hardware_root_of_trust():
    # Implement this function with the specific hardware root of trust information.
    return "Not implemented"


if __name__ == "__main__":
    hardware_profile = get_hardware_info()
    for category, info in hardware_profile.items():
        print(f"{category}:")
        print(info)
        print("\n")
