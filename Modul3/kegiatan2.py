def konversi_minggu(weeks=0):
    def konversi_hari(days=0):
        def konversi_jam(hours=0):
            def konversi_menit(minutes=0):
                return f"{weeks}{days}{hours}{minutes}"  
            return konversi_menit
        return konversi_jam
    return konversi_hari

data = ["3 minggu 3 hari 7 jam 21 menit", 
        "5 minggu 5 hari 8 jam 11 menit", 
        "7 minggu 1 hari 5 jam 33 menit"]
outputdata = []

for input_str in data:
    components = input_str.split()
    weeks = int(components[0])
    days = int(components[2])
    hours = int(components[4])
    minutes = int(components[6])

    konvert = konversi_minggu(weeks)(days)(hours)(minutes)
    outputdata.append(konvert)

# Fungsi untuk memisahkan setiap angka ke dalam list string
def split_digits(data):
    return [list(str(x)) for x in data]

split_outputdata = [split_digits(konvert) for konvert in outputdata]
print("Hasil Filtering : ")
for item in split_outputdata:
    print(item)


