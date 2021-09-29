from flask import Flask, request
from FuzzyAHP import fuzzy_ahp_method

app = Flask(__name__)

@app.route('/')
def hello():
  q = request.args.get('q')
  print(q)
  return { "message": "Hello! python" }, 201

@app.route('/ahp', methods=['POST'])
def book():
  if request.method == 'POST':
    body = request.get_json()
    #print(fuzzy_ahp_method(body))
    #weight_derivation = 'geometric' # 'mean' or 'geometric'
    #weights, rc = ahp_method(dataset, wd = weight_derivation)

    return fuzzy_ahp_method(body), 201


if __name__ == '__main__':
    app.run(debug=True)