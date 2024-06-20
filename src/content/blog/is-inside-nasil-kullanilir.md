---
title: is-inside.me Nasıl Kullanılır?
description: ShareX gibi kendi internet servisinize resim yüklemeyi destekleyen programlar için EGGSY ve Tresmos tarafından geliştirilen is-inside.me sitesi nedir ve nasıl kullanılır?
tags:
  - sharex
createdAt: 2019-11-07T13:27:00.000Z
---

<blog-notification type="danger">Bu proje, 3 yıllık hizmetinin ve onbinlerce dosyanın, hâtrı sayılır trafiğin ve kullanıcının ardından kapanma kararı almıştır. Bundan sonra yeni kullanıcı kabul etmeyecek ve yakında tarihe gömülecektir.</blog-notification>

Öncelikle, ShareX'in ne olduğu hakkında kısa bir bilgi vereceğim, bu sayfanın amacı ShareX'in nasıl kullanılacağı değil, is-inside.me ayarlarını ShareX programına nasıl aktarılacağını göstermektedir. Eğer ShareX'in ne olduğunu zaten biliyorsanız bu kısmı atlayabilirsiniz.

ShareX, sadece ekran görüntüsü almaya değil, ekran videosu çekmeye, dosya göndermeye, QR kod okumaya ve birçok araçlara sahip Windows programıdır. Evet, sadece Windows desteklemesiyle birlikte diğer işletim sistemlerinde alternatifleri olsa da hiçbiri ShareX'in yaptığı işlerin "tamamını" yapamıyor. Ancak ShareX, açık kaynak olduğu için bir gün elbet bir geliştirici uygulamanın Linux ve Mac sürümünü çıkartacağını düşünüyorum. Tabii bunun şimdiye kadar gerçekleşmediğini de var sayarsak sanırım ShareX özelliklerini bir süre daha sadece Windows üzerinde görmeye devam edeceğiz.

ShareX, bir Türk geliştirici tarafından birkaç kişiyle birlikte ortaya çıkmış bir projedir. Oldukça başarılı olan bu proje, bugün birçok Windows kullanıcısının bilgisayarında yüklü, yüklü değilse bile yüklenmesi gereken bir programdır. Eğer siz de ShareX'e sahip olmak istiyorsanız [buraya](https://getsharex.com/?utm_source=eggsy.xyz) tıklayabilir ve masaüstü sürümünü edinebilirsiniz. Eğer ShareX'e Steam'de sahip olma gibi bir fanteziniz varsa da [buraya](https://store.steampowered.com/app/400040/ShareX/?utm_source=eggsy.xyz) tıklayıp Steam üzerinden ücretsiz bir şekilde kütüphanenize ekleyebilirsiniz. Eğer is-inside.me servisini kullanmak istiyorsanız bu programa ihtiyacınız var.

### is-inside.me nedir?

is-inside.me, benim ve Tresmos'un ortak bir "eğlence" projesidir. Öyle ki anlamı "içimde" demektir. İşin en güzel yanı ise sadece alan adının ismi değil, alan adının başına istediğiniz bir şeyi (veya kişiyi ( ͡° ͜ʖ ͡°)) ekleyebilmeniz. Evet, projenin asıl amacı "kayıt bazlı alt alan adı" üzerine çalışmaktır. Bu aslında Tresmos'un ve benim bir deneme projesi olsa bile şu anda içerisinde yaklaşık 10 GB resmi barındırıyor. 10 GB belki az gibi gözükebilir ama neredeyse 50000 dosya bulunan bu servis, tamamen sizlerin yaratıcılığına kalmış bir biçimde çalışıyor. Kısacası, is-inside.me üzerinden bir hesap açıyorsunuz, ve bu hesabınıza, resim, video, ZIP/JavaScript/HTML/CSS ve yazı dosyalarını yükleyebiliyorsunuz. İşin asıl eğlenceli kısmı elbette bir siteye bir dosya yüklemek değil. is-inside.me tamamen alan adında bitiyor. Örnek vermek gerekirse bazı güzel alan adları şöyle:

- the-person-under-this-message.is-inside.me (bu mesajın altındaki kişi içimde)
- eggsy.is-inside.me (eggsy içimde)
- your-mom.is-inside.me (annen içimde ( ͡° ͜ʖ ͡°))

Alt alan adlarının ne olacağını belirlemek tamamen sizlere kalmış. Eğer sitenin mevzusunu anladıysanız şimdi nasıl işlediğine geçelim.

1. **Kayıt olun**: Sistemi kullanabilmek için öncelikle bir alt alan adına ve şifreye ihtiyacınız var. Bunu da saniyeler içerisinde yapabilirsiniz, şifreleriniz veritabanımızda şifrelenerek tamamen güvenli bir şekilde saklanacaktır. Bu yüzden hiçbir şekilde korkmanıza gerek yok. Eğer korkuyorsanız da şifrenizi rastgele bir şeyler yapabilirsiniz. Siteyi ziyaret etmek ve kayıt olmak için buraya tıklayabilirsiniz.
   <smart-figure src="https://i.imgur.com/7i8LVC6.png"></smart-figure>

2. Kontrol panelinden gerekli bilgileri alın Kayıt olduktan sonra sizi otomatik olarak kontrol paneline atacaktır. Bu sayfada aslında sistemin nasıl kullanılacağı belirtiliyor ancak sistem İngilizce olduğu için bu sayfayı yazmayı gerek gördüm.
   <smart-figure src="https://i.imgur.com/37q8Q4q.png" caption="Resimde gösterilen yerlerden sizin kullanmanız için tek ihtiyacınız olan kısım 'Yükleyici program' seçeneğinin hemen altında bulunan 'Download' yazısı. Bu yazıya tıkladığınızda tarayıcınız, 'is-inside.sxcu' adında bir dosya indirmeye başlayacaktır. Bu dosya, ShareX için özel olarak hazırlanmış ayar dosyasıdır."></smart-figure>

3. **Dosyayı aktifleştirme**: Dosyayı aktifleştirmek için sadece dosyayı açmanız ve gelen uyarıda evet seçeneğine basmanız yeterli olacaktır. Bundan sonra resim yüklerken resimleriniz otomatik olarak is-inside.me sitesine, seçtiğiniz alt alan adına yüklenecektir.
   <smart-figure src="https://i.imgur.com/9YO0YwU.png"></smart-figure>

4. **İlk yüklemenizi yapma**: Evet, artık her şey hazır, ayarlarınız içe aktarıldı ve yükleme yapmaya hazırsınız. Ancak bundan önce ShareX üzerinden birkaç ayara değiştirmeniz gerekiyor. Bu kısımda çok detaya girmeyeceğim, daha fazlasını kendiniz ShareX uygulamasını kurcalayarak bulabilir ve kafanıza göre ayarlayabilirsiniz. Aşağıdaki GIF'i izleyerek yükleme işleminin nasıl gerçekleştiğini görebilirsiniz.
   <smart-figure src="https://i.imgur.com/xawCPNF.gif"></smart-figure>

GIF'de gördüğünüz işlemlerden "Yakalama Sonrası" yapılacak seçeneklerin içerisinden "Resim düzenleyicide aç" seçeneğini de aktifleştirirseniz, yukarıdaki kontrol paneli resminde gördüğünüz gibi düzenlemeler yapabilir ve yükleyebilirsiniz.

ShareX sadece Windows'ta mevcut olduğundan dolayı yukarıda gördüğünüz tüm yazı sadece Windows'ta geçerli olacaktır. Eğer bir Linux kullanıcısıysanız ve yine de is-inside.me servisini kullanmak istiyorsanız KShare adındaki programı kullanabilirsiniz. Site üzerindeki adımları takip ederek o yükleyici ile de yükleme işlemlerinizi gerçekleştirebilirsiniz.
