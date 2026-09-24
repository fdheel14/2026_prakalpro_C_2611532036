# Input dari user
total_belanja_2036 = float(input("Masukkan total belanja Anda (Rp): "))

# Input status member (mengecek apakah user mengetik "y" atau "ya")
input_member_2036 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_2036 = input_member_2036 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik "y" atau "ya")
input_promo_2036 = input("Apakah Anda Memiliki Kode Promo (y/t): ").strip().lower()
kode_promo_valid_2036 = input_promo_2036 in ["y", "ya"]

total_diskon_persen_2036 = 0

if total_belanja_2036 >= 100000:
    total_diskon_persen_2036 += 10 # Diskon belanja besar

if is_member_2036:
    total_diskon_persen_2036 += 5 # Diskon member

if kode_promo_valid_2036:
    total_diskon_persen_2036 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2036 = total_belanja_2036 * (total_diskon_persen_2036 / 100)
total_bayar_2036 = total_belanja_2036 - nominal_diskon_2036

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon: {total_diskon_persen_2036}% (Rp {nominal_diskon_2036:,.0f})")
print(f"Total Bayar: Rp {total_bayar_2036:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2036}%")
