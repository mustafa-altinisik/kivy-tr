.. _paketleme:

##########
Paketleme
##########

.. Caution::

    Bu bölüm taslak halindedir.

Bu bölümde hazırlanan Kivy programının Android paketi haline getirilmesi anlatılacaktır.

:index:`Buildozer` Kurulumu
****************************

Kivy programlarını paketlemenin en kolay yolu Buildozer kullanmaktır. Ne yazıkki Buildozer şimdilik sadece Linux'ta çalışmaktadır.
Windows kullanıcıları için VirtualBox üzerinde Sanal Linux Makina disk görüntüsü hazırlanmıştır. Windows kullanıcıları belkide çoğu
Linux kullanıcıları :ref:`SanalLinux` bölümünde anlatılanları yapabilirler.

Burada sadece Debian Jessie'de (8.3) nasıl kurulacağını anlatacağız. 
Sisteminizde ``git`` kurulu değilse: 

.. code-block:: console

  # apt-get install git

Yazılım havuzundan indirelim:

.. code-block:: console

  # git clone https://github.com/kivy/buildozer.git
  
Kurulumu gerçekleştirelim:

.. code-block:: console

  # cd buildozer
  # python setup.py install

Eğer sisteminizde eksik paket var ise, size hangilerinin eksik olduğu bildirilecektir. Bu kurulum yeni kurulmuş  Debian Jessie'de (8.3) de
denenmiştir. İleriki zamanlarda buildozer debian paketi çıkarsa daha kolay kurulum gerçekleştirilebilir.

Muhtemelen sisteminizde zlib1g-dev ve Cython kurulu olmayacak:

.. code-block:: console

  # apt-get install zlib1g-dev
  # apt-get install cython
  
Henüz Java derleyicisini kurmamış iseniz:

.. code-block:: console

  # apt-get install gcj-jdk 

Buildozer'in paketleyebilmesi için 32 bit kütüphanelere ihtiyacı olacak. Şu şekilde kurabilirsiniz:


.. code-block:: console

  # dpkg --add-architecture i386
  # apt-get update
  # apt-get install build-essential ccache git lib32z1 libncurses5:i386 libstdc++6:i386 python2.7 openjdk-7-jdk unzip zlib1g-dev zlib1g:i386


Muhtemelen aapt (Android Asset Packaging Tool) ihtiyacımız olacak:

.. code-block:: console

  # apt-get install aapt

Tüm bu anlattıklarımı, VirtualBox üzerinde bir sanal makinada yaptım ve kullanımınız için "...." adresine koydum. Tek yapmanız gereken
VirtualBox'u kurmak.


Paket Derleme
**************

Paket haline getirmek için önce başlatalım:


.. code-block:: console

  $ buildozer init

Daha sonra buildozer.spec dosyasını düzenleyelim. Ben sadece aşağıdaki değişiklikleri yaptım:

::

  # (str) Title of your application
  title = Kivy Metin Duzenleyici

  # (str) Package name
  package.name = kiviymetinduzenleyici

  
  
 
Şimdi de sıra paketlemeye geldi:

.. code-block:: console

  $ buildozer android release

İlk kez paketleme yapıyorsanız, ANT, SDK, NDK indirilecektir. Lütefn sabırlı olun. Daha sonra paketleme işlemi yapılacaktır. Benim
sanal makinamda bu işlem 10 dakikadan fazla sürmektedir. Şu şekilde sonlanması gerekir:

# Android packages installation done.
# Check application requirements
# Check garden requirements
# Compile platform
# Distribution compiled.
# Build the application #1
# Package the application
# Android packaging done!
# APK KivyMetinDuzenleyici-0.1-release-unsigned.apk available in the bin directory




İmzalama
********

Paketinizi kurmadan önce imzalamanız gerekir. Bunun en kolay yolu `apk-signer <http://shatter-box.com/download/android/apk-signer-1.8.5.zip>`_
kullanmaktdır. Programı indirdikten sonra zip paketini açın çalıştırın. Tarafımdan hazırlanan Sanal Linux Makina  kullanıyorsanız, masaüstünde `apk-signer`
simgesi üzerine tıklayın. 

Anahtar Oluşturma
-----------------

Önce anahtar oluşturacağız (:ref:`SanalLinux` kullananlar için `kivy` ev klasöründe bir tane anahtar mevcut). Programınız çalıştığında *Key Generator*
sekmesinde olacaktır. Bu sekmede iken ilk yapacağınız anhtarınızı kaydedeceğiniz dosyayı belirlemek. Bu amaçla *[ Save as... ]* düğmesine tıklayın.
Anahtarınızı kaydedeceğiniz klasörü seçin (bizdeki örnekte `/home/kivy`) ve dosya adını yazın (biz `benim` yazdık). Yaptıklarımız
:numref:`anahtarDosyasiImg` görünmektedir.


.. _anahtarDosyasiImg:

.. figure:: ./resimler/paketleme/anahtarDosyasi.png

   Anahtar Dosyası

Daha sonra gerekli bilgileri doldurun. *Password* ve *Confirm* alanlarına aynı parolayı girin (en az 8 karakter). Bizim örneğimizde
`kivy123` girdik. Bir *Alias* belirleyin, biz `Kivy` yaptık. Alias'ınız için yine parola (*Alias password* ve *Confirm* alanlarına)
girin. Biz yine `kivy123` girdik. Bu parolaları unutmayın, çünkü bundan sonra imzalayacağınız her pakette kullanacaksınız. Diğer
alanları istediğiniz gibi doldurun. :numref:`anahtarDosyasiImg`'de oluşturduğumuz anahtar için bilgilerin girilmiş hali görünmektedir.

.. _anhatarOlusturmaImg:

.. figure:: ./resimler/paketleme/anahtarOlusturma.png

   Anahtar Oluşturma

*Generete Keyfile* düğmesine tıklayarak anahtarınızı oluşturun.

İmzalama
---------
Anahtarınızı (aslına imzanız) oluşturduktan hemen sonra paketinizi imzalayabilirsiniz. Bunun için *Signer* sekmesine geçin. 
Önce *[ Load Keyfile... ]* düğmesine tıklayarak, oluşturduğunuz anahtarı seçin. Eğer oluştruruken yukarıdaki gibi `benim` 
yazmışsanız, ev dizininizde `benim.keystroke` dosyasını seçin. Bu imzanın parolasını *Password* alanına yazın. Bir Alias seçin 
(yukarıda `Kivy` yazdık) ve bunun parolasını *Alias password* alanına girin. *[ Load target file... ]* düğmesine tıklayın. Açılan
pencerede imzalamak istediğiniz paketi seçin, biz Kivy Metin Düzenleyici'yi derlemiştik onu seçiyoruz (`MetinDuzenleyici/bin/
KivyMetinDuzenleyici-0.1-release-unsigned.apk`). Yaptıklarımız :numref:`imzalamaImg`'de görünmektedir.


.. _imzalamaImg:

.. figure:: ./resimler/paketleme/imzalama.png

   APK Paketini imzalama

Son olarak *Sign* düğmesine tıklayın. Şimdi `MetinDuzenleyici/bin/KivyMetinDuzenleyici-0.1-release-SIGNED_UNALIGNED.apk`
dosyasını bir Android cihaza kurabilirsiniz.

.. _SanalLinux:

Sanal Linux Makina
*******************

Windows kullanıcıları için Linux'u ve diğer paketleri kurmadan (epeyce zahmetli bir iş), programlarını apk haline getirebilecekleri
bir sanal makina disk görüntüsü hazırlanmış 
`https://docs.google.com/uc?export=download&confirm=Ser1&id=0B3-o4L3R6zHvOE9OdDBCUmhLZ0E <https://docs.google.com/uc?export=download&confirm=Ser1&id=0B3-o4L3R6zHvOE9OdDBCUmhLZ0E>`_
adresine konulmuştur. Sanal makine disk görüntüsü Oracle VirtualBox 5.0.16 r105871
sürümü ile hazırlanmıştır. Kullanıcılar mutlaka bu sürümü indirmelidir. Diğer sürümlerde windows-linux bağlantısı
sağlanamayabilir ve ana makinanızın dosyalarına erişiminiz olamayabilir.

