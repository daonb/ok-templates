Open Knesset Templates
======================

This repository holds the code for `Open Knesset`_ templates, sample data and 
code to run as development server.  You are invited to fork the code, improve
the design and send a pull request

.. _Open Knesset: http://oknesset.org

Quick Start
-----------

* Clone the repo: ``git clone git@github.com:hasadana/ok-templates.git``
* Start the local server: ``python server.py``
* Browse to http://localhost:8000/index

Designing
---------

the templates themselves are located at the ``templates`` folder and written in 
Mustache_ logicless templating language.  The templates have a ``.mustache``
ending and are rendered using a context based on a general `context.yaml`` 
on the project's root and a template specific yaml file.
To render the template ``foo.mustach`` point your browser at 
http://localhost:8000/foo 

Once stasified with your changes, commit your changes to your fork with a
meaningful commit message and send a pull request to `hasadna's fork`_

.. _Mustache: http://mustache.github.com
.. _hasadna's fork: https://github.com/hasadna/ok-templates
