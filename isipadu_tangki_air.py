# Atur cara bagi mengira luas permukaan dan isipadu
# tangki air berbentuk silinder

# Pengisytiharan pemboleh ubah dan pemalar
pi = 3.142

def dapat_jejari_tinggi():
    r = float(input("Masukkan jejari tangki air: ")) 
    h = float(input("Masukkan tinggi tangki air: "))
    return r, h 

def kira_isipadu(r, h):
    # Pengiraan isipadu tangki air (V) 
    V = pi * r**2 * h
    return V

def main():
    jejari, tinggi = dapat_jejari_tinggi()
    isipadu = kira_isipadu(jejari, tinggi)
    # Output
    print(f"Isipadu tangki air = {isipadu:.2f}")

# JANGAN UBAH ATUR CARA DI BAWAH BARIS INI 
if __name__ == "__main__":
    main()