from flask import Flask, flash, request, redirect, make_response
import csv
import io
import csv_parser
from ingredient import Ingredient

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Initialize a string-type object to write bytes into
            file_contents_str = request.files['file'].read().decode("utf-8", "strict")
            fake_file =  io.StringIO(file_contents_str,newline='')
            pantry_list = csv_parser.parse(fake_file)
            list_string = ''
            for i in range(0,len(pantry_list)):
                list_string = list_string + Ingredient.to_instructions(pantry_list[i]) + '\n'
            response = make_response(list_string,200)
            response.mimetype = 'text/plain'
            return response

    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form> """

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)