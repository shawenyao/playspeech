from server_config import server_port, dir
from flask import *
from gtts import gTTS 
from datetime import datetime
from waitress import serve
import os

os.chdir(dir)

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    text = request.get_json().get("text")

    speech = gTTS(text=text, lang="en", slow=False) 
    
    file = f"{datetime.now().timestamp()}.mp3"
    speech.save(f"{dir}/temp/{file}")
    os.rename(f"{dir}/temp/{file}", f"{dir}/unplayed/{file}")

    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}\t {text}")
    
    response = {"status": "success"}
    return jsonify(response), 200

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=server_port)
