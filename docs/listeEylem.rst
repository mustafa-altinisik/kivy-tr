.. _listeEylemCubuguBolumu:


################################
Liste Görünümü ve Eylem Çubuğu
################################

.. warning::
   
   Bu bölüm tamamlanmamıştır. Zaman buldukça yazıyorum.


Bu bölümde listeler, liste görünümü açılır kutu (dropdawn) ve Eylem çubuğunu anlatacağız. Konuları anlatırken daha önce
geliştirdiğimiz uygulamalara eklentiler yaparak uygulamasını da göstereceğiz.

Liste Görünümü
===============
Kivy'de listeler ve ilgili görünümler (adaptör, uyarlayıcı kullanarak), daha önce kullandığım GUI (GKA)'lardan biraz farklı
çalışıyor. Bu farklılık listelerin kullanımınız biraz zorşaltırmış gibi görünse de, bu ona listelerin daha esnek ve kullanışlı
olmasını sağlıyor. İlk olarak basit bir liste oluşturalım. Bu liste sadece verileri görüntülemek için kullanılacak, seçim
yapılamayacak ve herhangi bir eylem tanımlanamayacaktır. Bir liste oluşturmak için  :index:`ListView` nesnesini kullanırız.
``ListView`` nesnesinin en basit kullanımı paramtere olarak :index:`item_strings` vermektir. Bu parametre Python
listesi helinde listelenecek olan elemanları alır. Programlamada dillerini listeleyecek bir programı 
:numref:`listeGorunumu`'deki gibi yazabiliriz.

.. literalinclude:: ./programlar/listeEylem/programlar/1/listeGorunumu.py
    :linenos:
    :tab-width: 4
    :caption: listeGorunumu.py
    :name: listeGorunumu
    :language: python

Programı çalıştırdığımızda :numref:`Şekil %s <basitListe1Img>`'de görünen pencere açılacaktır.

.. _basitListe1Img:

.. figure:: ./programlar/listeEylem/programlar/1/basitListe.png

   Liste Görünümü (Temel)


SimpleListAdapter Adaptörü Kullanımı
-------------------------------------
Liste görünümlerini değiştirmek ve işerliğe kavuşturmak için ``ListView`` nesnesine bir adaptör vermektir.
Bu adaptörlerden en basiti ise :index:`SimpleListAdapter` nesnesidir. Bu adaptör sadece listelemek için kullanılır. Programlama dillerininin isismlerini
gösteren programı bu adaptörü kullanarak tekrar yazmak istersek: :numref:`basitListe`'deki gibi ``basitListe.py``
dosyasını  hazırlamamız gerekcek.

.. literalinclude:: ./programlar/listeEylem/programlar/1/basitListe.py
    :linenos:
    :tab-width: 4
    :caption: basitListe.py
    :name: basitListe
    :language: python
    
Şimdi bu programı açıklamaya çalışalım. Programda 14. satırdaki ``programlama_dilleri`` listesi basit bir Python listesidir.
Görüntülemek istediğimiz elemanları bu listeye yazabiliriz. Liste yerine tüp (tuple) kullanabilirsiniz. Liste görünümünde
kullanabileceğimiz en basit adaptörün ``SimpleListAdapter`` olduğunu söylemiştik. Bu adaptör sadece bir dizi elemanı
ekranda görüntülemek için kullanılabilir. Herhangi bir seçim ya da eylem gerçekleştiremezsiniz. Kullanımı oldukça basittir:
paramatere olarak :index:`data` (listelenecek elemanlar) ve :index:`cls` (görüntüleme biçimi) alır. Görüntüleme
biçimi basit olarak bir etiket (Label) ya da düğme (Button) olabilir. Biz yukarıda etiket (Label) kullandık. 
İsterseniz aynı programı düpme (Button) ile tekrar çalıştırın. Program çalıştığında  yine
:numref:`Şekil %s <basitListe1Img>`'de görünen pencere açılacaktır.

   
:numref:`Şekil %s <basitListe2Img>`'de resimde aynı programın, listedeki görüntüleme biçiminin (``cls=Button``) düğme (Button) hali
görünmektedir.

.. _basitListe2Img:

.. figure:: ./programlar/listeEylem/programlar/1/basitListe2.png

   Basit Liste (Düğme)


:numref:`basitListe`'deki programı, ``c:\windows`` (Linux için ``/usr``) klasöründeki dosya ve dizinleri
gösterecek şekilde uyarlayınız. Linux için programınızın çalışmış hali :numref:`Şekil %s <basitListe-klasorImg>`'deki gibi olacaktır.


.. _basitListe-klasorImg:

.. figure:: ./programlar/listeEylem/programlar/1/basitListe-klasor.png

   Dosya ve Klasörlerin Listelenmesi (Linux)

Çözüm:

basitListe-klasorler.py:       https://github.com/mbaser/kivy-tr/blob/master/docs/programlar/listeEylem/programlar/1/basitListe-klasorler.py


Sonraki konuya geçmeden önce listelerin ``kv`` dili ile nasıl hazırlanacağına bakalım. :numref:`basitListe`'deki programımızın
aynısını ``kv`` dili ile yazalım. Önce Python programını :numref:`basitListeKv`'deki gibi yazalım


.. literalinclude:: ./programlar/listeEylem/programlar/1/basitListeKv.py
    :linenos:
    :tab-width: 4
    :caption:  basitListeKv.py
    :name: basitListeKv
    :language: python

Sanırım bu program çok kolay oldu ve herhangi bir açıklamaya ihtiyacı yok. Bu program tarafından kullanılacak ``kv``
dosyasını :numref:`basitListeKv_kv`'de görüldüğü gibi yazabiliriz.

.. literalinclude:: ./programlar/listeEylem/programlar/1/basitlisteuyg.kv
    :linenos:
    :tab-width: 4
    :caption:  basitlisteuyg.kv
    :name: basitListeKv_kv

Bu ``kv`` dosyasının ilk iki stırında ``Label`` ve  ``SimpleListAdapter`` nesnelerini ilgili modüllerden nasıl içerdiğimizi
iyice inceleyiniz. Program içerisinden adaptöre ve adaptörün verilerine ulaşabilir, güncelleyebilirsiniz ve hatta başka adaptör
kullanabilirsiniz. Aşağıdaki kodu ``build()`` işlevinin altına yazarsanız, programlama dilleri listesine "Pascal", "C" ve "C++" nin de
eklendiğini göreceksiniz:

::

        for pr in ["Pascal", "C", "C++"]:
            self.root.ids.listeci.adapter.data.append(pr)


ListAdapter ve DictAdapter Adaptörü Kullanımı
---------------------------------------------
Listeler genellikle arasından birisni seçmek için kullanılır ve daha önce anlatılan basit liste görünümü oluşturmaktan 
daha karmaşık veriye sahip olabilir. Bunları ``ListAdapter`` veya ``DictAdapter`` adaptörlerini kullanarak yapabiliriz.

Önce :index:`ListAdapter` kullanımına bakalım. Daha önce söyledğimiz gibi ``ListView`` parçacığında adaptörler, veriyi
içerir. Bu veri ``ListAdapter`` için her biri birer sözlük olan Python Listesidir. Örneğin kitaplara ait veriyi ele alalım
(*not: kitaplar rastgele seçilmiştir, seçimde herhangi bir tercih yoktur*)::

    kitaplar=[ {'adi':'Python', 'yazari':'Mustafa Başer', 'yayinevi':'Dikeyeksen'},
               {'adi':'Ruby', 'yazari':'Timur Karaçay', 'yayinevi':'Seçkin'},
               {'adi':'Perl-CGI', 'yazari':'Rıza Çelik', 'yayinevi':'Seçkin'},
               {'adi':'Php', 'yazari':'Mehmet Şamlı', 'yayinevi':'Kodlab'} ]


Burada ``kitaplar`` bildiğimiz bir Python listesi ve elemanları bildiğimiz Python sözlükleridir. Her sözlük 
``adi``, ``yazarı`` ve ``yayinevi`` anahtarları ile bunlara ait birer değer içermektedir. ``kitaplar`` listesini
olduğu gibi ``Listadapter`` nesnesine veri seti olarak atayabiliriz. Peki kullanıcıya ne gösterilecek? Bunu ise bir
işlev yadımı ile belirleyebiliriz. Bu işeve :index:`argüman çevirici` (:index:`arg_converter`) diyoruz. Argüman çevirici
kendisine gelen veriyi, listede gösterilecek şekilde düzenler ve yine bir sözlük döndürür. Bu sözlükte bulunması gereken
tek zorunlu anahtar ``text`` dir. Bu anahtarın değeri kullanıcıya listede gösterilen metindir. İsterseniz gösterilecek olan liste
elemanı (burada :index:`ListItemButton` olacaktır) (liste düğmesi) ile ilgili görünümü değiştirebilirsiniz; örneğin boyutunu.

Şimdi bunları birleştirelim ve seçilebilir bir liste oluşturalım.
*devam edecek...*
