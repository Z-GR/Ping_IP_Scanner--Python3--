import subprocess
import time

def ping_ip_range(start, end):
    for i in range(start, end+1):
        ip_address = f'192.168.0.{i}'  # Change the prefix and adjust the format as needed
        try:
            #subprocess.run(['ping', '-c', '1', ip_address], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #Unix
            r = subprocess.run(['ping', '-n', '1', ip_address], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #Windows
            print("STDOUT:", r.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("STDOUT:", e.stdout.decode('utf-8'))
            print("STDERR:", e.stderr.decode('utf-8'))

if __name__ == "__main__":
    start_ip = 1  # Start of the IP range
    end_ip = 15   # End of the IP range

    start_timer = time.perf_counter()

    ping_ip_range(start_ip, end_ip)

    end_timer = time.perf_counter()
    print(f"Pinged in {end_timer - start_timer:0.4f} seconds")