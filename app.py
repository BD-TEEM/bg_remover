import os
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    try:
        if 'file' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['file']
        input_image = Image.open(file.stream)
        
        # AI Background Removal
        output_image = remove(input_image)
        
        img_io = io.BytesIO()
        output_image.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    # Render এর নিজস্ব পোর্ট ব্যবহারের জন্য
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
