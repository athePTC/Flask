import os
import requests

def download_svg_from_image(image_file):
    filename = os.path.splitext(image_file.filename)[0]  # Get the name of the uploaded file without the extension
    svg_filename = f"{filename}.svg"  # Append .svg extension to the filename

    response = requests.post(
        'https://vectorizer.ai/api/v1/vectorize',
        files={'image': image_file},
        data={
            # TODO: Add more upload options here
        },
        headers={
            'Authorization':
            'Basic dmtuZnF5OXRkZjU1Z3pkOjE2bjR2OWI0MmtzZ3V1MmtsbmpmZzI3NGtqZGowc2g1czV2cG9hb2F0bDEzZDE4NjZqa3U='
        },
        verify=False
    )

    if response.status_code == requests.codes.ok:
        # Save the SVG result with the desired filename
        with open(svg_filename, 'wb') as out:
            out.write(response.content)

        return filename
    else:
        print("Error:", response.status_code, response.text)
        return False
