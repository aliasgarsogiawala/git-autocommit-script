# 🚀 Git Auto Commit Script
[![Auto Commit](https://github.com/aliasgarsogiawala/git-autocommit-script/actions/workflows/autocommit.yml/badge.svg)](https://github.com/aliasgarsogiawala/git-autocommit-script/actions/workflows/autocommit.yml)


Automatically keep your GitHub streak alive—without lifting a finger!

This  script automates Git commits by appending a line to a file and pushing it to your GitHub repository every morning at 10 AM IST. Perfect for maintaining your contribution streak even when you're busy (or asleep 😴)!

## ✨ Features

- ✅ Runs indefinitely and waits for the perfect time to commit
- ✅ Appends a timestamp entry to commits.txt automatically
- ✅ Commits and pushes changes to GitHub every single day
- ✅ Easy to set up using github actions or locally with python script.
- ✅ Perfect for automation nerds, developers, and streak warriors

## 🛠️ How It Works

This workflow uses github actions checking the time.
When the clock strikes 10:00 AM IST, it:
- Appends a line with the current timestamp to commits.txt
- Commits the change with a descriptive message
- Pushes the commit to your GitHub repo on the main branch
- Waits until the next day before repeating the cycle


## 🚀 Getting Started

### 1. Clone this repo or create your own

```bash
git clone https://github.com/aliasgarsogiawala/git-autocommit-script.git
cd git-autocommit-script 
``` 

### 2. Edit the workflow autocommit.yml



## 🧰 Requirements
- Git installed and configured

<!-- ## 🌐 Pro Tips
Want this script to run **24/7** without keeping your laptop on?

👉 Deploy it on a **VPS** (DigitalOcean, AWS EC2)  
👉 OR use **GitHub Actions** for serverless automation (check the Actions example in this repo) -->

## 📜 License
MIT License. Use it, tweak it, automate your life.

## ✨ Author
👨‍💻 **Aliasgar Sogiawala**  

Built for **automation lovers** and **GitHub streak warriors** 🔥  

Feel free to connect!
