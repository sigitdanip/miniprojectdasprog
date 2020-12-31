#mini project dasar pemrograman
#aplikasi klinik kesehatan pintar

penyakit = ['covid', 'demam berdarah dengue', 'tiphus', 'gagal ginjal', 'gagal jantung',
            'demam', 'hipertensi','diare', 'migrain']

#data obat tiap-tiap penyakit
obat_dbd = ['acetaminophen', 'aspirin', 'analgesic', 'ibuprofen', 'naproxen sodium']
obat_tiphus = [ 'antibiotic', 'penicillin']
obat_gagalginjal = ['vitamin', 'agen pengurang kalsium', 'stimulan sumsum tulang', 'diuretik', 'suplemen diet']
obat_gagaljantung = ['diuretik', 'penghambat beta', 'penghambat enzim konversi angiotensin', 'obat anti darah tinggi',
                    'suplemen diet', 'pengatur tekanan darah', 'vasodilator', 'antianginal']
obat_demam = ['paracetamol', 'ibuprofen', 'naproxen', 'aspirin']
obat_hipertensi = [ 'diuretic', 'vasodilator', 'obat anti darah tinggi']
obat_diare = ['paracetamol ', 'oralit', 'loperamide', 'pepto bismol', 'doxycycline', 'ampicili']
obat_migrain = ['antipsychotic', 'analgesic', 'stimulan', 'triptant', 'neurotoxin']

#ketersediaan obat
stock_dbd = [1, 2, 3, 4, 5]
stock_tiphus = [1, 2, 3, 4, 5]
stock_gagalginjal = [1, 2, 3, 4, 5]
stock_gagaljantung = [1, 2, 3, 4, 5]
stock_demam = [1, 2, 3, 4, 5]
stock_hipertensi = [1, 2, 3, 4, 5]
stock_diare = [1, 2, 3, 4, 5]
stock_migrain = [1, 2, 3, 4, 5]

#daftar ruangan
regular = ['regular1', 'regular2', 'regular3', 'regular4', 'regular5']
vip = ['vip1','vip2', 'vip3']
vvip = ['vvip1', 'vvip2']
ruang_isolasi = ['isolasi1', 'isolasi2']

while True:
    print('-------- Selamat Datang di Klinik Kesehatan Pintar ---------')
    print('Data Diri Pasien')
    nama = input('Nama: ')
    umur = input('Usia: ')
    kelamin = input('Jenis Kelamin: ')

    #diagnosa pasien
    diagnosa = input('Diagnosa Pasien: ')
    if diagnosa in penyakit:
        print('Sedang diproses...')
        print('Penyakit terdaftar')
        if diagnosa == 'covid':
            print('Pasien harus dimasukkan kedalam ruang isolasi')
            print('Menyiapkan ruang isolasi...')
            print('Ruang isolasi ditemukan!')
            if len(ruang_isolasi) > 0:
                print('________________________________')
                print('Keterangan Rawat Inap')
                print('Nama:', nama)
                print('Usia: ', umur)
                print('Jenis Kelamin: ', kelamin)
                print('Diagnosa: ', diagnosa)
                print('dirawat di: ')
                print('Ruang: ', ruang_isolasi[-1])
                print('________________________________')
                ruang_isolasi.pop()
            else:
                print('Mohon Maaf')
                print('Ruang isolasi tidak tersedia, silahkan hubungi rumah sakit lain')
        elif diagnosa == 'demam berdarah dengue':
            print('Pasien harus dirawat inap')
            print('ruangan yang Tersedia: ')
            print(regular)
            print(vip)
            print(vvip)
            print('kluster yang diinginkan pasien: regular/vip/vvip')
            kluster = input()
            print('Menyiapkan ruangan...')
            print('Ruangan ditemukan!')
            if kluster == 'regular':
                if len(regular) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', regular[-1])
                    print('________________________________')
                    regular.pop()
                else:
                    print('Ruangan tidak tersedia!, silahkan melakukan rawat jalan')
                    if len(stock_dbd) > 0:
                            print('Menyiapkan obat...')
                            print('______________________________')
                            print('Keterangan Rawat Jalan')
                            print('Nama:', nama)
                            print('Usia: ', umur)
                            print('Jenis Kelamin: ', kelamin)
                            print('Diagnosa: ', diagnosa)
                            print('Obat pasien: ')
                            print(obat_dbd)
                            print('______________________________')
                            stock_dbd.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vip':
                if len(vip) > 0:
                        print('________________________________')
                        print('Keterangan Rawat Inap')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('dirawat di: ')
                        print('Ruang: ', vip[-1])
                        print('________________________________')
                        vip.pop()
                else:
                    print('Ruangan tidak tersedia!, silahkan melakukan rawat jalan')
                    if len(stock_dbd) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_dbd)
                        print('______________________________')
                        stock_dbd.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vvip':
                if len(vvip) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', vvip[-1])
                    print('________________________________')
                    vvip.pop()
                else:
                    print('Ruangan tidak tersedia!, silahkan melakukan rawat jalan')
                    if len(stock_dbd) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_dbd)
                        print('______________________________')
                        stock_dbd.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
        elif diagnosa == 'tiphus':
            print('Pasien harus dirawat inap')
            print('ruangan yang Tersedia: ')
            print(regular)
            print(vip)
            print(vvip)
            print('kluster yang diinginkan pasien: regular/vip/vvip')
            kluster = input()
            print('Menyiapkan ruangan...')
            print('Ruangan ditemukan!')
            if kluster == 'regular':
                if len(regular) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', regular[-1])
                    print('________________________________')
                    regular.pop()
                else:
                    if len(stock_tiphus) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_tiphus)
                        print('______________________________')
                        stock_tiphus.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vip':
                if len(vip) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', vip[-1])
                    print('________________________________')
                    vip.pop()
                else:
                    if len(stock_dbd) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_dbd)
                        print('______________________________')
                        stock_dbd.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vvip':
                if len(vvip) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', vvip[-1])
                    print('________________________________')
                    vvip.pop()
                else:
                    if len(stock_tiphus) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_tiphus)
                        print('______________________________')
                        stock_tiphus.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
        elif diagnosa == 'gagal ginjal':
            print('Pasien harus dirawat inap')
            print('ruangan yang Tersedia: ')
            print(regular)
            print(vip)
            print(vvip)
            print('kluster yang diinginkan pasien: regular/vip/vvip')
            kluster = input()
            print('Menyiapkan ruangan...')
            print('Ruangan ditemukan!')
            if kluster == 'regular':
                if len(regular) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', regular[-1])
                    print('________________________________')
                    regular.pop()
                else:
                    if len(stock_gagalginjal) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_gagalginjal)
                        print('______________________________')
                        stock_gagalginjal.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vip':
                if len(vip) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', vip[-1])
                    print('________________________________')
                    vip.pop()
                else:
                    if len(stock_gagalginjal) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_gagalginjal)
                        print('______________________________')
                        stock_gagalginjal.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vvip':
                if len(vvip) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', vvip[-1])
                    print('________________________________')
                    vvip.pop()
                else:
                    if len(stock_gagalginjal) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin:', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_gagalginjal)
                        print('______________________________')
                        stock_gagalginjal.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
        elif diagnosa == 'gagal jantung':
            print('Pasien harus dirawat inap')
            print('ruangan yang Tersedia: ')
            print(regular)
            print(vip)
            print(vvip)
            print('kluster yang diinginkan pasien: regular/vip/vvip')
            kluster = input()
            print('Menyiapkan ruangan...')
            print('Ruangan ditemukan!')
            if kluster == 'regular':
                if len(regular) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', regular[-1])
                    print('________________________________')
                    regular.pop()
                else:
                    if len(stock_gagaljantung) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_gagaljantung)
                        print('______________________________')
                        stock_gagaljantung.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vip':
                if len(vip) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', vip[-1])
                    print('________________________________')
                    vip.pop()
                else:
                    if len(stock_gagaljantung) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin: ', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_gagaljantung)
                        print('______________________________')
                        stock_gagaljantung.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
            elif kluster == 'vvip':
                if len(vvip) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', vvip[-1])
                    print('________________________________')
                    vvip.pop()
                else:
                    if len(stock_gagaljantung) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin:', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('Obat pasien: ')
                        print(obat_gagaljantung)
                        print('______________________________')
                        stock_gagaljantung.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan dirujuk ke rumah sakit terdekat')
        elif diagnosa == 'demam':
            demam = int(input('berapa hari pasien demam? '))
            suhu = int(input('berapa suhu anda saat ini? '))
            rapid = input('apakah anda pernah berinteraksi dengan pengidap covid-19. ya/tidak ')
            if rapid == 'ya' or 'y':
                if demam in range(4) and suhu in range(40):
                    if len(stock_demam) > 0:
                        print('Menyiapkan obat...')
                        print('______________________________')
                        print('Keterangan Rawat Jalan')
                        print('Nama:', nama)
                        print('Usia: ', umur)
                        print('Jenis Kelamin:', kelamin)
                        print('Diagnosa: ', diagnosa)
                        print('lama demam: ', demam, ' hari')
                        print('Suhu: ', suhu)
                        print('Covid: Negatif')
                        print('Obat pasien: ')
                        print(obat_demam)
                        print('______________________________')
                        stock_demam.pop()
                    else:
                        print('Mohon Maaf')
                        print('Obat tidak tersedia, anda akan diberikan resep untuk membeli di apotik pilihan anda')
                        print('------------------------------')
                        print('Resep Obat')
                        print(obat_demam)
                        print('------------------------------')
                else:
                    print('anda membutuhkan pertolongan lebih lanjut, silahkan hubungi dokter anda')
            elif rapid == 'tidak' or 'n':
                print('Pasien harus dimasukkan kedalam ruang isolasi')
                print('Menyiapkan ruang isolasi...')
                print('Ruang isolasi ditemukan!')
                if len(ruang_isolasi) > 0:
                    print('________________________________')
                    print('Keterangan Rawat Inap')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin: ', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('dirawat di: ')
                    print('Ruang: ', ruang_isolasi[-1])
                    print('________________________________')
                    ruang_isolasi.pop()
                else:
                    print('Mohon Maaf')
                    print('Ruang isolasi tidak tersedia, silahkan hubungi rumah sakit lain')
        elif diagnosa == 'hipertensi':
            tensi = int(input('tensi sistolik: '))
            if tensi in range(130, 139):
                print('Anda menderita hipertensi stadium 1')
                if len(stock_hipertensi) > 0:
                    print('Menyiapkan obat...')
                    print('______________________________')
                    print('Keterangan Rawat Jalan')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin:', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('Tensi Darah: ', tensi)
                    print('Obat pasien: ')
                    print(obat_hipertensi)
                    print('______________________________')
                    stock_hipertensi.pop()
                else:
                    print('Mohon Maaf')
                    print('Obat tidak tersedia, anda akan diberikan resep untuk membeli di apotik pilihan anda')
                    print('------------------------------')
                    print('Resep Obat')
                    print(obat_hipertensi)
                    print('------------------------------')
            elif tensi in range(140, 180):
                print('anda menderita hipertensi stadium 2')
                if len(stock_hipertensi) > 0:
                    print('Menyiapkan obat...')
                    print('______________________________')
                    print('Keterangan Rawat Jalan')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin:', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('Tensi Darah: ', tensi)
                    print('Obat pasien: ')
                    print(obat_hipertensi)
                    print('______________________________')
                    stock_hipertensi.pop()
                else:
                    print('Mohon Maaf')
                    print('Obat tidak tersedia, anda akan diberikan resep untuk membeli di apotik pilihan anda')
                    print('------------------------------')
                    print('Resep Obat')
                    print(obat_hipertensi)
                    print('------------------------------')
            elif tensi > 180:
                print('Anda menderita darurat Hipertensi')
                if len(stock_hipertensi) > 0:
                    print('Menyiapkan obat...')
                    print('______________________________')
                    print('Keterangan Rawat Jalan')
                    print('Nama:', nama)
                    print('Usia: ', umur)
                    print('Jenis Kelamin:', kelamin)
                    print('Diagnosa: ', diagnosa)
                    print('Tensi Darah: ', tensi)
                    print('Obat pasien: ')
                    print(obat_hipertensi)
                    print('______________________________')
                    stock_hipertensi.pop()
                else:
                    print('Mohon Maaf')
                    print('Obat tidak tersedia, anda akan diberikan resep untuk membeli di apotik pilihan anda')
                    print('------------------------------')
                    print('Resep Obat')
                    print(obat_hipertensi)
                    print('------------------------------')
        elif diagnosa == 'diare':
            if len(stock_diare) > 0:
                print('Menyiapkan obat...')
                print('______________________________')
                print('Keterangan Rawat Jalan')
                print('Nama:', nama)
                print('Usia: ', umur)
                print('Jenis Kelamin:', kelamin)
                print('Diagnosa: ', diagnosa)
                print('Obat pasien: ')
                print(obat_diare)
                print('______________________________')
                stock_diare.pop()
            else:
                print('Mohon Maaf')
                print('Obat tidak tersedia, anda akan diberikan resep untuk membeli di apotik pilihan anda')
                print('------------------------------')
                print('Resep Obat')
                print(obat_diare)
                print('------------------------------')
        elif diagnosa == 'migrain':
            if len(stock_migrain) > 0:
                print('Menyiapkan obat...')
                print('______________________________')
                print('Keterangan Rawat Jalan')
                print('Nama:', nama)
                print('Usia: ', umur)
                print('Jenis Kelamin:', kelamin)
                print('Diagnosa: ', diagnosa)
                print('Obat pasien: ')
                print(obat_migrain)
                print('______________________________')
                stock_migrain.pop()
            else:
                print('Mohon Maaf')
                print('Obat tidak tersedia, anda akan diberikan resep untuk membeli di apotik pilihan anda')
                print('------------------------------')
                print('Resep Obat')
                print(obat_migrain)
                print('------------------------------')
    else:
        print('Sedang diproses...')
        print('Mohon Maaf')
        print('Penyakit tidak terdaftar dalam sistem')
