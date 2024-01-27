from flask import Flask, render_template

app = Flask('Pizzeria', template_folder="templates", static_folder="static")

@app.route('/')
@app.route('/index')
def main_page():
    return render_template("main_page.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/about_us')
def about_us():
    return render_template("about_us.html")

if __name__ == "__main__":
    app.run(debug=True)