
import json
import os
import urllib.parse
import urllib.request

def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    message = "Halo Bro Haz! 🚀 Bot automation kamu berhasil berjalan."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": message,
    }).encode()

    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read())

    if not result.get("ok"):
        raise RuntimeError(f"Telegram API error: {result}")

    print("Pesan berhasil dikirim ke Telegram!")

if __name__ == "__main__":
    main()
