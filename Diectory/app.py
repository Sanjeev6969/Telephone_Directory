from flask import Flask,render_template,request
from forms import SignUpForm

app=Flask(__name__)
app.config['SECRET_KEY'] = 'surya'
@app.route("/")
def Register():
    return render_template('home.html')

@app.route("/Add")
def Add():
    form=SignUpForm()
    return render_template('signup.html',form=form)

@app.route("/Search")
def Search():
    form=SignUpForm()
    return render_template('Search.html',form=form)

if __name__=="__main__":
    app.run(debug=True)
