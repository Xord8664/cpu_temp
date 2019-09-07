#!/usr/bin/python3

import os
import time
import datetime
import csv

cpufreq_dir = "/sys/devices/system/cpu/cpufreq/"
freqs_dir = []
header = []
temp_file = "/sys/class/hwmon/hwmon1/temp1_input"
csv_log = "/home/xord/Documents/" + time.strftime("%Y-%m-%d_%H:%M:%S") + ".csv"

listing = os.listdir("/sys/devices/system/cpu/cpufreq/")

for dirs in listing:
    if "policy" in dirs:
        freqs_dir.append(dirs)
        header.append(dirs)

header.append("temp")
print(header)

log_write_header = open(csv_log, "w")
head_write = csv.writer(log_write_header, delimiter = "\t")
head_write.writerow(header)
log_write_header.close()

while True:
    values = []
    for dir_with_freq in freqs_dir:
        f = open(cpufreq_dir + dir_with_freq + "/" + "scaling_cur_freq", "r")
        values.append(int(f.read()))
        f.close()

    temp_open = open(temp_file, "r")
    temp_value = int(temp_open.read())/1000
    values.append(temp_value)
    temp_open.close()
    print(values)
    log_write = open(csv_log, "a")
    values_write = csv.writer(log_write, delimiter = "\t")
    values_write.writerow(values)
    log_write.close()
    time.sleep(1)
