import psutil
import time
import os
import subprocess
import schedule
import yaml
from datetime import datetime

# Load config
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

log_file = config['log_file']

def log_activity():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_line = f"{timestamp} | CPU: {cpu}% | RAM: {memory}%\n"
    print(log_line.strip())

    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, 'a') as f:
        f.write(log_line)

    # Git push logic
    if config['auto_push']:
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", config['commit_message']], check=True)
            subprocess.run(["git", "push"], check=True)
        except subprocess.CalledProcessError as e:
            print("Git error:", e)

# Schedule it
schedule.every(config['check_interval']).minutes.do(log_activity)

print(f"Starting System Monitor Logger every {config['check_interval']} minutes.")
log_activity()  # run once at start

while True:
    schedule.run_pending()
    time.sleep(1)
