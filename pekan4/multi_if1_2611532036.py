umur_2036 = int(input("Masukkan Umur Anda: "))
sim_2036 = input("Apakah Anda Sudah Punya Sim C ? (y/t): ") [0]

if umur_2036 >= 17 and sim_2036 == "y":
    print("Anda Sudah Dewasa dan Boleh Mengendarai Motor")

if umur_2036 >= 17 and sim_2036 != "t":
    print("Anda Sudah Dewasa tapi Tidak Boleh Mengendarai Motor")

if umur_2036 < 17 and sim_2036 == "y":
    print("Anda Belum Cukup Umur punya SIM")

if umur_2036 < 17 and sim_2036 != "y":
    print("Anda Belum Cukup Umur bawa motor")