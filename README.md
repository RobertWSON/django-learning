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


## 🧭 Django Learning Roadmap (Before (With) Setup Instructions)

  I recommend to get familiar with how Django works and how it is setup, have a read over links up to 1.7 Django View below.
       
  Note: localhost will not be able to be used until 1.8 Django URL   
 
  Setup Instructions that follow after this part of learning roadmap, cover most important parts to consider with Django setup. 
  Please also read this as well, carefully before setting up Django project.


  | Step   | Topic                                  |      Links
  |--------|----------------------------------------|--------------------------- 
  |  1     |  Django Setup                          |  [Django Setup](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/)
  |        |                                        |  [django_setup_refs.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_setup_refs.html) 
  |        |                                        |
  |  1.1   |    └─  Django Intro                    |  [django_intro.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_intro.html)  

  |  1.2   |    └─  Django Get Started              |  [django_get_started.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_get_started.html) 

  |  1.3   |    └─  Virtual Environment             |  [django_virtual_env.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_virtual_env.html)

  |  1.4   |    └─  Install Django                  |  [django_install.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_install.html) 

  |  1.5   |    └─  Django Project                  |  [django_project.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_project.html)

  |  1.6   |    └─  Django App                      |  [django_app.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_app.html)

  |  1.7   |    └─  Django View                     |  [django_views.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_views.html)

  |  1.8   |    └─  Django URL                      |  [django_url.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_url.html)
  |        |                                        |  [Django URL (localhost)](http://127.0.0.1:8000/django_setup/url)         
  |        |                                        | 
  |  1.9   |    └─  Django Template                 |  [django_template.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_template.html)
  |        |                                        |  [Django Template (localhost)](http://127.0.0.1:8000/django_setup/template)         
  |        |                                        | 
  |  1.10  |    └─  Django Model                    |  [django_model.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_model.html)
  |        |                                        |  [Django Model (localhost)](http://127.0.0.1:8000/django_setup/model)         
  |        |                                        | 
  |  1.11  |    └─  Django Insert Data              |  [django_insert_data.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_insert_data.html)
  |        |                                        |  [Django Insert Data (localhost)](http://127.0.0.1:8000/django_setup/insert_data)         
  |        |                                        | 
  |  1.12  |    └─  Django Update Data              |  [django_update_data.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_update_data.html)
  |        |                                        |  [Django Update Data (localhost)](http://127.0.0.1:8000/django_setup/update_data)                                      |
  |        |                                        |
  |  1.13  |    └─  Django Delete Data              |  [django_delete_data.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_delete_data.html)
  |        |                                        |  [Django Delete Data (localhost)](http://127.0.0.1:8000/django_setup/delete_data)                                      |
  |        |                                        |
  |  1.14  |    └─  Django Update Model             |  [django_update_model.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_setup/django_update_model.html)
  |        |                                        |  [Django Update Data (localhost)](http://127.0.0.1:8000/django_setup/update_data) 
  

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


  | Step   | Topic                                  |      Links
  |--------|----------------------------------------|---------------------------                 |     
  |  2     |  Django Code Examples                  |  [Testing Django Examples - template.html](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing)
  |        |                                        |  [Testing Django Examples (localhost)](http://127.0.0.1:8000/testing/)
  |        |                                        |  
  |  2.1   |    └─  Display Data (includes Forms)   |  [display_data](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing/display_data)
  |        |                                        |  [Display Data (localhost)](http://127.0.0.1:8000/testing/)
  |        |                                        |
  |        |       └─  Prepare Template             |  [Prepare Template (localhost)](http://127.0.0.1:8000/testing/prepare_template)  
  |        |       └─  Prepare Django View          |  [Prepare Django View (localhost)](http://127.0.0.1:8000/testing/prepare_template#prepare_view)  
  |        |       └─  Add Link to Details          |  [Add Link to Details (localhost)](http://127.0.0.1:8000/testing/details_link)
  |        |       └─  Add Details View             |  [Add Details View (localhost)](http://127.0.0.1:8000/testing/details_link#details_view)
  |        |       └─  Add Master Template          |  [Add Master Template (localhost)](http://127.0.0.1:8000/testing/master_template)
  |        |       └─  Add Main Index Page          |  [Add Main Index Page (localhost)](http://127.0.0.1:8000/testing/main_page)
  |        |       └─  Django 404 Template          |  [Django 404 (localhost)](http://127.0.0.1:8000/testing/django_404)
  |        |       └─  Add Test View                |  [Django Test View (localhost)](http://127.0.0.1:8000/testing/add_test_view)
  |        |       └─  Django Forms                 |  [Django Forms (localhost)](http://127.0.0.1:8000/testing/django_forms)
  |        |                                        | 
  |  2.2   |    Django Syntax                       |  [django_syntax](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_syntax)
  |        |                                        |
  |  2.2.1 |       └─  Django Variables             |  [Django Syntax - Django Variables (localhost)](http://127.0.0.1:8000/testing/) 
  |        |                                        |  
  |        |             └─  Django Variable        |  [Django Variable(localhost)](http://127.0.0.1:8000/testing/variables_tested)
  |        |             └─  View Variable          |  [View Variable (localhost)](http://127.0.0.1:8000/testing/variables_tested#view)
  |        |             └─  Template Variable      |  [Template Variable (localhost)](http://127.0.0.1:8000/testing/variables_tested#template) 
  |        |             └─  Data from a Model      |  [Model Data (localhost)](http://127.0.0.1:8000/testing/variables_tested#model_data)
  |        |                                        |
  |  2.2.2 |       └─  Django Tags                  |  [Django Syntax - Django Tags (localhost)](http://127.0.0.1:8000/testing/) 
  |        |                                        |  
  |        |             └─  Template Tags          |  [Template Tags (localhost)](http://127.0.0.1:8000/testing/tags_tested)
  |        |             └─  Django Code            |  [Django Code (localhost)](http://127.0.0.1:8000/testing/tags_tested#django_code)
  |        |                                        | 
  |  2.2.3 |       └─  Django If Else               |  [Django Syntax - Django If Else (localhost)](http://127.0.0.1:8000/testing/) 
  |        |                                        |  
  |        |             └─  If Statement           |  [If Statemet (localhost)](http://127.0.0.1:8000/testing/if_tested)
  |        |             └─  Elif Statement         |  [ElIf Statemet (localhost)](http://127.0.0.1:8000/testing/if_tested#elif)
  |        |             └─  Else Statement         |  [Else Statemet (localhost)](http://127.0.0.1:8000/testing/if_tested#else)
  |        |             └─  Operator Dropped       |  [Operator Dropped (localhost)](http://127.0.0.1:8000/testing/if_tested#drop_operator)
  |        |             └─  Operator ==            |  [Operator == (localhost)](http://127.0.0.1:8000/testing/if_tested#==_operator)
  |        |             └─  Operator !=            |  [Operator != (localhost)](http://127.0.0.1:8000/testing/if_tested#!=_operator)
  |        |             └─  Operator <             |  [Operator < (localhost)](http://127.0.0.1:8000/testing/if_tested#<_operator)
  |        |             └─  Operator <=            |  [Operator <= (localhost)](http://127.0.0.1:8000/testing/if_tested#<=_operator)
  |        |             └─  Operator >             |  [Operator > (localhost)](http://127.0.0.1:8000/testing/if_tested#>_operator)
  |        |             └─  Operator >=            |  [Operator >= (localhost)](http://127.0.0.1:8000/testing/if_tested#>=_operator)
  |        |             └─  Operator and           |  [Operator and (localhost)](http://127.0.0.1:8000/testing/if_tested#and_operator)
  |        |             └─  Operator or            |  [Operator and (localhost)](http://127.0.0.1:8000/testing/if_tested#or_operator)
  |        |             └─  Operator and / or      |  [Operator and / or (localhost)](http://127.0.0.1:8000/testing/if_tested#and-or_operator)
  |        |             └─  Operator not in        |  [Operator not in (localhost)](http://127.0.0.1:8000/testing/if_tested#not-in_operator)
  |        |             └─  Operator is            |  [Operator and (localhost)](http://127.0.0.1:8000/testing/if_tested#is_operator)
  |        |             └─  Operator == replace is |  [Operator == replace is (localhost)](http://127.0.0.1:8000/testing/if_tested#==replace_is_operator)
  |        |             └─  Operator is & with     |  [Operator and (localhost)](http://127.0.0.1:8000/testing/if_tested#if_is_&_with_operator)
  |        |             └─  Operator is not        |  [Operator and (localhost)](http://127.0.0.1:8000/testing/if_tested#is-not_operator)
  |        |                                        | 
  |  2.2.4 |       └─  Django For Loop              |  [Django Syntax - Django For Loop (localhost)](http://127.0.0.1:8000/testing/) 
  |        |                                        |  
  |        |             └─  For Loops              |  [For Loops (localhost)](http://127.0.0.1:8000/testing/for_loop_tested)
  |        |             └─  Data From a Model      |  [Model Data (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#model_data)
  |        |             └─  Reversed               |  [Reversed (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#reversed)
  |        |             └─  Empty an Empty Object  |  [Empty and Empty Object (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#empty)
  |        |             └─  Empty No Object        |  [Empty No Object (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#empty_noobject)
  |        |             └─  forloop.counter        |  [For Loop Counter (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#counter)
  |        |             └─  forloop.counter0       |  [For Loop Counter0 (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#counter0)
  |        |             └─  forloop.first          |  [For Loop First (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#first)
  |        |             └─  forloop.last           |  [For Loop Last (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#last)
  |        |             └─  forloop.parentloop     |  [For Loop Parent (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#parent)
  |        |             └─  forloop.revcounter     |  [For Loop Last (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#revcounter)
  |        |             └─  forloop.revcounter0    |  [For Loop Parent (localhost)](http://127.0.0.1:8000/testing/for_loop_tested#revcounter0)
  |        |                                        | 
  |  2.2.5 |       └─  Django Comment               |  [Django Syntax - Django Comment (localhost)](http://127.0.0.1:8000/testing/) 
  |        |                                        |  
  |        |             └─  Comments               |  [For Loops (localhost)](http://127.0.0.1:8000/testing/comments_tested)
  |        |             └─  Comment Description    |  [Model Data (localhost)](http://127.0.0.1:8000/testing/comments_tested#comment_description)
  |        |             └─  Smaller Comments       |  [For Loops (localhost)](http://127.0.0.1:8000/testing/comments_tested#comment_smaller)
  |        |             └─  Comments in Views      |  [Model Data (localhost)](http://127.0.0.1:8000/testing/comments_tested#comment_views)
  |        |                                        | 
  |  2.2.6 |       └─  Django Include               |  [Django Syntax - Django Include (localhost)](http://127.0.0.1:8000/testing/) 
  |        |                                        |  
  |        |             └─  Include                |  [For Loops (localhost)](http://127.0.0.1:8000/testing/include_tested)
  |        |             └─  Variables in Include   |  [Model Data (localhost)](http://127.0.0.1:8000/testing/include_tested#include_variablesn)
  |        |                                        | 
  |  2.3   |    └─  Django Querysets                |  [django_querysets](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/testing/django_querysets)
  |        |                                        |  [Django Querysets (localhost)](http://127.0.0.1:8000/testing/)
  |        |                                        |
  |  2.3.1 |       └─  Queryset Introduction        |  [Django Querysets - Queryset Intro (localhost)](http://127.0.0.1:8000/testing/)
  |        |                                        |
  |        |             └─  Django Queryset        |  [Django Queryset (localhost)](http://127.0.0.1:8000/testing/queryset_intro)
  |        |             └─  Query Data             |  [Query Data (localhost)](http://127.0.0.1:8000/testing/queryset_intro#query_data)
  |        |                                        |  
  |  2.3.2 |       └─  Queryset Get                 |  [Django Querysets - Queryset Get (localhost)](http://127.0.0.1:8000/testing/)
  |        |                                        |
  |        |             └─  values() method        |  [Values Method (localhost)](http://127.0.0.1:8000/testing/queryset_get)
  |        |             └─  Return Columns         |  [Return Specific Columns (localhost)](http://127.0.0.1:8000/testing/queryset_get#columns)
  |        |             └─  Return Rows            |  [Return Specific Rows (localhost)](hhttp://127.0.0.1:8000/testing/queryset_get#rows)
  |        |                                        |  
  |  2.3.3 |       └─  Queryset Filter              |  [Django Querysets - Queryset Filter (localhost)](http://127.0.0.1:8000/testing/)
  |        |                                        |
  |        |             └─  Queryset Filter        |  [Filter (localhost)](http://127.0.0.1:8000/testing/queryset_filter)
  |        |             └─  Filter with And        |  [Queryset Filter with And (localhost)](http://127.0.0.1:8000/testing/queryset_filter#and)
  |        |             └─  Filter with Or         |  [Queryset Filter with Or (localhost)](http://127.0.0.1:8000/testing/queryset_filter#or)
  |        |             └─  Field Lookups          |  [Field Lookups](http://127.0.0.1:8000/testing/queryset_filter#field_lookups)
  |        |                                        |  
  |  2.3.4 |       └─  Queryset Order By            |  [Django Querysets - Queryset Set (localhost)](http://127.0.0.1:8000/testing/)
  |        |                                        |
  |        |             └─  Order By        |      [  [Order By (localhost)](http://127.0.0.1:8000/testing/queryset_order_by)
  |        |             └─  Descending Order       |  [Descending Order (localhost)](http://127.0.0.1:8000/testing/queryset_order_by#descend)
  |        |             └─  Mulitple Order Bys     |  [Multiple Order Bys (localhost)](http://127.0.0.1:8000/testing/queryset_order_by#multiple)
  |        |                                        |   
  |        |                                        | 
  |  3     |  Django Admin                          |  [Django Admin Section](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_admin)
  |        |                                        |  [django_admin_refs.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_admin/django_admin_refs.html) 
  |        |                                        |  [Django Admin Section (localhost)](http://127.0.0.1:8000/django_admin/)
  |        |                                        |
  |  3.1   |    └─  Django Admin                    |  [Django Admin (localhost)](http://127.0.0.1:8000/django_admin/admin)
  |        |                                        | 
  |  3.2   |    └─  Create User                     |  [Create Django Admin User (localhost)](http://127.0.0.1:8000/django_admin/create_user)

  |  3.3   |    └─  Include Models                  |  [Include Django Models (localhost)](http://127.0.0.1:8000/django_admin/include_models)
  
  |  3.4   |    └─  Set List Display                |  [Set Model Fields to Display (localhost)](http://127.0.0.1:8000/django_admin/list_display)

  |  3.5   |    └─  Update Members                  |  [Update Model Members (localhost)](http://127.0.0.1:8000/django_admin/update_members)

  |  3.6   |    └─  Add Members                     |  [Add a Model Member (localhost)](http://127.0.0.1:8000/django_admin/add_members)

  |  3.7   |    └─  Delete Members                  |  [Delete a Model Member (localhost)](http://127.0.0.1:8000/django_admin/delete_members)
  |        |                                        | 
  |        |                                        | 
  |  4     |  Django Static                         |  [Django Static](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_static)
  |        |                                        |  [django_static_refs.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_static/django_static_refs.html)
  |        |                                        |  [Django Static (localhost)](http://127.0.0.1:8000/django_static/) 
  |        |                                        |
  |  4.1   |    └─  Django Static Folder and Files  |  [Django - Add Static File (localhost)](http://127.0.0.1:8000/django_static/files)

  |  4.2   |    └─  Install Whitenoise              |  [Django - Installing Whitenoise (localhost)](http://127.0.0.1:8000/django_static/whitenoise)

  |  4.3   |    └─  Collect Static Files            |  [Django - Global Static Files (localhost)](http://127.0.0.1:8000/django_static/global)
  |        |                                        |
  |  4.4   |    └─  Add Styles to Project           |  [Add Styles with CSS Files to Django Project (localhost)](http://127.0.0.1:8000/django_static/styles)
  |        |                                        |
  |        |                                        |
  |  5     |  Django PostgreSQL                     |  [Django PostgreSQL](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql)
  |        |                                        |  [django_postgresql_refs.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_postgresql/django_postgresql_refs.html)
  |        |                                        |  [PostgreSQL with Django (localhost)](http://127.0.0.1:8000/django_postgreSQL/)
  |        |                                        |
  |  5.1   |    └─  PostgreSQL Intro                |  [Introduction to PostgreSQL (localhost)](http://127.0.0.1:8000/django_postgreSQL/intro)
  |        |                                        | 
  |  5.2   |    └─  Create AWS Account              |  [Create AWS Account (localhost)](http://127.0.0.1:8000/django_postgreSQL/AWS)
  |        |                                        | 
  |  5.3   |    └─  Create Database in RDS          |  [Create PostgreSQL Database in RDS (localhost)](http://127.0.0.1:8000/django_postgreSQL/RDS)
  |        |                                        | 
  |  5.4   |    └─  Connect to Database             |  [Connect to PostgreSQL Database (localhost)](http://127.0.0.1:8000/django_postgreSQL/RDS_Connect)
  |        |                                        |  
  |  5.5   |    └─  Add Members                     |  [PostgreSQL - Add Members (localhost)](http://127.0.0.1:8000/django_postgreSQL/members) 
  |        |                                        |
  |        |                                        |
  |  6     |  Django Deployment                     |  [Django Deployment](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy)
  |        |                                        |  [django_deploy_refs.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_deploy/django_deploy_refs.html)
  |        |                                        |  [Deploy Django (locahost)](http://127.0.0.1:8000/django_deploy/)   
  |        |                                        |
  |  6.1   |    └─  Deployment Provider             |  [Choose Provider](http://127.0.0.1:8000/django_deploy/choose_provider)

  |  6.2   |    └─  Create Requirements             |  [Create Requirements](http://127.0.0.1:8000/django_deploy/requirements)

  |  6.3   |    └─  Create django.config            |  [Create Django Config](http://127.0.0.1:8000/django_deploy/config)

  |  6.4   |    └─  Create Django .zip File         |  [Create zip File](http://127.0.0.1:8000/django_deploy/zip)

  |  6.5   |    └─  Deploy with Elastic Beanstalk   |  [Deploy with Elastic Beanstalk](http://127.0.0.1:8000/django_deploy/deploy_eb)

  |  6.6   |    └─  Update Django Project           |  [Update Django Project](http://127.0.0.1:8000/django_deploy/update_project)
  |        |                                        |
  |        |                                        |
  |  7     |  More Django                           |  [Django More](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_more)
  |        |                                        |  [django_more_refs.html](https://github.com/RobertWSON/django-learning/blob/main/W3Schools-Django/my_tennis_club/members/templates/django_more/django_more_refs.html)
  |        |                                        |  [Django More (localhost)](http://127.0.0.1:8000/django_more/) 
  |        |                                        |
  |  7.1   |    └─  Django Slug Field               |  [Slug (localhost)](http://127.0.0.1:8000/django_more/slug)
  |        |                                        | 
  |  7.2   |    └─  Add Bootstrap 5                 |  [boostrap 5 (localhost)](http://127.0.0.1:8000/django_more/bootstrap)
  |        |                                        |
  |        |                                        | 
  |  8     |  Django References                     |  [django_refs](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs)
  |        |                                        |
  |  8.1   |    └─  Template Tag                    |  [template](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs/template)
  |        |                                        |  [Template Tags (localhost)](http://127.0.0.1:8000/template/) 
  |        |                                        | 
  |  8.2   |    └─  Filter                          |  [filter](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs/filter)
  |        |                                        |  [Filter Tags (localhost)](http://127.0.0.1:8000/filter/) 
  |        |                                        |
  |  8.3   |    └─  Field Lookups                   |  [field](https://github.com/RobertWSON/django-learning/tree/main/W3Schools-Django/my_tennis_club/members/templates/django_refs/field)
  |        |                                        |  [Field Lookups Tags (localhost)](http://127.0.0.1:8000/field/)


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