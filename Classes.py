
from Carbon.Aliases import true

class topcu:
    ad=""
    soyad=""
    yas=""
    takim=""

    def kayit(self):
        self.ad= input("ad gir:")
        self.soyad= input("soyad gir:")
        self.yas= input("yas gir:")
        self.takim= input("takim gir:")

    def show_info(self):
        print("ad: "'{}'.format(self.ad))
        print("soyad: "'{}'.format(self.soyad))
        print("yas: "'{}'.format(self.yas))
        print("takim: "'{}'.format(self.takim))

topcuk = topcu()
topcuk.kayit()
topcuk.show_info()

#-------------------------------------------------

class futbolcu():

    def __init__(self,ad,soyad,yas,takim):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.takim = takim

    def show_info(self):
        print("ad: "'{}'.format(self.ad))
        print("soyad: "'{}'.format(self.soyad))
        print("yas: "'{}'.format(self.yas))
        print("takim: "'{}'.format(self.takim))


futbolcu1 = futbolcu("memo","ak","34","sportif")
futbolcu1.show_info()

#-------------------------------------------------

class robot():
    kol = ""
    bacak = ""
    kafa = ""

    def kayit(self):

        self.kol = "yok"
        self.bacak = "yok"
        self.kafa = "yok"
        a = int(input("--Robota kaç numaralı özelliği eklemek istersiniz?--\n1-Kol\n2-Bacak\n3-Kafa\n-->"))
        if a == 1:
            self.kol = "Robot kol eklendi."
        elif a == 2:
            self.bacak = "Robot bacak eklendi."
        elif a == 3:
            self.kafa = "Robot kafa eklendi"
        else:
            print("---Hatalı işlem yaptınız.---")

    def show_info(self):
        print("1-Kol: "'{}'.format(self.kol))
        print("2-Bacak: "'{}'.format(self.bacak))
        print("3-Kafa: "'{}'.format(self.kafa))

robot1 = robot()
robot1.kayit()
robot1.show_info()

#-------------------------------------------------

class robot():

    def __init__(self, kol, bacak, kafa):
        self.kol = kol
        self.bacak = bacak
        self.kafa = kafa

    def show_info(self):
        b = 1
        while b<5:
            print("1-Kol: "'{}'.format(self.kol))
            print("2-Bacak: "'{}'.format(self.bacak))
            print("3-Kafa: "'{}'.format(self.kafa))

            a = int(input("--Eklemek istediğiniz özellik:\n"))
            if a == 1:
                self.kol = "Robot kol eklendi."
            elif a == 2:
                self.bacak = "Robot bacak eklendi."
            elif a == 3:
                self.kafa = "Robot kafa eklendi"
            else:
                print("---Hatalı işlem yaptınız.---")
            b += 1

robot1 = robot("-", "-", "-")
robot1.show_info()

