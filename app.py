from flask import Flask, request, jsonify  # redirect, url_for
from ver import verify_v2

import tempfile
import os
import soundfile

UPLOAD_FOLDER = "./"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
def index():
  return '<-- thefury speaker reco system -->'


@app.route('/spr-reco', methods=['POST',"GET"])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
            
            data = file.read()
            temp_file.write(data)
            
        try:
            ver = verify_v2(temp_file.name)
            return str(ver) 
        except soundfile.LibsndfileError:
            return 'Error: Invalid WAV file format.', 400
       # return 'File uploaded successfully.'
    return '''
      <!doctype html>
      <title>Upload new File</title>
      <h1>Upload new File</h1>
      <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
      </form>
      '''



if __name__ == '__main__':
  app.run(debug=True)
#  web.run(app)
