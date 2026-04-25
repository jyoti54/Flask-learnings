## Building URL Dynamically in Flask
## Variable Rules and url Building 

from flask import Flask, redirect,url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    # return 'Welcome to Flask. Jyoti is learning Flask .'
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    # return 'The person has passed and the score is ' + str(score)
    res = " "
    if score >= 50:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the score is ' + str(score)
#     # return "<html><body><h1>Fail<h></body></html>"
    

 ## Route Chaecker
@app.route('/results/<int:marks>')
def result(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    # return result
    return redirect(url_for(result, score=marks))

## Result checker html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['C'])
        data_science = float(request.form['data science'])
        total_score = (science + maths + c + data_science)/4
    res = " "
    # if total_score >=50:
    #     res = 'success'
    # else:
    #     res = 'fail'
    # return redirect(url_for(res, score=total_score))
    return redirect(url_for('success', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
    