# -*- coding: utf-8 -*-

class Oyun:
    def __init__(self, cevap, ipucu):
        self.ipucu = ipucu
        self.cevap = cevap

    def cevapBol(self):
        self.harfler = list(self.cevap)
        return self.harfler

    def kacHarf(self):
        self.harfsayisi = len(self.harfler)
        return self.harfsayisi

    def soruHazirlar(self):
        alinancevaplar = []
        for x in range(self.harfsayisi):
            alinancevaplar.append("__")
        return alinancevaplar

    def cevapVer(self):
        self.cevapBol()
        self.kacHarf()
        hatasayisi = 0
        dogrucevap = 0
        alinancevaplar = self.soruHazirlar()
        harfler = self.harfler
        print(f"İpucu : {self.ipucu} , {self.kacHarf()} Harfli")
        findedWords = []

        while True:
            a = input(f"{alinancevaplar}  Bir harf giriniz : ")
            if a == self.cevap:
                print("Tebrikler Kazazndınız :)")
                print("Cevap : ", self.cevap)
                break

            if hatasayisi < 7 and dogrucevap < self.harfsayisi:

                if a not in findedWords:
                    findedWords.append(a)

                    if a in harfler:

                        for x in range(self.harfsayisi):  # kacıcncı harf olduğunu bulma
                            if a == harfler[x]:
                                print(f"{x + 1}.harf {a}")
                                alinancevaplar[
                                    x] = a  # kacıncı harf oldugunu bulup girilen kelime ile yer deyiştiriyorum !
                                dogrucevap = dogrucevap + 1

                    else:
                        print(f"Kelimenin içinde bu harf yok : {a}")
                        hatasayisi += 1

                else:
                    print(f"Lütfen girilmemiş harfleri giriniz. Şu ana kadar girilen harfler {findedWords}")


            else:
                if hatasayisi > 6:
                    print("Kaybettiniz")

                else:
                    print("Tebrikler Kazazndınız :)")
                    print("Cevap : ", self.cevap)

                break


s1 = Oyun(cevap=f"{input('Bir cevap giriniz :')}", ipucu=f"{input('Bir ipucu giriniz :')}")
s1.cevapVer()
