Yazıdan Sese

Nasıl yapılabilir?

Öncelikle yazıyı parçalarına ayırmak gerek. Örneğin;

"Bu bir deneme yazısıdır." metnini analiz etmek gerekir. Bu cümlede sözcükler ve boşluklar var. Bu sözcükler harflerden oluşuyor.
Belki markdown gibi bir dil ile yazıyı sese çevirme kolaylaşır.

İşlemleme süreci

1.Metin analizi

Metin analizi düzenli yazılan bir metnin bir markdown diline çevrilmesi. Bu çevirim sadece metin - ipa çevirimi değil
2.Metin analizinden sonra seçilecek seslerin belirlenmesi
3.Seçilen sesleri konuşma sentezleyici tarafından üretilmesi


Metindeki seslerin ses çevresine göre formant analizi

a e ı i u ü o ö

b c ç d f g h j k l m n p r s ş t v y z




a
b
c
ç
d
e
f
g
ğ
h
ı
i
j
k
l
m
n
o
ö
p
r
s
ş
t
u
ü
v
y
z

her dört ileri harf için
[i1,i2,i3,i4...in]

her bir i için:
    4 kez tekrarla:
        bir array'a baştan başlayarak harf ekle
        elde edilen array'ı kontrol et (databaseden)
        eğer karşılaşma bulunursa (en küçük) hecelenmişler array'ına ekle
        devam et



karşıma
k1 a2 r3 ş4 ı5 m6 a7

V       a,e,ı,i,o,ö,u,ü
VC      ak,el,il
CV      ba,be,ka,ke
CVC     bak,bal,say,git
VCC     ilk,üst,ast
CCV     tra,pla,tre
CVCC    türk,sırt,kart

sırtlanmak
sırt lan mak

