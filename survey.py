from flask import Flask, render_template, request
app = Flask(__name__)





@app.route('/')
def surveyInfo():
    return render_template('idex.html')




@app.route('/results', methods=['POST'])
def showResults():
    print("Submitted Info")
    print(request.form)


    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comments_from_form = request.form['comments']
    options_from_form = request.form['radioChoice']


    return render_template("results.html",
    name= name_from_form,
    location= location_from_form,
    language= language_from_form,
    comments= comments_from_form,
    radioChoice= options_from_form)














if __name__=="__main__":
        app.run(debug=True)