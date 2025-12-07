print('### Selamat Datang di Program Hitung Bidang Datar ###')
countType=["1. Luas", 
           "2. Keliling"]

ShapeTypeA=['1. Persegi',
           '2. Segi Tiga',
           '3. Persegi Panjang',
           '4. Belah Ketupat',
           '5. jajar Genjang',
           '6. lingkaran',
           '7. Trapesium',
           '8. Layang-Layang']


#ask user to choice count Type Luas/Keliling
def option1_countType():
    for i in countType:
        print (i)
    userinputhandle1=int(input('Choice the count type: '))
    if userinputhandle1 == countType[0]:
        option2_luas()
    else:
        option2_Keliling()

#ask user to choice shape type for counthing the luas
def option2_luas():
    #loop shapeTypeA
    for i in ShapeTypeA:
        #show to user some types of shape
        print (i)

    #Logic Handling
    userinputHandle2=int(input('Choice a Shape Type: '))
    if userinputHandle2 == 1:
        SquareLuas()
    elif userinputHandle2 == 2:
        TriangleLuas()
    elif userinputHandle2 == 3:
        luasPerpan()
    elif userinputHandle2 == 4:
        luasbelahketupat()
    elif userinputHandle2 == 5:
        jajangLuas()        
    elif userinputHandle2 == 6:
        sircleLuas()
    elif userinputHandle2 == 7:
        traphesiumLuas()
    elif userinputHandle2 == 8:
        layang2Luas()


#ask user to choice shape type for counthing the keliling
def option2_Keliling():
    #loop shapeTypeA
    for i in ShapeTypeA:
        #show user some types of shape
        print (i)

    #logic handling
    userinputHandle2=int(input('Choice a Shape Type: '))
    if userinputHandle2 == 1:
        SquareKeliling()
    elif userinputHandle2 == 2:
        TriangKeliling()
    elif userinputHandle2 == 3:
        kelilingperpan()
    elif userinputHandle2 == 4:
        kelilingbelahketupat()
    elif userinputHandle2 == 5:
        jajangKeliling()
    elif userinputHandle2 == 6:
        sirclekeliling()
    elif userinputHandle2 == 7:
        traphesiumKeliling()
    elif userinputHandle2 == 8:
        layang2keliling()

#ask user to exit or counting again
def option3():
    userinputhandle3=(input('Do You Want to Count Again. yes/no?: '))
    if userinputhandle3 == "yes":
        option1_countType()
    else:
        exit()

#Square rumus
def SquareLuas():
    sisi=int(input("Sisi: "))
    print("Luas persegi adalah:", sisi*sisi)
    option3()
def SquareKeliling():
    sisi=int(input("Sisi: "))
    print("Keliling persegi adalah:", sisi*4)
    option3()

#Triangle Rumus
def TriangleLuas():
    sisi=int(input('Sisi: '))
    tinggi=int(input('Tinggi: '))
    print("Luas segi tiga adalah:", 1.5*sisi*tinggi)
    option3()
def TriangKeliling():
    sisia=int(input('Sisi a: '))
    sisib=int(input('Sisi b: '))
    sisic=int(input('Sisi c: '))
    print("Keliling segi tiga adalah: ", sisia*sisib*sisic)
    option3()

#Rumus Persegipanjang
def luasPerpan():
    panjang=int(input('Panjang: '))
    lebar=int(input('Lebar: '))
    print("Luas persegi panjang:", panjang*lebar)
    option3()
def kelilingperpan():
    panjang=int(input('Panjang: '))
    lebar=int(input('Lebar: '))
    print("keliling persegi panjang:", (panjang*lebar)*2)
    option3()

#belah ketupat Rumus
def luasbelahketupat():
    d1=int(input('Diagonal 1: '))
    d2=int(input('Diagonal 2: '))
    print("Luas:", 1.5*d1*d2)
    option3()
def kelilingbelahketupat():
    sisi=int(input('Sisi: '))
    print("keliling belah ketupat adalah:", sisi*4)
    option3()

#Layang-Layang rumus 
def layang2Luas():
    d1=int(input('diagonal 1: '))
    d2=int(input('diagonal 2: '))
    print("luas layang-layang adalah: ", d1*d2)
    option3()
def layang2keliling():
    sisia=int(input('sisi a: '))
    sisib=int(input('sisi b: '))
    print("keliling layang-layang Adalah: ", (sisia+sisib)*2)
    option3()

#Sircle Rumus
def sircleLuas():
    print("Sorry This Fiture is Developing :(")
    option3()
def sirclekeliling():
    print('Sorry This Fiture is Developing :(')
    option3()

#jajar genjang Rumus
def jajangLuas():
    alas=int(input('Alas: '))
    tinggi=int(input('Tinggi: '))
    print("Luas Jajar Genjang Adalah:", alas*tinggi)
    option3()
def jajangKeliling():
    alas=int(input('Alas: '))
    siring=int(input('Sisi Miring: '))
    print('Keliling Jajar Genjang Adalah:', (alas+siring)*2)
    option3()

#Traphesium Rumus
def traphesiumLuas():
    sijarA=int(input('Sisi Sejajar A: '))
    sijarB=int(input('Sisi Sejajar B: '))
    tinggi=int(input('Tinggi: '))
    print('Luas Traphesium adalah:', 1.5*(sijarA*sijarB)*tinggi)
    option3()
def traphesiumKeliling():
    sijarA=int(input('Sisi Sejajar A: '))
    sijarB=int(input('Sisi Sejajar B: '))
    siringA=int(input('Sisi Miring A: '))
    siringB=int(input('Sisi Miring B:'))
    print("Keliling Traphesium adalah:", sijarA+sijarB+siringA+siringB)
    option3()

#Show Welcome and dashboard
option1_countType()