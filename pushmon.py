# Libraries
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
    if config.get('auto_push', False):
        try:
            # Stage changes
            subprocess.run(["git", "add", "."], check=True)
            
            # Commit if there are actual changes
            result = subprocess.run(
                ["git", "diff", "--cached", "--quiet"]
            )
            if result.returncode == 1:
                subprocess.run(["git", "commit", "-m", config['commit_message']], check=True)
                subprocess.run(["git", "push"], check=True)
                print("Changes pushed to GitHub.")
            else:
                print("No new changes to commit.")
        except subprocess.CalledProcessError as e:
            print("Git error:", e)

# Schedule job
interval = config.get('check_interval', 5)
schedule.every(interval).minutes.do(log_activity)

print(f"[INFO] Starting System Monitor Logger every {interval} minutes.")
log_activity()  # Run once immediately

# Main loop
while True:
    schedule.run_pending()
    time.sleep(1)