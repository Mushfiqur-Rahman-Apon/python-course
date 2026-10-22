def timer():
    def inner():
        print('time started')
        
        print('time ended')
    return inner

# timer() ()

def get_factorial():
    print('factorial starting')
    
get_factorial()        