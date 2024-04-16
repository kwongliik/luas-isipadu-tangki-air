# Atur cara bagi mengira luas permukaan dan isipadu
# tangki air berbentuk silinder

# Ditulis oleh Cikgu Hu pada 25 April 2022

# Pengisytiharan pemboleh ubah dan pemalar
pi = 3.142

def jejari_tinggi():
    r = float(input("Masukkan jejari tangki air:")) 
    h = float(input("Masukkan tinggi tangki air:"))
    return (r, h)

def luas():
    (r,h) = jejari_tinggi()  
    # Proses
    # Pengiraan luas permukaan tangki air (A)
    A = (2 * pi * r * h) + (2 * pi * r ** 2)

    # Output
    print("Luas tangki air =", round(A,2))
    

def isipadu():
    (r,h) = jejari_tinggi()
    # Pengiraan isipadu tangki air (V) 
    V = pi * r ** 2 * h

    # Output
    print("Isipadu tangki air =", round(V,2))

if __name__ == "__main__":
    luas()
    isipadu()
