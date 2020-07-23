Word Count
===========

Counts the number of words in a block of text.

Assumptions:
==================

* As a user
    * when I view the application
        * then I see a form containing a text box to enter a body of text

    * and when I submit the form with some text
        * then I see a result containing the number of words in the text box

    * and when I submit the form with an empty text
        * then I see a form error telling me that some text input is required

* As an engineer
    * when I look at your project
        * then I should understand how to install and run it

------------
Dependencies
===========================
* Python 3.7 or higher
* Django 3.0 or higher
* Django Bootstrap-form


Installation
===========================
### Step 1: Virtual Environment Setup

This project runs in a _virtual environment_:


```
    # Linux
    python3 -m venv venv-wc #create
    source venv-wc/bin/activate #activate
    
    # Windows
    python -m venv venv-wc #create
    venv-wc\Scripts\activate.bat #activate
```

### Step 2: Install version


Install version and all of the dependencies that are required to be installed by pip for this package:


 
```
    git clone https://github.com/lcdcustodio/wordcount.git
    cd wordcount
    pip install -r requirements.txt
```

### Step 3: Launch the server:


```
    python manage.py runserver
```


You can get started at `http://127.0.0.1:8000`.

Run Tests
===========================

Run the test suite:

```
    python manage.py test
```



