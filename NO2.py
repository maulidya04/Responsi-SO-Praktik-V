print("")
print("==========Simulasi Management Penjadwalan Algoritma Round Robin==========")
print("")

print("")
print("Penjadwalan :")
print("")

import os
program = []

def head():
    os.system("cls")
    jumlah_proses = int(input('Jumlah Proses : '))

    for i in range(jumlah_proses):
        nama_program = input('Nama Program : ')
        lama_program = int(input('Lama Program [Menit] :'))
        program.append([nama_program,lama_program])

    quantum = int(input('Quantum Time / Jatah Waktu [Menit] : '))

    waktu_selesai = 0
    for i in program:
        waktu_selesai += i[1]

    print("")
    showRR(waktu_selesai,quantum,program)


#rumus
def showRR(waktu_selesai,quantum,programlist):
    start = 0
    while start < waktu_selesai:
        for i,data in enumerate(programlist):
            nm_program = data[0]
            lm_program = data[1]
            sisa = lm_program - quantum
            
            if(lm_program >= quantum):
                print(nm_program,' = ',start, ' - ', start + quantum )
            else:
                print(nm_program,' = ',start, ' - ', start + lm_program )
            
            if(lm_program >= quantum):
                start += quantum
            else:
                start += lm_program
                
            if( sisa > 0):
                program.append([nm_program,sisa])



head()

print("")
print("====================================================")
print("")