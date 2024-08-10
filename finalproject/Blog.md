# A To-Do App with Flask

This is my final project for [CS50's Introduction to Computer Science](https://cs50.harvard.edu/college/2021/fall), a task management website developed using Python and Flask. The application is designed to help users efficiently record and manage their tasks.

## Project Overview

The site features five main pages:

1. **Register Page**
   - **Description**: Users can create a new account by filling out a registration form.
   - **Fields**:
     - **Name**: The user's full name.
     - **Username**: The application checks for existing usernames and only accepts lowercase characters. Numbers and symbols are not allowed.
     - **Password**: The password is validated to ensure it matches the confirmation field.
   - **Screenshot**:
     ![Register Page](https://user-images.githubusercontent.com/92978761/151401244-536ac9da-413c-4cf7-962f-733b884e6eed.png)

2. **Login Page**
   - **Description**: Users can log in by entering their username and password. The application verifies credentials and creates a session for the user.
   - **Screenshot**:
     ![Login Page](https://user-images.githubusercontent.com/92978761/151401535-a16cca70-e08b-43c5-bf21-568b17abe425.png)

3. **Main Screen**
   - **Description**: Upon logging in, users are directed to the main screen, where they can view and manage tasks for the current date or any other date. Features include:
     - **Adding New Tasks**: Users can add new tasks for the current day or a different date. The "New Task" option opens a form with fields for task name and date.
       - **Screenshot**:
         ![Add New Task](https://user-images.githubusercontent.com/92978761/151402625-eb6348e0-a7b6-4e12-b9be-9fcd477438ac.png)
     - **Prioritizing Tasks**: Tasks can be moved to the top of the list for higher priority.
     - **Deprioritizing Tasks**: Completed tasks can be moved to the bottom of the list.
     - **Marking Tasks as Done**: Tasks can be marked as completed.
       - **Screenshot**:
         ![Mark Task Done](https://user-images.githubusercontent.com/92978761/151404650-7515cd54-07ad-46c3-a265-8de02e3748ba.png)
     - **Reopening Tasks**: Tasks marked as done can be reopened and edited.
     - **Editing Tasks**: Modify task details such as name or date using the same form used for adding tasks.
     - **Viewing Tasks**: Browse tasks by date, show only undone tasks, or view all daily tasks.
     - **Deleting Tasks**: Remove tasks permanently from the database.

   - **Screenshot**:
     ![Main Screen](https://user-images.githubusercontent.com/92978761/151403794-8a4132e4-47fc-405c-af8b-e16c516986af.png)

4. **Logout**
   - **Description**: Users can log out of the application by selecting the "log out" option in the page header.

## Technologies Used

- **SQL**: Used for managing the database, including user accounts and tasks. Passwords are securely hashed in the database to enhance security.
- **Python**: The primary language used for developing the application logic.
- **Flask**: A lightweight web framework that handles the application’s routing and server-side functionality.

## Security and User Management

- **Authentication**: Each route checks if the user is authenticated. Once logged in, users remain logged in until they log out.
- **User-Specific Data**: Each user can only view their own tasks. The application uses foreign keys in the database to associate tasks with users.

## Conclusion

Thank you for exploring my To-Do List application. I hope this project demonstrates the practical application of the skills I acquired during CS50. If you have any questions or feedback, feel free to reach out!

Enjoy using the app!

