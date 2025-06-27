import psutil
import shutil
import platform
import datetime
import os
from cleanup import clean_temp_folder

LOG_FILE = "logs/log.txt"

def write_log(message):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

def print_and_log(message):
    print(message)
    write_log(message)

def print_header():
    print_and_log("=" * 40)
    print_and_log("Tech Sweeper System Report")
    print_and_log("=" * 40)
    print_and_log(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print_and_log(f"System: {platform.system()} {platform.release()}")
    print_and_log(f"Processor: {platform.processor()}")
    print_and_log("")

def check_disk_usage():
    print_and_log("Disk Usage:")
    total, used, free = shutil.disk_usage("C:/")
    print_and_log(f"  Total: {total // (2**30)} GB")
    print_and_log(f"  Used:  {used // (2**30)} GB")
    print_and_log(f"  Free:  {free // (2**30)} GB")
    print_and_log("")

def check_cpu_memory():
    print_and_log("CPU & Memory:")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    print_and_log(f"  CPU Load:     {cpu}%")
    print_and_log(f"  Memory Used:  {memory.percent}%")
    print_and_log(f"  Total RAM:    {memory.total // (2**20)} MB")
    print_and_log("")

def main():
    write_log("=== Starting Tech Sweeper ===")
    print_header()
    check_disk_usage()
    check_cpu_memory()
    clean_temp_folder(log_func=write_log)
    print_and_log("Scan complete. Your system looks clean and healthy.")
    write_log("=== Tech Sweeper finished ===\n")

if __name__ == "__main__":
    main()
