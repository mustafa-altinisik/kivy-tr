******************
Kivy'nin Kurulumu
******************

Bu belgede tüm çalışmalar Linux üzerinde yapılmaktadır, ancak okuyucuların bir kısmının Windows üzerinde çalışma
ihtimaline karşı Windows üzerinde kurulumda anlatılacaktır.

Bu belgenin hazırlanmaya başladığı zamanda Python 3.5 sürümü desteklenmemektedir.
Dolayısı ile Python 3.4 ile çalışılacaktır.

Windows'da Kurulum
==================

Makinanızda Python Var mı?
-------------------------
Bu belgeyi okumaya başlamış iseniz, muhtemelen bilgisayarınızda Python kuruludur. Eğer kurulu değilse 
`Python'un İndirme Sayfası <https://www.python.org/downloads/windows/>`_'na giderek işletim sisteminize uygun 
olan 3.4 sürümünün son paketini indiriniz. Bu belge hazırlanırken 3.4.4 sürümü var idi. Belgenin üzerinde çalışıldığı 
Makinada 64 bitlik Windows 7 kurulu olduğundan şu paket indirildi "Windows x86-64 MSI installer" (python-3.4.4.amd64.msi). 
İndirdiğiniz msi dosyası üzerine çift tıklayın, eğer Windows'unuzun yönetici parolasını biliyorsanız, en iyisi tüm kullanıcılar için kurmaktır. 
Bunun için "Install for all users" seçili iken "Next" düğmesine tıkladığınızda kurulacak olan patikanın ``C:\\Python34\\`` olmasına 
özen gösterin. Birkaç tıklamadan sonra size yönetici parolası soarcaktır. Python 3.4 sürümü çalışabilir python.exe 
dosyasının bulunduğu ``C:\\Python34\\`` patikasını çevre değişkenine eklemez. Bunun için önce bir komut satırı açın 
(Başlat'a tıklayın "Programları ve dosyaları ara" kutucuğuna ``cmd`` yazın ve klavyeden "Enter" tuşuna basın. 
Bu size siyah siyah bir pencere açacaktır. Bu pencerede aşağıdaki komutu işletin:

::

	setx path "%path%;C:\Python34"


Artık Kivy'nin kurulumuna geçebiliriz. Bunun için komut satırında iken (siyah pencerede) aşağıdaki adımlarda belirtilen komutları çalıştırın:

1. ``pip`` ve ``wheel``'in son sürümünü yükleyelim:

  ::
  
      python -m pip install --upgrade pip wheel setuptools	

2. Kivy için gerekli olan pakteleri kuralım:

  ::
  	
  	  python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/
     
3. Ve son olarak Kivy'i kuralım:

  ::
      
      python -m pip install kivy
      
Kurulum bitti, artık kivy'i python içerisinden çağırabilirsiniz.
  	  

