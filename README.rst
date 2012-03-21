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
To render the template ``sample.mustache`` point your browser at 
http://localhost:8000/sample and you'll see a page render based on
``templates/sample.yaml`` context

The templates support i18n through gnu's gettext_. You can test if you have it
installed by running ``gettext --version``. If you don't, the easiest way is to
run ``apt-get install gettext`` on *Linux* or ``brew install gettext`` for the
*OSX*, and for the less fortunate ones, try the setup file 
`here<http://gnuwin32.sourceforge.net/packages/gettext.htm>`_.
To use static text in the the template, use natural language and wrap it in
``{{#_}}Natural Language{{/_}}``.  Once you've added strings to be translated
you need to update the ``.po`` file.  First run ``python makemsgs.py`` to update
the file ``locale/he/LC_MESSAGES/mustache.po`` with the new strings.  Next, edit
the file using a text editor or poedit_ and translate the strings.  Fianlly, you
need to compile the file using ``./compilemsgs``.

Once stasified with your changes, commit your changes to your fork with a
meaningful commit message and send a pull request to `hasadna's fork`_

.. _Mustache: http://mustache.github.com
.. _gettext: http://www.gnu.org/software/gettext/
.. _hasadna's fork: https://github.com/ohasadna/ok-templates
.. _poedit: http://www.poedit.net/
