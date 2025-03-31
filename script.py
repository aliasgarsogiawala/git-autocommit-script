#Use this script if you wanna switch to local mode
# import os
# import time
# from datetime import datetime
# import subprocess

# # Config
# REPO_PATH = os.path.expanduser("~/Desktop/git-autocommit-script")
# FILENAME = "commits.txt"

# def append_line():
#     file_path = os.path.join(REPO_PATH, FILENAME)
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
#     line = f"Commit made automatically on {now}\n"

#     with open(file_path, "a") as file:
#         file.write(line)

# def git_commit_push():
#     os.chdir(REPO_PATH)

#     subprocess.run(["git", "add", "."], check=True)
#     commit_msg = f"Auto commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST"
#     subprocess.run(["git", "commit", "-m", commit_msg], check=True)
#     subprocess.run(["git", "push", "origin", "main"], check=True)

# def main():
#     print("Starting Git auto-commit script... Waiting for 12 AM IST each day.")

#     while True:
#         now = datetime.now()
#         if now.hour == 0 and now.minute == 0:
#             print(f"Running auto-commit at {now.strftime('%Y-%m-%d %H:%M:%S')} IST")
#             try:
#                 append_line()
#                 git_commit_push()
#                 print("Commit successful! Waiting until tomorrow...")
#             except Exception as e:
#                 print(f"An error occurred: {e}")

#             time.sleep(61)
#         else:
#             time.sleep(30)

# if __name__ == "__main__":
#     main()
