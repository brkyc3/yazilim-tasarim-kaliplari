class User:
    def __init__(self,ad,soyad='YOK',yas=0,tel='-----------',email='NONE@NONE.com'):
        self.ad = ad #required parameter
        self.soyad = soyad
        self.yas = yas
        self.tel = tel
        self.email = email
        #Pattern amacini saglayan dil ozelligi varsa , ozelligin kullanilmasi daha temizdir.






user1 = User(ad='Burak',soyad='Yazici')

user2 = User(ad='Ali',email='brkyzc3@gmail.com')

user3 = User(ad='Atilla')