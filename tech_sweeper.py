# tech_sweeper.py

import psutil
import shutil
import platform
import datetime
from cleanup import clean_temp_folder

def print_header():
    print("=" * 40)
    print("🧹 Tech Sweeper System Report")
    print("=" * 40)
    print(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print("")

def check_disk_usage():
    print("💾 Disk Usage:")
    total, used, free = shutil.disk_usage("C:/")
    print(f"  Total: {total // (2**30)} GB")
    print(f"  Used:  {used // (2**30)} GB")
    print(f"  Free:  {free // (2**30)} GB")
    print("")

def check_cpu_memory():
    print("🧠 CPU & Memory:")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    print(f"  CPU Load:     {cpu}%")
    print(f"  Memory Used:  {memory.percent}%")
    print(f"  Total RAM:    {memory.total // (2**20)} MB")
    print("")

def main():
    print_header()
    check_disk_usage()
    check_cpu_memory()
    clean_temp_folder()
    print("✅ Scan complete. Your system looks squeaky clean!")

if __name__ == "__main__":
    main()
