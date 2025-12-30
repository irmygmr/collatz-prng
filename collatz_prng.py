import random

def orta_zorluk_collatz(bit_sayisi, anahtar):

    random.seed(anahtar)
    
    n = random.getrandbits(24) 
    
    uretilen_bitler = []
    
    while len(uretilen_bitler) < bit_sayisi:
        cift = []
        while len(cift) < 2:
            # Collatz Adımları
            if n % 2 == 0:
                cift.append(0)
                n //= 2
            else:
                cift.append(1)
                n = 3 * n + 1
            
            # Sayı 1'e ulaşırsa yeni bir 24-bitlik sayı al
            if n <= 1:
                n = random.getrandbits(24)
        
        # Von Neumann Dengelemesi (0 ve 1 sayısını eşitler)
        if cift == [0, 1]:
            uretilen_bitler.append(0)
        elif cift == [1, 0]:
            uretilen_bitler.append(1)
            
    return uretilen_bitler

if __name__ == "__main__":
    # Örnek Kullanım:
    GIZLI_ANAHTAR = 45826
    BIT_UZUNLUGU = 50
    
    sonuc = orta_zorluk_collatz(BIT_UZUNLUGU, GIZLI_ANAHTAR)
    print(f"Üretilen Rastgele Dizi: {''.join(map(str, sonuc))}")