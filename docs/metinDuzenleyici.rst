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
    :language: kv


Bu dosyada bilmediğimiz sadece ..
