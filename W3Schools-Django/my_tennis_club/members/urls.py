# Original 2 imports below, created in URLs, within (9 Django URLs) of Django Tutorial Section
# are originally used with members url 
# Note: URL is a Uniform Resource Locator, used for web addresses
from django.urls import path
# Here we are using a django.urls module for urls, to import a path library for path() function below
# see fulstackpython.com/django-urls-path-examples.html, javatpoint.com/django-url-mapping
# and blog.devgenius.io/django-urls-d59f38b6e3cb
from . import views
# Here . (single dot) is a convention from command line applications. 
# Single dot means current directory (or module/package) of file that is used to get what we need.
# Imports that use this single dot ( . ) syntax are called relative imports.
# in this case views file (views.py) is in same directory (folder) as this urls.py file, so we use a dot. 
# We are using views.py as a relative import to get what we need for url routes.   
# see stackoverflow.com/questions/44262586/django-tutorial-from-import-views
# found from "from django from . import views" google search


urlpatterns = [
    
    # To help understand path functions in urlpatterns I have found a website.
    # From https://www.meetgor.com/django-basics-views-urls/ , breaking down path function in URLpatterns,
    # it shows that '' is url path, views is a function_name (with . showing that view is within views.py file
    # and in same directory as urls.py) and name is a url name.
    
    # Add URL, within Django Add Main Index Page (19 Django - Add Main Index Page) of Django Display Data Section 
    # Now we need to make sure that root url points to correct main view (for Home Page).
    # Add a path to make sure that root url (for Home Page) points to main view. 
    # Here '' is root url path for home page, views.main a function_name (is main within views.py file)
    # and because url does not have a name in it eg '', we have decided to give it main as a name.
    
    # comment code for now  
    path('', views.main, name='main'),
    
    # URLs, within (9 Django URLs) of Django Tutorial Section
    # Original members path below makes sure that members url points to members view
    # Here 'members/' is url path, views.name a function_name (is members within views.py file)
    # and name has members as a url name. 
    
    
    # Add a hello path for a url that will is used for displaying just Hello World!
    # Note: I do not need name='first' for this tour for some reason. I need to research to find out why. 
    path('hello/', views.hello, name='hello'),
    
    # Add a first path for a url that will be used for displaying Hello World! 
    # and Welcome to my first Django project! below. I think this is a better way to approach as it keeps
    # members separate.
    # Note: I do not need name='first' for this tour for some reason. I need to research to find out why.
    #path('first/', views.first, name='first'),
    #I have found that first is also used in Django Reference Section for templates,
    #so I have to give this a different name
    path('first_django_page/', views.first_django_page, name="first_page"),
    
    
    # For handling Prepare Template and View Page I will use a testing//prepare_template url
    # This is for Django Prepare Template (16 Prepare Template & View) of Display Data Section.
    path('testing/prepare_template', views.prepare_template, name='prepare_template'),
    
    
    # comment code for now    
    path('members/', views.members, name='members'),
    
    # Add URLs, within Django Add Link to Details (17 Django - Add Link to Details ) of Django Display Data Section
    # Now we need to make sure that /details/ url points to correct details view, with id as a parameter.
    # Here # 'members/details/ part of url points to correct details view for a member.
    # # <int:id> is a path converter that matches zero or a positive integer, hence int.
    # In this case positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # and stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat 
    # Here views a function_name (is details within views.py file) and name has details in url name.
    # Note: url is members/details, so details name comes after members for a member.
    
    # comment code for now  
    path('members/details/<int:id>', views.details, name='details'), 
    
    
    # URLs, within Django Add Test View (21 Django - Add Test View) of Django Display Data Section
    # When testing different aspects of Django, it can be a good idea to have somewhere to test code 
    # without destroying main project. URL path below is only used for testing purposes. 
    # We have to make sure that incoming urls to /testing/ will be redirected to testing view
    # Here 'testing/' is url path, views.testing a function_name (is testing within views.py file)
    # and name has testing as a url name. 
   
    
    # comment code for now
     # Add path to make sure that testing url (just for testing purposes) points to testing view 
    path('testing/', views.testing, name='testing'),
    
    
    #Django Syntax Section
    
    # Django Tags Section 
    path('testing/tags_tested', views.tags_tested, name='tags_tested'),
    
    #path('testing/tags_tested', views.django_code, name='django_code'),
    
    # Django If Tag
    path('testing/if_tested', views.if_tested, name='if_tested'),
    
    # path('testing/if_tested', views.if_elif, name='if_elif'),
    
    # path('testing/if_tested', views.if_else, name='if_else'),
    
    # path('testing/if_tested', views.if_drop_operator, name='if_drop_operator'),

    # path('testing/if_tested', views.if_==_operator, name='if_==_operator'),
    
    # path('testing/if_tested', views.if_!=_operator, name='if_!=_operator'),
    
    # path('testing/if_tested', views.if_<_operator, name='if_<_operator'),
    
    # path('testing/if_tested', views.if_<=_operator, name='if_<=_operator'),
    
    # path('testing/if_tested', views.if_>_operator, name='if_>_operator'),
    
    # path('testing/if_tested', views.if_>=_operator, name='if_>=_operator'),
    
    # path('testing/if_tested', views.if_and_operator, name='if_and_operator'),
    
    # path('testing/if_tested', views.if_or_operator, name='if_or_operator'),
    
    # path('testing/if_tested', views.if_and_operator, name='if_and-or_operator'),
    
    # path('testing/if_tested', views.if_in_operator, name='if_in_operator'),
    
    # path('testing/if_tested', views.if_not-in_operator, name='if_not-in_operator'),
    
    # path('testing/if_tested', views.if_is_operator, name='if_is_operator'),
    
    # path('testing/if_tested', views.if_==_replace_is_operator, name='if_==replace_is_operator'),
    
    # path('testing/if_tested', views.if_is_&_with_operator, name='if_is_&_with_operator'),
    
    # path('testing/if_tested', views.if_is-not_operator, name='if_is-not_operator'),
    
    
    # Django For Loops
    path('testing/for_loop_tested', views.for_loop_tested, name='for_loop_tested'),
    
    path('testing/for_loop_tested', views.for_loop_dict, name='for_loop_dict'),
    
    path('testing/for_loop_tested', views.for_loop_modeldata, name='for_loop_modeldata'),
    
    #path('testing/for_loop_tested', view )
    
    
    # Django Comment Section
    
    path('testing/comments_tested', views.comments_tested, name='comments'),
    
    path('testing/comments_tested', views.comment_views, name='comment_views'),
    
    #Route for Django Include Tag
    # Do not use this route below for Django Syntax section
    # path('testing/include', views.include, name='template'),
    
    # Use this route for Django Syntax include section.
    path('testing/include_tested', views.include_tested, name='include_tested'),
    
    
    # I do not need path code for this below, but I may need description for understanding on what these paths do. 
    # , so I will Comment it out for now. 
    
    # "/details/ url points to correct details view with id as a parameter" 
    # <int:id> is a path converter that matches zero or a positive integer. 
    # In this case the positive integer is an id. see docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
    # Also see stackoverflow.com/questions/57993808/what-difference-it-makes-when-using-intid-instead-of-slug-in-url-pat
    #path('members/details/<int:id>', views.details, name='details'),
    
   
    
    
    # Add Routes for Django References Section
    # Template Tag Reference 
    path('template/', views.template, name='template'),
    
    # Temporary Route, to see if I can get a few Tag reference along with its example showing on a page. #
    # Remove 2 autoescape routes for Autoescape on and off.
    #path('template/autoescape', views.autoescape_off, name='autoescape'), 
    #path('template/autoescape', views.autoescape_on, name='autoescape'), 
    
    # Only need one route for autoescape because it can be used for both examples in same page.
    path('template/autoescape', views.autoescape, name="autoescape"),

    # Django Template Block Tag Page
    path('template/block', views.block, name='block'),
    # Need to use blockchild view for using child template
    path('template/block', views.blockchild, name='blockchild'),
    
    # Page with Comment Examples
    path('template/comment', views.comment, name='comment'),
    
    path('template/cycle', views.cycle, name='cycle'),    
    
    path('template/extends', views.extends, name='extends'),    
    
    path('template/extends_example', views.extends_example, name='extends_example'),
    
    # Filter Template Tag Example 
    path('template/filter_tag', views.filter_tag, name='filter_tag'),
    
    path('template/firstof', views.firstof, name='firstof'),    
    
    #path('template/for', views.for, name='for'),    
    
    #path('template/if', views.if, name='if'),
    
    #path('template/ifchanged', views.ifchanged, name='ifchanged'),   
    
    path('template/include', views.include, name='include'),
    
    # lorem tag inserts a specified amount of random text.
    path('template/lorem', views.lorem, name='lorem'),
    
    #now tag inserts current date and/or time, according to specific format.
    path('template/now', views.now, name='now'),
    
    path('template/regroup', views.regroup, name='regroup'),
    
    path('template/resetcycle', views.resetcycle, name='resetcycle'),
    
    
    # Spaceless Tag used for removing whitespace between HTML tags
    path('template/spaceless', views.spaceless, name='spaceless'),
    
    path('template/templatetag', views.templatetag, name='templatetag'),
    
    path('template/verbatim', views.verbatim, name='verbatim'),
    
    # For displaying with page link
    #path('template/with', views.with, name='with'),
    path('template/with', views.with_template, name='with_template'),
    
    
    # Filter Reference
    path('filter/', views.filter, name='filter'),
    
    # Temporary Route, to see if I can get Tag reference along with its example showing on a page.  #
    path('filter/add', views.add, name='add'),
    # Add Check not working just yet
    #path('filter/add', views.addcheck, name='addcheck'),
    path('filter/add', views.add_example2, name='add_example2'),
    
    path('filter/add', views.add_example3, name='add_example3'),
    
    
    path('filter/addslashes', views.addslashes, name='addslashes'),
    
    path('filter/capfirst', views.capfirst, name='capfirst'),
    
    path('filter/center', views.center, name='center'),
    
    path('filter/cut', views.cut, name='cut'),
    
    path('filter/default', views.default, name='default'),
    
    path('filter/default_if_none', views.default_if_none, name='default_if_none'),
    
    path('filter/dictsort', views.dictsort, name='dictsort'),
    
    path('filter/dictsortreversed', views.dictsortreversed, name='dictsortreversed'),
    
    path('filter/divisibleby', views.divisibleby, name='divisibleby'),
    
    path('filter/escape', views.escape, name='escape'),
    
    path('filter/escapejs', views.escapejs, name='escapejs'),
    
    path('filter/filesizeformat', views.filesizeformat, name='filesizeformat'),
    
    # Used first to display first item of an object
    path('filter/first', views.first, name='first'),
    
    # Also use first for displaying first character of a string in an object
    path('filter/first', views.first_example2, name='first_example2'),
    
    path('filter/floatformat', views.floatformat, name='floatformat'),
    
    path('filter/floatformat', views.floatformat_example2, name='floatformat_example2'),
    
    path('filter/floatformat', views.floatformat_example3, name='floatformat_example3'),
    
    path('filter/floatformat', views.floatformat_example4, name='floatformat_example4'),
    
    path('filter/get_digit', views.get_digit, name='get_digit'),
    
    path('filter/join', views.join, name='join'),
    
    path('filter/json_script', views.json_script, name='json_script'),
    
    path('filter/last', views.last, name='last'),
    
    # This is used with include for example 2
    path('filter/last', views.last_example2, name='last_example2'),
    
    path('filter/length', views.length, name='length'),

    path('filter/length', views.length_example2, name='length_example2'),

    # This is used with include for example 2
    path('filter/length', views.length_example2, name='length_example2'),

    path('filter/length_is', views.length_is, name='length_is'),
    
    path('filter/length_is', views.length_is_example2, name='length_is_example2'),
    
    path('filter/linebreaks', views.linebreaks, name='linebreaks'),
    
    path('filter/linebreaksbr', views.linebreaksbr, name='linebreaksbr'),
    
    path('filter/linenumbers', views.linenumbers, name='linenumbers'),
    
    path('filter/ljust', views.ljust, name="ljust"),
    
    path('filter/lower', views.lower, name="lower"),
    
    path('filter/make_list', views.make_list, name="make_list"),
    
    path('filter/phone2numeric', views.phone2numeric, name="phone2numeric"),
    
    path('filter/pluralize', views.pluralize, name='pluralize'),
    
    path('filter/random', views.random, name='random'),
    
    path('filter/rjust', views.rjust, name='rjust'),
    
    path('filter/slice', views.slice, name='slice'),
    
    path('filter/slugify', views.slugify, name='slugify'),
    
    # This is used with include for example 2
    path('filter/slugify', views.slugify_example2, name='slugify_example2'),
    
    path('filter/striptags', views.striptags, name='striptags'),
    
    # Need to import datetime in views.py to make this work
    path('filter/time', views.time, name='time'),
    
    path('filter/timesince', views.timesince, name='timesince'),
    
    # This is used with include for example 2
    path('filter/timesince', views.timesince_example2, name='timesince_example2'),
    
    # This is used with include for example 3
    path('filter/timesince', views.timesince_example3, name='timesince_example3'),
    
    # Use timeuntil for displaying difference between two date times. 
    path('filter/timeuntil', views.timeuntil, name='timeuntil'),

    # This is used with include for example 2
    #path('filter/timeuntil', views.timeuntil_example2, name='timeuntil_example2'),

    # This is used with include for example 3
    #path('filter/timeuntil', views.timeuntil_example3, name='timeuntil_example3'),


    path('filter/title', views.title, name='title'),
    
    path('filter/truncatechars', views.truncatechars, name='truncatechars'),
    
    path('filter/truncatechars_html', views.truncatechars_html, name='truncatechars_html'),
    
    path('filter/truncatewords', views.truncatewords, name='truncatewords'),
    
    path('filter/truncatewords_html', views.truncatewords_html, name='truncatewords_html'),
    
    path('filter/unordered_list', views.unordered_list, name='unordered_list'),
    
    path('filter/unordered_list', views.unordered_list_nested, name='unordered_nested'),
    
    path('filter/upper', views.upper, name='upper'),
    
    
    # Field Lookups Reference
    path('field/', views.field, name='field'),
    
    # Temporary Route, to see if I can get Tag reference along with its example showing on a page.  #
    path('field/contains', views.contains, name='contains'),
    
    path('field/icontains', views.icontains, name='icontains'),
    
    path('field/endswith', views.endswith, name='endswith'),
    
    path('field/iendswith', views.iendswith, name='iendswith'),
    
    path('field/exact', views.exact, name='exact'),
    
    path('field/iexact', views.iexact, name='iexact'),
    
    #path('field/in', views.in, name='in'),
    
    path('field/gt', views.gt, name='gt'),
    
    path('field/gte', views.gte, name='gte'),
    
    path('field/lt', views.lt, name='lt'),
    
    path('field/lte', views.lte, name='lte'),
    
    #path('field/range', views.range, name='range'),
    
    
    path('field/startswith', views.startswith, name='startswith'),
    
    path('field/istartswith', views.istartswith, name='istartswith'),
    
    
    
    # Django Examples Testing Home Page 
    # path('testing/', views.testing, name='testing')
    
    # Links to Django Examples Pages, which are tested for how they are displayed
    
    
]