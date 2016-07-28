#############
Giriş
#############

Bu belge Kivy ile mobil programlamayı öğretmek amacı ile hazırlanmıştır.

Kivy Hakkında
**************
Kivy mobil cihazlarda da çalışabilecek programların yazılabileceği bir Python modülüdür. Diğer bir deyişle Mobil GUI Toolkit 
(Mobil Grafik Kullanıcı Arayüzü Aracı) diyebiliriz. Python ile Mobil Uygulama geliştirmek isteyenlerin çoğunluğu Kivy'i tercih etmektedir.
Kivy ile yazacağınız programlar hemen her platformda çalışabilir. Bu platformları şöyle sıralaybiliriz;

* Masaüstü Bilgisayarlar: Linux, Mac OS X, Windows
* Talbletler: Android cihaziar, iPad, iPhone

Kivy dokunmatik ekranlar için optimize edilmiş olmasına rağmen, geliştirilen uygulamalar
masaüstü bilgisayarlarda da rahatlıkla çalışabilmektedir. Bununla birlikte masaüstü bilgisayarlarda
kullanılan diğer GUI araçlarındaki birçok özelliği bulma şansınız yok.

Kivy aslında `Pygame <http://www.pygame.org>`_ üzerine kurulmuş bir yapıdır. Tüm widgetler (grafik bileşenleri) Pygame ile çizilmektedir.
Kivy ile yazdığınız (aslında programı Python programa dili ile yazıyorsunuz) programlar, bir Linux makina (veya sanal makinada çalışan bir Linux)
ile kolaylıkla Android paketleri haline getirilebilmektedir. Getirilen paketler içerisinde Python ve diğer bileşenler
eklendiğinden, uygulama paketi kurulduğunda başka herhangi bir eklentiye gerek kalmadan çalışmaktadır.

Belge Hakkında
***************


Bu belge 
|author|
tarafından zaman buldukça hazırlanmaktadır ve sahibi © |copyright|'dir.
Bu belge `GNU Özgür Belgeleme Lisansı <https://tr.wikipedia.org/wiki/GNU_%C3%96zg%C3%BCr_Belgeleme_Lisans%C4%B1>`_ ile dağıtılmaktadır.

Sürüm ve son değişiklik
========================

| **Sürüm**: |version|
| **Son Değiştirme Tarihi**: |my_build_date| 

Belgeye katkıda bulunanlar
==========================

* |author|

Katkıda bulunmak için mbaser <at> mail.com adresine mail atabilirsiniz.

Ne Bilmeliyim?
**************
Bu doküman sadece Kivy üzerinde yoğunlaşacaktır. Kivy ile program yazabilmek için Python bilmeniz gerekir. Python'u çeşitli
web sitelerinden ya da bu dokümanın yazarı tarafından yazılmış Dikeyeksen yayınlarındaki `Python <http://www.dikeyeksen.com/products/python>`_
kitabından öğrenebilirsiniz. Kitabın birinci kısmını öğrendiğiniz varsayılmıştır.

Bunun dışında komut satırına (Windows için cmd) aşina olmanız gerekmektedir. Böylelikle :ref:`paketleme` bölümünde anlatacağımız 
sanal makina üzerinde paketleme işini yapabilirsiniz.

UYARI
*****
Bu belgede anlatılan içerik ve yayınlanan programlar ve kurulmu anlatılan programlmarın/paketlerin neden olabileceği sorunlardan
belgenin yazarı sorumlu tutulamaz.

