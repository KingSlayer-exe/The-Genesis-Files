import os
import re
import time
import random
from datetime import datetime

# === Config ===
LOG_FILE = "sample_log.log"
ALERT_FILE = "alerts.log"

# Regex patterns to detect suspicious activity
PATTERNS = {
    "failed_login": re.compile(r"FATAL: password authentication failed"),
    "db_error": re.compile(r"ERROR:"),
    "suspicious_sql": re.compile(r"(DROP TABLE|DELETE FROM)"),
}

# Predefined sample users and SQL commands for dynamic generation
USERS = ["admin", "reporting", "hacker", "intruder", "guest"]
TABLES = ["orders", "customers", "sensitive_data", "users"]

# === Utility functions ===
def log_alert(alert_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_line = f"[{timestamp}] ALERT: {alert_type} - {message}"
    print(alert_line)
    with open(ALERT_FILE, "a") as f:
        f.write(alert_line + "\n")

def incident_response(action, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Response triggered: {action} | {details}")

# === Create initial sample log ===
def create_sample_log():
    if not os.path.exists(LOG_FILE):
        sample_entries = [
            "2025-08-17 12:00:00 [1001] postgres@mydb LOG: connection authorized: user=admin",
            "2025-08-17 12:01:10 [1002] postgres@mydb FATAL: password authentication failed for user \"hacker\"",
            "2025-08-17 12:02:30 [1003] postgres@mydb ERROR: relation \"users\" does not exist",
            "2025-08-17 12:03:20 [1004] postgres@mydb LOG: SELECT * FROM customers;",
            "2025-08-17 12:06:40 [1005] postgres@mydb LOG: DELETE FROM orders WHERE id=10;",
            "2025-08-17 12:07:50 [1006] postgres@mydb LOG: DROP TABLE sensitive_data;",
        ]
        with open(LOG_FILE, "w") as f:
            for line in sample_entries:
                f.write(line + "\n")
        print(f"[+] Created {LOG_FILE} with initial sample entries")

# === Function to append random log entries ===
def append_random_log_entry():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pid = random.randint(2000, 3000)
    user = random.choice(USERS)
    choice = random.randint(1, 5)

    if choice == 1:
        # Successful login
        entry = f"{timestamp} [{pid}] postgres@mydb LOG: connection authorized: user={user}"
    elif choice == 2:
        # Failed login
        entry = f"{timestamp} [{pid}] postgres@mydb FATAL: password authentication failed for user \"{user}\""
    elif choice == 3:
        # Database error
        table = random.choice(TABLES)
        entry = f"{timestamp} [{pid}] postgres@mydb ERROR: relation \"{table}\" does not exist"
    elif choice == 4:
        # Suspicious DELETE
        table = random.choice(TABLES)
        entry = f"{timestamp} [{pid}] postgres@mydb LOG: DELETE FROM {table} WHERE id={random.randint(1,100)};"
    else:
        # Suspicious DROP
        table = random.choice(TABLES)
        entry = f"{timestamp} [{pid}] postgres@mydb LOG: DROP TABLE {table};"

    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")
    return entry

# === Main monitoring loop ===
def monitor_logs():
    create_sample_log()

    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        print(f"[+] Monitoring {LOG_FILE}...")

        while True:
            line = f.readline()
            if not line:
                # Generate a new log entry every 2 seconds
                new_entry = append_random_log_entry()
                print(f"[+] New log entry appended: {new_entry}")
                time.sleep(2)
                continue

            # Check all patterns
            for alert_type, pattern in PATTERNS.items():
                if pattern.search(line):
                    log_alert(alert_type, line.strip())
                    incident_response(f"Triggered response for {alert_type}", line.strip())

# === Entrypoint ===
def main():
    monitor_logs()

if __name__ == "__main__":
    main()


