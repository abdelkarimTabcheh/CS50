# A TODO app with flask
 This is my last project for the cs50 Introduction to Computer Science (https://cs50.harvard.edu/college/2021/fall) a tasks recording website with python-flask.

The site contains 5 tracks or pages:


This is a web page where the user records the tasks to be completed. You can add tasks and delete tasks, it's very easy to use.
I did this project because the organization of tasks is very important not for every programmer, but for every human.

Technologies used:

    SQL
    Python
    Flask

1. A register route, where you can register for a new account by applying form (username/password).
You need to enter these fields:

      Name
      Username: the application check if already exist a user with de same name, Only lowercase characters are accepted. Numbers and symbols are not allowed.
      Password: it is checked to match.


![Screenshot from 2021-12-14 20-30-27](https://user-images.githubusercontent.com/92978761/146683835-22c6a94e-7f75-4fc2-8cdd-9213c2c84513.png)



2. A login page, will check if the username and password match then creates a session for the user.



![Screenshot from 2021-12-14 20-29-59](https://user-images.githubusercontent.com/92978761/146684190-0cce8264-ba81-4874-ad23-edee13f656e1.png)




3.  After logging in, the main screen opens, on it, you will find the date and all the tasks related to that date and the logged-in user. On this screen you can:

    Registering new tasks:
 You can record all tasks for that day or another day in the "New Task" option.
 
 A new screen for this recording will open with two fields: task name and date.
 
 The date will be suggested by the date depicted on the home screen.
 
 The tasks will be added to the end of the list.
 

    Prioritize tasks (top task in the list) :
  Completed tasks are considered.
Deprioritizing tasks (below the task in the list) : 
  Completed tasks are considered.
    Mark "done":
To finish the task by marking "Done" on the screen.
    Mark Not Done: Reopens the task, and removes the mark on the screen.
Edit tasks:
 In this option, you can edit the date or name of the task. The same New Task screen will open with the data already filled in.
    Check other day's assignments: you can browse between dates.
    Show only undone tasks.
    View all tasks daily.

    You can delete tasks:
The task will be permanently deleted from the database.

By clicking on the "TASKS" icon in the title, you will be redirected to today's tasks.

All options are on this home screen. Several icons have been used with images to make them more intuitive and simple to use. Each user will be able to view only their tasks. For this reason, there is a registration of users.





![Screenshot from 2021-12-19 19-58-54](https://user-images.githubusercontent.com/92978761/146686237-97771b60-d921-4f13-b14b-eb64ef87c2f5.png)


![Screenshot from 2021-12-19 19-58-54](https://user-images.githubusercontent.com/92978761/146686382-f10a6684-372f-4ed2-ad55-37b5e64dda79.png)

Each route checks if the user is authenticated. Once logged in you will remain logged in, who is using the web page is saved.
Database stores all users and tasks. Important: The password is saved in the hashed database to improve website security. The table 'tasks' uses foreign keys to related users.


5. Logout:
To exit the web page just go to the "log out" option at the page header.

That's all enjoy!



