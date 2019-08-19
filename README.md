# Fullstack Milestone Project - Unicorn Attractor Issue Tracker

Welcome to my fullstack milestone project, for this project I have created an issue tracker for an app called Unicorn Attractor.
The Issue Tracker allows users to report bugs they have discovered on Unicorn Attractor by creating a bug ticket or if they have an idea for a new feature they can create a feature ticket which requires a donation.

---

## UX

This web application will be for users who have discovered issues with Unicorn Attractor and want to report them or have
an idea for a new feature.

### User Stories

- As a user, I want to register an account through an easy to use UI, so I can 'Feature' or 'Bug' create tickets.
- As a user, I want to report a bug I have found on Unicorn Attractor by adding a 'Bug' ticket to the database, so the developers can see my ticket and fix the bug.
- As a user, I want to have the ability to suggest a new feature by adding a 'Feature' ticket to the database, so the developers can see my idea and implement it.
- As a user, I would like the ability to change the 'Open' or 'Closed' status of my ticket, so other users know if the feature or bug is open or not.
- As a user, I would like my tickets to be secure, so only I can edit or delete them.
- As a user, I would like the ability to upvote on tickets, so I can see how many upvotes a ticket has.
- As a user, I would like the ability to delete my ticket, so I can remove the ticket from the database when I wish.

### Wireframes

- [Desktop/Mobile Wireframes **All Tickets Page**](https://github.com/dan360z/Full-Stack-Project/blob/master/static/wireframes/all-tickets.jpg?raw=true)
- [Desktop/Mobile Wireframes **Full Ticket Page**](https://github.com/dan360z/Full-Stack-Project/blob/master/static/wireframes/full-ticket.jpg?raw=true)
- [Desktop/Mobile Wireframes **All Forms Page**](https://github.com/dan360z/Full-Stack-Project/blob/master/static/wireframes/forms.jpg?raw=true)


---

## Features

### Existing Features

- All tickets page - This is the landing page, on this page users are welcomed with and introduction to the website and all the tickets displayed.

- Register - Users can click on the Register link in the navigation menu and they will be taken to a registration form, once a user has completed the form an account will be created for them and they will have access to creating their own tickets.

- Login - Users can login through this form if they have already registered an account.

- Logout - Users can logout through this form if they are signed in.

- Profile page - Users can view their profie which contains usefull information about their account; e.g. username and email.

- Create 'Bug' Ticket - If a user is signed in they can create 'Bug' tickets by completing a form. Once the form is complete the ticket will be put into the database and displayed on the landing page for others to see.  

- Create 'Feature' ticket - If a user is signed in they can create a 'Feature' ticket, these tickets require a minimum donation of £5. Users will have to complete a form to create a ticket and a payment form which takes their bank card details. If the payment goes through a 'Feature' ticket is created.

- Full ticket page - This page displays full ticket to the user which is the tickets name, total upvotes, ticket status and category. This page also includes edit and delete buttons that are only available to the creator of the ticket.

- Upvote - This is a button located on the full ticket page. When a user clicks on the upvote button the total upvotes is incremented by 1.

- Edit ticket - This page is accessed though the edit ticket button. This page contains an edit ticket form where the form fields are pre filled with the existing data of the ticket so it is easy to edit.

- Delete ticket - When a user clicks this button the recipe will be removed from the database.

### Features Left to Implement

- User profile extended - This page will show more information about the user; e.g. profile image, bio and more. 

---

## Technologies Used

- **[HTML](https://en.wikipedia.org/wiki/HTML)**
    - This project uses **HTML** to build the foundation of the website and including links to CSS and JavaScript scripts.

- **[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)**
    - This project uses **CSS** to style the website.

- **[Materialize 0.100.2](http://archives.materializecss.com/0.100.2/)**
    - This project uses the **Materialize** library's navigation bar, modal, forms, buttons, and css helpers.     

- **[Bootstrap CSS](https://getbootstrap.com/)**
    - This project uses the **Bootstrap** CSS library for it's grid system and css helpers.
 
- **[JavaScript](https://www.javascript.com/)/[JQuery js](https://jquery.com/)**
    - This project uses **JavaScript**/**JQuery** to initialize the Materialize dropdown menus, navigation bar, modal and to connect to the **[Stripe](https://stripe.com/gb)** API to process payments.

- **[Stripe](https://stripe.com/gb)**
    - This project uses **Stripe** a payment processing platform to process the donations when a user creates a 'Feature' ticket.

- **[Python](https://www.python.org/)**
    - This project uses **Python** as the back-end programming language.

- **[Django 1.11.17](https://www.djangoproject.com/)**
    - This project uses the **Django** framework.

- **[Heroku](https://www.heroku.com/)**
    - This project uses the cloud application platform **Heroku** to host the application.

---


## Testing

User scenarios:

1. Create an account:
    1. Go to the navigation menu and click on register.
    2. Complete the form.
    3. Click on the register button and verify you have been signed in, a message will appear confirming this.

2. Login:
    1. If you have an existing account go to navigation menu and click on login.
    2. Enter your credentials.
    3. Click on the login button and verify you have been signed in a message will appear confirming this.

3. Logout:
    1. If you are already logged in, go to the navigation menu and click on logout.
    2. Verify you have been logged out, a message will appear confirming this.

4. View full ticket:
    1. On the landing page all the tickets will be dispalyed.
    2. Click on one of these tickets.
    3. You will be taken to full ticket page and Verify that the full ticket is displayed.

5. Add 'Bug' ticket:
    1. On the landing page click the create 'Bug' ticket button.
    2. Complete the form and click the save button.
    3. You will be taken to the full ticket page and verify that your ticket has been created.

6. Add 'Feature' ticket:
    1. On the landing page click the create 'Feature' ticket button.
    2. Complete the ticket form and payment form then click the donate button.
    3. You will be taken to the full ticket page and verify that your ticket has been created.          

7. Edit ticket:
    1. On the full ticket page if the ticket is yours you can click on an edit button.
    2. Make a change to the prefilled form and click save.
    3. Verify that your changes have been made to the ticket.

8. Delete ticket:
    1. On the full ticket page if the ticket is yours you can click on the delete button.
    2. Click 'Yes, I'm sure' in the delete confirmation modal.
    3. You will be taken back to the landing page verify that your ticket has been removed form the database.

#### Responsiveness
- I have tested the website extensively on all screen sizes in vertical and portrait mode:
    - Extra small (I phone 5).
    - Small (Samsung Galaxy S8).
    - Medium (I pad, I pad pro).
    - Large (Laptop, Desktop).
    - Extra large (TV).
    - Google Chrome's developer tools to see how the website functioned and looked across all the different device screen sizes.

#### Browser Support
- I tested the website on Chrome, Microsoft Edge and Firefox.

#### Validation
- I have validated the HTML using **[W3C Markup Validation Service](https://validator.w3.org/)**. Unfortunately the W3C HTML Validator shows alot of errors when reading the Django templating syntax. But the rest of the HTML is valid.
- I have validated the CSS using **[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)**.

---


## Deployment

### Local Deployment

To run this project locally you will need the following to be installed:

- Python3 to run the application.
- PIP to install all app requirements.
- Any IDE. I used Microsoft Visual Studio Code.
- GIT for version control.

Here are the steps for local deployment:

- Clone or download this repository by clicking the green 'Clone or download' button and unzipping the file that is downloaded, or you can enter the following into your Git CLI terminal:
    - `git clone https://github.com/dan360z/Full-Stack-Project.git` 

- Navigate to the directory where you unpacked the files if you are not already there. 

- Install all requirements from the requirements.txt file using this command:
    - `sudo pip3 -r requirements.txt`

- Create an environment variable on your machine or in a `.env` file for your 'SECRET_KEY', remember to reference the `.env` file in a `.gitignore` file. The key and value pair will be:
    - SECRET_KEY : `'Your secret key'`.

- Sign up for an account on [Stripe](https://stripe.com) a payment processing platform. Once you have created an account you have access to your API test keys: Publishable key and Stripe Secret key. Place these in your `.env` file. The key and value pairs will be:
    - STRIPE_PUBLISHABLE : `Publishable key`.
    - STRIPE_SECRET : `Secret key`.

- Now you can run your application using the following command in your CLI:
    - `./manage.py runserver`

- Once you have run the application for the first time a `db.sqlite3` file will be created remember to reference this on your `.gitignore` file.

     Stop the server using:
    - `ctrl` + `C`

- Make migrations to create the database schema by running the following commands:
    - `./manage.py makemigrations`
    - `./manage.py migrate`

- To access the Django Admin Panel, you must create a superuser:
    - `manage.py createsuperuser`   

- Add `'127.0.0.1'` to Allowed Hosts in settings.py.

- Now you can run your application again using the following command in your CLI:
    - `./manage.py runserver`

- The app should now be running on *local host* `http://127.0.0.1:5000/`. Copy and paste this into a browser of your choice.     

### Remote Deployment

I have deployed this project to [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To deploy this project on Heroku I took the following steps:

- Sign up for an Heroku account and create a new app.

- Click on the resources tab and go to Add-ons, search for Postgres and install the remote database.

- Click the Deploy tab, click on Connect GitHub, and Enable Automatic Deployment. When you push your code to GitHub Heroku will automatically deploy your project. 

- In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:
    - SECRET_KEY : `Your Secret Key`
    - STRIPE_PUBLISHABLE : `Your Stripe Publishable Key`
    - STRIPE_SECRET : `Your Stripe Secret`

- Also in Config Vars you will see the DATABASE_URL for the remote database. You will need to add this key and value pair to your `.env` file inside the project.

- Once you have done this make migrations to create the database schema for Postgres by running the following commands:
    - `./manage.py migrate`

- Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: gunicorn issuetracker.wsgi:application`

- Commit and Push your code to GitHub.

- Go back to Heroku and your application should be successfully deployed. If it is not deployed successfully check the logs they are very informative.

---

## Credits


### Acknowledgements

- [Code Institute](https://courses.codeinstitute.net). Help with processing payments with stripe and authentication functionality.
- [Stack OverFlow](https://stackoverflow.com/). Help with various code related problems.

### Designer/Developer
Unicorn Attractor Issue Tracker was designed and developed by **Daniel Field**.