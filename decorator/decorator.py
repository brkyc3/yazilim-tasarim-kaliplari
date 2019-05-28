from keras.losses import mae
from keras.models import Model
import keras.backend.tensorflow_backend as K
from keras.models import load_model


class Loss:

    def __init__(self, loss_weight, center):
        self.loss_weight = loss_weight
        self.center = center

    # keras loss function icin  ytrue,ypred seklinde iki parametre bekliyor.
    # Daha farkli parametrelere ihtiyac duyuldugunda decorator pattern kullanilabilir
    def custom_loss(self):
        def c_loss(ytrue, ypred):
            loss = mae(ytrue, ypred)
            print(type(loss))
            loss += self.loss_weight * K.square((K.mean(ypred) - self.center))

            return loss

        return c_loss


m = load_model('../models/simplemodel.h5')
loss = Loss(10, 0.5)
m.compile(loss=loss.custom_loss(), optimizer='sgd')
m.summary()

print(m.loss)
