# İstifadəçidən iki ədəd daxil etmək
reqem1 = float(input("Birinci ədədi daxil edin: "))
reqem2 = float(input("İkinci ədədi daxil edin: "))

# Əməliyyatları yerinə yetirib nəticələri hesablamaq
cemi = reqem1 + reqem2
ferqi = reqem1 - reqem2
hasil = reqem1 * reqem2

# Bölmə əməliyyatı üçün səhvən 0-a bölməyinizi önləmək üçün əlavə yoxlama
if reqem2 != 0:
    bolme = reqem1 / reqem2
else:
    bolme = "0-a bölmə mümkün deyil"

# Nəticələri ekrana çıxarmaq
print(f"{reqem1} + {reqem2} = {cemi}")
print(f"{reqem1} - {reqem2} = {ferqi}")
print(f"{reqem1} * {reqem2} = {hasil}")
print(f"{reqem1} / {reqem2} = {bolme}")