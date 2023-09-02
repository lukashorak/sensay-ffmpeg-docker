from flask import Flask, request, jsonify, send_file
from datetime import datetime
from urllib.parse import urlparse
import time
import requests
import subprocess
import os
import base64


app = Flask(__name__)


@app.route('/convert4', methods=['GET'])
def convert4():
    startTime = datetime.now()
    #url = urlparse(request.args.get('urlB64'))
    url = base64.b64decode(request.args.get('urlB64'))
    print('Download URL: {}'.format(url), flush=True)
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    
    # Getting the current date and time
    dt = datetime.now().isoformat()
    curr_time = round(time.time()*1000)	
    
    # Download file
    ogg_file = 'input_'+str(curr_time)+'.ogg'
    mp3_file = 'output_'+str(curr_time)+'.mp3'
    
    
    
    response = requests.get(url)
    print('Download code: {}'.format(response.status_code), flush=True)
    with open(ogg_file, 'wb') as f:
        f.write(response.content)

    # Run FFmpeg command to convert OGG to MP3
    command = ['ffmpeg','-loglevel', 'error', '-i', ogg_file, mp3_file]
    subprocess.run(command)


    endTime = datetime.now()
    delta = int((endTime - startTime).total_seconds() * 1000)
    print('OGG -> MP3: {} - {} - {}'.format(ogg_file, mp3_file, delta), flush=True)
    # Return MP3 file
    return send_file(mp3_file,
                     mimetype='audio/mpeg',
                     as_attachment=True,
                     download_name='output.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
