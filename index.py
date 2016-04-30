from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'post'])
def view_form():
    if request.method == 'POST':
        name = request.form['name'];
        message = request.form['message']
        return render_template('index.html', name=name, message=message)
    else:
        return render_template('index,html')


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)