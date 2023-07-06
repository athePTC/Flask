from flask import Flask, render_template, request, send_file
from apiTest import download_svg_from_image
import subprocess as sp
import os
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle the image submission
        image = request.files['image']
        filename = download_svg_from_image(image)
        if filename is not None and filename is not False:
            output_folder = os.path.join(app.root_path, "Logos")
            sp.call(['blender', '--background', '--python', 'importSVG.py', filename + '.svg', app.root_path, output_folder])
            return send_file(os.path.join(output_folder, filename + '.fbx'), as_attachment=True)
    return render_template('index.html')

def get_open_port():
    """
    Find an available port by attempting to bind to a socket with port 0.
    Returns the port number if successful, or None if no port is available.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        _, port = sock.getsockname()
        sock.close()
        return port
    except OSError:
        return None

if __name__ == '__main__':
    port = get_open_port()
    if port is None:
        print("No available port found.")
    else:
        app.run(host='0.0.0.0', port=port)