from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')


if __name__ == '__main__':
    app.run(debug=True)
