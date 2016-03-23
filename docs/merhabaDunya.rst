.. _merhabaDunyaBolumu:

###############
Merhaba Dünya
###############

Hemen her programlma dilinde ilk yazılan program "Merhaba Dünya" cümlesinin yazılmasıdır. Bu belgede de bu geleneği bozmayacağız
ve Kivy'i öğrenmeye bununla başlayacağız. IDLE'e kullanarak aşağıdaki program kodunu yazın ve :ref:`merhabaDunya` olarak kaydedin.

.. literalinclude:: ./programlar/merhabaDunya.py
    :linenos:
    :caption: merhabaDunya.py
    :name: merhabaDunya
    :language: python

Programı çalıştırdığınızda :ref:`merhabaDunyaImg` deki gibi bir pencere açılacaktır.



.. _merhabaDunyaImg:

.. figure:: ./resimler/ilkUygulama.png

   Merhaba Dünya

Biraz bu program üzerinde konuşalım. Buraya kadar geldiğinize göre ``import`` satırlarını
biliyor olmalısınız, bu nedenle burayı geçiyorum. Bütün Kivy programları bir ana
sınıf tarafından yönetilir. Bu anasınıf Kivy'deki ``App`` sınıfını içerir. Bu programdaki ana
sınıfımız ``ilkUygulama()``  dır. Ana sınıftaki ``build()`` işlevi mutlaka bir pencer düzeni döndürür
ve bu düzen program açıldığında kullanıcnın ilk gördüğü penceredir. Buradaki program
çok basit olduğundan bir pencere düzeni döndürmek yerine sadece bir etiket (``Label``) döndürmüştür,
ve bu etikat ana pencere olarak karşımıza çıkmaktadır. Uygulamanın çalıştırılması,
ana sınıfın ``run()`` özelliği ile yapılır. Buradaki ``ilkUygulama().run()`` satırı
uygulamamızın çalışmasını sağlar.

Eğer pencere ismi verilmemişse, pencerinin başlığında ana sınıfın ismi görünecektir. Pencere başlığını
değiştirmek için, ``title`` özelliğini kullanabiliriz. Sınıf tanımlanır tanımlanmaz hemen altında (``def build(self):``
ile aynı hizada) aşağıdaki satırı ekleyerek yapabilirsiniz:

::
	
	title = 'Benim Kivy Programım'
	
Bir diğer yöntem ise, ``build()`` işlevi altında ``return`` etmeden hemen önce şu satırı eklemektir:


::
	
	self.title = 'Benim Kivy Programım'
	
Benzer şekilde pencere için kullanılacak olan simgeyi de ``icon`` özelliğini kullanarak yapabilirsiniz. Son durumda ``build()``
işlevini şu şekilde yazabilirsiniz:

::

	def build(self):
		self.title = 'Benim Kivy Programım'
		self.icon = 'simge.png'
		return Label(text='Merhaba Dünya!')
        
        
``simge.png`` dosyası, ya ``merhaba_dunya.py`` dosyasının kaydedildiği yerde olmalı ya da tam patika yazılmalıdır. Örneğin ``resimler``
klasörüne koymuş iseniz:

::

	self.icon = 'resimler/simge.png'
	
şeklinde yazılmalıdır.

.. _merhabaDunyaPencereDuzenleri:

Pencere Düzenleri
=================
Bir pencereye birden fazla grafik parçacığı (widget) koyacaksanız, bir pencere düzeni oluşturmalısınız. Kivy programlarındaki pencere düzenleri iki şekilde oluşturulabilir: 

* Pencere düzenleri kodlarıya
* Kivy ``kv`` dili ile

Bu belge kapsamında ``kv`` dili kullanılacaktır. Ancak bir fikir vermesi açısından kodlayarak nasıl yapıldığını basit bir örnek
ile açıklamaya çalışalım. Şöyle bir pencereye ihtiyacımız olsun:


.. figure:: ./resimler/kullaniciGirisMockups.png

Bunun için altı adet grafik parçacığına (aslında pencere düzeni ile yedi) ihtiyacımız var. İki tanesi etiket (``Label``) iki tanesi metin kutusu (``TextInput``) ve bir
tanesi Düğme (``Button``). Bir tanede boş grafik parçacığı (``Widget``). Bu programı :ref:`girisFormu` gibi yazabiliriz.

.. literalinclude:: ./programlar/girisFormu.py
    :linenos:
    :caption: girisFormu.py
    :name: girisFormu
    :language: python
    

Programımız şimdilik bir işe yaramamaktadır. Tek yaptığı bir giriş penceresi
oluşturmak ve bunu kullanıcıya göstermektir. Düğmenin nasıl kullanılacağı, metin kutularındaki değerlerin nasıl alınacağı ileriki 
konularda anlatılacaktır. Burada  ``GridLayout()`` ile ızgara pencere düzeni oluşturulmuştur. Bu sınıfa verilen ``cols=2`` parametresi
ızgaranın iki sütundan oluşacağını söylemktedir. Kaç satırdan oluşuacağını belirtmiyoruz. Bir garfik parçacığına (burada ızgara pencere
düzeni) bir başka grafik parçacığını ``add_widget()`` ile ekliyoruz. Buradaki ızgaramız iki sütunlu olduğundan
ızgara düzenine eklenen her iki parçacık bir satırda bulunur ve daha sonra yeni satıra geçilir. 
Şimdi size bir soru: Sizce 25. satırı ``duzen.add_widget(Widget())`` neden yazmışızdır? 

Programımız çalıştığında :ref:`kullaniciGirisImg` deki gibi bir pencere açılacaktır. 


.. _kullaniciGirisImg:

.. figure:: ./resimler/girisFormu.png

   Giriş Formu


İkinci yöntem olarak, bir pencerenin görüntülenmesi ve pencere düzeni ve diğer birçok işlem için Kivy ``kv`` dili kullanılabilir,
bu muhteşem dil :ref:`kivyDili` bölümünde anlatılmaktadır.
