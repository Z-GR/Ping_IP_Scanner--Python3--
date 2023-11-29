import concurrent.futures
import subprocess
import time

specified_ip = "192.168.0.5"

def ping_ip(ip_address):
    try:
        #r = subprocess.run(['ping', '-c', '1', ip_address], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #Unix
        r = subprocess.run(['ping', '-n', '1', ip_address], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #Windows
        if r.stdout.decode('utf-8').find(specified_ip) != -1:
            return f'{ip_address} is unreachable'
        else:
            return f'{ip_address} is reachable'
    except subprocess.CalledProcessError:
            return f'{ip_address} timed out'

def ping_ip_range(start, end):
    ip_range = [f'192.168.0.{i}' for i in range(start, end + 1)]  # Adjust the IP address format and prefix
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(ping_ip, ip_range))

    for result in results:
        print(result)

if __name__ == "__main__":
    start_ip = 1  # Start of the IP range
    end_ip = 255   # End of the IP range

    start_timer = time.perf_counter()

    try:
        ping_ip_range(start_ip, end_ip)
    except KeyboardInterrupt:
        print("\nPing operation interrupted by user.")
    
    end_timer = time.perf_counter()
    print(f"Pinged in {end_timer - start_timer:0.4f} seconds")