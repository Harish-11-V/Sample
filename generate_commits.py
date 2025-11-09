import os
import subprocess
from datetime import datetime, timedelta

# === CONFIGURATION ===
start_date = datetime(2024, 9, 26)
end_date = datetime(2024, 11, 9)
pattern = [4, 8, 6]  # repeating pattern
repo_path = r"C:\Users\HARISH KUMAR V\Sample"  # your local repo path
message_base = "Daily Commit Simulation"

os.chdir(repo_path)

current_date = start_date
pattern_index = 0

while current_date <= end_date:
    commits_today = pattern[pattern_index % len(pattern)]
    pattern_index += 1

    for i in range(commits_today):
        with open("streak.txt", "a") as f:
            f.write(f"{current_date.date()} - Commit {i+1}\n")

        subprocess.run(["git", "add", "streak.txt"])
        subprocess.run([
            "git", "commit", "--date", current_date.strftime("%Y-%m-%dT12:00:%S"),
            "-m", f"{message_base} on {current_date.date()} #{i+1}"
        ])

    current_date += timedelta(days=1)

# Finally push all commits
subprocess.run(["git", "push", "-u", "origin", "main"])
