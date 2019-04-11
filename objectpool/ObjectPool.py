import threading
import time


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
        print()
        time.sleep(5)
        waitForResource()


def useAndReleaseResource():
    resource = pool_manager.getResource()
    time.sleep(10)
    pool_manager.releaseResource(resource)


threading.Thread(target=useAndReleaseResource).start()
rs = [waitForResource() for _ in range(100)]
