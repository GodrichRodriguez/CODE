# month in number 1 to 12
# list off zodiac sign  
#  Aries,  Taurus,  Gemini,  Cancer, 5 Leo,  Virgo
#  Libra,  Scorpio,  Sagittarius,  Capricorn,  Aquarius,  Pisces
month = int(input("enter a month base on 1/12: "))
days = int(input("enter a day: "))

if (month == 3 and days >= 21) or (month == 4 and days <= 19):
    print("aries")
elif (month == 4 and days >= 20) or (month == 5 and days <= 20):
    print("taurus")
elif (month == 5 and days >= 21) or (month == 6 and days <= 20):
    print("gemini")
elif (month == 6 and days >= 21) or (month == 7 and days <= 22):
    print("cancer")
elif (month == 7 and days >= 23) or (month == 8 and days <= 22):
    print("leo")
elif (month == 8 and days >= 23) or (month == 9 and days <= 22):
    print("virgo")
elif (month == 9 and days >= 23) or (month == 10 and days <= 22):
    print("libra")
elif (month == 10 and days >= 23) or (month == 11 and days <= 21):
    print("scorpio")
elif (month == 11 and days >= 22) or (month == 12 and days <= 21):
    print("Sagittarius")
elif (month == 12 and days >= 22) or (month == 1 and days <= 19):
    print("Capricorn")
elif (month == 1 and days >= 20) or (month == 2 and days <= 18):
    print("Aquarius")
elif (month == 2 and days >= 19) or (month == 3 and days <= 20):
    print("Pisces")
else:
    print("invalid")


    
                





