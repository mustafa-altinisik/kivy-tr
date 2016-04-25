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

Ana Pencere
===========

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

``main.py`` programı çalıştırdığımızda metin düzenleyicimizin penceresi Sonucu :numref:`Şekil %s <metinDuzenleyici1Img>` 'deki gibi açılacaktır.


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

Farklı Kaydet
=============

Bir dosyayı kaydetmek için, öncelikle kaydedilecek klasörün belirtilmesi ve daha sonra da dosya adının 
girilmesi gerekir. Eğer kullanıcıya basitçe bir metin kurtusu sağlayıp buraya dosyanın tam patikasını yazmasını
isterseniz (örneğin ``C:\dosyalarım\odevlerim\fizik\newton.txt`` şeklinde), kusura bakmayın ama programınızı
kimse kullanmaz. 1990'lı yıllarda olsaydınız buna kimse itirtaz etmezdi ancak şimdi GUI (Grafik Kullanıcı Arayüzü)
icat edildi. O halde klasörler arasında gezinti yapabilecek bir arayüze ihtiyacımız var. Bun kendiniz yapabilirsiniz.
Nasıl mı? ``os.listdir()``'i biliyorsunuz. Her bir elemanı ızgara düzenine bir düğme olarak yerleştirip gezinti
sağlayabilirsiniz. Ama bunu yapmayın. Çünkü Kivy geliştiricileri bizim için daha iyisini yapmış:
:index:`FileChooserListView`. Bu grafik parçacığı bize dizinler arası gezinti yapmamızı sağlayacak bir araç
sunmaktadır. Bu parçacığın :index:`filters` özelliği sayesinde, hangi dosyaları liseteleyeciğimizi de 
belirtebiliyoruz (aşağıda ``['*.*']`` kodu tüm dosyaların listeleneceğini göstermektedir.
Üstelik bir seçim yaptığımızda :index:`on_selection` olayı sayesinde, seçim ile ilgili
işlemlerimizi yapabiliyoruz. O halde bu parçacığı en üste koyalım, altına bir adet dosya adının yazılabileceği
metin kutusu, onun altına da iki adet düğme: "Kaydet", "Vazgeç". O halde metin düzenleyicimizin pencerelerinin
oluşturulduğu ``metinduzenleyici.kv`` dosyasına aşağıdaki gibi yeni bir form ekleyelim:

.. literalinclude:: ./programlar/metinDuzenleyici/2/farkliKaydetForm.kv
    :linenos:
    :tab-width: 4
    :caption: FakrliKaydetForm
    :name: metin_duzenleyici_FakrliKaydetForm


Bu formu kullanacak bir sınıf tanımlamak gerekiyor. Bunu ``class metinDuzenleyici(App)`` satırından önce aşağıdaki
kodları ekleyerek yapabiliriz:

::

  class farkliKaydetForm(Popup):
      pass


Dosya ismini  ve kaydedildiği patikayı takip etmemiz gerekmektedir. Nedenini şöyle açıklayabiliriz, eğer bir dosya açılmış
(ya da bir isimle kaydedilmiş) ise, dosya ismi var olacağından tekrar kaydedilmesi sırasında bı dosya ismini
kullanmamız gerekmektedir. Dosya ismi gerekli ise, kaydedildiği klasör de gereklidir. O halde tüm programımız içerisinde
dosya ismi ve patikayı kullanabileceğimizden, ``build()`` işlevine aşağıdaki satırları eklememiz gerekecek.

::
  
  self.son_patika= os.getcwd()
  self.son_dosya=''

Sanırım ``main.py`` programının başında ``os`` modülünü çağırma nedenimizi anladınız. Burada son patika
ön tanımlı olarak programın çalıştığı patikayı göstermektedir, son dosya ise boş bir cümledir, yani dosya adı yoktur.

Ana pencerede "Farklı Kaydet" düğmesine tıklandığında ``farkliKaydetForm``'nun açılabilmesi için, üzerinde "Farklı Kaydet"
yazan düğmeye tıklandığında bir işlevin çağrılması ve bu işlev altından da bu formu gösterebilmemiz gerekiyor. O halde
bu düğmenin ``on_press`` özelliğini ``farkliKaydetDialog()`` işlevini çağıracak şekilde aşağıdaki gibi değiştirelim 
(:numref:`metin_duzenleyici_kv1`'deki 18, 19 ve 20. satırlar):

::

  Button:
      text: "Farklı Kaydet"
      on_press: app.farkliKaydetDialog()
     
İşimiz henüz bitmedi, çünükü düğmeye tıklandığında çağrılacak olab işlevi yazmadık, bunun için ``build()`` işlevinden hemen önce
aşağıdaki işlevi tanımlayalım:

::

  def farkliKaydetDialog(self):
      form = farkliKaydetForm()
      form.open()
        
        
Artık "Farklı Kaydet" düğmesine tıkladığımzda yeni bir pencere açılmaktadır. 
Açılacak olan pencereyi :numref:`Şekil %s <metinDuzenleyiciFarkliKaydetImg>` 'de görüyorsunuz:

.. _metinDuzenleyiciFarkliKaydetImg:

.. figure:: ./programlar/metinDuzenleyici/3/metinDuzenleyiciFarkliKaydetImg.png

   Farklı Kaydet Penceresi
   

 

Peki bu pencere şu anda ne iş yapar? 
Sadece dosya ve klasörleri listeler (bunuda biz yapmadık :ref:`metin_duzenleyici_FakrliKaydetForm`'de 7. satırda tanımladığımız
``FileChooserListView`` parçacığı yapıyor). Haa birde çok büyük bir iş olan "Vazgeç" düğmesine tıklandığında
pencere kapanıyor. Sanırım bunu bizden başka başarabilecek kimse de yok :-). Peki bu nasıl gerçekleşiyor?
Pencerenin kapanmasını bizim yazdığımız kod sağlamkta, şaka yapmıyorum :-) Peki nersi? Yanılmıyorsam 
(yanılıyorsam lütfen beni uyarın!), :ref:`metin_duzenleyici_FakrliKaydetForm`'deki 30. satır bu işi yapıyor olmalı.

Az zamanda çok işler başardığımızı söylemek isterdim, ancak gerçek bu değil. Daha henüz işe yarar birşey yapmadık.
Öncelikle ``FileChooserListView`` parçacığının gösterdiği dosya isimleri üzerine tıklandığında (diğer bir deyişle
var olan dosya ismini seçip bu dosya üzerine kaydetmek isteyebilir, aman dikkat !! çok tehlikeli, kaydetmeden önce
onay almalısınız, bunu size bırakıyoruz) bu dosya isminin dosya adı yazılacak olan (``id``'si ``dosya_adi`` olan
TextInput parçacığı) metin kutusunda belirmelidir. Bunu nasıl yapacağız? Daha önce demiştik ya ``on_selection``
özelliği ile. Bu özelliği dosya seçimi işleminden sonra çağrılacak olan işleve bağlayabiliriz. Yada böyle
basit işler için yeni işlev tanımlamaya gerek kalmadan ``kv`` dosyasında işimizi halledebiliriz. İşte şöyle
(:ref:`metin_duzenleyici_FakrliKaydetForm`'de 12. satırı aşağıdaki gibi değiştirin):

::

  on_selection: app.farkliKaydetSecim(root)
  
Burada ne yapılıyor? Her sonunun cevabını verdik te bunun cevabını mı esirgeyelim? Burada yapılan iş, formun kendisini
uygulamanın ``farkliKaydetSecim()`` işlevine argüman olarak göndermek. Gerisini bu işlev halletmektedir. O zaman bu işelvi
yazmalıyız. ``build()``'den hemen önce aşağıdaki işlevi tanımlayalım:

::

    def farkliKaydetSecim(self, form):
        secilen_dosya=form.ids.dosya_secim.selection
        if secilen_dosya:
            if len(secilen_dosya)>0:
                dosyaAdi=os.path.split(secilen_dosya[0])
                form.ids.dosya_adi.text=dosyaAdi
              
Bu işleve ``farkliKaydetForm``'nun kendisi argüman olarak geliyordu, bunu ``form`` değişkenine aktardık.
``FileChooserListView`` nesneninden seçilen dosyayı ``selection`` özelliği ile alabaliriz. Bu bize seçilen
tüm dosyaları (çoklu seçim yapılabilir, :index:`multiselect` özelliğinin değeri ``True`` yapılarak).
Ön tanımlı olarark sadece bir dosya seçilebildiğinden, ilk dosyayı patika ve dosya adı olarak ayırdıktan sonra
yaptığımız iş dosya adını formumuzda ids'si ``dosya_adi`` olan metin kutusunda göstermektir.

Şimdi gelelim "Kaydet" düğmesine tıklandığında yapılacak olan işe: formadki metin kutusundan dosya adını alacak ve
diske yazma işlemi gerçekleştirilecek. Diske yazma işlemini farklı bir işlevde yapacağız, çünkü ana pencerede 
"Kaydet" düğmesine tıklandığında da bu işlevi çağıracağız. Önce "Kaydet" düğmesine tıklandığında çağrılacak olan
işlevi belirtmeliyiz, ardındanda bu pencereyi kapatmalıyız. O halde :ref:`metin_duzenleyici_FakrliKaydetForm` deki
27. satırı şu şekilde değiştirelim:

::

  on_press: app.farkiKaydetIslevi(root); root.dismiss()

Gelelim ``farkiKaydetIslevi()`` işlevine: bu işlevi ``build()`` den hemen önce şu şekilde tanımlayabiliriz:

::

    def farkiKaydetIslevi(self, form):
        self.son_patika=form.ids.dosya_secim.path
        self.son_dosya=form.ids.dosya_adi.text
        self.dosyaKaydet()
        
Bu basit işlevde, formda dosyanın patikası alınıp ``self.son_patika`` değişkenine aktarılıyor. Benzer
şekilde ``self.son_dosya`` değişkenine formdaki ids'si ``dosya_adi`` olan metin kutusundaki dosya adı aktarılıyor.
Son olarak ``dosyaKaydet()`` işlevi çağrılıyor. Şimdi de bu işlevi yazalım (``build()`` den hemen önce):

::

    def dosyaKaydet(self):
        if not self.son_dosya:
            self.hataGoster("Dosya adı verdiğinizden eminmisiniz?")
        else:
            try:
                dosya_tam_isim = os.path.join(self.son_patika, self.son_dosya)
                F=open(dosya_tam_isim, 'w')
                F.write(self.root.ids.metin.text)
                F.close()
            except:
                self.hataGoster("Dosyayı yazamadım. Nedeni: [color=#FF0000]%s[/color]"
                                 % str(sys.exc_info()[1][1]))

Tahmin ettiğinizden daha karmaşık değilmi? Bir defa ``hataGoster()`` diye bir işlevin tanımlanması gerekiyor. 
Eğer kullanıcı dosya adı yamamış ise (formdaki ids'si ``dosya_adi`` olan metin kutusu boş ise), kullanıcıya
popup pencere ile bunu bildirmeliyiz. Bunu ``hataGoster()`` işlevini tanımlayarak yapabiliriz. Eğer dosya
ismi var ise, yazma işlemi gerçekleştirilecek. Bu ise biraz tehlikeli bir iş, öncelikle dosyanın tam adı
oluşturuluyor (``self.son_patika`` ve ``self.son_dosya`` değişkenlerinin değerleri ``os.path.join()`` ile).
Son olarak dosya açılıyor ve üzerine yazılıyor. Bunu ``try:`` bloğunda yaptık, çünkü dosya bir sebepten dolayı
yazılamayabilir. Nasıl bir sebep olabilir ki? Şöyle: disk dolu olabilir, dosyaya yazma yetkisi olmayabilir,
klasöre yazma yetkisi olmayabilir, böyle bir disk olmayabilir .... Her ne sebeptenolursa olsun, dosya 
yazılamadığında programın kırılmayacak ve ``except:`` bloğu işletilerek dosyanın yazılamama sebebi
kullanıcıla iletilecek. Bu da yine ``hataGoster()`` işlevi çağrılarak yapılıyor. Peki bu ``hataGoster()`` işlevi
kimin nesi? Kimsenin birşeyi değil! Sadece aşağıdaki kodlardan oluşan gariban bir işlev:

::

    def hataGoster(self, hata):
        icerik=Label(text=hata, markup=True)
        popup = Popup(title='Yapamadım !', content=icerik)
        popup.size_hint = (0.7,0.7)
        icerik.bind(on_touch_down=popup.dismiss)
        popup.open()

Bu işlevi ``build()`` den hemen önce tanımlayabilirsiniz. "Farklı Kaydet" bitti. Şimdi sıra geldi "Kaydet"e

Kaydet
======

Bu sandığınızdan daha kolay. Çünkü birçok işi, "Farklı Kaydet"de yaptık. Öncelikle ana pencerede "Kaydet" düğmesinde
tıklandığında bir işlev çağırmalıyız ve tüm işi bu işelve yaptırtmalıyız. Bunun için :numref:`metin_duzenleyici_kv1`'deki
17. satırı aşağıdaki gibi değiştirelim:

::

  on_press: app.dosyaKaydetIslevi()
  

Şimdi de bu işlevi yazalım, ``build()`` den hemen önce şu şekilde tanımlayabiliriz:

::

    def dosyaKaydetIslevi(self):
        if self.son_dosya: self.dosyaKaydet()
        else: self.farkliKaydetDialog()

Burada dikkat ederseniz, öncelikle dosya adının olup olmadığına bakılıyor. Dosya adı var ise doğrudak ``dosyaKaydet()``
işlevi çağrılıyor. Bunu daha önce yazmıştık. Dosya adı yok ise, ``farkliKaydetDialog()`` işlevi çağrılıoyor.
Bunu da "Farklı Kaydet" kesitinde yazmıştık. Çok kolaymış değil mi?
