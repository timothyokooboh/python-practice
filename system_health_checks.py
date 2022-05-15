#!/usr/bin/env python3
import shutil
import psutil

def check_disk_space():
    disk_space = shutil.disk_usage("/")
    percent_free_space = disk_space.free / disk_space.total * 100
    print("Disk space is {:.2f}% free".format(percent_free_space))

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print("CPU usage is {}%".format(usage))

check_disk_space()
check_cpu_usage()
