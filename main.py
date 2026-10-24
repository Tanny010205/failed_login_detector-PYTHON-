
from collections import Counter

LOG_FILE = "sample_logs.txt"
THRESHOLD = 3


def analyze_logs():
    failed_attempts = Counter()

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for line in file:
                if "FAILED_LOGIN" in line:
                    for item in line.split():
                        if item.startswith("ip="):
                            ip_address = item.split("=", 1)[1]
                            failed_attempts[ip_address] += 1

    except FileNotFoundError:
        print("Error: Log file not found!")
        return

    print("\n===== FAILED LOGIN REPORT =====")

    if not failed_attempts:
        print("No failed login attempts found.")
        return

    for ip, count in failed_attempts.items():
        print(f"IP Address: {ip} | Failed Attempts: {count}")

        if count >= THRESHOLD:
            print("WARNING: Suspicious repeated login attempts!")


if __name__ == "__main__":
    analyze_logs()
