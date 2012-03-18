Open Knesset Templates
======================

This repository holds the code for 'Open Knesset'_ templates, sample data and 
code to run as development server.  You are invited to get the code, improve
the design and send a pull request

Get the Code:
-------------
::

    Browse to http://github.com/mushon/ok-template click Fork
    Browse to your Open-Knesset fork and click the SSH button. 
    Copy the SSH address and run the following command
    $ git clone paste_the_ssh_address_here.git


Using
-----

To run a local server to test the templates, you'll need 
'python'_ and its 'setup tools'_ installed.
One you have that open the shell, cd into your project home and type::

    $ easy_install pystache
    $ python server.py
    
The server is up and running and all that's left is pointing the 
browser at localhost:8080/`template_name` and the server will return
a page rendered based on the template found in templates/`template_name`.html

