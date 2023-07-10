from flask import Flask, render_template, request, send_file
from apiTest import download_svg_from_image
import subprocess as sp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle the image submission
        image = request.files['image']
        filename = download_svg_from_image(image)
        if filename is not None and filename is not False:
            output_folder = os.path.join(app.root_path)
            sp.call(['blender', '--background', '--python', 'importSVG.py', filename + '.svg', app.root_path, output_folder])
            return send_file(os.path.join(output_folder, filename + '.fbx'), as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)