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

Bu satırları ekledikten sonra ``build()`` işlevindeki ``pass`` ifadesine gerek kalmayacak. 

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
     
İşimiz henüz bitmedi, çünükü düğmeye tıklandığında çağrılacak olan işlevi yazmadık, bunun için ``build()`` işlevinden hemen önce
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
özelliği ile. Bu özelliği dosya seçimi işleminden sonra çağrılacak olan işleve bağlayabiliriz. Bunun için
``FileChooserListView`` parçacığının ``on_selection`` özelliğini aşağıdaki gibi değiştirin
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
                dosyaAdi=os.path.split(secilen_dosya[0])[1]
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

Bu işlevi ``build()`` den hemen önce tanımlayabilirsiniz.

Aslında düzenlenen bir dosyayı bu şekilde doğrudan yazmak
akıllı bir programcını yapacağı iş değildir. Eğer bir nedenden dolayı dosya yazılamaz ise, program sonlanır ve 
kullanıcının önceki yeazdıkları da dahil olmak üzere kaybolur. Bu şekilde kaydedilirken bir problem çıkması durumunda
çoğu zaman boş bir dosya elde edilir. Olası durumları kontrol ettik, ancak birde kontrol edemediğimiz durumlar var. Öreğin
tam yazma aşamasında, elektrik kesilirse! Bu durumda kullanıcıya boş bir dosya verir bol küfür alırsınız. Tüm
programlama dillerinde diske yazma işlemi doğrudan gerçekleşmez, belirli bir buffer büyüklüğü vardır bu dolduğunda diske
yazılır daha sonra buffer'in tekrar dolması beklenir (hızdan tasaffur, disk kullanımından tasarruf gibi nedenlerle).
Bu nedenle dosya kapatılana kadar  (``close()``) yazma işleminden emin olmazsınız 
[her harfi yazdıktan sonra ``flush()`` kullanmamışsanız :-)]. En iyisi önce dosyayı geçici olarak yazmak, daha sonra
dosya adını değiştirmektir. Örneğin:

::

    F=open(dosya_tam_isim+'~', 'w')
    F.write(self.root.ids.metin.text)
    F.close()
    os.rename(dosya_tam_isim+'~', dosya_tam_isim)
    
Burada da yine dikkat etmemiz gereken şey, ``dosya_tam_isim`` dosyasının yazılabilir olduğundan emin olmaktır.
Bunuda

::

    os.access(dosya_tam_isim, os.W_OK)

ile kontrol edebilirsiniz. "Farklı Kaydet" bitti. Şimdi sıra geldi "Kaydet"e

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
işlevi çağrılıyor. Bunu daha önce yazmıştık. Dosya adı yok ise, ``farkliKaydetDialog()`` işlevi çağrılıyor.
Bunu da "Farklı Kaydet" kesitinde yazmıştık. Çok kolaymış değil mi?

Aç
======

Var olan bir dosyayı açmak için kullanacağımız bu düğme, eğer dikkatli olmazsak başımıza iş açabilir. Sebep?
Eğer düzenlenmekte olan bir dosya kaydedilmeden, başka bir dosya açılmaya kalkışılırsa ve siz bunu kullanıcya bildirmemişseniz,
bu durumda istenmedik laflar işitebilirsiniz (merak etmeyin, nasıl olas programı kullanan uzakta olacağından duymazsınız).
İşitmeseniz bile buna dikkat etmek iyi bir programcı olduğunuzu gösterir. Peki bir metnin değiştiğini ve kaydedildiğini
nasıl anlayacağız? Bunu bizim için yapacak bir kimse yok. Bu nedenle başımızın çaresine bakmalıyız.

Önce metnin değişip değişmediğini bilmemiz gerekiyor, bunu tanımlayacağımız
``self.metin_degisti`` değişkeni ile takip edebiliriz. O halde ``build()`` işlevi altına aşağıdaki satırları ekleyelim:

::

    self.metin_degisti=False
    
	
Değerini ``False`` yaptık çünkü başlangıçta bir netnin içeriği değişmemiştir. Metin değiştikçe bunun 
değerini ``True``, kaydettikçe değerini ``False`` yapmalıyız. Önce kaydettiğimizde değerin ``False`` olması
için ``dosyaKaydet()`` işlevindeki ``F.close()`` satırından hemen sonra şu satırı eklemeliyiz:

::

    self.metin_degisti=False

Bu tamam, peki metnin değiştiğini nasıl anlayacağız? Bunu bize Kivy söyleyebilir. ``TextInput`` perçacığının
``text``'ine bir işlev bağlarsak, metin değiştikçe bu işlev çağrılır. O halde ``build()`` işlevinin altına aşağıdaki
satırları eklemeliyiz:

::

    self.root.ids.metin.bind(text=self.metinDegisti)
    self.ilkAcilis=True
	
Buradaki ``self.ilkAcilis`` değişkeni, programın ilk açlıp açılmadığını takip etmek için gereklidir.
Çünkü ``TextInput`` nesnesi oluşturulur oluşturulmaz ``self.metinDegisti`` işlevi çağrılır. Buda programın ilk
açılıp açılmadığına göre ``self.metin_degisti`` değişkeninin değerini değiştirmelidir.
Bize gerekli olan ``metinDegisti()`` işlevini ``build()`` den hemen önce şöyle tanımlayabiliriz:

::

    def metinDegisti(self, nesne, deger):
        if self.ilkAcilis: self.ilkAcilis=False
        else: self.metin_degisti=True
        
Eğer programımız ilk açılışta bu işlev çağrılıyorsa, ``if self.ilkAcilis`` değişkeninin değeri ``False``
yapılıyor, sonraki çağrılışlarda (metin girişi yapılır veya dosya okunursa), ``self.metin_degisti``
değişkeninin değeri ``True`` yapılıyor.

Şu ana kadar dosya açma ile ilgili birşey yapmadık, sadece metnin değişip değişmediğini takip ettik.
Öncelikle dosya açılma işlemini tıpkı "Kaydet"de olduğu gibi, bir dizin tarayıcı oluşturmamız gerekiyor.
Bunu yine ``FileChooserListView`` ile yapabiliriz. Bunun için bir form ve bu formu oluşturacak ``kv``
kodlarına ihtiyacımız var. ``metinduzenleyici.kv`` dosyasına aşağıdaki kodu ekleyin:

.. literalinclude:: ./programlar/metinDuzenleyici/4/dosyaAcForm.kv
    :linenos:
    :tab-width: 4
    :caption: dosyaAcForm
    :name: metin_duzenleyici_dosyaAcForm

Bu ``kv`` formunu kullanacak sınıfı tanımlamak gerekiyor. Bunu ``class metinDuzenleyici(App)`` satırından önce aşağıdaki
kodları ekleyerek yapabiliriz:

::

  class dosyaAcForm(Popup):
      pass


Şimdide "Aç" düğmesine tıklandığında çağrılacak olan işlevi ``kv`` dosyasında belirtelim. 
Bunun için :numref:`metin_duzenleyici_kv1`'deki 14. satırı aşağıdaki satırı şöyle değiştirelim:

::

    on_press: app.dosyaAcIsleviDialog()
	
	
Şimdi de bu işlevi tanımlamak gerekiyor. ``build()`` den hemen önce işlevimizi şöyle tanımlayabiliriz:

::

    def dosyaAcIsleviDialog(self):
        if self.metin_degisti: 
            self.hataGoster("Dosya kaydedilmedi. Önce kaydedin.")
        else: 
            self.dosyaAcDialog()


Bu işlev anladığınız üzere, dosyanın değişip değişmediğini kontrol ediyor. Eğer kaydedilmemişse,
kaydetmesi için uyarıyor. Kaydedilmiş ise, ``dosyaAcDialog()`` işlevini çağırıyor. O halde bu işevi de 
``build()`` den hemen önce şu şekilde tanımlayabiliriz:

::

    def dosyaAcDialog(self):
        form = dosyaAcForm()
        form.open()

"Dosya Aç" formu açıldığında allta iki adet düğmemiz olacak. "Vazgeç" düğmesine tıklandığında form kapanacak. "Aç"
düğmesine tıklandığında ise, ``dosyaOku()`` işlevi çağrılıyor (``metinduzenleyici.kv`` dosyasına eklediğimiz
:numref:`metin_duzenleyici_dosyaAcForm`'deki 17. satır). Bu işlev oldukça basit, sadece seçilen 
dosyayı gidip okuması gerekiyor. Bunu da ``build()`` den hemen önce aşağıdaki gibi tanımlayabiliriz:

::

    def dosyaOku(self, dosya_secim):
       if dosya_secim.selection:
            if len(dosya_secim.selection)>0:
                (self.son_patika,self.son_dosya)=os.path.split(dosya_secim.selection[0])
                try:
                    self.root.ids.metin.text=open(dosya_secim.selection[0]).read()
                    self.root.ids.metin.cursor=self.root.ids.metin.get_cursor_from_index(0)
                    self.metin_degisti=False
                except:
                    self.hataGoster("Dosyayı Okuyamadım. Nedeni: [color=#FF0000]%s[/color]"
                                 % str(sys.exc_info()[1][1]))
       else:
            self.hataGoster("Dosya seçtiğinizden eminmisiniz?")

Bu işlevdeki hemen herşeyi daha önce anlattık. Şimdi bir sorunumuz var (bitti mi ki?). Kullanıcı dosyayı düzenleyip
yeni dosya açmak istediğinde sadece "Dosya kaydedilmedi. Önce kaydedin." uyarısında bulunuyor. Oysa ki iyi bir program
dosyayı açmadan önce dosyanın değiştiğini uyarmalı ve kullanıcıya kaydedip kaydetmeyeceği ile ilgili
seçenek sunmalıdır. Bunun için yeni bir form tasarlamalıyız. Bu form sedece mevcut dosyanın kaydedilip kaydededilmemesini
veya dosya açma işleminden vazgeçilmesini önermelidir.  Böyle bir formu ``metinduzenleyici.kv`` dosyasına
aşağıdaki satırları ekleyerek tasarlayabiliriz:

.. literalinclude:: ./programlar/metinDuzenleyici/4/dosyaKaydedilmediForm.kv
    :linenos:
    :tab-width: 4
    :caption: dosyaKaydedilmediForm
    :name: metin_duzenleyici_dosyaKaydedilmediForm

Bu ``kv`` formunu kullanacak sınıfımızı  ``class metinDuzenleyici(App)`` satırından önce aşağıdaki
kodları ekleyerek yazabiliriz:

::

    class dosyaKaydedilmediForm(Popup):
        pass
        
Peki bu form'u nerede çağıracağız? Bildiniz değilmi? Yoksa bilemediniz mi? Bilemeyenlere hemen söyleyeyim, 
``dosyaAcIsleviDialog()`` işlevinde dosya açmak istediğinde "Dosya kaydedilmedi. Önce kaydedin." 
uyarısında bulunuyorduk ya işte burada. Yani bu uyarının yapıldığı satırın yerine yazmalıyız. 
O halde ``dosyaAcIsleviDialog()`` işlevini aşağıdaki gibi değiştirmeliyiz:

::

    def dosyaAcIsleviDialog(self):
        if self.metin_degisti:
            kaydedilmedi_form = dosyaKaydedilmediForm()
            kaydedilmedi_form.open()
        else:
            self.dosyaAcDialog()


Dosyanın kaydedilmediği durumda dosya açmaya kalkışıldığında kullandığımız form'da kullanıcı "Kaydet" düğmesine
tıklarsa dosyamızın kaydedilmesi için ``dosyaKayedilmediKaydet()`` işlevi çağrılmaktadır
(:numref:`metin_duzenleyici_dosyaKaydedilmediForm`'deki 15. satır). Bu işlevi ``build()`` den önce şu şekilde yazabiliriz:

::

    def dosyaKayedilmediKaydet(self, kok):
        if self.son_dosya: 
            self.dosyaKaydet()
            kok.dismiss()
            self.dosyaAcDialog()
        else:
            kok.dismiss()
            self.hataGoster("Dosya adı yok. 'Farklı Kaydet' kullanarak kaydetmelisiniz.")

Burada benimde hoşalşamadığım ve birçok kullanıcı için de garip gelecek bir durum var.
Eğer dosya daha önce kaydedilmemiş ise, dosya adı (``self.son_dosya`` değişkeninde saklanan)
olmayacaktır ve bu durumda kullanıcıya "Farklı Kaydet"i kullanarak kaydetmesi önerisi sunulmaktadır.
Oysa ki bunun yerine doğrudan farklı kaydet dialoğu (``farkliKaydetDialog()``) çağrılmalıydı.
Bu Kivy'de olmadı. Bunu yapabilmemiz için, bu diyalog açıldıktan sonra, programın kullanıcıdan
tepki gelene kadar hiçbir iş yapmaması gerekir (diğer bir deyişle program akışı durdurulmalıdır).
Kivy'de ne yazıkki bu yok, en azından ben bilmiyorum.

Yeni
======

Kullanıcı bir dosya üzerinde çalışırken yeni bir dosya açmak isteyebilir. Bunun için ana penceremizin sağ alt
tarafya bunulnan "Yeni" düğmesine tıklayacak. Şimdi bunun üzerinde çalışalım. Yapacağımız işi şöyle özetleyebiliriz:
ilk olarak mevcut dosya değiştirilmiş ve henüz kaydedilmemiş ise, bunu kullanıcıya bildirmemiz gerekir, daha sonra
yeni dosya oluşturma işlemine geçeceğiz. Öncelikle ana penceredeki "Yeni" düğmesine tıklandığında
çağrılacak olan işlevi belirtmek için ``metinduzenleyici.kv`` dosyasındaki (:numref:`metin_duzenleyici_kv1`)
23. satırı şu şekilde değiştirmemiz gerekmektedir:

::

    on_press: app.yeniDosyaAcIslevi()
    
Bu işlevi de ``build()`` den önce şu şekilde yazabiliriz:

::

    def yeniDosyaAcIslevi(self):
        if self.metin_degisti:
            form = yeniDosyaForm()
            form.open()
        else:
            self.yeniDosyaAc()

Burada metnin değişmesi durumumnda yeni bir dialog (form) açılacak. Bu forma ait ``kv`` kodlarını
``metinduzenleyici.kv`` dosyasına aşağıdaki satırları ekleyerek oluşturabiliriz:

.. literalinclude:: ./programlar/metinDuzenleyici/5/yeniDosyaForm.kv
    :linenos:
    :tab-width: 4
    :caption: yeniDosyaForm
    :name: metin_duzenleyici_yeniDosyaForm

Bu ``kv`` kodlarını kullanacak olan ``yeniDosyaForm()`` sınıfınıda ``class metinDuzenleyici(App)`` satırından önce aşağıdaki
kodları ekleyerek yazabiliriz:

::

    class yeniDosyaForm(Popup):
        pass

        
yeniDosyaForm'unda kullanıcı yeni dosya açmaktan vazgeçerse
zaten form kapanıyor, eğer kaydetmek için "Evet" düğmesine tıklarsa, ``yeniDosyaAc()`` işlevi çağrılıyor.
Yeni dosya açma işlevini ``build()`` den hemen önce şöyle yazabiliriz.

::

    def yeniDosyaAc(self):
        self.root.ids.metin.text=""
        self.son_dosya=""

En kolayı bu oldu sanırım, ``self.son_dosya`` değişkeninin değeri ile metin alanının değerini boş cümle yaparak
yeni dosyayı oluşturmuş olduk.

Çıkmadan Önce
===============

Henüz bitmedi. Çıkmadan önce yapılacak işlerimiz var. Kullanıcı metni düzenlerken çıkmak isterse ne yapacağız?
Öncelikle, maobil cihazın "Geri" tuşuna basarak programdan çıkması engellenmeli ve çıkış kontrollü bir şekilde
yapılmalıdır. "Geri" tuşuna basarak çıkmayı engellemek için programın başında bunu yapmak gerekiyor, yani daha
uygulamayı başlatmadan önce. Geri tuşu ile çıkışı engellemek için ``main.py`` programının ikinci ve üçüncü
satırına aşağıdaki kodları yazabilirsiniz:

::

    from kivy.config import Config
    Config.set('kivy', 'exit_on_escape', 'False')

aslında :index:`Config` modülü daha fazla iş yapabilmektedir. Burada sadece geri tuşu ile çıkmayı engellemek için
kullandık, bunu :index:`exit_on_escape` parametresini ``False`` yaparak gerçekleştirmiş olduk. Windows ya da Linux'da
pencere kapatma düğmesi ile hala programdan çıkılıyor olmalı, bunu dikkate almayın çünkü nasıl olsa programımız
mobil cihazlarda çalışacak. Geri tuşu ile çıkmayı engelledik te, kullanıcı nasıl çıkacak? İsterseniz ana penceremizin
sağ alt köşesine küçük bir düğme koyalım ve bu düğmeye tıklandığında çıkışı gerçekleştirelim. Böylelikle çıkmak isteyen
kullanıcı bu tuşa basacak ve bir işlev çağrılacaktır. Bu işlevde istediğimizi kontrol edebiliriz. Çıkış düğmesini
eklemek için ``metinduzenleyici.kv`` dosyasının (:numref:`metin_duzenleyici_kv1`) ana pencere düzenini oluşturan
``metinDuzenleyici`` formunun altındaki düğmeleri oluşturan ``BoxLayout`` altına aşağıdaki gibi bir düğme ekleyelim:

::

        Button:
            id: cik_dugmesi
            size_hint_x: .15
            background_color: (0, 1, 0, 1)
            on_press: app.cik()

Dikkat etmişseniz, oldukça küçük bir düğme (%15 boyutunda) ve arka plan rengi yeşil olarak görünecek.
Bir düğmenin :index:`arka plan rengi` ni :index:`background_color` özelliği ile ayarlayabiliyoruz. Bu özellik,
diğer Kivy :index:`renk` tanımlarında da kullanılabileceği gibi, bir tüp 
(isterseniz bir liste) alır. Bu tüpün 4 elemanı olacaktır. Bu tüp ile rengi şöyle belirliyoruz:

::

  (R, G, B, T)
    
Buradaki harfleri anlamları şöyledir:

**R**: Kırmızı, **G**: Yeşil, **B**:Mavi
    
Renk oranlarını belirtmektedir. değerleri 0 ile 1 arasındadır. Bildiğimiz standart :index:`RGB` ile aynı ancak 1 sayısı 255'e
karşılık gelmektedir. En sondaki **T** Saydamlığı belirtmektedir. Bu değere 1 girerseniz tam katı (kesif, opak), 0 girerseniz tam saydam olur.

Tekrar dönelim düğmemize, akrka plan rengini neden yeşil yaptık? Çünkü yeşil doğa ve orman rengi değil mi? :-)
Elbette bunun için değil, düğme yeşil olduğunda çıkış serbest olacak, kırmızı olduğunda metin değiştirilmiş
fakat kaydedilmemiş olacak. O halde programımız içerisinde

::

    self.metin_degisti=False

satırının olduğu her yerde aşağıdaki satırı ekleyerek düğmeinin yeşil renkli olmasını sağlayacağız:

::

    self.root.ids.cik_dugmesi.background_color = [0, 1, 0, 1]
    
Peki ne zaman kırmızı yapacağız? ``self.metin_degisti`` değişkeninin değerinin ``True`` olduğu yerlerde. Bunu da 
programımız içerisindeki

::

    self.metin_degisti=True

satırının olduğu her yerde aşağıdaki satırı da eklemeliyiz:

::

    self.root.ids.cik_dugmesi.background_color = [1, 0, 0, 1]
    
Bu satırları yazmayı ben başarabildim, eminim (aslında Mustafa'yım da sözün gelişi) sizde yapabileceksiniz.
Çık düğmesinin yeşile dönmesi gereken bir yer daha kaldı: `yeniDosyaAc()` işlevi. Bu işlevin en sonuna da aşağıdaki
satırı eklemeliyiz:

::

    self.root.ids.cik_dugmesi.background_color = [0, 1, 0, 1]
    
Şimdi programınızı çalıştırın ve düğmenin rengini takip edi. Program açılışta yeşil renki çık düğmesi ile başlayacak.
Ne zaman metin yazarsanız, renk kırmızıya dönecek. Metni kaydettiğinizde tekrar yeşile dönecek. Ancak henüz çık düğmesi
işe yaramıyor çünkü düğmeye tıklandığında çağrılacak olan ``app.cik()`` işlevini yamadık. Önce bu düğmenin nasıl 
davranacağını düşleyelim. Bir defa metin değişmiş ise, programdan çıkmadan önce kaydedilip kaydedilmeyeceğini
sormalı. O zaman bir tane form oluşturmalıyız ve bunu sormalıyız. ``metinduzenleyici.kv`` dosyasına aşağıdaki
gibi bir form ekleyelim:

.. literalinclude:: ./programlar/metinDuzenleyici/6/cikmadanOnceForm.kv
    :linenos:
    :tab-width: 4
    :caption: cikmadanOnceForm
    :name: metin_duzenleyici_cikmadanOnceForm
    
    
Bu form'da bilmediğiömiz tek şey :index:`stop()` işlevidir. Bu işlev uygulamadan çıkma işlemini gerçekleştirir. 
Bu formu kullanacak sınıfımızı da ``class metinDuzenleyici(App)`` satırından önce aşağıdaki
kodları ekleyerek yazabiliriz:

::

    class cikmadanOnceForm(Popup):
        pass

Son olarak ``cik()`` işlevini yazalım. ``build()``'den hemen önce aşağıdaki satırları yazalım:

::

    def cik(self):
        if self.metin_degisti:
            kaydedilmedi_form = cikmadanOnceForm()
            kaydedilmedi_form.open()  
        else:
            self.stop()

Programımız artık temel ihtiyaçları karşılayacak düzeye geldi. Peki bitti mi? Haaayııır. Neler kaldı?
Hayal etmenin sınırı yok. Örneğin son açılan dosyaların listesi, program açıldığında en çalışılan dosyanın
otomatik açılması, kelime bulma ve değiştirme ... Başka ? Bir de kahve yapsın, yemek istemiyoruz :-)

Anlattıklarımızı takip edemediyseniz, yada ben yaptıklarımı gözden kaçırıp eksik yazmışsam,
bu bölümde anlattıklarımı yaptığım dosyaları şu adreslerden alabilirsiniz:

main.py: https://github.com/mbaser/kivy-tr/blob/master/docs/programlar/metinDuzenleyici/6/main.py

metinduzenleyici.kv: https://github.com/mbaser/kivy-tr/blob/master/docs/programlar/metinDuzenleyici/6/metinduzenleyici.kv
