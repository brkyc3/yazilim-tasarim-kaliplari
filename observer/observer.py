import abc
import uuid
import random
import time
import threading
class Image:
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



    def save_image(self, data):
        print(data," saved !")
        self._notify(data)

class Subscriber(abc.ABC):

    def __init__(self):
        self._subject = None
        self._subscriber_id = uuid.uuid4()


    @abc.abstractmethod
    def update(self, data):
        pass


class LabelSubscriber(Subscriber):


    def update(self, data):
        print(self._subscriber_id," image label :", data['label'])


class ExtentionSubscriber(Subscriber):

    def update(self, data):
        print(self._subscriber_id, " extension :", data['ext'])




def background(subject):
    while 1:
        rnd = random.randint(50,200)/100
        time.sleep(rnd)


        label =''.join([chr(random.randint(ord('a'),ord('z'))) for i in range(10)])
        extention = ''.join([chr(random.randint(ord('a'), ord('z'))) for i in range(5)])
        data = {'label':label,'ext':extention}
        subject.save_image(data)


def main():
    subject = Image()
    subs4_label = LabelSubscriber()
    subs4_type = ExtentionSubscriber()
    subject.subscribe(subs4_label)
    subject.subscribe(subs4_type)


    t = threading.Thread(target=background,args=[subject])
    t.start()

    while(1):
        print("MAIN MAIN MAIN MAIN ! ! !")
        time.sleep(0.1)


if __name__ == "__main__":
    main()