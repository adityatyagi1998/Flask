from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/profile/<user>")
def profle(user=None):
    return render_template("user.html", user=user)

if __name__=='__main__':
    app.run()