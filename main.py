from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div',class_='card')

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a

        print(course_name)
        print(course_price)
        




    #Buscar e imprimir tags h5
    #courses_html_tags = soup.find_all('h5')
    #for course in courses_html_tags:
     #   print(course.text)