def eksponensial(angka, pangkat):
    hasil = 1
    for i in range(pangkat):
        hasil = hasil * angka
    return hasil

print(eksponensial(2,2))
print(eksponensial(3,3))
print(eksponensial(10,5))