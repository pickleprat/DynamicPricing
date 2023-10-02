import os 

def execute(): 
    directory = 'data'
    for ds in os.listdir(directory):
        os.rename(
            os.path.join(directory, ds), 
            os.path.join(directory, ds.replace(" ", ""))
        )
    return 
    
if __name__ == '__main__': 
    execute()
    
