import flask
from agents import GroqAgent

agents = [
    GroqAgent
]


app = flask.Flask(__name__)

@app.route("/")
def main():
    return("Servidor ejecutándose correctamente.")

@app.route("/agents", methods=["GET"])
def show_agents():
    pass

@app.route("/agents", methods=["POST"])
def ask_agents():
    pass

if __name__ == "__main__":
    app.run(debug=True)