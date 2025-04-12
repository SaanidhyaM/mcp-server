from flask import Flask, request, jsonify
from voice_cloning import clone_voice
from error_handling import log_exception

app = Flask(__name__)

@app.route('/clone', methods=['POST'])
def clone():
    try:
        data = request.json
        text = data['text']
        voice_id = data['voice_id']
        api_key = data['api_key']

        path = clone_voice(text, voice_id, api_key)
        if path:
            return jsonify({"success": True, "file_path": path})
        else:
            return jsonify({"success": False, "error": "Voice cloning failed"}), 500

    except Exception as e:
        log_exception(e, "Error in /clone endpoint")
        return jsonify({"success": False, "error": "Internal Server Error"}), 500
    
if __name__ == '__main__':
    print("Server is starting...")
    app.run(port=5050)

