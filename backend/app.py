from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import io
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def compress_image(image_data, quality=85):
    """Compress image while maintaining aspect ratio"""
    img = Image.open(io.BytesIO(image_data))
    
    # Convert to RGB if image is in RGBA mode
    if img.mode in ('RGBA', 'LA'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])
        img = background
    
    # Save compressed image to bytes
    output = io.BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)
    output.seek(0)
    
    return output.getvalue()

@app.route('/api/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        # Read image data
        image_data = file.read()
        original_size = len(image_data)
        
        # Compress image
        compressed_data = compress_image(image_data)
        compressed_size = len(compressed_data)
        
        # Save compressed image temporarily
        filename = secure_filename(file.filename)
        compressed_path = os.path.join(UPLOAD_FOLDER, f'compressed_{filename}')
        with open(compressed_path, 'wb') as f:
            f.write(compressed_data)
        
        return jsonify({
            'message': 'Image compressed successfully',
            'original_size': original_size,
            'compressed_size': compressed_size,
            'compression_ratio': round((1 - compressed_size / original_size) * 100, 2),
            'filename': f'compressed_{filename}'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/<filename>')
def download_file(filename):
    try:
        return send_file(
            os.path.join(UPLOAD_FOLDER, filename),
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000) 