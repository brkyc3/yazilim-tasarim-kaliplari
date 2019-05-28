import threading
import time
import random

class Connection:

    def __init__(self):
        self.__connection()

    def __connection(self):
        pass


class ObjectPoolSingleton:
    __pool_size = 100
    __pool = []
    __instance = None
    __lck = threading.Lock()

    @classmethod
    def get_Instance(cls):
        if not cls.__instance:
            with cls.__lck:

                if not cls.__instance:
                    cls.__instance = ObjectPoolSingleton()
                    cls.__pool = [Connection() for _ in range(cls.__pool_size)]
                    return cls.__instance

        return cls.__instance

    def getResource(self):
        with self.__lck:
            if len(self.__pool) > 0:
                print('Resource acquired , current pool size = ', len(self.__pool)-1)

                return self.__pool.pop()

            else:
                print('There are no resources available !!!')
                return None

    def releaseResource(self, resource):
        with self.__lck:
            self.__pool.append(resource)
        print('Resouce released , current pool size = ', len(self.__pool))


pool_manager = ObjectPoolSingleton.get_Instance()


def waitForResource():
    resource = pool_manager.getResource()
    if resource is None:
        print("waiting for resource  . . .")
        time.sleep(5)
        return waitForResource()
    else:
        return resource


def useAndReleaseResource(resource,threadNum):

    time.sleep(random.randint(1,4))
    pool_manager.releaseResource(resource)
    print(threadNum," finished !")

rs = [threading.Thread(target=useAndReleaseResource,args=[waitForResource(),i]).start()for i in range(300)]
