.. _metinDuzenleyiciBolumu:

#################
Metin Düzenleyici
#################

Birçok yeni programcı, programların çok basit şekilde hazırlanabileceğini düşünür. Oysa ki en küçük programda
bile çok fazla düşlünülecek ve yapılacak iş vardır. Bu bölümde basit bir metin düzenleyici yapacağız. Elbette
yapacağımız metin düzenleyici üretim açamlı olmayacaktır. Sadece bir program yazılırken, programcıların nelere
dikkat etmeleri gerektiği, nereleri düşünmeleri gerektiğine bir ışık tutacağız. Basit bir metin düzenleyici
yazmak için ne kadar çok yapılacak iş olduğunu göreceksiniz. Bir programı yazmaya başlayınca, düşünmenin sınırı
ve yapılacakların sonu olmadığını göreceksiniz. Biz burada bir yol açalım, gerisini size bırakacağız.

Buradaki metin düzenleyici basitçe bir metin alanı ve kullanıcıya dosyasını açıp kaydedebileceği birkaç seçenek
sunmaktan ibaret (tamamı bu değildir elbette) olacak. O halde öncelikle ana penceremizi hazırlayalım, bunun için
şimdilik metin alanımızı ve altına işlem yapmayan birkaç düğme koyalım. Daha sonra bu düğmelere işlerlik
kazandıracağız. ``main.py`` dosyasını :numref:`metin_duzenleyici_main1`'deki gibi yazalım.

.. literalinclude:: ./programlar/metinDuzenleyici/1/main.py
    :linenos:
    :tab-width: 4
    :caption: main.py
    :name: metin_duzenleyici_main1
    :language: python
    
    
Bu programda bilmediğimiz hiçbirşey yok. ``os`` ve ``sys`` modüllerini neden içerdiğimizi ileride göreceksiniz.
Şimdi de, bu program tarafından kullanılacak ``kv`` dosyasını :numref:`metin_duzenleyici_kv1`'deki gibi yazalım:

.. literalinclude:: ./programlar/metinDuzenleyici/1/metinduzenleyici.kv
    :linenos:
    :tab-width: 4
    :caption: metinduzenleyici.kv
    :name: metin_duzenleyici_kv1


Bu dosyada bilmediğimiz sadece ``TextInput`` parçacığının :index:`multiline` özelliğine ``True`` değerinin atanmış
olmasıdır. ``TextInput`` parçacığını

::

  metin = TextInput(multiline=True)
  
şeklinde tanımlayacak olursak, çok satırlı bir metin girdi alanı elde etmiş oluruz. ``TextInput`` parçacığı
ön tanımlı olarak tek satırdan oluşur, ``multiline`` özelliğine ``True`` değeri atamkla çok satırlı bir
metin giriş alanı elde etmiş oluruz ki, bir metin düzenleyicinin metin yazılacak alanı tam da bu yaptığımız
gibidir.

``main.py`` programı çalıştırdığımızda metin düzenleyicimizin penceresi 'deki gibi açılacaktır.


.. _metinDuzenleyici1Img:

.. figure:: ./programlar/metinDuzenleyici/1/metinDuzenleyici1Img.png

   Metin Düzenleyicimiz Kullanıma Hazır :-)
   
   
Şimdi yukarıdaki düğmelere tıklayın bakalım dosya açacak mı, dosyanızı kaydedecek mi? Sizce olur mu? Neden
olmasın ki? Ben düğmeyi koydum, program da gitsin dosyamı kaydedeceğini anlasın ve kaydetsin. Benzer cümleleri
her sınıfımda kullanırım. Ancak ne yazıkki bu programları yazanlar, bizim koyduğumuz düğmelerin (ya da menülerin)
üzerindeki metinlere bakarak, ne iş yapmak istediğimizi anlamayacak kadar becereksizler. Öyle mi? Elbette değil.
Bir düğme koyduysanız, ona tıklandığında ne yapılması gerektiğini siz yazacaksınız, bir başkası değil. Bu kadar
söylendikten sonra gelin, bu düğmelere işlerlik kazandıralım. Öncelikle "Farklı Kaydet" düğmesinden başlayalım.
Neden mi? Çünkü "Kaydet" dedğimizde, daha önceden bir dosya adı verilmemişse "Farklı Kaydet" çağrılacaktır.

Bir dosyayı kaydetmek için, öncelikle kaydedilecek klasörün belirtilmesi ve daha sonra da dosya adının 
girilmesi gerekir. Eğer kullanıcıya basitçe bir metin kurtusu sağlayıp buraya dosyanın tam patikasını yazmasını
isterseniz (örneğin ``C:\dosyalarım\devlerim\fizik\newton.txt`` şeklinde), kusura bakmayın ama programınızı
kimse kullanmaz. 1990'lı yıllarda olsaydınız buna kimse itirtaz etmezdi ancak şimdi GUI (Grafik Kullanıcı Arayüzü)
icat edildi. O halde klasörler arasında gezinti yapabilecek bir arayüze ihtiyacımız var. Bun kendiniz yapabilirsiniz.
Nasıl mı? ``os.listdir()``'i biliyorsunuz.


