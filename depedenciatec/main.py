from flask import Flask
import random

app = Flask(__name__)
facts_list = {"La dependencia tecnológica es el uso excesivo de dispositivos tecnológicos, como teléfonos móviles, tablets, computadoras o videoconsolas. Puede afectar a personas, empresas, sectores o economías",
              }


@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/random_fact")
def facts():
    return f'<h1>{random.choice(facts_list)}</h1>'

app.run(debug=True)