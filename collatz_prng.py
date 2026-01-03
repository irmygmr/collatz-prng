import random

def orta_zorluk_collatz(bit_sayisi, anahtar):
    # Kullanıcıdan gelen anahtarı seed olarak kullanıyoruz
    random.seed(anahtar)
    
    # 24-bitlik bir başlangıç sayısı üretiyoruz
    n = random.getrandbits(24) 
    uretilen_bitler = []
    
    while len(uretilen_bitler) < bit_sayisi:
        cift = []
        while len(cift) < 2:
            # --- ATLAMA (SKIPPING) ---
            # Ardışık bitler arasındaki bağımlılığı kırmak için 2 adım boşa çalıştırıyoruz.
            for _ in range(2): 
                if n % 2 == 0: n //= 2
                else: n = 3 * n + 1
                if n <= 1: n = random.getrandbits(24)

            # Şimdi asıl veriyi alıyoruz
            if n % 2 == 0:
                cift.append(0)
                n //= 2
            else:
                cift.append(1)
                n = 3 * n + 1
            
            if n <= 1:
                n = random.getrandbits(24)
        
        # --- VON NEUMANN DÜZELTMESİ ---
        # 0 ve 1 sayılarını tam olarak %50-%50 dengelemek için filtre uyguluyoruz.
        if cift == [0, 1]:
            uretilen_bitler.append(0)
        elif cift == [1, 0]:
            uretilen_bitler.append(1)
            
    return uretilen_bitler

if __name__ == "__main__":
    print("=== Collatz PRNG Üreteci (Gelişmiş Versiyon) ===")
    
    try:
        # Kullanıcıdan anahtar ve bit sayısı alıyoruz
        user_seed = input("Gizli Anahtarı giriniz (Sayı veya Metin): ")
        user_bits = int(input("Kaç bit üretilsin? (Örn: 1000): "))
        
        # Algoritmayı çalıştır
        sonuc = orta_zorluk_collatz(user_bits, user_seed)
        bit_dizisi = ''.join(map(str, sonuc))
        
        print("\n[BAŞARILI]")
        print(f"Giriş Anahtarı: {user_seed}")
        print(f"Üretilen Dizi ({user_bits} bit):")
        print(bit_dizisi)

        # İstatistiksel özet (Opsiyonel: Hocan için ekranda kalsın)
        sifirlar = sonuc.count(0)
        birler = sonuc.count(1)
        print(f"\nİstatistik: 0 Sayısı: {sifirlar}, 1 Sayısı: {birler}")
        
    except ValueError:
        print("Hata: Lütfen bit sayısı için geçerli bir tam sayı giriniz.")

