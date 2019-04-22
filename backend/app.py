from flask import Flask
import json
app = Flask(__name__)

@app.errorhandler(404)#for handling page not found error
def page_not_found(e):
    return "404 not found"

@app.route('/api/pokemon')
def index():
    bar= {
        "pokemon_name": 
        [
            "bulbasaur", 
            "charmander", 
            "squirtle"  
        ]
    }
    json_obj = json.dumps(bar)
    return json_obj

if __name__ == "__main__" :
    app.run(port='8006',debug=True)