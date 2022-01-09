# No 1
print("")
print("==========Responsi SO Praktik Simulasi Management RAM==========")
print("")

total_ram=int(input("Kapasitas total ram (Mbps) = "))
total_petabit=int(input("Total peta bit = "))
os=int(input("Kapasitas Sistem operasi (Mbps) = "))
program1=int(input("Kapasitas program 1 = "))
program2=int(input("Kapasitas program 2 = "))

#convert dari Mbps ke Kbps
ramtokb=total_ram*1024
ostokb=os*1024

#rumus 
total=program1+program2
perpetabit=ramtokb/total_petabit
ram_terpakai=ostokb+total
blok_bernilai1=ram_terpakai/total_petabit
ram_tdk_terpakai=ramtokb-ram_terpakai
blok_bernilai0=perpetabit-blok_bernilai1


print("")
print("==========Hasil Simulasi Management RAM==========")
print("")


print("Total ram: "+str(ramtokb))
print("Peta bit: "+str(total_petabit))
print("Kapasitas per petabit: "+str(perpetabit))
print("Ram terpakai: "+str(ram_terpakai))
print("Ram tidak terpakai: "+str(ram_tdk_terpakai))
print("Jumlah blok bernilai 1: "+str(blok_bernilai1))
print("Jumlah blok bernilai 0: "+str(blok_bernilai0))

print("")
print("====================================================")
print("")
