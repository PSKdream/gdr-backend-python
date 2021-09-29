from flask import Flask, request
from FuzzyAHP import fuzzy_ahp_method

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/ahp', methods=['POST'])
def ahp():
  if request.method == 'POST':
    body = request.get_json()
    #print(fuzzy_ahp_method(body))
    #weight_derivation = 'geometric' # 'mean' or 'geometric'
    #weights, rc = ahp_method(dataset, wd = weight_derivation)

    return fuzzy_ahp_method(body), 201


if __name__ == '__main__':
    app.run(debug=False)