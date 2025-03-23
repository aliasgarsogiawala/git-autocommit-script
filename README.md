# 🚀 Git Auto Commit Script

Automatically keep your GitHub streak alive—without lifting a finger!

This Python script automates Git commits by appending a line to a file and pushing it to your GitHub repository every night at 12 AM IST. Perfect for maintaining your contribution streak even when you're busy (or asleep 😴)!

## ✨ Features

- ✅ Runs indefinitely and waits for the perfect time to commit
- ✅ Appends a timestamp entry to commits.txt automatically
- ✅ Commits and pushes changes to GitHub every single night
- ✅ Easy to set up, no crontab or external tools required
- ✅ Perfect for automation nerds, developers, and streak warriors

## 🛠️ How It Works

This script runs in an infinite loop, checking your system time.
When the clock strikes 12:00 AM IST, it:
- Appends a line with the current timestamp to commits.txt
- Commits the change with a descriptive message
- Pushes the commit to your GitHub repo on the main branch
- Waits until the next day before repeating the cycle

## 📂 Project Structure

git-autocommit-script/

├── commits.txt          // The file that gets updated daily

├── script.py            // The Python auto-commit script

└── README.md            // You're reading it!

## 🚀 Getting Started

### 1. Clone this repo or create your own

```bash
git clone https://github.com/your-username/git-autocommit-script.git
cd git-autocommit-script 
``` 

### 2. Edit REPO_PATH (if needed)
Inside `script.py`:

Make sure it points to the directory where your `commits.txt` file lives.

### 3. Make sure Git is set up
Ensure:

- You are on the correct branch (`main` or adjust in `git_commit_push()`)
- Git credentials/SSH keys are working so `git push` doesn't prompt for a password

### 4. Run the script
```bash
python3 script.py
