<h1><b>Printcentre Workflow Manager Project Resubmission</b></h1>

[View the live project here.](https://printcentre-workflowmanager.herokuapp.com/)
<br />
[Github link of previous failed milestone project 3 submission.](https://github.com/DuggyL/workflow-milestone-project-3/)

This Python and Data-Centric Development project aims to design a simple task manager for Printcentre Wales (my current employer), a commercial printing company. 

<img src=images/am-i-responsive.png>

## Purpose & Goals

Printcentre management currently uses desktop software to manage customers’ databases. This software can only be accessed by the management team. 

Print production starting from admin handled customer’s information and jobs specifications. When a job is booked, the admin creates a job docket containing customer details and work instructions. 
The docket passes to the pre-press department where they prepare artwork for production and to the Printroom/ Finishing department till job completion. 
Finally, the docket passes back to the admin to organise invoice, payment and delivery. 

A single docket passes through multiple departments, if the docket is incorrect, outdated or misplaced, it can lead to mistakes during the production. 
To correct the problem, the production team requests a new / updated job docket from the admin which can be time-consuming and costly. 
If all the staff have access to the same information on the job docket at the same time I believe it can improve efficiency and reduce mistakes.

The purpose & goals of this project are to create a simple web application that allows all staff to access a simple task management system containing work instructions and customer details. 
The web application can be accessed on all devices, where admin or staff can read, add, edit and delete.

## User Experience (UX)

-   ### New, Returning and Frequent Visitor Goals

    - As a User, I want to register and create a user profile.
    - As a User, I want to easily navigate across the site so that I can find the information I need.
    - As a User, I want to see messages responding to my interaction with the web application i.e. logging in, logging out, registering, adding, edit or delete.
    - As a User, I want the ability to add, edit and delete jobs.
    - As a User, I want customer’s details and work instructions available to me. 
    - As a User, I want a responsive website so that I can access it on different devices.

## Design
-   #### Colour Scheme
    -   The two main primary colours used are Black & White
    -   Black text for readability on white background.
    
The reason I chose these 2 combinations of colours for my project is to keep the page clean and readable and maintain professionalism. 

-   #### Typography
    -   I used Roboto throughout the webpage to maintain cohesion across the project. Using different font weights to convey emphasis and importance on some of the content. It has friendly features and great letter-spacing that leads to ease of communication.

## Responsive Design, Features & CRUD Operations

### CRUD Operations
Using the CRUD's four basic functions (create, read, update and delete), here are the design and features:

-   The ability to create tasks and customer database
-   The ability to read/check work instructions, and customer information
-   The ability to update/edit jobs work instructions
-   The ability to delete tasks, assignments and schedule

<img src=images/homepage.png>

-   ### Navigation Bar
    -   Featured on all pages, the full responsive navigation bar includes links to the Logo, tasks, add tasks, add customer, log in and register page and is identical on each page to allow for easy navigation.
    -   Navigation bar will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.
    -   The navigation bar displays different links depending on whether the user is logged in, logged out.

<img src=images/mobile-nav.png>

-   ### Home Page
    -   Tasks display on the landing page. Users can interact with the collapsible to see more in-depth details of the work instruction.
    -   Unregistered and logout users do not have edit or delete button/icon available to them but can still interact with work instructions collapsible.  
    -   Only users who created the task can see buttons that allow users to edit or done.

<img src=images/add-task.png>

<img src=images/add-task-mobile.png>

-   ### Add Task Page
    -   Allow users to add to the database and display created tasks on the home page, users can cancel the adding by clicking on the cancel button.
    -   Clicking on both cancel and submit buttons will bring the user back to the task display page.
    -   It uses a combination of 2 mongo databases (Tasks and Customers).

<img src=images/edit-task.png>

-   ### Edit Tasks Page
    -   Edit task page allows users to edit the tasks database, users can cancel the edit by clicking on the cancel button.
    -   Clicking on both cancel and submit buttons will bring the user back to the task display page.
    -   The previous data value will automatic fill the form, avoiding the need for users to re-input the data. 

<img src=images/customers.png>

-   ### Customers Page
    -   Table display list of existing customers.
    -   Search function available at the top if users want to search for specific customer by customer's name or company's name.
    -   Clicking on "Add Customer" button to send users directly to add customer page.

<img src=images/add-customer.png>

-   ### Add Customer Page
    -   Allow users to add to the database and display created customer on the customers page. Users can cancel by clicking on the cancel button.
    -   Clicking on both cancel and submit buttons will bring the user back to the customers page.

<img src=images/edit-customer.png>

-   ### Edit Customer Page
    -   Edit customer page allows users to edit the customers database, users can cancel the edit by clicking on the cancel button.
    -   Clicking on both cancel and submit buttons will bring the user back to the customers page.
    -   The previous data value will automatic fill the form, avoiding the need for users to re-input the data. 

<img src=images/profile.png>

-   ### Profile Page
    -   A page is dedicated to the user when they are logged in. Currently, blank and more features are implemented at later project stages.

### Defensive Design

<img src=images/defensive.png>

-   ### Form Validation
    -   Form validation has been added to every form to ensure all required information is included before submission.
    -   If incorrect data is input a warning red line indicates the data invalid i.e no letters in strictly number field, minimum and maximum character depend on expected data.

<img src=images/log-in-error.png>

-   ### Success and Error Flash message
    -   Flash message will appear at the of the page in response to user activity. For example, if you input the wrong password, an error message will appear letting user know the reason for the error. (Green for success and red for error).

<img src=images/defensive-wrong-input.png>

-   ### Input Validation
    -   Some of the forms have input restriction, i.e maximum and minimum characters length, integer only etc. The input field will turn red if the data input are not acceptable and green if the data input are ok. A small message will appear below active input form to let users know what type data it required.

-   ### Unauthorised Page
    -   Unregister or logged out users cannot access to add tasks, profiles or customer page

<img src=images/log-in.png>

## Future Features
-   I would like to add more features to the profile page, like tasks history.
-   The ability for users to change their username and password
-   Improvement of user experience to task collapsible 
-   The ability to add comments to a task is collapsible while the task is still active

## Technologies Used

### Languages Used

-   HTML5
-   CSS3
-   Javascript
-   Python

### Frameworks, Libraries & Programs Used

1. [Materialize](https://materializecss.com)
    - Materialize was used to assist with the responsiveness and styling of the website.
1. [Flask v2.1](https://flask.palletsprojects.com/en/2.1.x)
    - Flask framework is used to assist in the building of the web application.
1. [MongoDB](https://www.mongodb.com)
    - Cloud-hosted database service used to store tasks/ work instruction information and staff login details.
1. [Google Fonts:](https://fonts.google.com)
    - Google fonts were used to import the 'Roboto font family', which is used on all pages throughout the project.
1. [jQuery:](https://jquery.com)
    - jQuery came with Materialize
1. [Git](https://git-scm.com)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com)
    - GitHub is used to store the projects code after being pushed from Git.

## Testing

The JSHint Lighthouse, W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no errors in the project.

-   JSHint Found 9 functions with same 2 warnings regarding browser extension. [link](images/JSHint.png)
-   HTML Validator found 1 error from Materialize jQuery preset. [link](images/html-checker.png) 
-   CSS Validator found 1 error from Materialize css preset. [link](images/css-checker.png) 
-   Python PEP8 online found 2 error regarding expected lines

### Testing User Stories from User Experience (UX) Section

-   #### New, Returning and Frequent Visitor Goals

    1. As a User, I want to register and create a user profile.

        - The site allow user to register to the task manager using register page and set up their own profile

    2. As a User, I want to easily navigate across the site so that I can find the information I need.

        - The site has been designed to easily navigate. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.

    3. As a User, I want to see messages responding to my interaction with the web application i.e. logging in, logging out, registering, adding, edit or delete.

        - If users correctly or successfully input data, a green success flash will appear with appropriate messages and flash red if failed or input data incorrectly.
    
    4. As a User, I want the ability to add, edit and delete jobs.

        - Users can add, edit and delete tasks/customer from the database.

    5. As a User, I want customer’s details and work instructions available to me. 

        - All the created tasks are display on the main page and customer information on customer page.

    6. As a User, I want a responsive website so that I can access it on different devices.
        
        - The forms and tasks collaspible and resize to small screen size on different devices.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   Testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

# Deployment

### GitHub Pages
The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).
2. At the top of the Repository locate the "Settings".
3. Click on "Pages" will open "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. At the top near github header to locate the now published site [link](https://github.com/DuggyL/workflow-milestone-project-3/).

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:-

1. Log in to GitHub and locate the GitHub Repository.
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
1. Log in to GitHub and locate the GitHub Repository.
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied.

# Credits

### Code
-   This project is heavily based on Code Institute task manager tutorials.
-   Python Website Full Tutorial - Flask, Authentication, Databases & More by Tech With Tim [link](https://www.youtube.com/watch?v=dam0GPOAvVI&list=PLDpvVzk1kZl_xWyRhgVk5o2QUIaW_WyQc&index=53&t=7552s)
-   How to Use Databases With SQLAlchemy by Codemy.com [link](https://www.youtube.com/watch?v=Q2QmST-cSwc&list=PLDpvVzk1kZl_xWyRhgVk5o2QUIaW_WyQc&index=54)

### Media
-   All icons from Materialize
-   Images used in readme were screen shot from W3 Validators and Am I Responsive.

### Acknowledgements
-   My Mentor [Narender Singh](https://github.com/nar3nd3r) for helpful feedback regarding design, features and functionality.