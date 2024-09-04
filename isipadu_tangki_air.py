# Atur cara bagi mengira luas permukaan dan isipadu
# tangki air berbentuk silinder

# Ditulis oleh Cikgu Hu pada 25 April 2022

# Pengisytiharan pemboleh ubah dan pemalar
pi = 3.142

def jejari_tinggi():
    r = float(input("Masukkan jejari tangki air:")) 
    h = float(input("Masukkan tinggi tangki air:"))
    return (r, h) 

def isipadu():
    (r,h) = jejari_tinggi()
    # Pengiraan isipadu tangki air (V) 
    V = pi * r**2 * h

    # Output
    print(f"Isipadu tangki air = {V:.2f}")

if __name__ == "__main__":
    isipadu()