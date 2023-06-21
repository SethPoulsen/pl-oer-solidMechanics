import math
import random


def generate(data):

    k1 = random.randint(200, 300)
    k2 = random.randint(100, 200)
    L = 200
    theta = random.randint(20, 40)
    P = random.randint(10, 20)
    anglerad = theta * math.pi / 180
    cossquare = math.pow(math.cos(anglerad), 2)
    delta2 = P / (2 * (k2 + k1 * cossquare))

    data["params"]["k1"] = k1
    data["params"]["k2"] = k2
    data["params"]["L"] = L
    data["params"]["theta"] = theta
    data["params"]["P"] = P

    data["correct_answers"]["delta2"] = delta2

    return data
