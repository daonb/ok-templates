Open Knesset Templates
======================

This repository holds the code for `Open Knesset`_ templates, sample data and 
code to run as development server.  You are invited to fork the code, improve
the design and send a pull request

.. _Open Knesset: http://oknesset.org

Quick Start
-----------

* Clone the repo: ``git clone git@github.com:daonb/ok-templates.git``
* if you don't have python installed (you can test for it by typing 
  ``python`` on your prompt) get it from http://www.python.org/download/.
  Version 2.7.2 is best
* Change your working directory to the project's: ``cd ok-templates``
* Start the local server: ``python server.py``
* Browse to http://localhost:8000/agenda/1;s

Designing
---------

the templates themselves are located at the ``templates`` folder and written in 
Mustache_ logicless templating language.  The templates have a ``.mustache``
ending and are rendered using a context based on a general `context.yaml`` 
on the project's root and a template specific json file.

Sample
------

The repository includes a ``agenda_detail.mustache`` file that is based on a
`1.0 template`_ and all the required template tags and include files. To see
the template, point your browser at http://locahost:8000/agenda/1;s and you
will see a page rendered based on the template and a context file from 
``fixtures/agenda/1.json``.
Behind the scenes, when the server identify a url that ends with ``;s`` it 
eaves most of the rendering to the client and uses 
``template/small_base.mustache`` to render a page with basic html and the
javascript needed to render the page on the client. Without the ``;s``
rendering is done on the server, using pystache. This mode is not tested
and is less usuable as pystache does not return meaningfull errors (yet?).


.. _1.0 template: src/knesset/templates/agendas/agenda_detail.html

I18N & L10N
-----------

The templates support i18n through gnu's gettext_. You can test if you have it
installed by running ``gettext --version``. If you don't, the easiest way is to
run ``apt-get install gettext`` on *Linux* or ``brew install gettext`` for the
*OSX*, and for the less fortunate ones, try the setup file 
`here <http://gnuwin32.sourceforge.net/packages/gettext.htm>`_.
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
.. _hasadna's fork: https://github.com/hasadna/ok-templates
.. _poedit: http://www.poedit.net/
