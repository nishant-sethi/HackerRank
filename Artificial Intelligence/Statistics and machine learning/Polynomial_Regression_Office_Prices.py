import numpy as np
import pandas as pd
from sklearn import linear_model as lm
from sklearn import preprocessing as pp

F, N = map(int, input().split())
train = np.array([input().split() for _ in range(N)], float)
T = int(input())
test = np.array([input().split() for _ in range(T)], float)

mod = lm.LinearRegression()
XtoP = pp.PolynomialFeatures(3, include_bias=False)
mod.fit(XtoP.fit_transform(train[:, :-1]), train[:, -1])

ymod = mod.predict(XtoP.fit_transform(test))
print(*ymod, sep='\n')