
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

parser = argparse.ArgumentParser(description="subdomain scanner")
parser.add_argument("--target", required=True, help="target domain")
parser.add_argument("--threads", type=int, default=10, help="number of threads")
parser.add_argument("--verbose", action="store_true", help="show detailed output")
args = parser.parse_args()

target = args.target
threads = args.threads
verbose = args.verbose

if target.startswith("http"):
    target = target.split("//")[1]
target = target.replace("www.", "")

print(f"\n[+] scanning subdomains for {target} ...\n")

with open("subdomains.txt") as f:
    subdomains = f.read().splitlines()

headers = {
    "User-Agent": "Mozilla/5.0"
}

found = []
lock = Lock()

def scan(sub):
    url = f"https://{sub}.{target}"
    
    if verbose:
        print(f"[*] checking {url}")

    for _ in range(2):
        try:
            response = requests.get(url, timeout=3, headers=headers)

            if response.status_code < 400:
                if verbose:
                    print(f"[FOUND] {url} (status: {response.status_code})")
                with lock:
                    found.append(url)
                return

        except requests.exceptions.RequestException:
            continue

with ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(scan, subdomains)

found = list(set(found))
found.sort()

print("\n[+] scan complete!")

if found:
    print(f"[+] total found: {len(found)}")
else:
    print("[-] no subdomains found")

filename = f"{target}_subdomains.txt"

with open(filename, "w") as file:
    for f in found:
        file.write(f + "\n")

print(f"\n[+] results saved to {filename}")

