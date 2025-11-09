import os
<<<<<<< HEAD
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
=======
import datetime
from git import Repo

# Path to your local repository
repo_path = "C:/Users/HARISH KUMAR V/Sample"
repo = Repo(repo_path)

# Starting and ending dates
start_date = datetime.date(2024, 9, 26)
end_date = datetime.date(2024, 11, 9)

# Pattern of commits: 4, 8, 6, 4, 8 repeating
pattern = [4, 8, 6, 4, 8]
pattern_index = 0

# Generate commits day by day
current_date = start_date
while current_date <= end_date:
    num_commits = pattern[pattern_index % len(pattern)]
    pattern_index += 1

    for i in range(num_commits):
        filename = os.path.join(repo_path, "log.txt")

        with open(filename, "a") as file:
            file.write(f"Commit made on {current_date}, commit {i+1}\n")

        # Format date correctly for Git
        date_str = current_date.strftime("%Y-%m-%dT12:00:00")

        repo.index.add([filename])
        repo.index.commit(
            f"Commit for {current_date} #{i+1}",
            author_date=date_str,
            commit_date=date_str
        )

    current_date += datetime.timedelta(days=1)

print("✅ Commits generated successfully from 26 Sep to 9 Nov!")
>>>>>>> 3a703af (Added commit generator script)
