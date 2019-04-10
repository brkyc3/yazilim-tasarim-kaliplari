import copy

class BulkyObject:
    def __init__(self,name,userid,bulky_data):
        self.bulky_data = bulky_data
        self.userid = userid
        self.name = name

    def deepclone(self):
        return copy.deepcopy(self)
    def clone(self):
        return copy.copy(self)


a = [1,2,3]


ob1 = BulkyObject('burak',123,a)

cpy = ob1.clone()

deep = ob1.deepclone()


deep.bulky_data+=[123321]
print(ob1.bulky_data , deep.bulky_data)

cpy.bulky_data+=[111]

print(ob1.bulky_data , cpy.bulky_data)
