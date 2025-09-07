# django-learning
This repository is used to help me learn Django through a collection of projects, to gain a good understanding of where Django fits in with web development. Each folder represents a unique project, with the major one being ***W3Schools-Django***, which I will explain below.

---

## Current Project

### **1. W3Schools-Django

- **Description:**

   A Django learning website based on W3Schools tutorial, restructured for improved clarity with logical sections and practical examples. This project is built with scalability in mind, focusing on core functionality and responsive design.


- **Features:**  

  - Clear navigation across structured tutorial sections using Django templates and views.
  - Virtual Environment for each project.
  - Scalable database design using Django models and migrations.
  - Custom Django forms for user input and validation.
  - Static file handling for CSS and images.
  - Designed with future responsiveness and deployment in mind.


- **Technologies:**

  **Front-end:**

  - HTML with Django   
  - CSS served using Django static files
  - *(Planned)* Bootstrap 5 for layout and styling
  - *(Planned)* Responsive design using media queries

  **Back-end:** 

  - Python as main programming language
  - Django for routing, views, models, forms and migrations
  - SQLite3 as development database
  - Django Admin Panel for CRUD operations

  **Build Tools / Environment:**

  - Virtual Environment for managing isolated dependencies
  - Pip for installing project packages
  - Django Admin Command Line Interface tools (`manage.py` and `django-admin`)
  - Whitenoise for serving static files in production
  - *(Planned)* requirements.txt for tracking dependencies
  - *(Planned)* PostgreSQL for new database, AWS for host provider and Elastic Beanstalk for deployment

- **Front-end operations:**

  - Rendering pages using Django templates (`.html`) with dynamic data from views
  - Applying styling using static CSS files
  - *(Planned)* Improve user interface with Bootstrap 5 and mobile responsiveness


- **Back-end operations:**
  - Handling page routing and logic using Django views
  - Creating and managing data using Django models and SQLite3 database
  - Using Django forms to handle user input abd validation
  - Django admin panel used for creating, reading, updating or deleting data records 


## 🧭 Django Learning Roadmap (Before Setup Instructions)
 
  Roadmap below is used to understand structure, setup, and running of Django Learning project. 

  Note: Localhost becomes available only after 1.7 Django Views, so read to that point first to get familiar with Django and its setup.

  Please read setup instructions that follow, as they cover most important steps for preparing your Django project.


  | Step   |        Topic                           |     Localhost (after setup)             | 
  |--------|----------------------------------------|-----------------------------------------|
  |  1     |  [Django Setup](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/)                         |                                                        
  |        |  └─ [Django Setup Home](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_setup_refs.html)              |  [Django Setup (Localhost)](http://127.0.0.1:8000/django_setup/ "http://127.0.0.1:8000/django_setup/")                |
  |        |     │                                  |     
  |  1.1   |     └─ [Django Introduction](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_intro.html)              |                                                  
  |  1.2   |     └─ [Django Get Started](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_get_started.html)              |                                         
  |  1.3   |     └─ [Virtual Environment](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_virtual_env.html)             |                                                                                 
  |  1.4   |     └─ [Install Django](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_install.html)                    |                                                                                   
  |  1.5   |     └─ [Django Project](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_project.html)                   |                                                                             
  |  1.6   |     └─ [Django App](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_app.html)                          |                                                                             
  |  1.7   |     └─ [Django View](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_views.html)                       |                                          
  |  1.8   |     └─ [Django URL](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_url.html)                      |  [Django URL (Localhost)](http://127.0.0.1:8000/django_setup/url "http://127.0.0.1:8000/django_setup/url")                          
  |  1.9   |     └─ [Django Template](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_template.html)                  |  [Django Template (Localhost)](http://127.0.0.1:8000/django_setup/template "http://127.0.0.1:8000/django_setup/template")                     
  |  1.10  |     └─ [Django Model](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_model.html)                      |  [Django Model (Localhost)](http://127.0.0.1:8000/django_setup/model "http://127.0.0.1:8000/django_setup/model")                      
  |  1.11  |     └─ [Django Insert Data](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_insert_data.html)                 |    [Django Insert Data (Localhost)](http://127.0.0.1:8000/django_setup/insert_data "http://127.0.0.1:8000/django_setup/insert_data")                   
  |  1.12  |     └─ [Django Update Data](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_update_data.html)                 |    [Django Update Data (Localhost)](http://127.0.0.1:8000/django_setup/update_data "http://127.0.0.1:8000/django_setup/update_data")            
  |  1.13  |     └─ [Django Delete Data](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_delete_data.html)                |  [Django Delete Data (Localhost)](http://127.0.0.1:8000/django_setup/delete_data "http://127.0.0.1:8000/django_setup/delete_data")                                             
  |  1.14  |     └─ [Django Update Model](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_update_model.html)               |    [Django Update Data (Localhost)](http://127.0.0.1:8000/django_setup/ "http://127.0.0.1:8000/django_setup/")          
  
  
  - [/members](http://127.0.0.1:8000/members "http://127.0.0..1:8000/members") works at first, but is later used for tennis club data.
  - Use [/hello](http://127.0.0.1:8000/hello "http://127.0.0..1:8000/hello") route for the Hello World example instead. 


- **Setup Instructions**

  Now that you are familiar with Django setup, we can look at how a new repository can be setup on your computer locally. 

  To run this project locally, follow these steps:

  1.  **Check if Python is installed**
      - Django requires Python and I recommend using version 3.4 or later, because that comes with PIP, refer to [django_get_started.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_get_started.html). 
      - Check for a Python version with `python --version`.
      - If you need to install python, visit `https://www.python.org/` and hover downloads dropdown menu to find a suitable Python 3 version.

  2.  **Clone Django Repository**

      - Copy remote repository onto computer locally using following command:

        `git clone https://github.com/RobertWSON/django-learning`

      - Navigate to project folder, mine is W3Schools-Django with following command:

        `cd workspace/django-learning/W3Schools-Django` 

        Note: I have a workspace for my web development projects, so depending on your setup you may    have a similar or slightly different intial folder.

  3.  **Set up a virtual environment**

      To get an understanding on how a Virtual Environment works with Django, refer to 
      [Django Virtual Environment](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_virtual_env.html)

      - Setup for each Django project using command:

      `python -m venv env` 
      
      where `env` is name of virtual environment 

      Activate (use) environment with these commands:

      Windows

      `env\Scripts\activate.bat`

      Mac

      `source env/bin/activate`

  4.  **Django Setup**

        - **Django Installation**

          To get an understanding on how Django installation works, refer to 
          https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_install.html

          - Install Django while in virtual environment using command:      

          `python -m pip install Django`

        - **Create Django Project**  

          To get an understanding on how to create a Django project, refer to 
          https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_project.html 
            
          - Create a Django project using command:

          `django-admin startproject project_name`

          where `project_name` is name of Django project

        - **Create Django Application** 

          To get an understanding on how to create a Django application, refer to
          https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_app.html

          - Create a Django Web Application using command:

          `python manage.py startapp app_name`

          where `app_name` is name of web application

        - **Setup Local Development Server** 

          <b>Before running the development server</b>, please read through these two pages on views, followed by URL from my Django project repository:

          [Django Views](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_views.html)

          [Django URL](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_url.html)

          This will help you understand how to create a simple "Hello World" view and link it with a URL route.

          Once that is set up, you can run development server and test that the page displays correctly in browser.

        - **Run Local Development Server**

          Now that your view and url are configured, local development server can be run with this command:

          `python manage.py runserver` 


## 🧭 Django Learning Roadmap (Using Django)

  Now we can look at how Django can be used with examples, references and right through to deployment for full-stack development.


  | Step   |            Topic                       |      GitHub Links               |
  |--------|----------------------------------------|---------------------------------|
  |        |                                        |                                 |      
  |  2     |  [Django Code Examples](http://127.0.0.1:8000/testing/)                  |  [Test Django Examples (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing)
  |           └─ [Django Examples Home](http://127.0.0.1:8000/testing/)               |    [Examples Home (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/template.html)  
  |        |  │  │                                   |  
  |  2.1   |  │  └─ [Display Data](http://127.0.0.1:8000/testing/)   |  [Display data (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data)
  |        |  │     │                                |  
  |        |  │     └─  [Prepare Template](http://127.0.0.1:8000/testing/prepare_template "localhost http://127.0.0.1:8000/testing/prepare_template")             |       [Prepare Template (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/template_and_view.html)  
  |        |  │     └─  [Prepare Django View](http://127.0.0.1:8000/testing/prepare_template#prepare_view)                  |  [Prepare View (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/template_and_view.html#L40)               
  |        |  │     └─  [Add Link to Details](http://127.0.0.1:8000/testing/details_link)          |  [Details Link (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/details_link.html)  
  |        |  │     └─  [Add Details View](http://127.0.0.1:8000/testing/details_link#details_view)             |  [Details View (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/details_link.html#L46)  
  |        |  │     └─  [Add Master Template](http://127.0.0.1:8000/testing/master_template)         |  [Master Template (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/master_template.html)  
  |        |  │     └─  Add Main Index Page[Add Main Index Page (localhost)](http://127.0.0.1:8000/testing/main_page)          |  [Index Page (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/main_index.html)  
  |        |  │     └─  [Django 404 Template](http://127.0.0.1:8000/testing/django_404)          |  [Django 404 (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/django_404.html)  
  |        |  │     └─  [Add Test View](http://127.0.0.1:8000/testing/add_test_view)                |  [Test View (Github)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/add_test_view.html)  
  |        |  │     └─  [Django Forms](http://127.0.0.1:8000/testing/django_forms)                 |  [Django Forms (Github)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data/django_forms.html)  
  |        |  │                                     | 
  |  2.2   |  ├- [Django Syntax](http://127.0.0.1:8000/testing/)                    |  [Django Syntax (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax)
  |        |  │   │                                 |
  |  2.2.1 |  │   └─  [Django Variables](http://127.0.0.1:8000/testing/)             |  [Django Syntax - Variables (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/variables_tested.html)   
  |        |  │   │      │                          |  
  |        |  │   │      └─  [Django Variable](http://127.0.0.1:8000/testing/variables_tested)        |  [Django Variable (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/variables_tested.html#L14)
  |        |  │   │      └─  [View Variable](http://127.0.0.1:8000/testing/variables_tested#view)          |  [View Variable (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/variables_tested.html#L32)
  |        |  │   │      └─  [Template Variable](http://127.0.0.1:8000/testing/variables_tested#template)      |  [Template Variable (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/variables_tested.html#L57) 
  |        |  │   │      └─  [Data from a Model](http://127.0.0.1:8000/testing/variables_tested#model_data)      |  [Model Data (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/variables_tested.html#L85)
  |        |  │   │                                 |
  |  2.2.2 |  │   └─  [Django Tags](http://127.0.0.1:8000/testing/)                   |  [Django Syntax - Tags (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/tags_tested.html) 
  |        |  │   │      │                          |  
  |        |  │   │      └─  [Template Tags](http://127.0.0.1:8000/testing/tags_tested)          |  [Template Tags (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/tags_tested.html#L13)
  |        |  │   │      └─  [Django Code](http://127.0.0.1:8000/testing/tags_tested#django_code)            |  [Django Code (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/tags_tested.html#L33)
  |        |  │   │                                 | 
  |  2.2.3 |  │   └─  [Django If](http://127.0.0.1:8000/testing/)                |  [Django Syntax - If (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_tested.html) 
  |        |  │   │      │                          |  
  |        |  │   │      └─  [If Statement](http://127.0.0.1:8000/testing/if_tested)           |  [If Statement (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_tested.html)
  |        |  │   │      └─  [Elif Statement](http://127.0.0.1:8000/testing/if_tested#elif)         |  [ElIf Statement (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_elif.html)
  |        |  │   │      └─  [Else Statement](http://127.0.0.1:8000/testing/if_tested#else)         |  [Else Statement (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_else.html)
  |        |  │   │      └─  [Operator Dropped](http://127.0.0.1:8000/testing/if_tested#drop_operator)       |  [Operator Dropped (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_else.html)
  |        |  │   │      └─  [Operator ==](http://127.0.0.1:8000/testing/if_tested#==_operator)        |  [Operator == (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_%3D%3D_operator.html)
  |        |  │   │      └─  [Operator !=](http://127.0.0.1:8000/testing/if_tested#!=_operator)            |  [Operator != (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_!%3D_operator.html)
  |        |  │   │      └─  [Operator <](http://127.0.0.1:8000/testing/if_tested#<_operator)             |  [Operator < (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_%3C_operator.html)
  |        |  │   │      └─  [Operator <=](http://127.0.0.1:8000/testing/if_tested#<=_operator)        |  [Operator <= (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_%3C%3D_operator.html)
  |        |  │   │      └─  [Operator >](http://127.0.0.1:8000/testing/if_tested#>_operator)             |  [Operator > (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_%3E_operator.html)
  |        |  │   │      └─  [Operator >=](http://127.0.0.1:8000/testing/if_tested#>=_operator)            |  [Operator >= (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_%3E%3D_operator.html)
  |        |  │   │      └─  [Operator and](http://127.0.0.1:8000/testing/if_tested#and_operator)           |  [Operator and (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_and_operator.html)
  |        |  │   │      └─  [Operator or](http://127.0.0.1:8000/testing/if_tested#or_operator)            |  [Operator and (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_or_operator.html)
  |        |  │   │      └─  [Operator and / or](http://127.0.0.1:8000/testing/if_tested#and-or_operator)      |  [Operator and / or (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_and-or_operator.html)
  |        |  │   │      └─  [Operator not in](http://127.0.0.1:8000/testing/if_tested#not-in_operator)        |  [Operator not in (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_not-in_operator.html)
  |        |  │   │      └─  [Operator is](http://127.0.0.1:8000/testing/if_tested#is_operator)            |  [Operator and (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_is_operator.html)
  |        |  │   │      └─  [Operator == replace is](http://127.0.0.1:8000/testing/if_tested#==replace_is_operator) |  [Operator == replace is (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_%3D%3Dreplace_is_operator.html)
  |        |  │   │      └─  [Operator is & with](http://127.0.0.1:8000/testing/if_tested#if_is_&_with_operator)     |  [Operator and (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_is_%26_with_operator.html)
  |        |  │   │      └─  [Operator is not](http://127.0.0.1:8000/testing/if_tested#is-not_operator)        |  [Operator and (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/if_is-not_operator.html)
  |        |  │   │                                 | 
  |  2.2.4 |  │   └─  [Django For Loop](http://127.0.0.1:8000/testing/)               |  [Django Syntax - For Loop (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_tested.html) 
  |        |  │   │      │                          |  
  |        |  │   │      └─  [For Loops - Item](http://127.0.0.1:8000/testing/for_loop_tested)              |  [Item (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_item.html)
  |        |  │   │      └─  [For Loops - Dictionary](http://127.0.0.1:8000/testing/for_loop_tested)      |  [Dictionary (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_dict.html)
  |        |  │   │      └─  [Data From a Model](http://127.0.0.1:8000/testing/for_loop_tested#model_data)      |  [Model Data (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_modeldata.html)
  |        |  │   │      └─  [Reversed](http://127.0.0.1:8000/testing/for_loop_tested#reversed)               |  [Reversed (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_reversed.html)
  |        |  │   │      └─  [Empty an Empty Object](http://127.0.0.1:8000/testing/for_loop_tested#empty)  |  [Clear Empty Object (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_emptyobject.html)
  |        |  │   │      └─  [Empty No Object](http://127.0.0.1:8000/testing/for_loop_tested#empty_noobject)        |  [Empty No Object (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_noemptyobject.html)
  |        |  │   │      └─  [forloop.counter](http://127.0.0.1:8000/testing/for_loop_tested#counter)        |  [Counter (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_counter.html)
  |        |  │   │      └─  [forloop.counter0](http://127.0.0.1:8000/testing/for_loop_tested#counter0)       |  [Counter0 (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_counter0.html)
  |        |  │   │      └─  [forloop.first](http://127.0.0.1:8000/testing/for_loop_tested#first)          |  [First (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_first.html)
  |        |  │   │      └─  [forloop.last](http://127.0.0.1:8000/testing/for_loop_tested#last)           |  [Last (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_last.html)
  |        |  │   │      └─  [forloop.parentloop](http://127.0.0.1:8000/testing/for_loop_tested#parent)     |  [Parent (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_parent.html)
  |        |  │   │      └─  [forloop.revcounter](http://127.0.0.1:8000/testing/for_loop_tested#revcounter)     |  [Revcounter (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_revcounter.html)
  |        |  │   │      └─  [forloop.revcounter0](http://127.0.0.1:8000/testing/for_loop_tested#revcounter0)    |  [Revcounter0 (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/for_loop_revcounter0.html)
  |        |  │   │                                 | 
  |  2.2.5 |  │   └─  [Django Comment](http://127.0.0.1:8000/testing/)                |  [Django Syntax - Comment (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/comments_tested.html)  
  |        |  │   │      │                          |  
  |        |  │   │      └─  [Comments](http://127.0.0.1:8000/testing/comments_tested)               |  [Comments (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/comments_tested.html#L13)
  |        |  │   │      └─  [Comment Description](http://127.0.0.1:8000/testing/comments_tested#comment_description)    |  [ Comment Description (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/comments_tested.html#L27)
  |        |  │   │      └─  [Smaller Comments](http://127.0.0.1:8000/testing/comments_tested#comment_smaller)       |  [Smaller Comments (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/comments_tested.html#L46)
  |        |  │   │      └─  [Comments in Views](http://127.0.0.1:8000/testing/comments_tested#comment_views)      |  [View Comments (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/comments_tested.html#L63)
  |        |  │   │                                 | 
  |  2.2.6 |  │   └─  [Django Include](http://127.0.0.1:8000/testing/)                |  [Django Syntax - Include (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/include_tested.html) 
  |        |  │          │                          |  
  |        |  │          └─  [Include](http://127.0.0.1:8000/testing/include_tested)                |  [Include Tag (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax/include_tested.html#L11)
  |        |  │          └─  [Variables in Include](http://127.0.0.1:8000/testing/include_tested#include_variables)   |  [Include Variables (GitHub)](http://127.0.0.1:8000/testing/include_tested#include_variables)
  |        |  │                                     | 
  |  2.3   |  └─  [Django Querysets](http://127.0.0.1:8000/testing/)                  |  [Django Querysets (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets)
  |        |  │    │                                |
  |  2.3.1 |  │    └─  [Queryset Introduction](http://127.0.0.1:8000/testing/)        |  [Django Querysets - Intro (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_intro.html)
  |        |  │    │     │                          |
  |        |  │    │     └─  [Queryset](http://127.0.0.1:8000/testing/queryset_intro)        |  [Queryset (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_intro.html#L15)
  |        |  │    │     └─  [Query Data](http://127.0.0.1:8000/testing/queryset_intro#query_data)             |  [Query Data (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_intro.html#L26)
  |        |  │    │                                |  
  |  2.3.2 |  │    └─  [Queryset Get](http://127.0.0.1:8000/testing/)                 |  [Django Querysets - Get (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_get.html)
  |        |  │    │     │                          |
  |        |  │    │     └─  [values() method](http://127.0.0.1:8000/testing/queryset_get)        |  [Values Method (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_get.html#L21)
  |        |  │    │     └─  [Specific Columns](http://127.0.0.1:8000/testing/queryset_get#columns)         |  [Return Specific Columns (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_get.html#L58)
  |        |  │    │     └─  [Return Rows](http://127.0.0.1:8000/testing/queryset_get#rows)            |  [Return Specific Rows (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_get.html#L89)
  |        |  │    │                                |  
  |  2.3.3 |  │    └─  [Queryset Filter](http://127.0.0.1:8000/testing/)              |  [Django Querysets - Filter (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_filter.html)
  |        |  │    │     │                          |
  |        |  │    │     └─  [Filter Method](http://127.0.0.1:8000/testing/queryset_filter)       |   [Filter Method (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_filter.html#L15)
  |        |  │    │     └─  [And Method](http://127.0.0.1:8000/testing/queryset_filter#and)        |  [And Method (localhost)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_filter.html#L57)
  |        |  │    │     └─  [Or Method](http://127.0.0.1:8000/testing/queryset_filter#or)         |  [Or Method (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_filter.html#L100)
  |        |  │    │     └─  [Field Lookups](http://127.0.0.1:8000/testing/queryset_filter#field_lookups)          |  [Field Lookups](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_filter.html#L168)
  |        |  │    │                                |  
  |  2.3.4 |  │    └─  [Queryset Order By](http://127.0.0.1:8000/testing/)            |  [Django Querysets - Order By (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_order_by.html)
  |        |  │          │                          |
  |        |  │          └─  [Order By](http://127.0.0.1:8000/testing/queryset_order_by)               |  [Order By (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_order_by.html#L15)
  |        |  │          └─  [Descending Order](http://127.0.0.1:8000/testing/queryset_order_by#descend)       |  [Descending Order (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_order_by.html#L53)
  |        |  │          └─  [Mulitple Order Bys](http://127.0.0.1:8000/testing/queryset_order_by#multiple)     |  [Multiple Order Bys (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets/queryset_order_by.html#L93)
  |        |  │                                     |   
  |        |  │                                     | 
  |  3     |  ├─ [Django Admin](http://127.0.0.1:8000/django_admin/)                       |  [Django Admin Section (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_admin)
  |        |  │  └─ [Django Admin Home](http://127.0.0.1:8000/django_admin/)               |  [Django Admin Home (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/django_admin_refs.html)
  |        |  │     |                               |
  |  3.1   |  │     └─  [Django Admin Tool](http://127.0.0.1:8000/django_admin/admin)       |  [Admin Tool (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/django_admin.html) 
  |  3.2   |  │     └─  [Create User](http://127.0.0.1:8000/django_admin/create_user)                 |  [Admin User (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/create_user.html)
  |  3.3   |  │     └─  [Include Django Models](http://127.0.0.1:8000/django_admin/include_models)       |  [Include Models (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/include_models.html)  
  |  3.4   |  │     └─  [Set List Display](http://127.0.0.1:8000/django_admin/list_display)            |  [List Model Fields (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/set_list_display.html)
  |  3.5   |  │     └─  [Update Members](http://127.0.0.1:8000/django_admin/update_members)              |  [Update Model Records (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/update_members.html)
  |  3.6   |  │     └─  [Add Members](http://127.0.0.1:8000/django_admin/add_members)                 |  [Add Model Record (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/add_members.html)
  |  3.7   |  │     └─  [Delete Members](http://127.0.0.1:8000/django_admin/delete_members)              |  [Delete Model Member (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/delete_members.html)
  |        |  │                                     | 
  |        |  │                                     | 
  |  4     |  ├─ [Django Static](http://127.0.0.1:8000/django_static/)                      |  [Django Static Section (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_static)
  |        |  │  └─ [Django Static Home](http://127.0.0.1:8000/django_static/)              |  [Django Static Home (Github)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_static/django_static_refs.html)
  |        |  │     │                               |
  |  4.1   |  │     └─  [Static Folder and Files](http://127.0.0.1:8000/django_static/files)     |  [Add Static File (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_static/static_files.html)
  |  4.2   |  │     └─  [Install Whitenoise](http://127.0.0.1:8000/django_static/whitenoise)          |  [Install Whitenoise (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_static/install_whitenoise.html)
  |  4.3   |  │     └─  [Collect Static Files](http://127.0.0.1:8000/django_static/collect)        |  [Collect Static (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_static/collect_static.html)
  |  4.4   |  │     └─  [Global Static Files](http://127.0.0.1:8000/django_static/global)        |  [Global Static (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_static/global_static.html)
  |  4.5   |  │     └─  [Add Styles to Project](http://127.0.0.1:8000/django_static/styles)       |  [Project CSS Styles (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_static/project_styles.html)
  |        │  │                                     |
  |        │  │                                     |
  |  5     │  ├─ [Django PostgreSQL](http://127.0.0.1:8000/django_postgreSQL/)                     |  [Django PostgreSQL Section (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql)
  |        |  │  └─ [PostgreSQL Home](http://127.0.0.1:8000/django_postgreSQL/)                    |  [PostgreSQL Home (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql/django_postgresql_refs.html)
  |        |  │     │                               |
  |  5.1   |  │     └─  [PostgreSQL Intro](http://127.0.0.1:8000/django_postgreSQL/intro)            |  [PostgreSQL Intro (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql/postgresql_intro.html) 
  |  5.2   |  │     └─  [Create AWS Account](http://127.0.0.1:8000/django_postgreSQL/AWS)          |  [AWS Account (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql/aws.html)
  |  5.3   |  │     └─  [Create Database in RDS](http://127.0.0.1:8000/django_postgreSQL/RDS)      |  [PostgreSQL Database (Github)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql/rds.html) 
  |  5.4   |        └─  [Connect to Database](http://127.0.0.1:8000/django_postgreSQL/RDS_Connect)         |  [Database Connection (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql/rds_connect.html)
  |  5.5   |   │    └─  [Add Members](http://127.0.0.1:8000/django_postgreSQL/members)                 |  [Database Records (Github)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql/members.html) 
  |        |   │                                    |
  |        |   │                                    |
  |  6     |   ├─ [Django Deployment](http://127.0.0.1:8000/django_deploy/)                     |  [Django Deploy Section (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy)
  |        |   │  └─ [Deployment Home](http://127.0.0.1:8000/django_deploy/)                    |  [Deployment Home (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/django_deploy_refs.html) 
  |        |   │     │                              |
  |  6.1   |   │     └─  [Deployment Provider](http://127.0.0.1:8000/django_deploy/choose_provider)        |  [Choose Provider (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/choose_provider.html)
  |  6.2   |   │     └─  [Create Requirements](http://127.0.0.1:8000/django_deploy/requirements)        |  [Requirements (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/requirements.html)
  |  6.3   |   │     └─  [Create django.config](http://127.0.0.1:8000/django_deploy/config)       |  [Django Config (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/django_config.html)
  |  6.4   |   │     └─  [Create Django .zip File](http://127.0.0.1:8000/django_deploy/zip)         |  [Zip File (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/django_zip.html)
  |  6.5   |   |     └─  [Deploy with Elastic Beanstalk](http://127.0.0.1:8000/django_deploy/deploy_eb)   |  [Elastic Beanstalk (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/deploy_eb.html)
  |  6.6   |   |     └─  [Update Django Project](http://127.0.0.1:8000/django_deploy/update_project)      |  [Update Django Project](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/update_django_project.html)
  |        |   │                                    |
  |        |   │                                    |
  |  7     |   ├─ [More Django](http://127.0.0.1:8000/django_more/)                       |  [Django More](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_more)
  |        |   │  └─ [More Django Home](http://127.0.0.1:8000/django_more/)               |  [More Django Home (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_more/django_more_refs.html)
  |        |   │     │                              |
  |  7.1   |   │     └─  [Django Slug Field](http://127.0.0.1:8000/django_more/slug)          |  [Slug (GitHub)](http://127.0.0.1:8000/django_more/slug)
  |  7.2   |   │     └─  [Add Bootstrap 5](http://127.0.0.1:8000/django_more/bootstrap)            |  [Boostrap 5 (GitHub)](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_more/bootstrap.html)
  |        |   │                                    |
  |        |   │                                    | 
  |  8     |   ├─ Django References                 |  [Django Refs (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs)
  |        |   │  │                                 |
  |  8.1   |   │  └─  [Template Tag](http://127.0.0.1:8000/template/)                  |  [Template Tags (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs/templatee)  
  |  8.2   |   │  └─  [Filter Keywords](http://127.0.0.1:8000/filter/)                        |  [Filter (Github](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs/filter)
  |  8.3   |   │  └─  [Field Lookup Keywords](http://127.0.0.1:8000/field/)              |  [Field Lookups (GitHub)](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs/field)


- **Future Enchancements**

  1st Intro version
  - Modularize views.py: As the number of views increases, the current single views.py file will be refactored into multiple modular views files (e.g., setup_views.py, display_views.py, admin_views.py) within a dedicated views/ folder. This will improve maintainability, readability and separation of concerns across different sections of Django app.

  2nd Intro version  
  As number of views in project increases, I plan to refactor current `views.py` file into separate, modular files (e.g., setup_views.py, display_views.py, admin_views.py) stored within a views/ folder. This will make codebase easier to navigate and maintain. 

  3rd Intro version
  combined paragraph for views and urls:

  As the number of views and URL routes in the project grows, I plan to refactor the existing views.py and urls.py files into modular files (e.g., django_setup_views.py, display_views.py, admin_views.py, and corresponding django_setup_urls.py, etc.). These will be organized into dedicated views/ and urls/ folders, improving code clarity and maintainability as the application scales.

  4th Intro version
  As the number of views and URL routes in the project grows, I plan to refactor the existing views.py and urls.py files.

  Views can be separated into files such as django_setup_views.py, display_views.py, and admin_views.py, while URLs can be organized into files like django_setup_urls.py. This modular approach keeps related logic grouped together.

  These files will be stored in dedicated views/ and urls/ folders to improve code clarity and maintainability as the application scales. Clarity comes from having less code in each file, making it easier to read, while maintainability improves because updates are more isolated and manageable.


  5th (Final) Intro version  (I thought this maybe best version)
  As the number of views and URL routes grow, I plan to refactor the existing views.py and urls.py files into smaller, modular files such as django_setup_views.py, display_views.py, and django_setup_urls.py.

  These will be organized into dedicated views/ and urls/ folders to improve clarity and maintainability. Having less code in each file makes it easier to read, and more manageable to update as the project scales. 


  Planned technical enhancements include:

  - Restructure Home Page, for a more clearer introduction on website learning purpose. 
  - Add `slug` fields to improve URL structure and enable dynamic routing
  - Style project using CSS (Bootstrap 5) for consistent and repsonsive layouts
  - Use Whitenoise to manage static file handling in production
  - Implement responsive design for mobile and tablet screen sizes
  - Replace SQLite3 with PostgreSQL for improved scalability and performance
  - Use AWS to host Django project and PostgreSQL database
  - Add a `requirements.txt` file to track Python dependencies
  - Add a `.ebextensions/django.config` file to configure for elastic Beanstalk
  - Deploy website using Elastic Beanstalk 

  These enhancements aim to elevate the project from a local development prototype to a scalable, secure, and production-ready web application.


- **W3Schools Django Project Goals**

  Original Project Goals version

  - Expand upon W3Schools Django tutorial with clearer examples and practical enhancements
  - Build a functioning Django website that incorporates models, forms and URL routing
  - Practice structuring a Django project for scalability and future production deployment
  - Prepare site for online hosting, including static file management and environment configuration
  - Demonstrate understanding of full-stack development without using JavaScript frameworks


  Changed Version that has an introduction before bullet points

  I created this project to understand the full Django stack and practice deploying a real site online. The aim was to build a learning website that closely follows the W3Schools Django tutorial, while adding practical improvements that make it more useful in real-world development.

  - Follow and extend the W3Schools Django tutorial with clearer examples and more complete project structure
  - Add improvements such as better form handling, responsive design, and template reuse
  - Develop and test a scalable project in a virtual environment with SQLite3 and Django models
  - Demonstrate full-stack Django development using Python, HTML, and Django’s templating system — without relying on JavaScript frameworks, to better understand how dynamic sites can be built using Django alone

  Last bullet point without em dash
  - Demonstrate full-stack Django development using Python, HTML, and Django’s templating system, without relying on 
    JavaScript frameworks to better understand how dynamic sites can be built using Django alone

  Slighly Shorter version of last bullet point
  - Demonstrate Django full-stack development using Python, HTML, and its templating system, without relying on     JavaScript frameworks  