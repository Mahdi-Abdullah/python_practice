class Menu:
    '''A class containing menu functionalities'''

    def __init__(self):
        '''Initialize attributes'''
        pass

    def main_menu(self):
        '''To display the main menu'''
        print('1. Display all courses')
        print('2. Search a course by course code or course title')
        print('3. Add a new course')
        print('4. Delete an existing course')
        print('5. Update an existing course')
        print('6. Enter quit or 6 to Exit\n')

    def search_menu(self):
        '''To display the course menu'''
        while True:
            try:
                user_input = input('Enter course code or course title: ')
                break
            except ValueError:
                print('Invalid input!')
        return user_input

    def add_new_course_menu(self):
        '''To display the faculty menu'''
        while True:
            try:
                user_input_course_code = input('Enter course code: ')
                break
            except ValueError:
                print('Invalid input!')
        while True:
            try:
                user_input_course_title = input('Enter course title: ')
                break
            except ValueError:
                print('Invalid input!')
        while True:
            try:
                user_input_course_credit = int(input('Enter course credit: '))
                break
            except ValueError:
                print('Invalid input!')
        while True:
            try:
                user_input_prerequisites = input('Enter prerequisites: ')
                break
            except ValueError:
                print('Invalid input!')
        print()
        input_list = [user_input_course_code, user_input_course_title.capitalize(), user_input_course_credit, user_input_prerequisites]
        return input_list

    def delete_existing_course_menu(self):
        '''To display the student menu'''
        while True:
            try:
                user_input = input('Enter course code or course title: ')
                break
            except ValueError:
                print('Invalid input!')
        return user_input

    def update_exitsing_course_menu(self):
        '''To display the exit menu'''
        while True:
            try:
                user_input = input('Enter course code or course title of the course to update: ')
                break
            except ValueError:
                print('Invalid input!')
        while True:
            try:
                user_input_course_code = input('Enter course code: ')
                break
            except ValueError:
                print('Invalid input!')
        while True:
            try:
                user_input_course_title = input('Enter course title: ')
                break
            except ValueError:
                print('Invalid input!')
        while True:
            try:
                user_input_course_credit = int(input('Enter course credit: '))
                break
            except ValueError:
                print('Invalid input!')
        while True:
            try:
                user_input_prerequisites = input('Enter prerequisites: ')
                break
            except ValueError:
                print('Invalid input!')
        print()
        input_list = [user_input, user_input_course_code, user_input_course_title.capitalize(), user_input_course_credit, user_input_prerequisites]
        return input_list