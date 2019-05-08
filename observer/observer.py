import abc
import uuid
import random
import time
import threading
class News:
    def __init__(self):
        self._subscribers = set()


    def subscribe(self, subscriber):
        subscriber._subject = self
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        subscriber._subject = self
        self._subscribers.discard(subscriber)

    def _notify(self,data):

        for subscriber in self._subscribers:
            subscriber.update(data)



    def create_new(self, data):
        print(data," created !")
        self._notify(data)

class Subscriber(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._subscriber_id = uuid.uuid4()


    @abc.abstractmethod
    def update(self, data):
        pass


class ConcreteSubscriberName(Subscriber):


    def update(self, data):
        print(self._subscriber_id," haber adi ", data['name'])


class ConcreteSubscriberType(Subscriber):

    def update(self, data):
        print(self._subscriber_id, " haber turu ", data['tp'])




def backgroud(subject):
    while(1):
        rnd = random.randint(50,200)/100
        time.sleep(rnd)


        name =''.join([chr(random.randint(ord('a'),ord('z'))) for i in range(10)])
        tp = ''.join([chr(random.randint(ord('a'), ord('z'))) for i in range(5)])
        data = {'name':name,'tp':tp}
        subject.create_new(data)


def main():
    subject = News()
    subs4_name = ConcreteSubscriberName()
    subs4_type = ConcreteSubscriberType()
    subject.subscribe(subs4_name)
    subject.subscribe(subs4_type)


    t = threading.Thread(target=backgroud,args=[subject])
    t.start()

    while(1):
        print("MAIN MAIN MAIN MAIN ! ! !")
        time.sleep(0.1)
    t.join()

if __name__ == "__main__":
    main()