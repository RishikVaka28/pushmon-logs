# 🚀 PushMon: GitHub Streak Keeper + System Monitor

**PushMon** is a lightweight Python-based tool that:
- Monitors system performance (CPU, memory)
- Logs the data locally
- Automatically commits and pushes updates to GitHub
- ✅ Keeps your GitHub streak alive, even on busy days

---

## 🔧 Features

- 📈 Tracks CPU and memory usage using `psutil`
- 🕒 Scheduled logging using `schedule` or `cron`
- 🔄 GitHub integration with `git add/commit/push`
- 💡 Smart commit detection (avoids "nothing to commit" errors)
- 🔐 Supports HTTPS and SSH Git remotes
- 🛠 Easily configurable with `config.yaml`

---

## 🛠 Technologies Used

- Python 3
- `psutil`, `schedule`, `PyYAML`
- Git (CLI)
- Optional: Docker, Cron, Flask (for future UI)
