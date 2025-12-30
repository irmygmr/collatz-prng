# Collatz PRNG - Sözde Kod (Pseudo Code)

Bu dosya, algoritmanın çalışma mantığını adım adım açıklamaktadır.

## Algoritma Adımları

1. **Giriş:** Kullanıcıdan `bit_sayisi` ve `anahtar` (seed) değerlerini al.
2. **Başlatma:** Rastgele sayı üreticini `anahtar` ile kur ve `n` değişkenine 24-bitlik rastgele bir sayı ata.
3. **Ana Döngü:** İstenen bit sayısına ulaşılana kadar devam et:
    - **Bit Üretimi:** Collatz adımlarını kullanarak (n çift ise n/2, tek ise 3n+1) iki adet bit üret.
    - **Döngü Kontrolü:** Eğer `n` değeri 1'e ulaşırsa, `n` değişkenine tekrar 24-bitlik rastgele bir sayı ata.
    - **Von Neumann Dengelemesi:**
        - Üretilen ikili `01` ise: Listeye `0` ekle.
        - Üretilen ikili `10` ise: Listeye `1` ekle.
        - Üretilen ikili `00` veya `11` ise: Bu bitleri atla ve başa dön.
4. **Bitiş:** Hedeflenen bit sayısı dolduğunda oluşan listeyi sonuç olarak döndür.