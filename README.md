# CS50
# Blog-CS50-Recap & Final Project
hello all, this blog is about what i learned throught my walk in CS50 and my final project.
# What is CS50?
CS50 is probably the most popular of all programming courses, especially for beginners.
In 10 weeks, students learn different topics: Scratch, C, Arrays, Data Structures, Algorithms, Python, SQL, front-end and back-end, every week you learn to solve Labs and some problems.
At the end of the course, we have you have to create your final project.
# CS50 Course Content
1. Week 0: Computer science basics(Binary, what is an algorithm, Scratch...)
2. Week 1 --> Week 5: Everything you will learn in these five weeks, you will apply in C, 
C intro (if statements, for & while loops, functions, data types..), libraries, then you will learn searching and sorting algorithms, big O notation, and data structures(linked lists, tree, hash tables, tries...).
In these weeks, you will find it difficult to solve problems if the information is new to you.
3. Week 6: After learning C, you will learn high-level python, with simple syntax, and won't let you worry about some issues like data allocation, semi-columns, segmentation faults, this week focus on some Python topics like dictionaries, teach you how to handle possible CSV files In C but way harder. You have to learn in Python everything you learned in C
4. Week 7: This week will show you a more efficient way to store data. You will learn the basics of relational databases, SQL, SQLite. This week is full of fun problems.
5. Week 8: In this week you will learn the basics of the web (HTTP, TCP/IP...) and how to create a simple website using HTML, CSS, and JavaScript with some bootstrap...
6. Week 9: This week you will learn about Frameworks, Flask in particular, and learn how to create a fully functional website using python-flask, in addition to what you learned in the previous weeks (SQLite, HTML, Js...).
Solving this problem will be very interesting because you have to use everything you learned in the course.
 # Tasks/flask-project
 Description:

A project is a web page where the user records the tasks to be completed. You can add tasks and delete tasks, the use is very easy.
I did this project because the organization of tasks is very important for every programmer, but for every human, and because I prefer that my final project be within the scope of what we learned in this course

Technologies used:

    SQL
    Python
    Flask.
This is my last project for the cs50 Introduction to Computer Science (https://cs50.harvard.edu/college/2021/fall) a tasks recording website with python-flask.

The site contains 5 tracks or pages:

1. A register route, where you can register for a new account by applying form (username/password).
You need to enter these fields:

    Name
    Username: it is check if already exist a user with de same name. Only lowercase characters are accepted. Numbers and symbols are not allowed.
    Password: it is checked to match.


![Screenshot from 2021-12-14 20-30-27](https://user-images.githubusercontent.com/92978761/146683835-22c6a94e-7f75-4fc2-8cdd-9213c2c84513.png)



2. A login page, will check if the username and password match then creates a session for the user.



![Screenshot from 2021-12-14 20-29-59](https://user-images.githubusercontent.com/92978761/146684190-0cce8264-ba81-4874-ad23-edee13f656e1.png)




3.  After logging in, the main screen opens, on it, you will find the date and all the tasks related to that date and the logged-in user. On this screen you can:

    Registering new tasks:
 You can record all tasks for that day or another day in the "New Task" option. A new screen for this recording will open with two fields: task name and date. The date will be suggested by the date depicted on the home screen. The tasks will be added to the end of the list.
    Prioritize tasks (top task in the list) :
  Important: Completed tasks are considered.
Deprioritizing tasks (below the task in the list) : 
Important: Completed tasks are considered.
    Mark "done":
To finish the task by marking "Done" on the screen.
    Mark Not Done: Reopens the task, and removes the mark on the screen.
    You can delete tasks:
The task will be permanently deleted from the database.
Edit tasks:
 In this option, you can edit the date or name of the task. The same New Task screen will open with the data already filled in.
    Check other day's assignments: you can browse between dates.
    Show only undone tasks.
    View all tasks daily.

By clicking on the "TASKS" icon in the title, you will be redirected to today's tasks.

All options are on this home screen. Several icons have been used with images to make them more intuitive and simple to use. Each user will be able to view only their tasks. For this reason, there is a registration of users.

The task will be permanently deleted from the database.



![Screenshot from 2021-12-19 19-58-54](https://user-images.githubusercontent.com/92978761/146686237-97771b60-d921-4f13-b14b-eb64ef87c2f5.png)






