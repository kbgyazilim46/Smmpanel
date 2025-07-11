from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# 🔐 Telegram Bilgilerini BURAYA GİR
BOT_TOKEN = "8103484229:AAFn_a84yjG2Ed2LDWDLFULoFPKljtySEe0"
CHAT_ID = "5356846993"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Kimsebaşgöz SMM Panel</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 30px; background-color: #f7f7f7; }
        h1, h2 { color: #333; }
        .box { background: white; padding: 20px; border-radius: 10px; max-width: 500px; margin: auto; }
        label { display: block; margin-top: 10px; }
        input, select, textarea { width: 100%; padding: 8px; margin-top: 5px; }
        button { margin-top: 15px; padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; }
        .success { color: green; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Kimsebaşgöz SMM Panel</h1>

        {% if message %}
            <div class="success">{{ message }}</div>
        {% endif %}

        <h2>Hizmetler</h2>
        <ul>
            <li>Instagram Takipçi - 10₺ / 1000</li>
            <li>Instagram Beğeni - 5₺ / 1000</li>
            <li>YouTube İzlenme - 8₺ / 1000</li>
        </ul>

        <h2>Sipariş Formu</h2>
        <form method="POST">
            <label>Hizmet:</label>
            <select name="service" required>
                <option value="Instagram Takipçi">Instagram Takipçi</option>
                <option value="Instagram Beğeni">Instagram Beğeni</option>
                <option value="YouTube İzlenme">YouTube İzlenme</option>
            </select>

            <label>Link / Kullanıcı Adı:</label>
            <input type="text" name="link" required>

            <label>Miktar:</label>
            <input type="number" name="amount" required>

            <label>E-posta (isteğe bağlı):</label>
            <input type="email" name="email">

            <button type="submit">Sipariş Ver</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        service = request.form.get("service")
        link = request.form.get("link")
        amount = request.form.get("amount")
        email = request.form.get("email") or "Belirtilmedi"

        # 📨 Telegram mesajı
        msg = f"📩 Yeni Sipariş!\n\n📌 Hizmet: {service}\n🔗 Link: {link}\n🔢 Miktar: {amount}\n✉️ E-posta: {email}"
        send_telegram(msg)

        message = "✅ Sipariş başarıyla alındı!"

    return render_template_string(HTML_PAGE, message=message)