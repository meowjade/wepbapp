import flask
import requests
import json

app = flask.Flask(__name__)

@app.get("/")
def root():
    d = flask.request.args
    if "password" in d:
        return {"password": d["password"]}
    return {"a": 2, "b": 3}

@app.post("/form")
def form():
    d = flask.request.args
    d2 = flask.request.form
    print(d2)
    request_data = {}
    for k,v in d.items():
        request_data[k] = v
    for k,v in d2.items():
        request_data[k] = v
    return request_data

app.run(debug=True)



# with requests.get("https://campusapi-development.up.railway.app") as r:
    # print(r.json())