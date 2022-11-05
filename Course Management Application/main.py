from course import Course
from menu import Menu

def main():
    '''Main function'''
    course = Course()
    menu = Menu()
    print('\n==================== Welcome to the Course Management System ====================\n')
    while True:
        print('\n==================== Main Menu ====================\n')
        menu.main_menu()
        while True:
            try:
                user_input = input('Enter your choice: ')
                break
            except ValueError:
                print('Invalid input!')
        if user_input == '1':
            print()
            course.all_course_display()
        elif user_input == '2':
            print('\n==================== Search Menu ====================\n')
            course.individual_course_display(menu.search_menu())
        elif user_input == '3':
            print('\n==================== New Course Adding Menu ====================\n')
            input_list = menu.add_new_course_menu()
            if course.adding_new_course(input_list[0], input_list[1], input_list[2], input_list[3]):
                print('\nNew course added successfully!')
        elif user_input == '4':
            print('\n==================== Course Deleteing Menu ====================\n')
            if course.deleting_existing_course(menu.delete_existing_course_menu()):
                print('\nCourse deleted successfully!')
        elif user_input == '5':
            print('\n==================== Course Updating Menu ====================\n')
            input_list = menu.update_exitsing_course_menu()
            if course.update_existing_course(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4]):
                print('\nCourse updated successfully!')
        elif user_input == '6' or user_input.lower() == 'quit':
            print('Thank you for using the Course Management System!')
            break
        else:
            print('\nInvalid input. Please choose again!\n')

'''Call the main function'''
main()