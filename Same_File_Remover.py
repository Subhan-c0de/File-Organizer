import os
import hashlib

#=====================================================================
#Function 1:Create a File Hash 
#=====================================================================

def get_file_hash(filepath):
    hasher = hashlib.md5() # This is a Fingerprint Generater 
    #open file in Binary,Read Mode
    with open(filepath,"rb") as f:
        while chunk:=f.read(4096): #Read 4096 byte in one time and stored them in chunk variable by us ng walrus Operator. 1 bytes = 8 bit
            hasher.update(chunk) #The 4096 bytes storing . 
    return hasher.hexdigest() #return the fiinal data in chunk
    
#=====================================================================
#Function 2:Detect a Corresponding file
#=====================================================================

def find_duplicate(folder):
    hashes = {}  #Hash -> file_path
    duplicate = [] #duplicate files
    for root,dir,files in os.walk(folder): #Roots = Parent_Folder , dir = child_folder,fies = files
        for file in files :
            path = os.path.join(root,file) # Roots +/+files , e.g : D:DVD\Folder_name / file name
            try:
                file_hash = get_file_hash(path)
                
                if (file_hash in hashes): # if =  e.g : A571819hd in hashes? 
                    duplicate.append(path) 

                else:
                    hashes[file_hash] = path #else = e.f : hashes[A571819hd] = D:DVD\ Folder ,hashes["A571819hd": D\DVD /Folder]

            except Exception as e:
                print("Error:",e)
        print(duplicate)
    return duplicate 

#===================================================================
#Funcion 3: Duplicate File remover 
#===================================================================
def  remover_duplicates(duplicate_path):
    for file in duplicate_path: 
        os.remove(file)
        print("Deleted",file)

#===================================================================
#Main Program
#===================================================================
folder_path = input("Enter folder Path:")

#Calling for finding A Duplicate file
dupe = find_duplicate(folder_path) # Calling Func --> The Function separate  Folder,Images,and Files as root,dir,files 

print("\nDuplicates file Found.")
for d in dupe:
    print(d)

choice = input("Enter Your Choice y/n:")
if (choice.lower() =="y"):
    remover_duplicates(dupe)
    

                        #    #=====================================#    #


