from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Ambil pesan dari pengguna
    user_message = data.get("messages", [{}])[0].get("text", {}).get("body", "Tidak ada pesan")
    # Respon sederhana
    response_message = f"Kamu bilang: {user_message}"
    return jsonify({"text": response_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
