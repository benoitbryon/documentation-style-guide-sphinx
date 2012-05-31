############
Contributing
############

This document provides guidelines for people who want to contribute to the
documentation-style-guide-sphinx project.


**************
Create tickets
**************

Please use the `bugtracker`_ **before** starting some work:

* check if the bug or feature request has already been filed. It may have been
  answered too!
* else create a new ticket.
* if you plan to contribute, tell us, but don't wait for us! So that we are
  given an opportunity to discuss, join forces or give feedback as soon as
  possible.


***************
Fork and branch
***************

* Work in forks and branches.
* Prefix your branch with the ticket ID corresponding to the issue. As an
  example, if you are working on ticket #23 which is about headings convention,
  name your branch like ``23-headings``.


********************
Download and install
********************

System requirements:

* `Python`_ version 2.6 or 2.7.
  
  .. note::

    The provided Makefile uses ``python`` command. So you may use
    `Virtualenv`_ to make sure the active ``python`` is the adequate one.

Execute:

.. code-block:: sh

  git clone git@github.com/benoitbryon/documentation-style-guide-sphinx.git
  cd documentation-style-guide-sphinx/
  make install

If you cannot execute the Makefile, read it and adapt the few commands it
contains in the ``install`` section to your needs.


**************
Edit documents
**************

They said "Eat your own dog food", so follow `style guide for Sphinx-based
documentations`_.

In your commit messages, reference the ticket with some ``refs #TICKET-ID``
syntax.


**************
Test and build
**************

Tests and builds will automatically be triggered before commit:

* tests include the build of documentation and README as HTML.
* a `Git pre-commit hook`_ is installed during `Download and install`_.

If you want to run them manually, use the provided Makefile:

* run tests with ``make tests``
* build documentation with ``make documentation-build``
* build README with ``make README-build``


*****
Share
*****

* Push your code
* Submit a pull request


**********
References
**********

.. target-notes::

.. _`bugtracker`: 
   https://github.com/benoitbryon/documentation-style-guide-sphinx/issues
.. _`Python`: http://python.org
.. _`Virtualenv`: http://virtualenv.org
.. _`style guide for Sphinx-based documentations`:
   http://documentation-style-guide-sphinx.readthedocs.org/
.. _`Git pre-commit hook`: http://git-scm.com/book/en/Customizing-Git-Git-Hooks
