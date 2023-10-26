def konversi_minggu(minggu=0):
    def konversi_hari(hari=0):
        def konversi_jam(jam=0):
            def konversi_menit(menit=0):
                return ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
            return konversi_menit
        return konversi_jam
    return konversi_hari

data = ["3 minggu 3 hari 7 jam 21 menit", 
        "5 minggu 5 hari 8 jam 11 menit", 
        "7 minggu 1 hari 5 jam 33 menit"]
outputdata = []

for input_str in data:
    components = input_str.split()
    minggu = int(components[0])
    hari = int(components[2])
    jam = int(components[4])
    menit = int(components[6])

    konvert = konversi_minggu(minggu)(hari)(jam)(menit)  
    outputdata.append(konvert)

print("Output data =", outputdata)


