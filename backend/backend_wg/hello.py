from flask import Flask

app = Flask(__name__)


@app.route("/hello/<username>")
def hello_user(username):
    app.logger.info("111")
    return "Hello {}!".format(username)

if __name__ == '__main__':
    app.run(debug=True)
