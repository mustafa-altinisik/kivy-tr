.. _kivyDili:

#########################################
:index:`Kivy Dili`: kv (:index:`kv lang`)
#########################################

Kivy pencere düzenlerini oluşturmak için muhteşem bir dil sunmaktadır: ``kv`` Dili. Bu dili biraz HTML'ye biraz da css'ye benzetebilirsiniz. Bu bölümde ``kv`` dilini anlatmaya çalışacağız.

"Merhaba Dünya" yeniden
=======================
:ref:`merhabaDunya` programında ekrandaki "Merhaba Dünya" yazısını program kodu içerisinde bir etiket oluşturup, bu etiketin metinini değiştirerek yapmıştık. Bu etiketi daha sonra düzen olarak geri döndürmüştük (``return Label()``). Şimdi aynı pencereyi ``kv`` dilini kullanrak yapacağız. Önce program kodumuzu :ref:`kvDili`'deki gibi yazalım. Bu kodda hiçbir değişiklik yapmadan birçok pencere oluşturacağız. 


.. literalinclude:: ./programlar/kvDili.py
    :linenos:
    :caption: :download:`kvDili.py<./programlar/kvDili.py>`
    :name: kvDili
    :language: python
    

Gördüğünüz gibi bu program hiçbirşey döndürmüyor. Sadece basit bir pencere oluşturuyor. Pencere içeriğini ``kv`` dili oluşturacağız. Şimdi dosyasını :ref:`kvDili` programını kaydettiğiniz aynı dizinine (klasöre) kaydedin.

.. literalinclude:: ./programlar/kvdili.kv
    :linenos:
    :caption: :download:`kvdili.kv<./programlar/kvdili.kv>`
    :name: kvDiliKV
    
Bu dosyanın adı, python programının dosya adı değil, uygulamanın adı ile aynı olacaktır. Eğer uygulamanızın adı ``kullaniciGirisFormu()`` ise ``kv`` dosyasının adı ``kullanicigirisformu.kv`` olacaktır. Dosya adında küçük harfleri kullanmanızı yeğlerim.
