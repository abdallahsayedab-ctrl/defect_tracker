# Defect Tracker Pro — Public Share Setup

## Quick Start (Share with Team)

### Option A — Double-click (Windows)
Just double-click **`run_tracker.bat`**
- It installs everything automatically
- Prints a public HTTPS link you can share

### Option B — Command line
```
pip install -r requirements.txt
python run_with_share.py
```

---

## First-Time Setup (Stable Links — Recommended)

Without an authtoken, ngrok links expire after a few hours.
To get a free persistent tunnel:

1. Sign up free at **https://ngrok.com**
2. Go to **https://dashboard.ngrok.com/get-started/your-authtoken**
3. Copy your token, then run once:
   ```
   python run_with_share.py --set-token_TOKEN3DWP3VmgGYPBG5oLAwc9UPCY43h_4vEreBw1U8uNDj7QzyUBu_
   ```
4. From now on, just run `run_tracker.bat` normally.

---

## What Your Team Sees

When you run the app, you get 3 links:

| Link | Who can use it |
|------|---------------|
| `http://127.0.0.1:5002` | Only you (this PC) |
| `http://YOUR-LAN-IP:5002` | Anyone on same WiFi/LAN |
| `https://xxxx.ngrok-free.app` | **Anyone worldwide** ✅ |

Send the **PUBLIC** link to your team. They can open it on any browser.

---

## Notes

- **The public link changes every restart** (unless you use ngrok paid plan with a fixed domain)
- **Keep the window open** while your team uses the app — closing it stops everything
- pyngrok downloads its own ngrok binary (~20 MB) on first run — internet required once
- Your database stays local on your PC — nothing is uploaded to the cloud

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `pyngrok not installed` | Run `pip install pyngrok` |
| `authtoken` error | Follow the "Stable Links" steps above |
| App loads but no data | Make sure PostgreSQL is running |
| Team gets "site not found" | Check the window is still open |
