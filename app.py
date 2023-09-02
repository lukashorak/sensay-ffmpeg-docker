from flask import Flask, request, jsonify, send_file
from datetime import datetime
from urllib.parse import urlparse
import time
import requests
import subprocess
import os
import base64


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

@app.route('/convert2', methods=['POST'])
def convert2():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Getting the current date and time
    dt = datetime.now().isoformat()
    curr_time = round(time.time()*1000)	
    
    # Download file
    ogg_file = 'input_'+str(curr_time)+'.ogg'
    mp3_file = 'output_'+str(curr_time)+'.mp3'
    
    response = requests.get(url)
    with open(ogg_file, 'wb') as f:
        f.write(response.content)

    # Run FFmpeg command to convert OGG to MP3
    command = ['ffmpeg', '-i', ogg_file, mp3_file]
    subprocess.run(command)

    # Return MP3 file
    return send_file(mp3_file,
                     mimetype='audio/mpeg',
                     as_attachment=True,
                     download_name='output.mp3')

@app.route('/convert3', methods=['GET'])
def convert3():
    #url = urlparse(request.args.get('url'))
    url = request.args.get('url')
    print('Download URL: {}'.format(url), flush=True)
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    
    # Getting the current date and time
    dt = datetime.now().isoformat()
    curr_time = round(time.time()*1000)	
    
    # Download file
    ogg_file = 'input_'+str(curr_time)+'.ogg'
    mp3_file = 'output_'+str(curr_time)+'.mp3'
    
    print('OGG -> MP3: {} - {}'.format(ogg_file, mp3_file), flush=True)
    
    response = requests.get(url)
    print('Download code: {}'.format(response.status_code), flush=True)
    with open(ogg_file, 'wb') as f:
        f.write(response.content)

    # Run FFmpeg command to convert OGG to MP3
    command = ['ffmpeg', '-i', ogg_file, mp3_file]
    subprocess.run(command)

    # Return MP3 file
    return send_file(mp3_file,
                     mimetype='audio/mpeg',
                     as_attachment=True,
                     download_name='output.mp3')

@app.route('/convert4', methods=['GET'])
def convert4():
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
    
    print('OGG -> MP3: {} - {}'.format(ogg_file, mp3_file), flush=True)
    
    response = requests.get(url)
    print('Download code: {}'.format(response.status_code), flush=True)
    with open(ogg_file, 'wb') as f:
        f.write(response.content)

    # Run FFmpeg command to convert OGG to MP3
    command = ['ffmpeg', '-i', ogg_file, mp3_file]
    subprocess.run(command)

    # Return MP3 file
    return send_file(mp3_file,
                     mimetype='audio/mpeg',
                     as_attachment=True,
                     download_name='output.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
