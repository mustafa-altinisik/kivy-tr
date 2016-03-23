##################
Kivy'nin Kurulumu
##################

Bu belgede tüm çalışmalar Linux üzerinde yapılmaktadır, ancak okuyucuların bir kısmının Windows üzerinde çalışma
ihtimaline karşı Windows üzerinde kurulumda anlatılacaktır.

Bu belgenin hazırlanmaya başladığı zamanda, :ref:`paketleme` bölümünde anlatacağımız Buildozer Python 2.7 ile hazırlandığı için
Python 2.7 ile çalışılacaktır.

Windows'da Kurulum
==================

Bu belgeyi okumaya başlamış iseniz, muhtemelen bilgisayarınızda Python kuruludur. Eğer kurulu değilse 
`Python'un İndirme Sayfası <https://www.python.org/downloads/windows/>`_'na giderek işletim sisteminize uygun 
olan 2.7 sürümünün son paketini indiriniz. Bu belge hazırlanırken 2.7.10 sürümü var idi. Belgenin üzerinde çalışıldığı 
Makinada 64 bitlik Windows 7 kurulu olduğundan şu paket indirildi "Windows x86-64 MSI installer" (python-2.7.10.amd64.msi). 
İndirdiğiniz msi dosyası üzerine çift tıklayın, eğer Windows'unuzun yönetici parolasını biliyorsanız, en iyisi tüm kullanıcılar için kurmaktır. 
Bunun için "Install for all users" seçili iken "Next" düğmesine tıkladığınızda kurulacak olan patikanın ``C:\Python27\`` olmasına 
özen gösterin. Birkaç tıklamadan sonra size yönetici parolası soarcaktır. Python 3.4 sürümü çalışabilir python.exe 
dosyasının bulunduğu ``C:\Python27\`` patikasını çevre değişkenine eklemez. Bunun için önce bir komut satırı açın 
(Başlat'a tıklayın "Programları ve dosyaları ara" kutucuğuna ``cmd`` yazın ve klavyeden "Enter" tuşuna basın. 
Bu size siyah siyah bir pencere açacaktır. Bu pencerede aşağıdaki komutu işletin:

::

	setx path "%path%;C:\Python27\"


Artık Kivy'nin kurulumuna geçebiliriz. Bunun için komut satırında iken (siyah pencerede) aşağıdaki adımlarda belirtilen komutları çalıştırın:

1. ``pip`` ve ``wheel``'in son sürümünü yükleyelim:

  ::
  
      python -m pip install --upgrade pip wheel setuptools	

2. Kivy için gerekli olan pakteleri kuralım (~100MB civarı dosya yüklenecektir biraz sabırlı olmalısınız):

  ::
  	
  	  python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/
     
3. Ve son olarak Kivy'i kuralım:

  ::
      
      python -m pip install kivy
      
Kurulum bitti, artık kivy'i python içerisinden çağırabilirsiniz. Düzgün kurulup kurulmadığını Python komut satırından aşağıdaki kodları çalıştırarak deneyebilirsiniz. Kurulum düzgün ise pencere başlığı "Bos Pencere" olan siyah ve boş bir pencere açılacaktır.

.. _kurulumDogrulama:

::
  
  >>> from kivy.app import App
  >>> App(title="Bos Pencere").run()


Linux'da Kurulum  	  
=================
Değişik Linux dağıtımlarında kurulum birbirinden farklıdır. Burada sadece Debian Jessie'de (8.3) nasıl kurulacağını anlatacağız. Linux'a kurmak
bana her zaman Windows'a kurmaktan daha kolay gelir. Öncelikle ``add-apt-repository`` programına ihtiyacınız var. Sisteminizde kurulu değilse
root yetkileri ile şu şekilde kurabilirsiniz:

.. code-block:: console

  # apt-get install software-properties-common


Şimdi yazılım havuzunu apt kaynaklarına ekleyelim:

.. code-block:: console

  # add-apt-repository ppa:kivy-team/kivy


Şimdi Kivy'i kurma zamanı:

.. code-block:: console

  # apt-get install python-kivy




kurulumun doğru gerçekleştiğini :ref:`yukarıda <kurulumDogrulama>` anlattığım gibi ile anlayabilirsiniz.



