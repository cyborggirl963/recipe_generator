from flask import Flask, flash, request, redirect, make_response, url_for, send_file
import csv
import io
import csv_parser
from ingredient import Ingredient
import cake_recipe as c

uploaded_ingredients_csv = None

def set_uploaded_ingredients_csv(new_value):
    global uploaded_ingredients_csv
    uploaded_ingredients_csv = new_value
def get_uploaded_ingredients_csv():
    return uploaded_ingredients_csv

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
            set_uploaded_ingredients_csv(file_contents_str)
            return redirect(url_for('upload_success'))

    return """
    <!doctype html>
    <h1>Recipe Generator</h1>
    <p>This app lets you upload a list of everything in your pantry, and then generates WEIRD CAKE RECIPES.</p>
    <p>You can download the csv template for entering ingredients from the link below.</p>
    <a href="/download"><button type="submit">Download template</button></a>
    <h2>Upload new File</h2>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form> """

@app.route('/download')
def downloadFile ():
    path = "template.csv"
    return send_file(path, as_attachment=True)

@app.route('/upload_success')
def upload_success():
    fake_file =  io.StringIO(uploaded_ingredients_csv,newline='')
    pantry_list = csv_parser.parse(fake_file)
    list_string = '<h1>Your ingredients:</h1><ul>'
    for i in range(0,len(pantry_list)):
        list_string = list_string + '<li>'+ Ingredient.to_instructions(pantry_list[i]) + '</li>'
    list_string = list_string + '</ul>' 
    list_string = list_string + '''<a href="generate">
        <button type="submit">Looks good!</button> 
    </form> '''
    response = make_response(list_string,200)
    #<form>%s</form>' % 
    #response.mimetype = 'text/html'
    return response

@app.route('/generate')
def generate():
    fake_file =  io.StringIO(uploaded_ingredients_csv,newline='')
    pantry_list = csv_parser.parse(fake_file)
    cake = c.cake_generator(pantry_list)
    ingredients = c.Cake_Recipe.return_ingredients(cake)
    print('Number Of Ingredients' + str(len(ingredients)))
    name = c.Cake_Recipe.return_name(cake)
    print('Name of cake: '+ str(name))
    instructions = name + '<ul>'
    for i in range(0,len(ingredients)):
        instructions = instructions + '<li>' + Ingredient.to_instructions(ingredients[i]) + '</li>'
    instructions = instructions + '</ul>' + '<a href=""><button type="submit">Give me another!</button></a>' + '<p><a href="/"><button type="submit">Modify my ingredients</button></a></p>'
    response = make_response(instructions)
    return response

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)