# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:37:53 2020
@author: HP
"""

import csv

def kota():
    print("Select a City")
    print("Departure \t Arrival")
    print("▶ Jakarta \t ▶ Jakarta")
    print("▶ Makassar \t ▶ Makassar")
    print("▶ Surabaya \t ▶ Surabaya")
    print("▶ Yogyakarta \t ▶ Yogyakarta")
    print("▶ Denpasar \t ▶ Denpasar")
    print("")

def date():
    print("Departure Date")
    
    global tanggal
    try:
        tanggal = int(input("Date (1-31)    : "))
        while tanggal not in range (1,32):
            print ("\nPlease input date")
            tanggal = int(input("Date (1-31)    : "))
    except ValueError:
        print("Please input date")
        tanggal = int(input("Date (1-31)    : "))
    
    global bulan    
    try:
        bulan = int(input ("Month (1-12)   : "))
        while bulan not in range (1,13):
            print ("\nPlease input month")
            bulan = int(input ("Month (1-12)   : "))
    except ValueError:
        print("Please input month")
        bulan = int(input ("Month (1-12)   : "))    
    
    global tahun
    try:
        tahun = int(input ("Year           : "))
        while tahun < 2020:
            print ("Please input the current year")
            tahun = int(input ("Year           : "))
    except ValueError:
        print ("Please input the current year")
        tahun = int(input ("Year           : "))    
    
def jumlahpenumpang():
    global penumpang_data
    try:
        penumpang_data = int(input("Passengers     : "))
    except ValueError:
        print("\nPlease input the number of passengers")
        jumlahpenumpang()
    
def Yogyakarta_Jakarta():
    flights = []
    with open('Yogyakarta_Jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def Yogyakarta_Makassar():
    flights = []
    with open('Yogyakarta_Makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")

def Yogyakarta_Surabaya():
    flights = []
    with open('Yogyakarta_Surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")

def Yogyakarta_Denpasar():
    flights = []
    with open('Yogyakarta_Denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def denpasar_jakarta():
    flights = []
    with open('denpasar_jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def denpasar_makassar():
    flights = []
    with open('denpasar_makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
        
def denpasar_surabaya():
    flights = []
    with open('denpasar_surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")        

def denpasar_yogyakarta():
    flights = []
    with open('denpasar_yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_jakarta():
    flights = []
    with open('makassar_jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_surabaya():
    flights = []
    with open('makassar_surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_yogyakarta():
    flights = []
    with open('makassar_yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def makassar_denpasar():
    flights = []
    with open('makassar_denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t\t {data['PRICE']}")
              
def jakarta_surabaya():
    flights = []
    with open('jakarta_surabaya.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
        
def jakarta_makassar():
    flights = []
    with open('jakarta_makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")

def jakarta_denpasar():
    flights = []
    with open('jakarta_denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
        
def jakarta_yogyakarta():
    flights = []
    with open('jakarta_yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
              
def Surabaya_Jakarta():
    flights = []
    with open('Surabaya_Jakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
        
def Surabaya_Denpasar():
    flights = []
    with open('Surabaya_Denpasar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
        
def Surabaya_Makassar():
    flights = []
    with open('Surabaya_Makassar.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")
        
def Surabaya_Yogyakarta():
    flights = []
    with open('Surabaya_Yogyakarta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("NO \t AIRLINES \t TIME \t\t PRICE")
    print("-" * 70)
    for data in flights:
        print(f"{data['NO']} \t {data['AIRLINES']} \t {data['TIME']} \t {data['PRICE']}")

def pesan():
    import math
    print("Frequently Added to Booking")
    asuransi_perjalanan = input("◽ Travel Insurance Rp 37.000/pax? (yes/no) : ")
    juml_tiket = penumpang_data
    print("")
    
    global asuransi
    if asuransi_perjalanan == "yes":
        asuransi = 37000
    elif asuransi_perjalanan == "no":
        asuransi = 0
    else:
        print ("Please try again")
    
    global total_harga
    total_harga = juml_tiket * (int(flights[pilih]['price']) + asuransi)
    global original
    original = math.ceil (juml_tiket * int(flights[pilih]['price']))
    global insurance
    insurance = math.ceil (juml_tiket * asuransi)
 
def totalHarga(): 
    print("Price You Pay           : Rp", total_harga)
    print("◾ Total Original Price : Rp ", original)
    print("◾ Insurance            : Rp ", insurance)
            
def nomorTelp():
    global nomor
    try:
        nomor = int(input("◾ Mobile Number : +62 "))
    except ValueError:
        print ("\nPlease input your phone number : ")
        nomorTelp()
       
def data_pemesan():
    print("Contact Details (for E-ticket/Voucher)")
    global pemesan
    pemesan =[]
    
    nama = input("◾ Full Name     : ")
    while nama == "":
        print("\nPlease input your full name")
        nama = input ("◾ Full Name     : ")
        
    nomorTelp()
    
    email = input("◾ Email         : ")
    while email == "":
        print ("Please input your email address")
        email = input ("◾ Email         : ")
        
    pemesan.append(nama)
    pemesan.append(nomor)
    pemesan.append(email)
              
def penumpang():
    print("Passenger Details")
    global datapenumpang
    datapenumpang =[]
    i = 1
    while i <= penumpang_data:
        dtpenumpang = {}
        print("Passenger ", i)
              
        title = input("◾ Title (Mr/Mrs/Ms) : ")
        while title not in ['Mr', 'Mrs', 'Ms']:
            print("Please select the title of passenger")
            title = input("◾ Title (Mr/Mrs/Ms) : ")
              
        name  = input("◾ Name              : ")
        while name == "":
            print("Please enter the name of passenger")
            name  = input("◾ Name              : ")              
              
        dtpenumpang['Name'] = name
        dtpenumpang['Title'] = title
        datapenumpang.append(dtpenumpang)
        i += 1
            
def dataTraveller():
    cIn = 0
    while cIn < penumpang_data:
        dt = datapenumpang[cIn]
        cIn += 1
        print(f"◾ Passenger {cIn} : ", dt['Title'], dt['Name'])
            
             
def flight_detail():
    print("============  FLIGHT DETAILS  ============")
    print("Please make sure that all information \nwritten below are correct")
    print("")
    print(flights[pilih]['airlines'])
    print("🛫", dari, "\t {}/{}/{}". format(tanggal, bulan, tahun))
    print(" | ", flights[pilih]['time'][0:5])
    print(" | ")
    print(" | ")
    print("🛬", ke)
    print("   ", flights[pilih]['time'][8:13])
    print("")
    print("CONTACT DETAILS")
    print("◾ Full Name     : ", pemesan[0])
    print("◾ Mobile Number :  +62", pemesan[1])
    print("◾ Email         : ", pemesan[2])
    print("\nPASSENGER DETAILS")
    dataTraveller()
    print("\nPRICE DETAILS")
    totalHarga()
    print("")
    print("We will send your booking confirmations to the above contact details,\nwhich will also be used for refund or reschedule purposes.")
              
ulang = True
inputuser = ""
import os
import time

while ulang == True:
    print("\n==================================")
    print(" TRAVELOKE 🛫 BOOK FLIGHT TICKET ")
    print("==================================")
    print("")
    
    kota()
              
    dari = input("Departure      : ")
    while dari == "":
        print("Please input departure city")
        dari = input("Departure      :")
              
    ke = input("Arrival        : ")
    while ke == "":
        print("Please input arrival city")
        dari = input("Arrival        : ")       
              
    date()
              
    jumlahpenumpang()
              
    os.system("cls")
    
    print("Looking for all available flights ...")
    time.sleep(4)
    if dari not in ['Jakarta', 'Surabaya', 'Yogyakarta', 'Makassar', 'Denpasar']:
        print("")
        print("Flights are not available")
        continue
        
    elif ke not in ['Jakarta', 'Surabaya', 'Yogyakarta', 'Makassar', 'Denpasar']:
        print("")
        print("Flights are not available")
        continue
    
    elif dari == "Jakarta" and ke == "Surabaya":
        jakarta_surabaya()
        f = open('jakarta_surabaya.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Jakarta" and ke == "Makassar":
        jakarta_makassar()
        f = open('jakarta_makassar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Jakarta" and ke == "Denpasar":
        jakarta_denpasar()
        f = open('jakarta_denpasar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Jakarta" and ke == "Yogyakarta":
        jakarta_yogyakarta()
        f = open('jakarta_yogyakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
              
    elif dari == "Makassar" and ke == "Jakarta":
        makassar_jakarta()
        f = open ('makassar_jakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Makassar" and ke == "Surabaya":
        makassar_surabaya()
        f = open ('makassar_surabaya.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Makassar" and ke == "Yogyakarta":
        makassar_yogyakarta()
        f = open ('makassar_yogyakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Makassar" and ke == "Denpasar":
        makassar_denpasar()
        f = open ('makassar_denpasar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
              
    elif dari == "Surabaya" and ke == "Jakarta":
        Surabaya_Jakarta()
        f = open('Surabaya_Jakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Surabaya" and ke == "Makassar":
        Surabaya_Makassar()
        f = open('Surabaya_Makassar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Surabaya" and ke == "Denpasar":
        Surabaya_Denpasar()
        f = open('Surabaya_Denpasar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Surabaya" and ke == "Yogyakarta":
        Surabaya_Yogyakarta()
        f = open('Surabaya_Yogyakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
              
    elif dari == "Yogyakarta" and ke == "Jakarta":
        Yogyakarta_Jakarta()
        f = open('Yogyakarta_Jakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
        
    elif dari == "Yogyakarta" and ke == "Makassar":
        Yogyakarta_Makassar()
        f = open('Yogyakarta_Makassar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Yogyakarta" and ke == "Surabaya":
        Yogyakarta_Surabaya()
        f = open('Yogyakarta_Surabaya.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
            
    elif dari == "Yogyakarta" and ke == "Denpasar":
        Yogyakarta_Denpasar()
        f = open('Yogyakarta_Denpasar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Denpasar" and ke == "Jakarta":
        denpasar_jakarta()
        f = open('denpasar_jakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
        
    elif dari == "Denpasar" and ke == "Makassar":
        denpasar_makassar()
        f = open('denpasar_makassar.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Denpasar" and ke == "Surabaya":
        denpasar_surabaya()
        f = open('denpasar_surabaya.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
    
    elif dari == "Denpasar" and ke == "Yogyakarta":
        denpasar_yogyakarta()
        f = open('denpasar_yogyakarta.csv', 'r')
        reader = csv.reader(f)
        flights = {}
        for row in reader:
            flights[row[0]] = {'airlines':row[1],'time':row[2],'price':row[3]}
        pilih = input("\nFlight Number : ")
        if pilih in flights:
            print("Airline : ", flights[pilih]['airlines'])
            print("Time    : ", flights[pilih]['time'])
            print("Price   : ", flights[pilih]['price'])
        else:
            print("Flights are not available")
            continue
              
    print("")
    pesan()
    print("")
    data_pemesan()
    print("")
    penumpang()
    print("")
    print("Wait a minute. Your data is being processed")
    time.sleep(5)
    os.system("cls")
    flight_detail()
    
    inputuser = input("Back to Menu? (yes/no) : ")
    if inputuser != "yes":
        ulang = False
        
print("")
print ("Thank You")