from flask import Flask, render_template
from students import Students

app = Flask(__name__)

Students = Students()


@app.route('/')
def table():
    return render_template('tables.html', students=Students)


if __name__ == "__main__":
    app.run(debug=True)