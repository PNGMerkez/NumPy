#Numpy Modülü Anlatımı @ykslkrkci tarafından Persona Non Grata için Hazırlanmıştır.
# Matrisler

import numpy as num
#Numpyı num olarak çağırıcağımı belirttim.

sifir_matris = num.zeros((2,4))                    #Sıfırlardan oluşan bir matris oluşturdum. 2 Satır 4 Sütun
#print(sifir_matris)                               #Matrisime selam çaktım.

d_sifir_matris = num.zeros((2,4),dtype='int')      #Tipini integer yaptık.
#print(d_sifir_matris)                             #Matrisime selam çaktım.

bir_matris = num.ones((2,4))                       #Birlerden oluşan matris oluşturdum.
#print(bir_matris)                                 #Matrisime selam çaktım.

d_bir_matris = num.ones((2,4),dtype='int')         #Tipini integer yaptık.
#print(d_bir_matris)                               #Matrisime selam çaktım.

birim_matris = num.eye(3)                          #3 Satır 3 Sütun birim matris oluşturdum.
#print(birim_matris)                               #Matrisime selam çaktım.

elemanlari_ayni_matris = num.full((3,3),1907)      #Bütün elemanları 1907 olan 3x3 matris oluşturdum.
#print(elemanlari_ayni_matris)                     #Matrisime selam çaktım.

rastgele_matris = num.random.rand(5,6)             #5x6 boyutunda rastgele matris oluşturdum.
#print(rastgele_matris)                            #Matrisime selam çaktım.

sifir_bir_arasi = num.empty((2,4))                 #0 ile 1 arasında 5x6 boyutlarında matris oluşturdum.
#print(sifir_bir_arasi)                            #Matrisime selam çaktım.

#Matrislerde 4 İşlem
print(bir_matris + sifir_matris)                   #Boyutları aynı olmasına dikkat etmelisiniz.
print(bir_matris - sifir_matris)                   #Boyutları aynı olmasına dikkat etmelisiniz.
print(bir_matris * sifir_matris)                   #Boyutları aynı olmasına dikkat etmelisiniz. Elemanlar arası çarpım yaptı. YANLIŞ.

print(num.dot(bir_matris.T,sifir_matris))          #2si de 2x4 dü birisinin Transpozesini aldım 4x2 ile 2x4 çarpılabilir hale geldi.
