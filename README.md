# Flask
Windows Instructions

Python Download:
https://www.python.org/downloads/release/python-380/ Scroll to the bottom and download the Windows x86-64 web-based installer.

Blender Download:
https://www.blender.org/download/releases/3-5/

How to add blender to environment variable path:
In the windows task bar search "Edit environment variables for your account"
Double click on "Path"
Press new and type the path that leads to blender on your folder. Ex. "C:\Program Files\Blender Foundation\Blender 3.5"

Instructions to run:
1) Download python & Blender 3.5. Make sure blender is added to your environment variable path.

2) Enter the terminal in the folder of the flask app.

3) Type "python -m venv env" to create the virtual environment

4) Type ".\env\Scripts\activate" to actiate the virtual environment

5) Type "pip install -r requirements.txt" to install the dependencies

6) Type "python app.py" to run the app

Notes:
Differnet versions of python will sometimes require you to type "py" or "python3" and "pip3" instead of python/pip respectively.