# imports
import mysql.connector
from mysql.connector import errorcode


# delete function
def deleteDef(cnx, cursor):
    print('\n--------------- Select Table to use SQL command DELETE -----------------\n')
    
    # example of the sql command
    print('To use the DELETE SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("DELETE FROM PERSONS\nWHERE PersonID = 1")
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
    print('10. Delete a specific table')
    
    print('\n------------------------------------------------------------------------\n')
    
    # table selection
    deleteSelection = input('Select a number: ')
    
    # ATHLETE table
    if deleteSelection == '1':
        print('\n--------------- ATHLETE Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM ATHLETE WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from ATHLETE table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # COACH table        
    elif deleteSelection == '2':
        print('\n--------------- COACH Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n-------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM COACH WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from COACH table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))

    # COUNTRY table
    elif deleteSelection == '3':
        print('\n--------------- COUNTRY Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM COUNTRY WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from COUNTRY table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # EVENT_SCHEDULE table            
    elif deleteSelection == '4':
        print('\n--------------- EVENT_SCHEDULE Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n----------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM EVENT_SCHEDULE WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from EVENT_SCHEDULE table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # INDIV_W table            
    elif deleteSelection == '5':
        print('\n--------------- INDIV_W Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM INDIV_W WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from INDIV_W table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # INDIVIDUAL_RESULTS table            
    elif deleteSelection == '6':
        print('\n--------------- INDIVIDUAL_RESULTS Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n--------------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM INDIVIDUAL_RESULTS WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from INDIVIDUAL_RESULTS table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PARTICIPANT table            
    elif deleteSelection == '7':
        print('\n--------------- PARTICIPANT Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM PARTICIPANT WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from PARTICIPANT table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # TEAM table            
    elif deleteSelection == '8':
        print('\n--------------- TEAM Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n-------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM TEAM WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from TEAM table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # TEAM_RESULTS table        
    elif deleteSelection == '9':
        print('\n--------------- TEAM_RESULTS Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM TEAM_RESULTS WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from TEAM_RESULTS table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # OLYMPICARCHERY database
    elif deleteSelection == '10':
        print('\n--------------- OLYMPICARCHERY Database ---------------\n')
        table = input('Insert the name of the table to delete all records on it (Be precise as possible): ')
        print('\n-------------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM {};'.format(table.upper()))
            cursor.execute(sqlCommand)
            print('Successfully dropped {} table!'.format(table.upper()))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))