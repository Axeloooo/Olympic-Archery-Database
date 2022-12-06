# imports
import mysql.connector
from mysql.connector import errorcode


# insert function
def insertDef(cnx, cursor):
    print('\n--------------- Select Table to use SQL command INSERT -----------------\n')
    
    # example of the sql command
    print('To use the INSERT SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("INSERT INTO PERSONS(PersonID, FName, LName)\nVALUES(1, 'Axel', 'Sanchez')")
    print('\n*********************************************\n')
    
    # tables
    print('1. ATHLETE')
    print('2. COACH')
    print('3. COUNTRY')
    print('4. EVENT_SCHEDULE')
    print('5. INDIV_W')
    print('6. INDIVIDUAL_RESULTS')
    print('7. PARTICIPANT')
    print('8. TEAM')
    print('9. TEAM_RESULTS')
    
    print('\n------------------------------------------------------------------------\n')

    # table selection
    insertSelection = input('Select a number: ')
            
    # ATHLETE table
    if insertSelection == '1':
        print('\n--------------- ATHLETE Table ---------------\n')
        olympicID = input('Insert OlympicID -> data type VARCHAR(10): ')
        sex = input('Insert Sex -> data type CHAR(1): ')
        birthYear = input('Insert BirthYear -> data type INT: ')
        firstGames = input('Insert FirstGames -> data type VARCHAR(20): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO ATHLETE(OlympicID, Sex, BirthYear, FirstGames) VALUES(%s, %s, %s, %s)')
            cursor.execute(sqlCommand, (olympicID, sex, birthYear, firstGames))
            cnx.commit()
            print('Successfully inserted into ATHLETE({}, {}, {}, {})!'.format(olympicID, sex, birthYear, firstGames))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # COACH table
    elif insertSelection == '2':
        print('\n--------------- COACH Table ---------------\n')
        olympicID = input('Insert OlympicID -> data type VARCHAR(10): ')
        orientation = input('Insert Orientation -> data type VARCHAR(20): ')
        print('\n-------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO COACH(OlympicID, Orientation) VALUES(%s, %s)')
            cursor.execute(sqlCommand, (olympicID, orientation))
            cnx.commit()
            print('Successfully inserted into COACH({}, {})!'.format(olympicID, orientation))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))

    # COUNTRY table
    elif insertSelection == '3':
        print('\n--------------- COUNTRY Table ---------------\n')
        cName = input('Insert Orientation -> data type VARCHAR(30): ')
        allTimeGold = input('Insert AllTimeGold -> data type INT: ')
        allTimeSilver = input('Insert AllTimeSilver -> data type INT: ')
        allTimeBronze = input('Insert AllTimeBronze -> data type INT: ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO COUNTRY(Orientation, AllTimeGold, AllTimeSilver, AllTimeBronze) VALUES(%s, %s, %s, %s)')
            cursor.execute(sqlCommand, (cName, allTimeGold, allTimeSilver, allTimeBronze))
            cnx.commit()
            print('Successfully inserted into COUNTRY({}, {}, {}, {})!'.format(cName, allTimeGold, allTimeSilver, allTimeBronze))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # EVENT_SCHEDULE table    
    elif insertSelection == '4':
        print('\n--------------- EVENT_SCHEDULE Table ---------------\n')
        eventID = input('Insert EventID -> data type VARCHAR(15): ')
        eventDate = input('Insert EventDate -> data type VARCHAR(15): ')
        location = input('Insert Location -> data type VARCHAR(30): ')
        print('\n----------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO EVENT_SCHEDULE(EventID, EventDate, Location) VALUES(%s, %s, %s)')
            cursor.execute(sqlCommand, (eventID, eventDate, location))
            cnx.commit()
            print('Successfully inserted into EVENT_SCHEDULE({}, {}, {})!'.format(eventID, eventDate, location))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # INDIV_W table
    elif insertSelection == '5':
        print('\n--------------- INDIV_W Table ---------------\n')
        eventDate = input('Insert EventDate -> data type VARCHAR(15): ')
        location = input('Insert Location -> data type VARCHAR(30): ')
        lName = input('Insert LName -> data type VARCHAR(25): ')
        country = input('Insert Country -> data type VARCHAR(30): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO INDIV_W(EventDate, Location, LName, Country) VALUES(%s, %s, %s, %s)')
            cursor.execute(sqlCommand, (eventDate, location, lName, country))
            cnx.commit()
            print('Successfully inserted into INDIV_W({}, {}, {}, {})!'.format(eventDate, location, lName, country))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # INDIVIDUAL_RESULTS table
    elif insertSelection == '6':
        print('\n--------------- INDIVIDUAL_RESULTS Table ---------------\n')
        eventID = input('Insert EventID -> data type VARCHAR(15): ')
        olympian = input('Insert Olympian -> data type VARCHAR(10): ')
        medal = input('Insert Medal -> data type VARCHAR(10): ')
        print('\n--------------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO INDIVIDUAL_RESULTS(EventID, Olympian, Medal) VALUES(%s, %s, %s)')
            cursor.execute(sqlCommand, (eventID, olympian, medal))
            cnx.commit()
            print('Successfully inserted into INDIVIDUAL_RESULTS({}, {}, {})!'.format(eventID, olympian, medal))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PARTICIPANT table
    elif insertSelection == '7':
        print('\n--------------- PARTICIPANT Table ---------------\n')
        olympicID = input('Insert OlympicID -> data type VARCHAR(10): ')
        lName = input('Insert LName -> data type VARCHAR(25): ')
        fName = input('Insert FName -> data type VARCHAR(25): ')
        country = input('Insert Country -> data type VARCHAR(30): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO PARTICIPANT(OlympicID, LName, FName, Country) VALUES(%s, %s, %s, %s)')
            cursor.execute(sqlCommand, (olympicID, lName, fName, country))
            cnx.commit()
            print('Successfully inserted into PARTICIPANT({}, {}, {}, {})!'.format(olympicID, lName, fName, country))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # TEAM table
    elif insertSelection == '8':
        print('\n--------------- TEAM Table ---------------\n')
        teamID = input('Insert TeamID -> data type VARCHAR(25): ')
        member1 = input('Insert Member1 -> data type VARCHAR(10): ')
        member2 = input('Insert Member2 -> data type VARCHAR(10): ')
        member3 = input('Insert Member3 -> data type VARCHAR(10): ')
        member4 = input('Insert Member4 -> data type VARCHAR(10): ')
        member5 = input('Insert Member5 -> data type VARCHAR(10): ')
        member6 = input('Insert Member6 -> data type VARCHAR(10): ')
        print('\n-------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO TEAM(TeamID, Member1, Member2, Member3, Member4, Member5, Member6) VALUES(%s, %s, %s, %s, %s, %s, %s)')
            cursor.execute(sqlCommand, (teamID, member1, member2, member3, member4, member5, member6))
            cnx.commit()
            print('Successfully inserted into TEAM({}, {}, {}, {}, {}, {}, {})!'.format(teamID, member1, member2, member3, member4, member5, member6))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # TEAM_RESULTS table
    elif insertSelection == '9':
        print('\n--------------- TEAM_RESULTS Table ---------------\n')
        eventID = input('Insert EventID -> data type VARCHAR(15): ')
        team = input('Insert Team -> data type VARCHAR(25): ')
        medal = input('Insert Medal -> data type VARCHAR(10): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO TEAM_RESULTS(EventID, Team, Medal) VALUES(%s, %s, %s)')
            cursor.execute(sqlCommand, (eventID, team, medal))
            cnx.commit()
            print('Successfully inserted into TEAM_RESULTS({}, {}, {})!'.format(eventID, team, medal))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))