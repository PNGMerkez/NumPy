#Numpy Modülü Anlatımı @ykslkrkci tarafından Persona Non Grata için Hazırlanmıştır.
# Diziler

import numpy as num
#Numpyı num olarak çağırıcağımı belirttim.

dizi = num.array([0,1,2,3,4])               #Dizimizi Oluşturduk.
#print(type(dizi))                          #Tipinin numpy.ndarray olduğunu öğrendik.

dizi = dizi.astype("float")                 #Dizinin tipini değiştirebiliyoruz.
#print(dizi.dtype)

dizi2 = num.array([[1,3,5,7],[2,4,6,8]])    #Virgül satırları arıyıyor.Köşeli parantezler içindekilerde satırların sütunları olucaktır.
#print(dizi2)
#print(dizi2.ndim)                          #Boyutunu öğrenebiliriz.

#print(dizi2.shape)                         #Satır ve Sütun değerlerini öğrebiliriz.

d_dizi = dizi2.reshape(1,8)                 #Boyutunu değiştirebiliriz. 1 satır 8 sütun
#print(d_dizi)

dizi3 = num.arange(1,10)                    #Rastgele dizi oluşturabiliriz. 1 -> Başlangıc değeri 10 -> Bitiş değeri(dahil değil)
#print(dizi3)

dizi4 = num.arange(0,10,2)                  #2 atlıyarak dizi oluşturucak. yani çift sayıları kullanıcak.
#print(dizi4)

print(dizi4[0:2])                           #0 dan başla 2. indexe kadar git.(dizilerde yaptığımız gibi)



