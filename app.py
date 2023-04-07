from flask import Flask, request  #redirect, url_for
from ver import verify
#from flask import Flask, flash, request, redirect, url_for
#from replit import web
#from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "./"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
  return '<-- thefury speaker reco system -->'


@app.route('/spr-reco', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    #filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "t.wav"))
    v = verify()
    return str(v)  #redirect(url_for('down', name=filename))
  return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
    </form>
    '''


#if __name__ == '__main__':
#  #app.run(debug=True)
#  web.run(app)
