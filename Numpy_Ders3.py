#Numpy Modülü Anlatımı @ykslkrkci tarafından Persona Non Grata için Hazırlanmıştır.
# Matrisler de Matematiksel İşlemler

import numpy as num

matris = num.array([[1,3,5],[2,4,6]])          #Matrisimi oluşturdum.
print(num.divide(matris,2))                    #Matrisimi 2ye bölmüş oldum ve ekrana bastırdım.

print(num.sum(matris))                         #Matrisimin içindeki değerleri topladım.
print(num.sum(matris,axis=0))                  #Matrisimin sütunları içindeki değerleri toplar.
print(num.sum(matris,axis=1))                  #Matrisimin satırların içindeki değerleri toplar.

print(num.mod(matris,2))                       #Matris değerlerimin 2 ye bölümünden kalanları görebilirim.

matris2 = num.array([[-1,3,-5],[2,-4,6]])      #Matrisimi oluşturdum.
print(num.abs(matris2))                        #Yeni matrisimin mutlak değerini alarak ekrana bastırdım.

print(matris2**2)                              #Matrisimin karesini aldım.

karekok_matris = num.sqrt(matris)              #Matrisimin karekökünü aldım başka bir değişkene eşitledim.
print(karekok_matris)

print(num.cos(matris))                         #Matrisimin kosinüsünü alabilirim.
print(num.sin(matris))                         #Matrisimin sinüsünü alabilirim.
print(num.tan(matris))                         #Matrisimin tanjantını alabilirim.


