import flask
from agents import groqAgent, cerebrasAgent, geminiAgent
import json

agents = [groqAgent, cerebrasAgent, geminiAgent]


app = flask.Flask(__name__)


def load_current_agent():
    global current_agent
    with open("../data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        return data["current_agent"]


def save_current_agent():
    global current_agent
    # Creamos directamente el diccionario con la clave y el valor
    data = {"current_agent": current_agent}

    # Guardamos en el JSON
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


current_agent = load_current_agent()


def next_agent():
    global current_agent
    current_agent = (current_agent + 1) % len(agents)
    save_current_agent()
    return agents[current_agent]


@app.route("/")
def main():
    return "Servidor ejecutándose correctamente."


@app.route("/agents", methods=["GET"])
def show_agents():
    question = flask.request.args.get("question")
    if question is None:
        return "<br>".join(str(agent) for agent in agents)
    else:
        agent = next_agent()

        def generate():
            for chunk in agent.generate(question):
                yield chunk

        return flask.Response(generate(), mimetype="text/plain")



@app.route("/agents", methods=["POST"])
def ask_agents():
    agent = next_agent()

    data = flask.request.get_json(force=True)
    question = data.get("question", "")

    def generate():
        for chunk in agent.generate(question):
            yield chunk

    return flask.Response(generate(), mimetype="text/plain")
