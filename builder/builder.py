class Kullanici:
    def __init__(self, ad, soyad='YOK', yas=0, tel='-----------', email='NONE@NONE.com'):
        self.ad = ad  # required parameter
        self.soyad = soyad
        self.yas = yas
        self.tel = tel
        self.email = email
        # Pattern amacini saglayan dil ozelligi varsa , ozelligin kullanilmasi daha temizdir.

    def resim_yukle(self, img):
        pass

    def benzerleri_bul(self, img):
        pass


user1 = Kullanici(ad='Burak', soyad='Yazici')

user2 = Kullanici(ad='Ali', email='brkyzc3@gmail.com')

user3 = Kullanici(ad='Atilla')

print(user1, user2, user3)
