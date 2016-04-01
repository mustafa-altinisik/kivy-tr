.. _paketleme:

##########
Paketleme
##########

Bu bölümde hazırlanan Kivy programının Android paketi haline getirilmesi anlatılacaktır.

:index:`Buildozer`
******************

Kivy programlarını paketlemenin en kolay yolu Buildozer kullanmaktır. Ne yazıkki Buildozer şimdilik sadece Linux'ta çalışmaktadır.
Windows kullanıcıları için VirtualBox disk görüntüsü hazırlanacaktır. Burada sadece Debian Jessie'de (8.3) nasıl kurulacağını anlatacağız. 
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
