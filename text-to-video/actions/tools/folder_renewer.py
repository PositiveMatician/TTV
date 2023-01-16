
def folder_renewer(folder_name,rm=True):
    import os
    '''Takes a folder name as arguement
    deletes everything from the folder
    And makes the folder if it already doesn't exist'''

    #Deletes The folder given with all items in it
    if os.path.exists(folder_name):
        if rm == True:
            items = os.listdir(folder_name)
            
            for item in items:
                os.remove(folder_name+'/'+item)
    else:
        #Create the folder
        os.mkdir(folder_name)
