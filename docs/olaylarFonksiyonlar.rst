.. _olaylarBolumu:

########################
Olaylar ve Fonksiyonları
########################

Türkçe'de "Ortaya çıkan, oluşan durum" olarak tanımladığımız :index:`olay` (:index:`event`), Kivy için de geçerlidir.
Örneğin  "düğmeye bastırmak", "bastırılmayı bırakmak", "seçim yapmak", "bir tuşa basmak" gibi birçok durum birer 
Kivy olayıdır. Bu olaylar gerçekleştiğinde, programımızın bir tepki vermesi gerekir. Bir olay gerçekleştiğinde verilecek
tepki bir işlev (fonksiyon) tarafından gerçekleştirilebilir. Olay gerçekleştiğinde ilgili fonksiyonun çağrılabilmesi
için, fonksiyonu olaya bağlamak gerekmektedir.

Önce bir düğmeye bastırıldığında üzeirndeki metnin değişmesini sağlayacak bir
program yazmaya çalışalım. Bu programı öncelikle Python kodu yazarak öğreneceğiz, daha sonra ``kvlang`` ile nasıl
gerçekleştirilebileceğine bakacağız. Programımız :numref:`olaylar_main1`'de görülmektedir.

.. literalinclude:: ./programlar/olaylar/1/main.py
    :linenos:
    :tab-width: 4
    :caption: main.py
    :name: olaylar_main1
    :language: python

:numref:`olaylar_main1`'deki programı çalıştırdığımızda tüm ekranı kaplayan bir düğme görünecektir. Düğmenin üzerinde
"Değiştir" metni görünmektedir. Bu düğmeyi ``self``'in bir özelliği yapmamaızın nedeni, sınıf içerisindeki tüm işlevlerden
erişebilmektir. Bu düğmeye bastırıldığında çağrılacak olan işlevi, düğmeinin ``bind()`` özelliği
ile bağlıyoruz. Bir olayı bir nesneye bağlamak için ``bind()`` özelliğini kullanırız. Bu işleve, hangi olayı
bağlamak istiyorsak, onu parametre ve bu parametreye de çağrılacak olan işlevi yazıyoruz. 15. satırda 
``bind()`` işlevine :index:`on_press` parametrisini (bu düğmeye bastırılma olayını ifade eder) ve değer olarak ta
``self.metni_degistir`` işlevini atadık. Böylelikle düğmeye bastırıldığında ``self.metni_degistir`` işlevi çağrılacaktır.
Çağrılan işleve nesnenin kendisi (burada ``self.dugme``'dir) argüman olarak gönderilir. Aslında ``dugme``'yi ``self``'in
özelliği yapmadan, gelen nesne üzerinden de metni değiştirebilirdik:

::

  nesne.text='Tıkladın ve değiştim.'

aynı görevi görürdü. Şimdi aynı programı ``kv lang`` ile yazalım. Programımızı :numref:`olaylar_main2`'da görüyorsunuz.

.. literalinclude:: ./programlar/olaylar/2/main.py
    :linenos:
    :tab-width: 4
    :caption: main.py
    :name: olaylar_main2
    :language: python

İlgili ``kv`` dosyasını :numref:`olaylar_kv2`'da görüyorsunuz.

.. literalinclude:: ./programlar/olaylar/2/olayuyg.kv
    :linenos:
    :tab-width: 4
    :caption: olayuyg.kv
    :name: olaylar_kv2

Şimdi biraz program ve ``kv`` dosyası üzerinde konuşalım. ``kv`` dilinde garfik parçacıklarına isimleri ``id`` özelliği
ile veriyoruz. 3. satırdaki ``id: dugme`` yapmamızın nedeni bu garfik parçacığına (nesneye) program içerisinden ulaşmak için kullanacağımızdır.
Bu düğmeye bastırıldığında çağrılacak olan işlevi ``app``'ın bir özelliği ile veriyoruz. Çağrılan uygulamanın tüm nesneleri,
``kv`` dili içerisinden ``app``'ın özelliği ile erişilir. :numref:`olaylar_main2` programına bakacak olursak, ``kv`` dili 
içerisinde tanımlanmış grafik parçacıklarına erişmek için ``self.root.ids``'nin bir özelliği ile eriştiğimizi anlarsınız. ``kv``'deki
bir nesneye erişmek için o nesnenin ``id`` ile verilmiş ismini kullanıyoruz.

Kullanıcının metin gireceği bir metin kutusu, altında bir etiket ve onun altında da bir düğme bulunan bir program yazalım. Bu programı
yazmadaki amacımız, metin kutusuna girilen değeri etikette görüntülemktir. Programımızı :numref:`olaylar_main3`'da görüyorsunuz.

.. literalinclude:: ./programlar/olaylar/3/main.py
    :linenos:
    :tab-width: 4
    :caption: main.py
    :name: olaylar_main3
    :language: python

Bu programla kullanacağımız ``kv`` dosyasını da :numref:`olaylar_kv3`'da görüyorsunuz.

.. literalinclude:: ./programlar/olaylar/3/olayuyg.kv
    :linenos:
    :tab-width: 4
    :caption: olayuyg.kv
    :name: olaylar_kv3

``kv`` dosyasında etiket için neden ``markup: True`` dediğimizi sonra açaıklayacağız. Programımızı çalıştıralım ve 
üstteki metin kutusuna adımızı yazalım. "Değiştir" düğmesine tıkladığımızda, metin kutusundaki isim etiket üzerine yazılacaktır. Programın çalışmış halini :numref:`Şekil %s <olaylar1Img>` 'de görüyorsunuz.

.. _olaylar1Img:

.. figure:: ./resimler/olaylar1Img.png

   Girilen metnin etikete yazılması
   
Renkler
=======
Şimdi biraz renkelnelim. 

