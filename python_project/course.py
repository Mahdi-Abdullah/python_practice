'''Console Based Course Management Application'''

class Course:
    '''A class containing course functionalitis'''

    def __init__(self):
        '''Initialize course_code, course_title, course_credit and prerequisites attributes'''
        self.course_code = 'N/A'
        self.course_title = 'N/A'
        self.course_credit = 0
        self.prerequisites = 'N/A'

    def read_course_file(self):
        '''To read the course file'''
        with open('course.txt', 'r') as file:
            course = file.readlines()
        return course

    def write_course_file(self):
        '''To write the course file.'''
        with open('course.txt', 'a') as file:
            file.write(self.course_code + ',' + self.course_title + ',' + str(self.course_credit) + ',' + self.prerequisites + '\n')

    def all_course_display(self):
        '''To display information about all the courses'''
        course = self.read_course_file()
        for line in course:
           print(line.split(',')[0], ' - ', line.split(',')[1], ' - ', line.split(',')[2], ' - ', line.split(',')[3])

    def course_search(self, keyword):
        '''To search a course.'''
        course = self.read_course_file()
        course_list = [line.split(',') for line in course]
        for course in course_list:
            if keyword == course[0] or keyword == course[1]:
                return course
        return False

    def individual_course_display(self, keyword):
        '''To display information about a particular course.'''
        course = self.course_search(keyword)
        if course != False:
            print('Course_code - Course_title - Course_credit - Prerequisites')
            print(course[0], ' - ', course[1], ' - ', course[2], ' - ', course[3].strip().split(' '))
        else:
            print('Course not found!')
        
    def prerequisite_check(self, keyword):
        '''To check if the prerequisites are met.'''
        course = self.course_search(keyword)
        if course == False:
            return False
        else:
            return True
         
    def adding_new_course(self, course_code, course_title, course_credit, prerequisites):
        '''To add a new course'''
        if self.course_search(course_code) != False or self.course_search(course_title) != False:
            print('Course already exits')
        elif self.prerequisite_check(prerequisites) == False and prerequisites != 'N/A':
            print('Prerequisite course missing. Please add prerequisites of this course.')
        else:
            self.course_code = course_code
            self.course_title = course_title
            self.course_credit = course_credit
            self.prerequisites = prerequisites
            self.write_course_file()
   
    def deleting_existing_course(self, keyword):
        '''To delete an existing course.'''
        course = self.course_search(keyword)
        if course == False:
            print('Course not found!')
        else:
            course_list = self.read_course_file()
            course_list.remove(','.join(course))
            with open('course.txt', 'w') as file:
                for line in course_list:
                    file.write(line)

    def update_existing_course(self, keyword, course_code, course_title, course_credit, prerequisites):
        '''To update an existing course.'''
        course = self.course_search(keyword)
        if course == False:
            print('Course not found!')
        else:
            course_list = self.read_course_file()
            course_list.remove(','.join(course))
            with open('course.txt', 'w') as file:
                for line in course_list:
                    file.write(line)
            self.adding_new_course(course_code, course_title, course_credit, prerequisites)
        pass

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
        print('6. Exit')

    def search_menu(self):
        '''To display the course menu'''
        user_input = input('Enter course code or course title: ')
        return user_input

    def add_new_course_menu(self):
        '''To display the faculty menu'''
        user_input_course_code = input('Enter course code: ')
        user_input_course_title = input('Enter course title: ')
        user_input_course_credit = int(input('Enter course credit: '))
        user_input_prerequisites = input('Enter prerequisites: ')
        input_list = [user_input_course_code, user_input_course_title.capitalize(), user_input_course_credit, user_input_prerequisites]
        return input_list

    def delete_existing_course_menu(self):
        '''To display the student menu'''
        user_input = input('Enter course code or course title: ')
        return user_input

    def update_exitsing_course_menu(self):
        '''To display the exit menu'''
        user_input = input('Enter course code or course title of the course to update: ')
        user_input_course_code = input('Enter course code: ')
        user_input_course_title = input('Enter course title: ')
        user_input_course_credit = int(input('Enter course credit: '))
        user_input_prerequisites = input('Enter prerequisites: ')
        input_list = [user_input, user_input_course_code, user_input_course_title.capitalize(), user_input_course_credit, user_input_prerequisites]
        return input_list

def main():
    '''Main function'''
    course = Course()
    menu = Menu()
    print('\nWelcome to the Course Management System\n')
    while True:
        menu.main_menu()
        user_input = input('Enter your choice: ')
        if user_input == '1':
            course.all_course_display()
        elif user_input == '2':
            course.individual_course_display(menu.search_menu())
        elif user_input == '3':
            input_list = menu.add_new_course_menu()
            course.adding_new_course(input_list[0], input_list[1], input_list[2], input_list[3])
        elif user_input == '4':
            course.deleting_existing_course(menu.delete_existing_course_menu())
        elif user_input == '5':
            input_list = menu.update_exitsing_course_menu()
            course.update_existing_course(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4])
        elif user_input == '6':
            break
        else:
            print('Invalid input!')

# Call the main function
main()