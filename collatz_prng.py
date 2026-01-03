import random

def orta_zorluk_collatz(bit_sayisi, anahtar):
    # Kullanıcının girdiği anahtarı seed olarak kullanıyoruz
    random.seed(anahtar)
    
    n = random.getrandbits(24) 
    uretilen_bitler = []
    
    while len(uretilen_bitler) < bit_sayisi:
        cift = []
        while len(cift) < 2:
            # Collatz Adımları (Algoritma aynı kaldı)
            if n % 2 == 0:
                cift.append(0)
                n //= 2
            else:
                cift.append(1)
                n = 3 * n + 1
            
            if n <= 1:
                n = random.getrandbits(24)
        
        # Von Neumann Dengelemesi
        if cift == [0, 1]:
            uretilen_bitler.append(0)
        elif cift == [1, 0]:
            uretilen_bitler.append(1)
            
    return uretilen_bitler

if __name__ == "__main__":
    print("--- Collatz PRNG Üreteci ---")
    
    # KULLANICI GİRİŞLERİ
    try:
        user_seed = input("Gizli Anahtarı giriniz (Sayı veya Metin): ")
        user_bits = int(input("Kaç bit üretilsin? (Örn: 50): "))
        
        # Algoritmayı çalıştır
        sonuc = orta_zorluk_collatz(user_bits, user_seed)
        
        print("\n[BAŞARILI]")
        print(f"Giriş Anahtarı: {user_seed}")
        print(f"Üretilen Dizi ({user_bits} bit):")
        print(''.join(map(str, sonuc)))
        
    except ValueError:
        print("Hata: Lütfen bit sayısı için geçerli bir tam sayı giriniz.")
