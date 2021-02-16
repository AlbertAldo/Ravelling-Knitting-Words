print("UJIAN 16 FEBRUARI 2021")
print("Albert Aldo")
print("Soal 3 - Ravelling & Knitting Words")
print("="*65)

"""
Buatlah sebuah file python yang berisi 2 buah return function, dengan 1 argumen yang dapat digunakan 
untuk mengurai & merajut sebuah string

fungsi ravel(...) akan mengurai string. contoh output yang diharapkan adalah sebagai berikut:
# Function Initialization :
def ravel(...):
    ......

# Use the function
print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))


# Output:
PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
DDiDigDigiDigitDigitaDigital
CCoCodCodiCodinCoding
SScSchSchoSchooSchool


Sedangkan fungsi knit(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya. 
contoh output yang diharapkan adalah sebagai berikut:

# Function Initialization :
def knit(...):
    ......
    
# Use the function
print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))

# Output:
Purwadhika
Digital
Coding
School
Catatan:

Silakan Commit & push (Upload) source code project ke Github Anda, buatlah repo dengan nama Ravel_Knit_Words. 
Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan 
operational_jkt@purwadhika.com dengan subjek email Exam Modul 1 - JCDS12 - Nama, url bisa dikirimkan 
dalam 1 email yg sama
"""

# purwadhika = "Purwadhika"
# listpurwadhika = []
# hasilpurwadhika = ""
# for i in purwadhika:
#     listpurwadhika.append(i)
#     hasilpurwadhika += "".join(listpurwadhika)

# print(hasilpurwadhika)

# digital = "Digital"
# listdigital = []
# hasildigital = ""

# for j in digital:
#     listdigital.append(j)
#     hasildigital += "".join(listdigital)

# print(hasildigital)

# coding = "Coding"
# listcoding = []
# hasilcoding = ""

# for k in coding:
#     listcoding.append(k)
#     hasilcoding += "".join(listcoding)

# print(hasilcoding)

# school = "School"
# listschool = []
# hasilschool = ""

# for l in school:
#     listschool.append(l)
#     hasilschool += "".join(listschool)

# print(hasilschool)

# knit2 = "DDiDigDigiDigitDigitaDigital"
# knit3 = "CCoCodCodiCodinCoding"
# knit4 = "SScSchSchoSchooSchool"

# knit1 = "PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"
# listknit1 = []
# bantulistknit1 = []
# hasilknit1 = ""
# for i in knit1:
#     listknit1.append(i)

# listknit1.reverse()
# print(listknit1)
# for j in listknit1:
#     if j not in bantulistknit1:
#         bantulistknit1.append(j)

# print(bantulistknit1)
# bantulistknit1.reverse()
# print(bantulistknit1)
# hasilknit1 += "".join(bantulistknit1)

def ravel(kata):
    listkata = []
    hasilkata = ""
    for i in kata:
        listkata.append(i)
        hasilkata += "".join(listkata)
    return hasilkata

def knit(knit1):
    listknit1 = []
    bantulistknit1 = []
    hasilknit1 = ""
    for i in knit1:
        listknit1.append(i)

    listknit1.reverse()
    # print(listknit1)
    for j in listknit1:
        bantulistknit1.append(j)
        if j.istitle() == True:
            break

    # print(bantulistknit1)
    bantulistknit1.reverse()
    # print(bantulistknit1)
    hasilknit1 += "".join(bantulistknit1)
    return hasilknit1

print("-"*28 + "RAVELLING" + "-"*28)
print(ravel("Purwadhika"))
print(ravel("Digital"))
print(ravel("Coding"))
print(ravel("School"))

print("-"*28 + "KNITTING" + "-"*28)
print(knit("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))
print(knit("DDiDigDigiDigitDigitaDigital"))
print(knit("CCoCodCodiCodinCoding"))
print(knit("SScSchSchoSchooSchool"))