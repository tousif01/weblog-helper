# Python Scripts to filter IP addresses from a given log file

## Filter IP Address List

The script `weblog_helper.py` takes below arguments:

* the log file to be parsed
* the ip list (space-separated) to be searched/filtered
* the optional output file to store the result

The output is the lines from the log file that contain the filtered IP addresses.

**Example Usage**

`python filter_logs.py logs.txt --ip 192.168.1.1 10.0.0.2`

## Filter IP Addresses from CIDR Range

The script `weblog_helper_iprange.py` takes below arguments:

* the log file to be parsed
* the CIDR ranges (space-separated) to be searched/filtered
* the optional output file to store the result

The output is the lines from the log file that contain the filtered IP addresses from the CIDR block. The code uses `ipaddress` library to expand on the CIDR block.

**Example Usage**

`python filter_logs.py logs.txt --ip 192.168.1.1 10.0.0.2`

