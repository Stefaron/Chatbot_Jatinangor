from flask import Flask, request, jsonify, send_from_directory
import aiml
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Buat kernel AIML dan pelajari berkas AIML
kernel = aiml.Kernel()
kernel.learn("start.xml")
kernel.respond("aiml a")

# Variabel untuk menyimpan pesan terakhir yang diterima
last_user_input = ""

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/get', methods=['POST'])
def get_response():
    global last_user_input
    user_input = request.json.get('user_input')
    # Check if the new message is different from the last one
    if user_input != last_user_input:
        logging.debug(f"User input : {user_input}")
        response = kernel.respond(user_input)
        logging.debug(f"respons aiml: {response}")
        if not response:
            response = "Maaf, saya kurang mengerti."
        last_user_input = user_input
    else:
        response = "Maaf, saya sudah memproses pesan sebelumnya."
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
