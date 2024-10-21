import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

# Presentation parameters
width, height = 1280, 720
folderpath = "presentation"
pathimages = sorted(os.listdir(folderpath), key=len)
imgnumber = 0
hs, ws = int(120 * 1), int(213 * 1)
gesturethreshold = 500

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

@app.route('/images', methods=['GET'])
def get_image():
    global imgnumber
    if 0 <= imgnumber < len(pathimages):
        pathFullImage = os.path.join(folderpath, pathimages[imgnumber])
        return send_file(pathFullImage)
    return jsonify({"error": "Image not found"}), 404

@app.route('/gesture', methods=['POST'])
def handle_gesture():
    global imgnumber
    data = request.json
    action = data.get('action')

    if action == 'next' and imgnumber < len(pathimages) - 1:
        imgnumber += 1
    elif action == 'previous' and imgnumber > 0:
        imgnumber -= 1
    
    return jsonify({"current_image": pathimages[imgnumber]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
