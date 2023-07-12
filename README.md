# Flask
Windows Instructions

Repository download:
1) Download github desktop https://desktop.github.com/
2) Open github desktop and go to file > clone repository
3) Click url and paste this url https://github.com/athePTC/Flask.git and hit clone

Python Download:
https://www.python.org/downloads/release/python-380/ Scroll to the bottom and download the Windows x86-64 web-based installer.

Blender Download:
https://www.blender.org/download/releases/3-5/

How to add blender to environment variable path:
1) In the windows task bar search "Edit environment variables for your account"
2) Double click on "Path"
3) Press new and type the path that leads to blender on your folder. Ex. "C:\Program Files\Blender Foundation\Blender 3.5"

Instructions to run:
1) Download python & Blender 3.5. Make sure blender is added to your environment variable path.

2) Enter the terminal in the folder of the flask app.

3) Type "python -m venv env" to create the virtual environment

4) Type ".\env\Scripts\activate" to actiate the virtual environment

5) Type "pip install -r requirements.txt" to install the dependencies

6) Type "python app.py" to run the app

Notes:
1) Differnet versions of python will sometimes require you to type "py" or "python3" and "pip3" instead of python/pip respectively.

Using the app:
1) Open up the website after running the app and pick an image file on your computer to create a logo.
2) It will take several seconds to process everything.
3) Once done you will automatically download an .fbx file which will be the 3d logo you can put into a scene.