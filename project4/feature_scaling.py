from sklearn.preprocessing import MinMaxScaler
import numpy as np
def sigmoid(logit):
    return 1./(1.+np.exp(-logit))
class SigmoidMinMaxScaler(MinMaxScaler):
    def transform(self, X):
        Y = super(SigmoidMinMaxScaler, self).transform(X)
        return sigmoid(Y)