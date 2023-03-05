class Profile:
    def __init__(self, username: str, password: str, ):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if 5 > len(value) or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self._username = value
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        is_valid_length = len(value)
        there_is_upper_letter = [idx for idx in range(len(value)) if value[idx].isupper()]
        there_is_digit = [idx for idx in range(len(value)) if value[idx].isdigit()]

        if is_valid_length < 8 or not there_is_upper_letter or not there_is_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self._password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
