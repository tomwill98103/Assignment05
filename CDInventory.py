#------------------------------------------#
# Title: CDInventory.py
# Desc: CD Inventory version 2.0
# Change Log: (Who, When, What)
# TWilliams, 2020-Aug-09, Created File
# TWilliams, 2020-Aug-09, Wrote dictionaries to Add, Display, and Save modules
# TWilliams, 2020-Aug-12, Wrote file load module
# TWilliams, 2020-Aug-13, Wrote item delete module
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {} # dictionary data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        print('Goodbye!')
        break
    
    if strChoice == 'l':
        # 1. load existing data from text file CDInventory.txt if the user chooses so
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id':lstRow[0],'title':lstRow[1], 'artist':lstRow[2]} # create rows as dictionaries
            lstTbl.append(dicRow)
        objFile.close()
        print('Inventory loaded from file.')
        print()
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'id': strID,'title':strTitle,'artist':strArtist} # create dictionary
        lstTbl.append(dicRow) # add dictionary to list as row
    
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print('{}, {}, {}'.format(row['id'],row['title'], row['artist']))
        print()
    
    elif strChoice == 'd':
        # 4. Delete an entry from the inventory if the user chooses so
        # Check if inventory is in memory
        if lstTbl == []:
            # If not, load it (this should be a function call but instead repeating load code)
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                dicRow = {'id':lstRow[0],'title':lstRow[1], 'artist':lstRow[2]}
                lstTbl.append(dicRow)
            objFile.close()
        # Ask user for ID of CD to delete
        strID = input('Enter the ID of the CD to delete: ')
        dicDel = {} # Initialize empty dictionary to hold delete target
        # loop through dictionaries to find delete target by matching ID
        for dic in lstTbl:
             if dic['id'] == strID:
                dicDel = dic # hold item to be deleted
                # Access dictionary items to print confirmation message
                print ('Deleting ' + dicDel['title']+' by '+dicDel['artist'])
                strDel = input('Type "OK" to confirm: ')
                if strDel.lower() != 'ok':
                    print('')
                    break
                elif strDel.lower() == 'ok':
                    lstTbl.remove(dic)
                    print('Item deleted')
                    print()
        if dicDel == {}: # if no matching ID found print message
            print('Sorry no CD with that ID in inventory.')
            print()
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Inventory saved to file.')
        print()
    
    else:
        print('Please choose either l, a, i, d, s or x!')

