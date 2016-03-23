.. _kivyDili:

#########################################
:index:`Kivy Dili`: kv (:index:`kv lang`)
#########################################

Kivy pencere düzenlerini oluşturmak için muhteşem bir dil sunmaktadır: ``kv`` Dili. Bu dili biraz HTML'ye biraz da css'ye benzetebilirsiniz. Bu bölümde ``kv`` dilini anlatmaya çalışacağız.

"Merhaba Dünya" yeniden
=======================
:ref:`merhabaDunya` programında ekrandaki "Merhaba Dünya" yazısını program kodu içerisinde bir etiket oluşturup, bu etiketin metinini değiştirerek yapmıştık. Bu etiketi daha sonra düzen olarak geri döndürmüştük
(``return Label()``). Şimdi aynı pencereyi ``kv`` dilini kullanrak yapacağız. Önce program kodumuzu :ref:`main1`'deki gibi yazalım.
Bu kodda hiçbir değişiklik yapmadan birçok pencere oluşturacağız. 


.. literalinclude:: ./programlar/kivyDili/1/main.py
    :linenos:
    :caption: main.py
    :name: main1
    :language: python
    

Gördüğünüz gibi bu program hiçbirşey döndürmüyor. Sadece basit bir pencere oluşturuyor. Pencere içeriğini ``kv`` dili oluşturacağız.
Şimdi dosyasını :ref:`girisformu1` programını kaydettiğiniz aynı dizinine (klasöre) kaydedin.

.. literalinclude:: ./programlar/kivyDili/1/girisformu.kv
    :linenos:
    :caption: girisformu.kv
    :name: girisformu1
    
Bu dosyanın adı, python programının dosya adı değil, uygulamanın adı ile aynı olacaktır. 
Eğer uygulamanızın adı ``kullaniciGirisFormu()`` ise ``kv`` dosyasının adı ``kullanicigirisformu.kv`` olacaktır.
Dosya adında küçük harfleri kullanmanızı yeğlerim. Buradaki :ref:`girisformu1` oldukça basit bir yapıya sahip.Sadece iki satırdan ibaret
ilk satır pencerede bir etiketin olacağı (Label), ikinci satırda ise bu etiketin üzerinde yazacak metni (text) belirtmektedir. Tıpkı Python'da
olduğu gibi ``kv`` dilinde de girintiler (indendation) önemlidir. Birinci satır penceredeki grafik parçacığının ismini belirtmektedir.
Grafik parçacığının isminden sonra iki nokta üst üste konulup sonraki satırda (sanki işlev tanımlar gibi), bu grafik parçacığının özelliklerine ait
yapılanmayı biraz içerde başlatıyoruz. 

:ref:`main1` programını çalıştırdığınızda :ref:`merhabaDunyaImg` deki gibi bir pencere açılacaktır.

:index:`Kutu Pencere Düzeni` (:index:`Box Layout`)
=====================================================

:ref:`merhabaDunyaBolumu` bölümündeki :ref:`merhabaDunyaPencereDuzenleri`'ni hatırlayın. Orada ızgara pencere düzenini oluşturmak için
``GridLayout()`` sınıfını kullanmıştık. ``kv`` dilinde de yine grafik parcacıklarının ismini kullanacağız. Kutu pencere düzeni ``BoxGridLayout()``
sınıfı ile oluşturulur. O halde ``kv`` dilinde ``BoxLayout`` ile kutu pencere düzenini oluşturabiliriz. :ref:`girisformu2`'deki gibi değiştirin.


.. literalinclude:: ./programlar/kivyDili/2/girisformu.kv
    :linenos:
    :caption: girisformu.kv
    :name: girisformu2


:ref:`main1` programını tekrar çalıştırdığımızda :ref:`girisformu2Img` deki gibi bir pencere açılacaktır.



.. _girisformu2Img:

.. figure:: ./resimler/girisformu2Img.png

   Kutu Pencere Düzeni
   
Bu pencerede yan yana iki tane etiketin oluştuğunu görüyorsunuz.
