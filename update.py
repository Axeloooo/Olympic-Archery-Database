# imports
import mysql.connector
from mysql.connector import errorcode


# update function
def updateDef(cnx, cursor):
    print('\n--------------- Select Table to use SQL command UPDATE -----------------\n')
    
    # example of the sql command
    print('To use the UPDATE SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("UPDATE PERSONS\nSET FName = 'Axel', LName = 'Sanchez'\nWHERE PersonID = 1 OR PersonID = 4;")
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
    updateSelection = input('Select a number: ')
    
    # ATHLETE table
    if updateSelection == '1':
        print('\n--------------- ATHLETE Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE ATHLETE SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # COACH table
    elif updateSelection == '2':
        print('\n--------------- COACH Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE COACH SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))

    # COUNTRY table
    elif updateSelection == '3':
        print('\n--------------- COUNTRY Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE COUNTRY SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # EVENT_SCHEDULE table    
    elif updateSelection == '4':
        print('\n--------------- EVENT_SCHEDULE Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE EVENT_SCHEDULE SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # INDIV_W table
    elif updateSelection == '5':
        print('\n--------------- INDIV_W Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE INDIV_W SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # INDIVIDUAL_RESULTS table
    elif updateSelection == '6':
        print('\n--------------- INDIVIDUAL_RESULTS Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE INDIVIDUAL_RESULTS SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PARTICIPANT table
    elif updateSelection == '7':
        print('\n--------------- PARTICIPANT Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE PARTICIPANT SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # TEAM table
    elif updateSelection == '8':
        print('\n--------------- TEAM Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE TEAM SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # TEAM_RESULTS table
    elif updateSelection == '9':
        print('\n--------------- TEAM_RESULTS Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE TEAM_RESULTS SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))