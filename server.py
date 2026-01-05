import flask
from agents import groqAgent, cerebrasAgent

agents = [
    groqAgent,
    cerebrasAgent
]


app = flask.Flask(__name__)

current_agent = 0

current_agent = 0

def next_agent():
    global current_agent
    current_agent = (current_agent + 1) % len(agents)
    return agents[current_agent]


@app.route("/")
def main():
    return("Servidor ejecutándose correctamente.")

@app.route("/agents", methods=["GET"])
def show_agents():
    return "<br>".join(str(agent) for agent in agents)

@app.route("/agents", methods=["POST"])
def ask_agents():
    agent = next_agent()

    data = flask.request.get_json(force=True)
    question = data.get("question", "")

    def generate():
        for chunk in agent.generate(question):
            yield chunk

    return flask.Response(generate(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)