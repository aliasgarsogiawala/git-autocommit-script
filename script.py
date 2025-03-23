import os
from datetime import datetime
import subprocess

# Config
REPO_PATH = "~/Desktop/git-autocommit-script" 
FILENAME = "commits.txt"         
def append_line():
    file_path = os.path.join(REPO_PATH, FILENAME)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    line = f"Commit made automatically on {now}\n"

    # Append to the file
    with open(file_path, "a") as file:
        file.write(line)

def git_commit_push():
    # Change to your repo directory
    os.chdir(REPO_PATH)

    # Git commands
    subprocess.run(["git", "add", FILENAME], check=True)
    commit_msg = f"Auto commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)  # Change 'main' to your branch if different

def main():
    append_line()
    git_commit_push()

if __name__ == "__main__":
    main()
