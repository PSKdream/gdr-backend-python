#from fuzzyMethod import fuzzyAhp
from flask import Flask, request
class fuzzyAhp:
    def __init__(self):
        self.weight_derivation = 'geometric'
        self.saaty_scale = {
            1: (1, 1, 1),
            3: (2, 3, 4),
            5: (4, 5, 6),
            7: (6, 7, 8),
            9: (9, 9, 9),
            2: (1, 2, 3),
            4: (3, 4, 5),
            6: (5, 6, 7),
            8: (7, 8, 9),
        }

    def getSaatyScale(self, weight):
        if(weight >= 1 and weight <= 9):
            return self.saaty_scale[weight]
        elif(weight >= 0):
            scale = self.saaty_scale[weight**-1]
            return (1/scale[2], 1/scale[1], 1/scale[0])

    def TriangularScale(self, dataset):
        matrix = []
        for (index, row) in enumerate(dataset):
            matrix.append([])
            for col in row:
                matrix[index].append(self.getSaatyScale(col))
        return matrix

    def weight_method(self, dataset):
        row_sum = []
        s_row = []
        f_w = []
        d_w = []
        for i in range(0, len(dataset)):
            a, b, c = 1, 1, 1
            for j in range(0, len(dataset[i])):
                d, e, f = dataset[i][j]
                a, b, c = a*d, b*e, c*f
            row_sum.append((a, b, c))
        L, M, U = 0, 0, 0
        for i in range(0, len(row_sum)):
            a, b, c = row_sum[i]
            a, b, c = a**(1/len(dataset)), b**(1 /
                                               len(dataset)), c**(1/len(dataset))
            s_row.append((a, b, c))
            L = L + a
            M = M + b
            U = U + c
        for i in range(0, len(s_row)):
            a, b, c = s_row[i]
            a, b, c = a*(U**-1), b*(M**-1), c*(L**-1)
            f_w.append((a, b, c))
            d_w.append((a + b + c)/3)
        n_w = [item/sum(d_w) for item in d_w]
        return f_w, d_w, n_w

    def fuzzy_ahp_method(self, dataset):
        dataset = self.TriangularScale(dataset)
        fuzzy_weights, defuzzified_weights, normalized_weights = self.weight_method(
            dataset)
        return {
            "fuzzy_weights": fuzzy_weights,
            "defuzzified_weights": defuzzified_weights,
            "normalized_weights": normalized_weights
        }

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/ahp', methods=['POST'])
def ahp():
  if request.method == 'POST':
    body = request.get_json()
    fAhp = fuzzyAhp()
    #print(fuzzy_ahp_method(body))
    #weight_derivation = 'geometric' # 'mean' or 'geometric'
    #weights, rc = ahp_method(dataset, wd = weight_derivation)

    return fAhp.fuzzy_ahp_method(body) , 201


if __name__ == '__main__':
    app.run()