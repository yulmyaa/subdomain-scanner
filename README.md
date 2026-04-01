# Subdomain Scanner
A simple subdomain enumeration tool.   
It quickly scans subdomains based on the domain you enter.

***

## Features
- Discovers subdomains automatically
- Fast scanning using multythreading
- Filters based on HTTP status codes
- Saves result file autometically
- CLI(Command Line Interface)

***

## Tech stack
- python 3
- requests
- concurrent.futures (ThreadPoolExecutor)

***

## Installation
git clone https://github.com/yulmyaa/subdomain-scanner.git   
cd subdomain-scanner   
pip install requests   

***

## Usage
python subdomain_scanner.py --target example.com --threads 20   

### Option
- `--target` : target domain (required)
- `--threads` : number of threads (default: 10)
- `--verbose` : verbose output for debugging (optional)

***

## Example output
[+] scan complete!   
[+] total found: 6   

[+] results saved to google.com_subdomains.txt   

***

## How it works
1. Loads the list of subdomains (`subdomains.txt`)
2. Sends HTTP requests to each subdomain
3. Checks the response status code
4. Saves valid subdomains

***

This tool is for educational purposes only.
