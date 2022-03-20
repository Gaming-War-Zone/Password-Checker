class PSW_check:      

    def __init__(self):
        self.PWD_DICT = {'pwd_len':0, 'has_uppercase':None, 'has_lowercase':None, 'has_digit':None, 'has_special_chr':None, 'has_wht_spc':None }
        self.password = 'b1enedictF@jt '
        self.count_passed_checks = 0

    def get_data(self):
        special_char = list("*-+,'[@_!#$%^&*()<>?/\|}{~:]")
        password = list(self.password)
        self.PWD_DICT['pwd_len'] = len(password)
        for index, char in enumerate(password):
            if char.isupper():
                self.PWD_DICT['has_uppercase'] = 'Yes'

            elif char.islower():
                self.PWD_DICT['has_lowercase'] = 'Yes'

            elif char.isnumeric():
                self.PWD_DICT['has_digit'] = 'Yes'
            
            elif char in special_char:
                self.PWD_DICT['has_special_chr'] = 'Yes'
            
            elif char.isspace():
                self.PWD_DICT['has_wht_spc'] = 'Yes'
        
        #checking how many checks have passed for use in "password_is_valid"
        for key in self.PWD_DICT:
            value = self.PWD_DICT.get(key)
            if value == 'Yes':
                self.count_passed_checks +=1
        
        if self.PWD_DICT.get('pwd_len') >8:
            self.count_passed_checks +=2
        
        elif self.PWD_DICT.get('pwd_len') >=1:
            self.count_passed_checks +=1



    def password_is_valid(self):
        for key in self.PWD_DICT:
            value = self.PWD_DICT.get(key)

            if key == 'pwd_len' and int(value) == 0:
                raise Exception('password should exist')

            elif key == 'has_uppercase' and value == None:
                raise Exception('password should have at least one uppercase letter')

            elif key == 'has_digit' and value == None:
                raise Exception('password should have at least have one digit')

            elif key == 'has_lowercase' and value == None:
                raise Exception('password should have at least one lowercase letter')
            
            elif key == 'has_special_chr' and value == None:
                raise Exception('password should have at least one special character')

            elif key == 'has_wht_spc' and value == None:
                raise Exception('password should have at least one whitespace character')

            elif key == 'pwd_len' and int(value) < 8:
                raise Exception('password should be longer than 8 characters')

        return self.PWD_DICT



    def password_strength(self):
        if self.PWD_DICT.get('pwd_len') == 0 or self.PWD_DICT.get('pwd_len') <8:
            return 'invalid'

        elif self.count_passed_checks >=6:
            return 'strong' 

        elif self.count_passed_checks >=4:
            return 'medium'

        elif self.count_passed_checks == 3:
            return 'weak'


my = PSW_check()
my.get_data()
print(my.password_strength())
my.password_is_valid()