from random import random, randrange
from flask import Flask, jsonify
from flask import request
import requests

app = Flask(__name__)

@app.route("/isthisacat", methods = ['POST'])
def is_this_a_cat():

    #Simulate request to algorithm.

    r = requests.post("https://jsonplaceholder.typicode.com/albums/1/photos", {'mock': 'file'})
    print(f"Server response status: {r.status_code}")
    print(f"Server response data: {r.json()}")

    #50% chance to return positive or negative result, to simulate algorithm result. 

    cat_or_not = randrange(0,2) 

    # Sending response back

    if r.status_code == 200 or 201:
        message = "It's a cat!" if cat_or_not else "It's not a cat."
    else:
        message = "Technical error."
    response = jsonify(message=message)
    
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == "__main__":
    app.run(debug=True)