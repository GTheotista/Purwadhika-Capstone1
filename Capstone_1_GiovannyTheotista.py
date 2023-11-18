<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:42:22 2023

@author: giovanny
"""
#pilih salah satu data yang akan didemokan
data=[[123,'Gio','MATH',3.75,5,90],[124,'Steve','IT',3.9,7,70]]
#data=[] #Data Kosong

while True:
    print('\n ====================')
    task=int(input('Main Menu: \n 1. Tambah data \n 2. Lihat data \n 3. Edit data \n 4. Hapus Data \n 5. Statistik Nilai Kalkulus \n 6. Stop Program \n Pilihan Anda: '))
    #1 Tambah Data
    if task==1:
        while True:
            print('\n ====================')
            id_mahasiswa=int(input('Input ID: '))
            nama=input('Input nama: ')
            prodi=input('Input Prodi: ')
            ipk=input('Input IPK: ')
            smst=input('Input Semester: ')
            kalkulus=int(input('Input Nilai Kalkulus: '))
            newdata=[id_mahasiswa,nama,prodi,ipk,smst,kalkulus]
            print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
            print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                newdata[0],newdata[1],newdata[2],newdata[3],newdata[4],newdata[5]))
            confirm=int(input('Apakah data yang dimasukan sudah benar? \n 1. Ya \n 2. Ulangi input data \n 3. Menu utama \n Pilihan Anda: '))
            print('\n ====================')
            if confirm==1:
                data.append(newdata)
                break
            elif confirm==2:
                continue
            else:
                break
    # Lihat Data
    elif task==2:
        print('\n ====================')
        if (len(data))!=0:
            while True:
                lihat=int(input('Lihat data: \n 1. Seluruh Data \n 2. Cari Data Dengan ID \n 3. Cari Data Dengan Nama \n 4. Kembali ke Menu Utama \n Pilihan Anda:'))
                print('\n ====================')
                if lihat == 1:
                    #Tampilkan seluruh data
                    print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                    for i in range (len(data)):
                        print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                            data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]))
                elif lihat == 2: 
                    input_id=int(input('Masukan ID yang Ingin Dicari: '))
                    print('\n ====================')
                    indeks = None
                    #Mencari index dari data pada sublist
                    for sublist in data:
                        if input_id in sublist:
                            indeks = sublist
                            break
                    #Tampilkan data jika indexnya sudah diketahui
                    if indeks is not None:
                        print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                        print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                            indeks[0],indeks[1],indeks[2],indeks[3],indeks[4],indeks[5]))
                    else:
                        print('\n Data Tidak Ditemukan')
                elif lihat ==3:
                    input_nama=str(input('Masukan Nama yang Ingin Dicari: '))
                    print('\n ====================')
                    print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                    #tampilkan seluruh data yang memiliki input_nama pada stringnya
                    for i in range (len(data)):
                        if input_nama in data[i][1]:
                            print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]))
                        else:
                            continue
                else:
                    break    
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Edit Data
    elif task==3:
        print('\n ====================')
        if (len(data))!=0:
            input_id=int(input('Masukan ID yang Ingin Diedit Datanya: '))
            print('\n ====================')
            indeks = None
            #Mencari index dari data pada sublist
            for sublist in data:
                if input_id in sublist:
                    indeks = sublist
                    break
            if indeks is not None:
                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                    indeks[0],indeks[1],indeks[2],indeks[3],indeks[4],indeks[5]))
                confirm_id=int(input('Apakah Benar Data Ini? \n 1. Untuk Ya \n 2. Ke Main Menu \n Pilihan Anda:'))
                if confirm_id==1:
                    print('\n ====================')
                    change=int(input('Data yang Ingin Diganti? \n 1. Nama \n 2. Prodi \n 3. IPK \n 4. Semester \n 5. Nilai Kalkulus \n 6. Kembali \n Pilihan Anda: '))
                    if change==1: #ganti nama
                        change_name=str(input('Masukan Nama Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[1] = change_name
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==2: #ganti prodi
                        change_prodi=str(input('Masukan Prodi Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[2] = change_prodi
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==3: #ganti ipk
                        change_ipk=str(input('Masukan IPK Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[3] = change_ipk
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==4: #ganti semester
                        change_smst=str(input('Masukan Semester Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[4] = change_smst
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==5: #ganti nilai kalkulus
                        change_nilai=str(input('Masukan Nilai Kalkulus Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[5] = change_nilai
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                print('Data Telah Diupdate')
            else:
                print('\n ====================')
                print('Data Tidak Ditemukan')
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Hapus Data
    elif task==4:
        print('\n ====================')
        if (len(data))!=0:
            input_id=int(input('Masukan ID yang Ingin Diedit Datanya: '))
            indeks = None
            #Mencari index dari data pada sublist
            for sublist in data:
                if input_id in sublist:
                    indeks = sublist
                    break
            if indeks is not None:
                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                    indeks[0],indeks[1],indeks[2],indeks[3],indeks[4],indeks[5]))
                confirm_id=int(input('Apakah Benar Data Ini? \n 1. Untuk Ya \n 2. Ke Main Menu \n Pilihan Anda:'))
                print('\n ====================')
                #remove data
                if confirm_id==1:
                    for sublist in data[:]:
                        if sublist[0] == input_id:
                            data.remove(sublist)
                    print('Data Telah Diupdate')
            else:
                print('\n ====================')
                print('Data Tidak Ditemukan')                
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Statistik Data
    elif task==5:
        print('\n ====================')
        if (len(data))!=0:
            nilai=[]
            for i in range (len(data)):
                nilai.append(data[i][5])
            #Urutkan nilai
            nilai.sort()
            #Hitung Rata rata
            mean=sum(nilai)/len(data)
            #Nilai Terendah
            minimum=nilai[0]
            #Nilai Teringgi
            maximum=nilai[len(nilai)-1]
            print(' Rata Rata Nilai Kalkulus: {} \n Nilai Kalkulus Terendah: {} \n Nilai Kalkulus Tertinggi: {}'.format(
                mean,minimum,maximum))
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Close Program
    elif task==6:
        print('Sampai Jumpa')
    else:
        print('Masukan Pilihan Lain')
        break
=======
#Capstone 1 Purwadhika Project

#pilih salah satu data yang akan didemokan
data=[[123,'Gio','MATH',3.75,5,90],[124,'Steve','IT',3.9,7,70]]
#data=[] #Data Kosong

while True:
    print('\n ====================')
    task=int(input('Main Menu: \n 1. Tambah data \n 2. Lihat data \n 3. Edit data \n 4. Hapus Data \n 5. Statistik Nilai Kalkulus \n 6. Stop Program \n Pilihan Anda: '))
    #1 Tambah Data
    if task==1:
        while True:
            print('\n ====================')
            id_mahasiswa=int(input('Input ID: '))
            nama=input('Input nama: ')
            prodi=input('Input Prodi: ')
            ipk=input('Input IPK: ')
            smst=input('Input Semester: ')
            kalkulus=int(input('Input Nilai Kalkulus: '))
            newdata=[id_mahasiswa,nama,prodi,ipk,smst,kalkulus]
            print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
            print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                newdata[0],newdata[1],newdata[2],newdata[3],newdata[4],newdata[5]))
            confirm=int(input('Apakah data yang dimasukan sudah benar? \n 1. Ya \n 2. Ulangi input data \n 3. Menu utama \n Pilihan Anda: '))
            print('\n ====================')
            if confirm==1:
                data.append(newdata)
                break
            elif confirm==2:
                continue
            else:
                break
    # Lihat Data
    elif task==2:
        print('\n ====================')
        if (len(data))!=0:
            while True:
                lihat=int(input('Lihat data: \n 1. Seluruh Data \n 2. Cari Data Dengan ID \n 3. Cari Data Dengan Nama \n 4. Kembali ke Menu Utama \n Pilihan Anda:'))
                print('\n ====================')
                if lihat == 1:
                    #Tampilkan seluruh data
                    print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                    for i in range (len(data)):
                        print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                            data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]))
                elif lihat == 2: 
                    input_id=int(input('Masukan ID yang Ingin Dicari: '))
                    print('\n ====================')
                    indeks = None
                    #Mencari index dari data pada sublist
                    for sublist in data:
                        if input_id in sublist:
                            indeks = sublist
                            break
                    #Tampilkan data jika indexnya sudah diketahui
                    if indeks is not None:
                        print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                        print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                            indeks[0],indeks[1],indeks[2],indeks[3],indeks[4],indeks[5]))
                    else:
                        print('\n Data Tidak Ditemukan')
                elif lihat ==3:
                    input_nama=str(input('Masukan Nama yang Ingin Dicari: '))
                    print('\n ====================')
                    print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                    #tampilkan seluruh data yang memiliki input_nama pada stringnya
                    for i in range (len(data)):
                        if input_nama in data[i][1]:
                            print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5]))
                        else:
                            continue
                else:
                    break    
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Edit Data
    elif task==3:
        print('\n ====================')
        if (len(data))!=0:
            input_id=int(input('Masukan ID yang Ingin Diedit Datanya: '))
            print('\n ====================')
            indeks = None
            #Mencari index dari data pada sublist
            for sublist in data:
                if input_id in sublist:
                    indeks = sublist
                    break
            if indeks is not None:
                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                    indeks[0],indeks[1],indeks[2],indeks[3],indeks[4],indeks[5]))
                confirm_id=int(input('Apakah Benar Data Ini? \n 1. Untuk Ya \n 2. Ke Main Menu \n Pilihan Anda:'))
                if confirm_id==1:
                    print('\n ====================')
                    change=int(input('Data yang Ingin Diganti? \n 1. Nama \n 2. Prodi \n 3. IPK \n 4. Semester \n 5. Nilai Kalkulus \n 6. Kembali \n Pilihan Anda: '))
                    if change==1: #ganti nama
                        change_name=str(input('Masukan Nama Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[1] = change_name
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==2: #ganti prodi
                        change_prodi=str(input('Masukan Prodi Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[2] = change_prodi
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==3: #ganti ipk
                        change_ipk=str(input('Masukan IPK Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[3] = change_ipk
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==4: #ganti semester
                        change_smst=str(input('Masukan Semester Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[4] = change_smst
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                    elif change==5: #ganti nilai kalkulus
                        change_nilai=str(input('Masukan Nilai Kalkulus Baru: '))
                        print('\n ====================')
                        for sublist in data:
                            if sublist[0] == input_id:
                                sublist[5] = change_nilai
                                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                                    sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5]))
                print('Data Telah Diupdate')
            else:
                print('\n ====================')
                print('Data Tidak Ditemukan')
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Hapus Data
    elif task==4:
        print('\n ====================')
        if (len(data))!=0:
            input_id=int(input('Masukan ID yang Ingin Diedit Datanya: '))
            indeks = None
            #Mencari index dari data pada sublist
            for sublist in data:
                if input_id in sublist:
                    indeks = sublist
                    break
            if indeks is not None:
                print('ID \t\t | Nama \t | Prodi \t | IPK \t | Semester \t | Nilai Kalkulus')
                print('{} \t | {} \t | {} \t \t| {} \t | {} \t \t | {}'.format(
                    indeks[0],indeks[1],indeks[2],indeks[3],indeks[4],indeks[5]))
                confirm_id=int(input('Apakah Benar Data Ini? \n 1. Untuk Ya \n 2. Ke Main Menu \n Pilihan Anda:'))
                print('\n ====================')
                #remove data
                if confirm_id==1:
                    for sublist in data[:]:
                        if sublist[0] == input_id:
                            data.remove(sublist)
                    print('Data Telah Diupdate')
            else:
                print('\n ====================')
                print('Data Tidak Ditemukan')                
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Statistik Data
    elif task==5:
        print('\n ====================')
        if (len(data))!=0:
            nilai=[]
            for i in range (len(data)):
                nilai.append(data[i][5])
            #Urutkan nilai
            nilai.sort()
            #Hitung Rata rata
            mean=sum(nilai)/len(data)
            #Nilai Terendah
            minimum=nilai[0]
            #Nilai Teringgi
            maximum=nilai[len(nilai)-1]
            print(' Rata Rata Nilai Kalkulus: {} \n Nilai Kalkulus Terendah: {} \n Nilai Kalkulus Tertinggi: {}'.format(
                mean,minimum,maximum))
        else:
            print('Data Kosong, Kembali Ke Menu Utama')
    #Close Program
    elif task==6:
        print('Sampai Jumpa')
    else:
        print('Masukan Pilihan Lain')
        break
>>>>>>> fcc9b867c682eaa320d8696f7a27795cc5af8007
