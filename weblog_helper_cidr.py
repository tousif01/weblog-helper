import re
import argparse
import ipaddress

def filter_logs_by_cidr(log_file, cidr_list, output_file=None):
    """
    Filters HTTP logs based on a list of CIDR ranges.

    :param log_file: Path to the HTTP log file
    :param cidr_list: List of CIDR ranges to filter
    :param output_file: Path to the output file (optional)
    """
    #ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')  # Regular expression for matching IPs

    ip_pattern = re.compile(r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)")
        
    # Convert CIDR ranges to networks
    networks = [ipaddress.ip_network(cidr) for cidr in cidr_list]
    
    print(f"\n\n{networks}\n\n")
    
    filtered_logs = []
    try:
        with open(log_file, 'r') as file:
            for line in file:
                match = ip_pattern.search(line)
                if match:
                    ip = ipaddress.ip_address(match.group())
                    # Check if the IP belongs to any of the CIDR networks
                    if any(ip in network for network in networks):
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
    parser = argparse.ArgumentParser(description="Filter HTTP logs based on CIDR ranges.")
    parser.add_argument("log_file", help="Path to the HTTP log file.")
    parser.add_argument("--cidr", nargs='+', required=True, help="CIDR ranges to filter (space-separated).")
    parser.add_argument("--output", help="Path to save the filtered logs (optional).")

    args = parser.parse_args()

    log_file_path = args.log_file
    cidr_ranges = args.cidr
    output_file_path = args.output

    filter_logs_by_cidr(log_file_path, cidr_ranges, output_file_path)

