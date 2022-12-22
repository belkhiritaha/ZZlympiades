from flask import Flask, request
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import os
import requests

app = Flask(__name__, static_url_path='/static')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
     return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def insertWaterMark(filename):
    try:
        # Open the meme image
        img = Image.open(filename).convert("RGBA")
        # Open the watermark image
        watermark = Image.open('static/assets/4gagLogo.png').convert("RGBA")
        # Get image size
        imgWidth, imgHeight = img.size
        # Resize watermark
        watermark = watermark.resize((int(imgWidth/4), int(imgHeight/4)))
        # Get watermark size
        watermarkWidth, watermarkHeight = watermark.size
        # Paste the watermark
        img.paste(watermark, (imgWidth - watermarkWidth, imgHeight - watermarkHeight), watermark)
        # Save the image
        newFilename = filename.rsplit('/', 1)[1]
        newFilename = 'static/memes/ZZ' + newFilename
        # Convert to RGB to avoid problems with non-PNG files
        img = img.convert("RGB")
        img.save(newFilename)

        print("New filename: ", newFilename)
        return {'status': 'success', 'image': f'static/memes/{newFilename}'}, 200

    except:
        print("Error")
        return {'status': 'failed', 'message': 'Something went wrong'}, 500


def getUpload():
    uploads = []
    for filename in os.listdir('static/uploads/'):
        if allowed_file(filename):
            print(filename + " is allowed")
            uploads.append(filename)
    return uploads


def getMemes():
    memes = []
    for filename in os.listdir('static/memes/'):
        if allowed_file(filename):
            print(filename + " is allowed")
            memes.append(filename)
    return memes


def editHTML(memes : list):
    # Load file and parse with BeautifulSoup
    html = open("src/index.html")
    print("HTML loaded")
    soup = BeautifulSoup(html, "html.parser")
    print("HTML parsed")
    for meme in memes:
        # Create a new div
        newDiv = soup.new_tag("div", **{"class": "meme"})
        # Create a new img tag
        newImg = soup.new_tag("img")
        # Set the src of the img tag
        newImg['src'] = f'static/memes/{meme}'
        # Add the img tag to the div
        newDiv.append(newImg)
        # Add the div to the memes div
        soup.find(id="memes").append(newDiv)
        
    # Write the new HTML to new file
    with open("output.html", "w") as file:
        file.write(str(soup))

    return str(soup)
    

@app.route('/')
def main():
    uploads = getUpload()
    for upload in uploads:
        insertWaterMark('static/uploads/' + upload)

    memes = getMemes()
    html = editHTML(memes)
    return html


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print("POST request")
        f = request.files['fileToUpload']
        print("File: ", f)
        f.save('static/uploads/' + f.filename)
        return 'file uploaded successfully, redirecting you shortly... <script>setTimeout(function(){window.location.href = "/";}, 2000);</script>'
    else:
        return 'something went wrong, redirecting you shortly... <script>setTimeout(function(){window.location.href = "/";}, 2000);</script>'


@app.route('/flag')
def flag():
    # if theres a file called showflag.txt, return the flag
    if os.path.isfile('showflag.txt'):
        return open('flag.txt').read()
    else:
        return 'No flag for you!'