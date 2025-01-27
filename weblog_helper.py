import re
import argparse

def filter_logs_by_ip(log_file, ip_list, output_file=None):
    """
    Filters HTTP logs based on a list of IP addresses.

    :param log_file: Path to the HTTP log file
    :param ip_list: List of IP addresses to filter
    :param output_file: Path to the output file (optional)
    """
    ip_pattern = re.compile(r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)")
    filtered_logs = []
    try:
        with open(log_file, 'r') as file:
            for line in file:
                match = ip_pattern.search(line)
                if match and match.group() in ip_list:
                    filtered_logs.append(line)
    except FileNotFoundError:
        print(f"Error: The file {log_file} was not found.")
        return
    
    if output_file:
        try:
            with open(output_file, 'w') as out_file:
                out_file.writelines(filtered_logs)
            print(f"Filtered logs saved to {output_file}.")
        except IOError:
            print(f"Error: Unable to write to {output_file}.")
    else:
        print("Filtered logs:")
        for log in filtered_logs:
            print(log)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter HTTP logs based on IP addresses.")
    parser.add_argument("log_file", help="Path to the HTTP log file.")
    parser.add_argument("--ip", nargs='+', required=True, help="IP addresses to filter (space-separated).")
    parser.add_argument("--output", help="Path to save the filtered logs (optional).")

    args = parser.parse_args()

    log_file_path = args.log_file
    ip_addresses = args.ip
    output_file_path = args.output

    filter_logs_by_ip(log_file_path, ip_addresses, output_file_path)

