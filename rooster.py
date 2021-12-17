# import modules
#import mysql.connector
import csv

# database met coaches, werktijden en voorkeuren
coaches = {
    1: {'Name': 'Sander', 'Mon1': 'True', 'Mon2': 'True', 'Tue1': 'False', 'Tue2': 'False', 'Wed1': 'True', 'Wed2': 'True', 'Thu1': 'False', 'Thu2': 'False', 'Fri': 'True', 'Sat': 'False', 'Sun': 'True', 'Pref-Morning': 'False', 'Pref-Noon': 'False', 'Pref-Evening': 'True', 'Pref-Day': 'False'},
    2: {'Name': 'Alexander', 'Mon1': 'True', 'Mon2': 'True', 'Tue1': 'False', 'Tue2': 'False', 'Wed1': 'False', 'Wed2': 'False', 'Thu1': 'True', 'Thu2': 'True', 'Fri': 'False', 'Sat': 'True', 'Sun': 'False', 'Pref-Morning': 'False', 'Pref-Noon': 'False', 'Pref-Evening': 'True', 'Pref-Day': 'False'},
    3: {'Name': 'Nick', 'Mon1': 'False', 'Mon2': 'False', 'Tue1': 'True', 'Tue2': 'True', 'Wed1': 'False', 'Wed2': 'False', 'Thu1': 'False', 'Thu2': 'False', 'Fri': 'True', 'Sat': 'False', 'Sun': 'False', 'Pref-Morning': 'True', 'Pref-Noon': 'True', 'Pref-Evening': 'True', 'Pref-Day': 'True'},
    4: {'Name': 'Sam', 'Mon1': 'False', 'Mon2': 'False', 'Tue1': 'False', 'Tue2': 'False', 'Wed1': 'True', 'Wed2': 'True', 'Thu1': 'False', 'Thu2': 'False', 'Fri': 'True', 'Sat': 'False', 'Sun': 'False', 'Pref-Morning': 'True', 'Pref-Noon': 'True', 'Pref-Evening': 'True', 'Pref-Day': 'True'},
    5: {'Name': 'Daniel', 'Mon1': 'False', 'Mon2': 'False', 'Tue1': 'True', 'Tue2': 'True', 'Wed1': 'False', 'Wed2': 'False', 'Thu1': 'True', 'Thu2': 'False', 'Fri': 'False', 'Sat': 'False', 'Sun': 'False', 'Pref-Morning': 'True', 'Pref-Noon': 'True', 'Pref-Evening': 'False', 'Pref-Day': 'True'},
    6: {'Name': 'Henok', 'Mon1': 'False', 'Mon2': 'False', 'Tue1': 'True', 'Tue2': 'True', 'Wed1': 'True', 'Wed2': 'True', 'Thu1': 'False', 'Thu2': 'False', 'Fri': 'False', 'Sat': 'False', 'Sun': 'False', 'Pref-Morning': 'False', 'Pref-Noon': 'True', 'Pref-Evening': 'True', 'Pref-Day': 'True'},
}


# database met standaard rooster, nog niet gevuld
rooster = {
    1: {'Dag': 'Maandag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': ''},
    2: {'Dag': 'Maandag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': ''},
    3: {'Dag': 'Dinsdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': ''},
    4: {'Dag': 'Dinsdag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': ''},
    5: {'Dag': 'Woensdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': ''},
    6: {'Dag': 'Woensdag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': ''},
    7: {'Dag': 'Donderdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': ''},
    8: {'Dag': 'Donderdag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': ''},
    9: {'Dag': 'Vrijdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': ''},
    10: {'Dag': 'Zaterdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': ''},
    11: {'Dag': 'Zondag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': ''},
}

# database gevuld, voor opdracht 2 sterren
ingeroosterd = {
    1: {'Dag': 'Maandag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': 'Sander'},
    2: {'Dag': 'Maandag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': 'Alexander'},
    3: {'Dag': 'Dinsdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': 'Daniel'},
    4: {'Dag': 'Dinsdag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': 'Nick'},
    5: {'Dag': 'Woensdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': 'Henok'},
    6: {'Dag': 'Woensdag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': 'Sam'},
    7: {'Dag': 'Donderdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': 'Daniel'},
    8: {'Dag': 'Donderdag', 'Van': '19:00', 'Tot': '21:00', 'Ingeroosterd': 'Alexander'},
    9: {'Dag': 'Vrijdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': 'Sander'},
    10: {'Dag': 'Zaterdag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': 'Alexander'},
    11: {'Dag': 'Zondag', 'Van': '09:00', 'Tot': '17:30', 'Ingeroosterd': 'Sander'},
}


fields = ['Name','Mon1','Mon2','Tue1', 'Tue2', 'Wed1', 'Wed2', 'Thu1', 'Thu2', 'Fri','Sat','Sun', 'Pref-Morning', 'Pref-Noon', 'Pref-Evening', 'Pref-Day']
csv_file = "coaches.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        for k in coaches:
            writer.writerow(coaches[k])
except IOError:
    print("I/O error")

fields = ['Dag','Van','Tot','Ingeroosterd']
csv_file = "ingeroosterd.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        for k in ingeroosterd:
            writer.writerow(ingeroosterd[k])
except IOError:
    print("I/O error")

fields = ['Dag','Van','Tot','Ingeroosterd']
csv_file = "leegRooster.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        for k in rooster:
            writer.writerow(rooster[k])
except IOError:
    print("I/O error")
