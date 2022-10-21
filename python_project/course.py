'''Course Management Application'''

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
           print(line.split(',')[0], ' - ' , line.split(',')[1], ' - ' , line.split(',')[2], ' - ' ,line.split(',')[3])
        
        

    def adding_new_course(self):
        '''To add a new course'''
        pass

    def updating_existing_course(self):
        '''To update an existing course.'''
        pass

    def deleting_existing_course(self):
        '''To delete an existing course.'''
        pass

    def individual_course_display(self):
        '''To display information about a particular course.'''
        pass

    def course_search(self):
        '''To search a course.'''
        pass

    def prerequisite_check(self):
        '''To check if the prerequisites are met.'''
        pass

class Menu:
    '''A class containing menu functionalities'''

    def __init__(self):
        '''Initialize name and age attributes'''
        pass

    def main_menu(self):
        '''To display the main menu'''
        pass

    def course_menu(self):
        '''To display the course menu'''
        pass

    def student_menu(self):
        '''To display the student menu'''
        pass

    def faculty_menu(self):
        '''To display the faculty menu'''
        pass

    def exit_menu(self):
        '''To display the exit menu'''
        pass

my_course = Course()
my_course.all_course_display()
my_course.write_course_file()