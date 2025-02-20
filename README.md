## Ping Test Troubleshooter

### Description
**Ping Test Troubleshooter** is a Python script designed to help users diagnose network connectivity issues. It automates essential network tests, making troubleshooting easier by providing clear, actionable output. The script can:
- Test connectivity to the gateway.
- Test remote connectivity to an external IP.
- Test DNS resolution.
- Display the system's default gateway.

### Features
- Simple menu-driven interface for ease of use.
- Uses **socket** and **subprocess** modules to perform network checks.
- Detects the default gateway dynamically (for full credit per assignment requirements).
- Runs on **CentOS 8** but should work on most Linux systems.

### Prerequisites
- Python 3 installed
- **CentOS 8** or a similar Linux-based system

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/minaramez/Ping-Test-Troubleshooter.git
   cd Ping-Test-Troubleshooter
   ```
2. Ensure the script has execute permissions:
   ```bash
   chmod +x ping_test.py
   ```

### Usage
Run the script using:
```bash
./ping_test.py
```
or
```bash
python3 ping_test.py
```

Follow the on-screen menu to perform the desired network test.

### Script Options
| Option | Description |
|--------|-------------|
| 1 | Test connectivity to the gateway |
| 2 | Test remote connectivity (Google DNS 8.8.8.8) |
| 3 | Test DNS resolution (www.google.com) |
| 4 | Display the system's default gateway |
| Q/q | Exit the script |

### Example Output
```
*******PING TEST TROUBLESHOOTER*******
Enter Selection:
1 - Test connectivity to your gateway.
2 - Test for remote connectivity.
3 - Test for DNS resolution.
4 - Display gateway IP address.

Enter a number from 1 - 4, or 'Q/q' to exit: 1
Successfully connected to the gateway!
```

### License
This script is released under the **MIT License**, which allows modification, distribution, and use with minimal restrictions.
