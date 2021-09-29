from pyDecisions.py_decisions.ahp.fuzzy_ahp import fuzzy_ahp_method as fahp

weight_derivation = 'geometric'  # 'mean' or 'geometric'
saaty_scale = {
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


def getSaatyScale(weight):
    if(weight >= 1 and weight <= 9):
        return saaty_scale[weight]
    elif(weight >= 0):
        scale = saaty_scale[weight**-1]
        return (1/scale[2], 1/scale[1], 1/scale[0])


def TriangularScale(dataset):
    matrix = []
    for (index, row) in enumerate(dataset):
        matrix.append([])
        for col in row:
            matrix[index].append(getSaatyScale(col))
    return matrix


def fuzzy_ahp_method(dataset):
    dataset = TriangularScale(dataset)
    fuzzy_weights, defuzzified_weights, normalized_weights = fahp(
        dataset)
    return {
        "fuzzy_weights": fuzzy_weights,
        "defuzzified_weights": defuzzified_weights,
        "normalized_weights": normalized_weights
    }
