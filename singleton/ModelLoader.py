import threading


class ModelLoader:
    __model_path = '../models/simplemodel.h5'
    __singleton_lock = threading.Lock()
    __model = None



    @classmethod
    def get_model(cls):
        if not cls.__model:
            with cls.__singleton_lock:

                if not cls.__model:
                    from keras.models import load_model
                    # sadece model yuklenirken lock gerekiyor
                    # bu yuzden lock if icinde kullanildi
                    # lock if icinden oldugundan birden fazla threadden if icine giren olabilir
                    cls.__model = load_model(cls.__model_path)
                    cls.__model._make_predict_function()
                    return cls.__model

        return cls.__model


# print(ModelLoader.get_model())
# print(ModelLoader.get_model())


for i in range(20):
    t = threading.Thread(target=lambda: print(ModelLoader.get_model()))
    t.start()
