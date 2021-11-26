nama = input("Masukan nama anda ")

print("Hai, Selamat Datang", nama)

playing =  input("Apakah anda ingin bermain? ya/tidak --> ")
if playing.lower() !="ya":
    quit()

print("Oke! Ayo bermain :)")
score = 0

answer = input ("Apa kepanjangan dari LAN? : ")
if answer.lower() == "local area network":
    print("Benar!")
    score +=1
else:
    print("Jawaban anda salah!")

answer = input ("Apa kepanjangan dari MAN? : ")
if answer.lower() == "metropolitan area network":
    print("Benar!")
    score +=1
else:
    print("Jawaban anda salah!")

answer = input ("Apa kepanjangan dari WAN? : ")
if answer.lower() == "wide area network":
    print("Benar!")
    score +=1
else:
    print("Jawaban anda salah!")

answer = input ("Apa kepanjangan dari SO? : ")
if answer.lower() == "sistem operasi":
    print("Benar!")
    score +=1
else:
    print("Jawaban anda salah!")

print("Kamu dapat " + str(score) + " jawaban benar.")
print("Kamu dapat " + str((score / 4) * 100) + "%.")