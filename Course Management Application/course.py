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
        while True:
            try:
                with open('course.txt', 'r') as file:
                    course = file.readlines()
                    return course
            except FileNotFoundError:
                print('File not found. Creating a new file.')
                with open('course.txt', 'w') as file:
                    pass

    def write_course_file(self):
        '''To write the course file.'''
        while True:
            try:
                with open('course.txt', 'a') as file:
                    file.write(self.course_code + ',' + self.course_title + ',' + str(self.course_credit) + ',' + self.prerequisites + '\n')
                    break
            except FileNotFoundError:
                print('File not found. Creating a new file.')
                with open('course.txt', 'w') as file:
                    pass

    def all_course_display(self):
        '''To display information about all the courses'''
        course = self.read_course_file()
        if course == []:
            print('No courses found!')
        else:
            for line in course:
                print(line.split(',')[0], ' - ', line.split(',')[1], ' - ', line.split(',')[2], ' - ', ', '.join(line.split(',')[3].strip().split(' ')))

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
            print(course[0], ' - ', course[1], ' - ', course[2], ' - ', ', '.join(course[3].strip().split(' ')))
        else:
            print('\nCourse not found!')
        
    def prerequisite_check(self, keyword):
        '''To check if the prerequisites are met.'''
        keyword_list = keyword.split(' ')
        for keyword in keyword_list:
            if self.course_search(keyword) == False:
                return False
        return True

    def existing_prerequisite(self, keyword):
        '''To check if a course is a prerequisite of another course.'''
        course = self.read_course_file()
        course_list = [line.split(',') for line in course]
        for course in course_list:
            if keyword in course[3].split(' '):
                return True
        return False

    def existing_prerequisite_course_display(self, keyword):
        '''To display the courses that have the given course as a prerequisite.'''
        course = self.read_course_file()
        course_list = [line.split(',') for line in course]
        for course in course_list:
            if keyword in course[3].split(' '):
                print(course[0], ' - ', course[1], ' - ', course[2], ' - ', ', '.join(course[3].strip().split(' ')))
         
    def adding_new_course(self, course_code, course_title, course_credit, prerequisites):
        '''To add a new course'''
        if self.course_search(course_code) != False or self.course_search(course_title) != False:
            print('\nCourse already exits')
            return False
        elif self.prerequisite_check(prerequisites) == False and prerequisites != 'N/A':
            print('\nPrerequisite course missing. Please add prerequisites of this course.')
            return False
        else:
            self.course_code = course_code
            self.course_title = course_title
            self.course_credit = course_credit
            self.prerequisites = prerequisites
            self.write_course_file()
            return True
   
    def deleting_existing_course(self, keyword):
        '''To delete an existing course.'''
        course = self.course_search(keyword)
        if course == False:
            print('\nCourse not found!')
            return False
        elif self.existing_prerequisite(keyword) == True:
            print('\nThis course is a prerequisite of another courses. Please delete the prerequisite course first.')
            print('\nCourses that have this course as a prerequisite: \n')
            self.existing_prerequisite_course_display(keyword)
            return False
        else:
            course_list = self.read_course_file()
            course_list.remove(','.join(course))
            with open('course.txt', 'w') as file:
                for line in course_list:
                    file.write(line)
            return True

    def update_existing_course(self, keyword, course_code, course_title, course_credit, prerequisites):
        '''To update an existing course.'''
        course = self.course_search(keyword)
        if course == False:
            print('Course not found!')
            return False
        elif self.prerequisite_check(prerequisites) == False and prerequisites != 'N/A':
            print('Prerequisite course missing. Please add prerequisites of this course.')
            return False
        else:
            course_list = self.read_course_file()
            course_list.remove(','.join(course))
            with open('course.txt', 'w') as file:
                for line in course_list:
                    file.write(line)
            if self.adding_new_course(course_code, course_title, course_credit, prerequisites) == True:
                return True
            else:
                self.adding_new_course(course[0], course[1], course[2], course[3].strip())
                return False