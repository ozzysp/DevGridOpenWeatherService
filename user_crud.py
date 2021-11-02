import json
import os

# Create the data JSON file if it doesn't exist
if not os.path.exists('data.json'):
    with open('user_crud.json', 'w') as f:
        f.write('{}')

# Load the data from the JSON file
data = json.load(open("user_crud.json"))

# Create a data_file variable to hold the path to the JSON file
data_file = os.path.join(os.path.dirname(__file__), "user_crud_1.json")



# This function reads the data file and returns a list of dictionaries
def read_data():
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        data = []

    return data

# This function writes the data to the data file
def write_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=2)

# This class represents a user
class User:
    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_password(self):
        return self.password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def set_password(self, password):
        self.password = password

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def save(self):
        data = read_data()
        data.append(self.__dict__)
        write_data(data)

    @staticmethod
    def get_all():
        data = read_data()
        users = []
        for user in data:
            users.append(User(user['first_name'], user['last_name'], user['password']))
        return users

    @staticmethod
    def find_by_name(name):
        data = read_data()
        for user in data:
            if user['first_name'] == name:
                return User(user['first_name'], user['last_name'], user['password'])
        return None

    @staticmethod
    def find_by_id(user_id):
        data = read_data()
        for user in data:
            if user['id'] == user_id:
                return User(user['first_name'], user['last_name'], user['password'])
        return None

    @staticmethod
    def delete_by_id(user_id):
        data = read_data()
        for i in range(len(data)):
            if data[i]['id'] == user_id:
                del data[i]
                write_data(data)
                return True
        return False

    @staticmethod
    def update_by_id(user_id, first_name, last_name, password):
        data = read_data()
        for i in range(len(data)):
            if data[i]['id'] == user_id:
                data[i]['first_name'] = first_name
                data[i]['last_name'] = last_name
                data[i]['password'] = password
                write_data(data)
                return True
        return False

    @staticmethod
    def authenticate(first_name, password):
        user = User.find_by_name(first_name)
        if user and user.get_password() == password:
            return user
        return None

    @staticmethod
    def is_authenticated(user):
        return True

    @staticmethod
    def is_active(user):
        return True

    @staticmethod
    def is_anonymous(user):
        return False

    def get_id(self):
        return self.id

    @staticmethod
    def get_by_id(user_id):
        return User.find_by_id(user_id)

    @staticmethod
    def get_all_users():
        return User.get_all()

    @staticmethod
    def delete_by_name(name):
        return User.delete_by_id(name)

    @staticmethod
    def update_by_name(name, first_name, last_name, password):
        return User.update_by_id(name, first_name, last_name, password)

    @staticmethod
    def authenticate_user(first_name, password):
        return User.authenticate(first_name, password)


# This function is a login function
def login():
    first_name = input('Enter your first name: ')
    password = input('Enter your password: ')
    user = User.authenticate_user(first_name, password)
    if user:
        print('Welcome, ' + user.get_full_name())
    else:
        print('Invalid credentials')

# This function is a register function
def register():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    password = input('Enter your password: ')
    user = User(first_name, last_name, password)
    user.save()
    print('User created successfully')

# This function is a delete function
def delete():
    first_name = input('Enter your first name: ')
    user = User.find_by_name(first_name)
    if user:
        User.delete_by_id(user.get_id())
        print('User deleted successfully')
    else:
        print('User not found')


# This function is a update function
def update():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    password = input('Enter your password: ')
    user = User.find_by_name(first_name)
    if user:
        User.update_by_id(user.get_id(), first_name, last_name, password)
        print('User updated successfully')
    else:
        print('User not found')


# This function is a list function
def list_users():
    users = User.get_all_users()
    for user in users:
        print(user.get_full_name())


# This function is a main function
def main():
    while True:
        print('1. Login')
        print('2. Register a new user')
        print('3. Delete a user')
        print('4. Update a current user')
        print('5. List users')
        print('6. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            delete()
        elif choice == '4':
            update()
        elif choice == '5':
            list_users()
        elif choice == '6':
            break
        else:
            print('Invalid choice')



if __name__ == '__main__':
    main()

# This is the end of the program
