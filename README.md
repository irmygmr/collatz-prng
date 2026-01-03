# Collatz PRNG (Sözde Rastgele Sayı Üreteci)

Bu proje, matematiksel kaos ve istatistiksel filtreleme yöntemlerini birleştirerek güvenilir bir Sözde Rastgele Sayı Üreteci (PRNG) oluşturmak amacıyla geliştirilmiştir. Algoritma, Collatz Sanısı'nın tahmin edilemez doğasını temel alır.

---

## 🛠 Algoritma Mantığı ve Çalışma Prensibi

Algoritmanın işleyişi dört ana aşamadan oluşmaktadır:

### 1. Matematiksel Temel: Collatz Teoremi (3n+1)
Algoritmanın rastgelelik kaynağı, **Collatz Sanısı**'dır. Sayıların izlediği yolun kaotik olması, bir PRNG için gereken "tahmin edilemezlik" özelliğini sağlar.

* **Süreç:** Kullanıcıdan alınan **Gizli Anahtar (Seed)**, başlangıç sayısını belirler.
* **İşleyiş:** Sayı çift ise $n/2$, tek ise $3n+1$ işlemi uygulanır.
* **Bit Dönüşümü:** Sayının her adımdaki çiftlik/teklik durumu (0 veya 1) ham veri olarak toplanır.


---

### 2. Örnekleme Stratejisi: Atlama (Skipping)
Saf Collatz dizisindeki ardışık adımlar arasında matematiksel bir bağ (korelasyon) bulunur. Bu bağımlılığı kırmak ve bitlerin birbirinden bağımsız olmasını sağlamak için **Atlama** yöntemi uygulanmıştır.

* **Yöntem:** Her bir bit çıktısı alınmadan önce algoritma arka planda **2 adım boşa** çalıştırılır.
* **Amaç:** Bu örnekleme aralığı, dizilim rastgeleliğini maksimize eder ve çıktıların tahmin edilebilirliğini düşürür.

---

### 3. İstatistiksel Denge: Von Neumann Filtresi
Rastgele sayı üretiminde en kritik konu, 0 ve 1 sayılarının eşit dağılmasıdır. Algoritma, **Von Neumann Bias Correction** tekniği ile bu dengeyi garanti altına alır.

* **Filtreleme Mantığı:** Bitler çiftler halinde incelenir:
    * `[0, 1]` çifti gelirse → Çıktı **0** kabul edilir.
    * `[1, 0]` çifti gelirse → Çıktı **1** kabul edilir.
    * `[0, 0]` veya `[1, 1]` gelirse → Bu çiftler reddedilir.
* **Sonuç:** Bu yöntem, her bitin gelme olasılığını matematiksel olarak tam **%50**'ye sabitler.

> **Not:** Küçük örneklemlerde görülen ufak farklar (örneğin 17-13) rastgeleliğin doğal bir sonucudur (varyans). Örneklem büyüdükçe (1000+ bit) dağılımın tam dengeye oturduğu Ki-Kare testiyle kanıtlanmıştır.

---

### 4. Kullanıcı Etkileşimi (Seed Mekanizması)
Algoritma, deterministik bir yapıya sahiptir; yani aynı anahtar girildiğinde aynı dizi üretilir. Ancak giriş anahtarındaki tek bir karakter değişimi bile (**Avalanche Effect**), Collatz dizisinin başlangıcını ve dolayısıyla tüm çıktı dizisini tamamen değiştirir.

---

## 📊 İstatistiksel Test Sonuçları

Algoritma, NIST standartlarına uygun iki temel testten başarıyla geçmiştir:

1.  **Ki-Kare (Chi-Square) Testi:** Bitlerin sayısal dengesini ölçer. (BAŞARILI)
2.  **Runs (Dizi) Testi:** Bitlerin dizilimindeki bağımsızlığı ölçer. (BAŞARILI)


---

## 🚀 Nasıl Çalıştırılır?

1. Python yüklü olduğundan emin olun.
2. `collatz_prng.py` dosyasını çalıştırın.
3. Gizli anahtarınızı ve üretmek istediğiniz bit sayısını girin.

4. Kullanıcı Etkileşimi: Seed (Tohum) Mekanizması
Algoritma, kullanıcıdan bir Gizli Anahtar (Seed) alır.

Bu anahtar random.seed() üzerinden Python'ın entropi havuzuna aktarılır.

Böylece algoritma her seferinde aynı yerden başlamaz; girilen her farklı anahtar, tamamen farklı bir rastgele dizi üretilmesini sağlar.
