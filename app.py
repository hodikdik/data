from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/costume')
def costume():  # put application's code here
    return render_template('costume.html')

@app.route('/nazenaze')
def nazenaze():  # put application's code here
    return render_template('nazenaze.html')

@app.route('/culture')
def culture():  # put application's code here
    return render_template('culture.html')

@app.route('/data')
def data():  # put application's code here
    return render_template('data.html')

if __name__ == '__main__':
    app.run()
