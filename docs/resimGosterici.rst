.. _resimGostericiBolumu:

################################
Atlıkarınca ve Resim Gösterici
################################

.. Caution::

    Bu bölüm taslak aşamasındadır.

Atlı karınca dememizin nedeni ":index:`carousel`" kelimesi İngilizce'de ":index:`atlıkarınca`" anlamını taşıması, 
elbette bir de at yarışlarındaki gösteri turnuvasına denmekte, ancak "carousel" isminin neye dayanarak
verildiğini bilmiyorum (merak etmiyor da değilim, yoksa şu parklarda gördüğümz askıda dönen salıncaklardan
mı geliyor acabağa). Bu "Carousel" denen şey nedir? Cep telefonunuzu
kullanırken, ekranı sağa sola (ya da üste alta) parmaklarınızın ucu ile kaydırıyorsunuz ya, işte o. 
Bu bölümde Corusel (atlıkarınca) kullanarak bir resim gösterici yapmayı planlıyoruz. Normalde
bir resim göstericisini atlıkarınca ile yapmak ne kadar mantıklı bilemiyorum. Çünkü tüm resimleri başta
atlıkarıncaya yüklüyorsunuz. Bu da sanırım bellek kullanımını artırır. Her neyse biz burada bu atlıkarıncayı
nasıl kullanacağımızı öğreneceğiz.

Atlıkarınca (Carousel)
=========================

Atlıkarınca, bir çeşit düzen gibi düşünülebilir. Bu düzen kendi çerisinde çeşitli sekemeleri bulunan ve 
her sekmenin kendi düzeni bulunan bir yapıdır. Sekmeler bir pencerede bulunmaz, kaydırılarak ulaşılırlar.
Burada atlıkarınca sekmelerine sadece resim koyacağız, ancak herhengi bir düzen de koyabilirsiniz.

Önce atlıkarıncanın nasıl çalıştığını öğrenelim. Atlıkarınca ``Carousel`` nesnesi ile oluşturulur. 
İstenilen bir düzen (tek bir etiket, tek bir resim ya da diğer düzenler) bu nesneye ``add_widget``
özelliği ile eklenir. :numref:`regimGosterici_main1`'deki gibi ``main.py`` dosyasını  yazalım.

.. literalinclude:: ./programlar/resimGosterici/1/main.py
    :linenos:
    :tab-width: 4
    :caption: main.py
    :name: regimGosterici_main1
    :language: python
    
Bu programı biraz açıklayalım: 10. satırda bir atlıkarınca nesnesi oluşturuluyor. Daha sonra bu karıncaya
5 adet etiket ekleniyor. Her etiketin üzerinde "Karınca Sayfası: 1", "Karınca Sayfası: 2" ... yazmaktadır.
Programı çalıştırıp fare ile sayfayı sola doğru itip bırakın. Bu size sonraki sayfayı görüntüleyecektir.
Mobil cihazlarda, sayfayı parmağınız ile sola doğru itmeniz yeterlidir. Atlıkarıncanın yönü ön tanımlı
olarak sola doğrudur. İsterseniz bunu :index:`direction` özelliği (parametresi) ile değiştirebilirsiniz.
Bu parametrenin (ya da özelliğin) alabileceği değerler şunlardır: right, left, top, bottom. Sanırım bunları
açıklamaya gerek yok. Programın çalışmış halini :numref:`Şekil %s <resimGosterici1Img>`'de görüyorsunuz.

.. _resimGosterici1Img:

.. figure:: ./programlar/resimGosterici/1/resimGosterici1Img.png

   Atlıkarınca

Bir Klasördeki Resimler
=======================

Atlıkarıncayı basit olarak, programın bulunduğu dizindeki resimleri gösterecek şekilde kullanmaya çalışalım.
Daha sonra programımızı geliştireceğimizden ``kv`` dilini kullanarak hazırlayalım. Öncelikle ``resimgosterici.kv``
dosyamızı :numref:`regimGosterici_kv1`'deki gibi yazalım.


.. literalinclude:: ./programlar/resimGosterici/2/resimgosterici.kv
    :linenos:
    :tab-width: 4
    :caption: resimgosterici.kv
    :name: regimGosterici_kv1

Buarada anadüzenimizi ``BoxLayout`` yaptık çünkü ilerde düğmeler yerleştireceğiz. Onun dışında bilmediğiniz bir kod
bulunmuyor. Atlıkarıncayı 4. satırdaki ``Carousel`` ile olışturduk. Bu nesneye ulaşmak için id'sini ``karinca`` yaptık.
Bu ``kv`` dosyasını kullanıp, programın çalıştığı klasördeki *png* resimlerini gösterecek ``main.py`` programını da
:numref:`regimGosterici_main2`'deki gibi yazabiliriz.

.. literalinclude:: ./programlar/resimGosterici/2/main.py
    :linenos:
    :tab-width: 4
    :caption: main.py
    :name: regimGosterici_main2
    :language: python


Bu programda ``os.listdir()`` ile bulunduğumuz klasördeki (``os.getcwd()`` ile alınıyor) dosylara üzerinde bir iterasyon
yapılıyor (11. satır). İterasyon içerisinde ``os.path.splitext()`` ile dosyaların (dosya_adı, uzantisi) şeklinde
ayrılıyor ve uzantısı *.png* olan dosyalardan bir :index:`resim` nesnesi oluşturuluyor. Resim nesnesi :index:`Image`
sınıfı ile oluşturulur. Bu sınıfa :index:`source` paramteresi ile oluşturulacak resmin tam dosya adı (yada programın
çalıştığı klasördeki dosya adı) verilir. Oluşturulan ``resim`` nesnesi atlıkarıncanın ``add_widget`` özelliği
ile ekleniyor. Ben programın çalıştığı klasöre Kivy, Android ve Python logolarını koydum 
(umarım telif haklarını ihlal etmemişimdir). Programı çalıştırıp resmi sürüklerken ekran görüntüsünü aşağıdaki
(:numref:`Şekil %s <resimGosterici2Img>`) gibi aldım.


.. _resimGosterici2Img:

.. figure:: ./programlar/resimGosterici/2/resimGosterici2Img.png
   
   Basit Resim Gösterici (kaydırırken)

Bir klasördeki resimleri dosyaların uzantılarına bakarak belirlemek deyim yerinde ise amele işi (burada ameleleri
küçümsemek gibi bir niyetimin olmadığını belirteyim), çünkü onlarda resim formatı var.
Bunun yerine bir dosyanın resim olup olmadığını, Python'un ``imghdr`` modülünü kullanarak anlayabiliriz. Bu modülün
``what`` özelliği resim dosyasının tipini döndürür. Dosya resim değil ise hiçbirşey döndürmez. O Halde programımızı
:numref:`regimGosterici_main3`'deki gibi güncelleyebiliriz.

.. literalinclude:: ./programlar/resimGosterici/3/main.py
    :linenos:
    :tab-width: 4
    :caption: main.py
    :name: regimGosterici_main3
    :language: python

Programın 2. satırında ``imghdr`` modülünü içerdiğimize dikkat edin.

*devam edecek...*
