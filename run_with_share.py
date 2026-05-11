"""
run_with_share.py
=================
Starts Defect Tracker Pro AND creates a public HTTPS link for your team
using pyngrok — no separate ngrok download needed.

HOW TO USE
----------
1. Install dependencies once:
       pip install pyngrok flask flask-login psycopg2-binary werkzeug openpyxl

2. (Optional but recommended) Set your free ngrok authtoken so tunnels last longer:
       python run_with_share.py --set-token YOUR_TOKEN_HERE
   Get a free token at: https://dashboard.ngrok.com/get-started/your-authtoken

3. Run the app with public sharing:
       python run_with_share.py

4. Share the printed HTTPS link with your team.
   The link changes every time you restart (unless you use an ngrok paid plan).

NOTE: pyngrok downloads its own ngrok binary on first run (~20 MB, one-time only).
"""

import sys
import os
import threading
import time
import socket

# ── Optional: set authtoken from command line ─────────────────────
if '--set-token' in sys.argv:
    try:
        from pyngrok import ngrok, conf
        token = sys.argv[sys.argv.index('--set-token') + 1]
        ngrok.set_auth_token(token)
        print(f"[OK] ngrok authtoken saved: {token[:8]}...")
        sys.exit(0)
    except IndexError:
        print("[ERROR] Usage: python run_with_share.py --set-token YOUR_TOKEN")
        sys.exit(1)
    except ImportError:
        print("[ERROR] pyngrok not installed. Run: pip install pyngrok")
        sys.exit(1)

PORT = 5002

# ── Get local IP for LAN link ──────────────────────────────────────
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# ── Start ngrok tunnel ────────────────────────────────────────────
def start_ngrok(port):
    try:
        from pyngrok import ngrok, conf, exception as ngrok_exc

        # Use a persistent log file so errors are visible
        conf.get_default().log_event_callback = None  # silence verbose logs

        print("\n[ngrok] Opening public tunnel...")
        tunnel = ngrok.connect(port, "http")
        public_url = tunnel.public_url

        # ngrok always gives http:// — upgrade to https:// automatically
        if public_url.startswith("http://"):
            public_url = "https://" + public_url[7:]

        return public_url

    except ImportError:
        print("\n[WARNING] pyngrok not installed.")
        print("  Run:  pip install pyngrok")
        print("  Then restart this script.\n")
        return None
    except Exception as e:
        err = str(e)
        if "authtoken" in err.lower() or "ERR_NGROK_105" in err or "402" in err:
            print("\n[ngrok] Free session limit reached or authtoken needed.")
            print("  1. Sign up free at https://ngrok.com")
            print("  2. Get your token at https://dashboard.ngrok.com/get-started/your-authtoken")
            print(f"  3. Run: python run_with_share.py --set-token YOUR_TOKEN\n")
        else:
            print(f"\n[ngrok] Could not start tunnel: {e}\n")
        return None

# ── Print the share banner ─────────────────────────────────────────
def print_banner(local_ip, public_url):
    print()
    print("=" * 62)
    print("  🏭  DEFECT TRACKER PRO  —  RUNNING")
    print("=" * 62)
    print(f"  📍 Local (this PC)  :  http://127.0.0.1:{PORT}")
    print(f"  🌐 LAN  (same WiFi) :  http://{local_ip}:{PORT}")
    if public_url:
        print(f"  🔗 PUBLIC (internet):  {public_url}")
        print()
        print("  ✅ Share the PUBLIC link with your team.")
        print("  ✅ Works on mobile, tablet, and PC worldwide.")
        print("  ⚠️  Link is active while this window stays open.")
    else:
        print()
        print("  ℹ️  Public link unavailable — see warning above.")
        print("  ✅ LAN link still works for devices on same network.")
    print("=" * 62)
    print("  Press Ctrl+C to stop the server.")
    print("=" * 62)
    print()

# ── Run Flask in background thread ───────────────────────────────
def run_flask():
    # Import app here so ngrok starts before Flask prints its own banner
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'   # suppress double-startup message
    from app import app
    app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)

# ── Main ──────────────────────────────────────────────────────────
if __name__ == '__main__':
    local_ip   = get_local_ip()
    public_url = start_ngrok(PORT)

    # Start Flask in a daemon thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Give Flask a moment to bind
    time.sleep(1.5)

    print_banner(local_ip, public_url)

    # Keep main thread alive (Ctrl+C will kill everything cleanly)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Stopped] Defect Tracker shut down.")
        try:
            from pyngrok import ngrok
            ngrok.kill()
        except Exception:
            pass
