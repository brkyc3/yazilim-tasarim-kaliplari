import threading


class ModelLoader:
    __model_path='/home/brkyzc/flowmodel3d.h5'
    __singleton_lock =threading.Lock()
    __model = None
    @classmethod
    def get_model(cls):
        if not cls.__model:
            with cls.__singleton_lock:

                if not cls.__model:
                    from keras.models import load_model
                    #sadece model yuklenirken lock gerekiyor
                    #bu yuzden lock if icinde kullanildi
                    #lock if icinden oldugundan birden fazla threadden if icine giren olabilir
                    cls.__model = load_model(cls.__model_path)
                    cls()
        return cls.__model



print(ModelLoader.get_model())
print(ModelLoader.get_model())
