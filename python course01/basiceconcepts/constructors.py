class Phone:
    manfactured = 'china'
    
    def __init__(self, owner, brand, price):
        
        delf.owner = owner
        self.brand = brand
        self.price = price
        
    def send_sms(self, phone,sms):
        text = f'sending to: {phone} {sms}'
        print(text)