from flask import Flask, request, jsonify
from datetime import datetime
import requests
import subprocess
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

	# Getting the current date and time
	dt = datetime.now().isoformat()
	
    # Download file
    ogg_file = 'input'+str(dt)+'.ogg'
	mp3_file = 'output'+str(dt)+'.mp3'
    
    response = requests.get(url)
    with open(ogg_file, 'wb') as f:
        f.write(response.content)

    # Run FFmpeg command to convert OGG to MP3
    command = ['ffmpeg', '-i', ogg_file, mp3_file]
    subprocess.run(command)

    # TODO: Return MP3 file or its URL
    return jsonify({'message': 'File converted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
