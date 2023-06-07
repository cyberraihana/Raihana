pengambilan_produk = 1020000
jumlah_kendaraan = 6

if pengambilan_produk >= 1000000:
    if jumlah_kendaraan >= 8:
       print("Anda memenuhi syarat menjadi distributor daerah.")
    else:
       print("Jumlah kendaraan anda tidak mencukupi.")
else:
     print("pengambilan produk anda kurang dari minimum yang di butuhkan.")
