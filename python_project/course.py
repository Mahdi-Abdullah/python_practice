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
        elif self.prerequisite_check(prerequisites) == False:
            print('Prerequisite course missing. Please add prerequisites of this course.')
        else:
            self.course_code = course_code
            self.course_title = course_title
            self.course_credit = course_credit
            self.prerequisites = prerequisites
            self.write_course_file()
   
    def deleting_existing_course(self, keyword):
        '''To delete an existing course.'''
        pass

    def update_existing_course(self):
        '''To update an existing course.'''
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
my_course.read_course_file()
#print(my_course.course_search('Electronic devices'))
#my_course.individual_course_display('CSC1205')
#my_course.adding_new_course('MAT110', 'Differential calculus & co-ordinate geometr',3,'8')
