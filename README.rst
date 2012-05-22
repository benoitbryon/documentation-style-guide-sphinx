###########################################
Style guide for Sphinx-based documentations
###########################################

This project is about coding standards for `Sphinx`_-based documentations.


**********
Ressources
**********

* `code repository`_
* `bugtracker`_
* `online documentation`_


******
Status
******

**This is a proposal.**

Although applied on private or small projects, this style guide should be
considered as a proposal. It is not industry standard and have not been
supported by some "big" projects.

However, **give it a try!**


******
Vision
******

Context
=======

In software development, documentation matters.

`Sphinx`_ is a great documentation builder. It is community standard for
`Python`_ projects, but is not tied to Python and can be used to document
almost everything. One of his strength is to use the `reStructuredText`_
syntax, which focuses on simplicity and readability for humans.

`Sphinx reStructuredText primer`_ and `docutils' reStructuredText
documentation`_ focus on syntax. They give examples, but they are quite
permissive.

When developers contribute to projects, they read and write documentation.
There are conventions about writing code, but there is no about writing
documentation. So documentations, despite they are based on a common toolkit,
are really heterogeneous:

* the more developers, the more heterogeneous.
* every project may use its own conventions.

Goal
====

.. code:: gherkin

  Feature: public documenting standards

    In order to improve readability of documentation and make it consistent
    across the wide spectrum of Sphinx-based documentations
    As member of a development team
    I want to follow coding standards

    Scenario: Adopt documentation-related conventions for a project
      Given a project
      And a team
      When the team chose Sphinx as documentation builder for project
      And the team needs conventions about the documentation
      Then team members follow the rules provided at
      http://documentation-style-guide-sphinx.readthedocs.org/
      And reference it in the project's documentation.

This project focuses on conventions about what `PEP 8`_ calls "style guide".

Related work
============

Style guide is mostly about syntax. It is not enough.

* Because writing documentation is not so easy, we need guidelines about
  documentation content, i.e. best-practices.
* Because we often adapt patterns while documenting, we need helpers to
  generate documentation content, i.e. templates.

Planning
========

* Write a draft.
* Publish it on some DVCS hosting platform.
* Use it in some projects managed by authors, contributors and early adopters.
* Communicate and get feedback. Propose it to some visible projects such as:

  * `Lettuce`_
  * `Read the docs`_
  * `Sphinx`_
  * `Python`_ (could it be a PEP?)

* Depending on the feedback and contributions, reconsider this project's
  relevance, adapt goals and planning.


*****
Usage
*****

* Read and follow `style guide for Sphinx-based documentations`_
* Reference the convention in your project's documentation.


**********
Contribute
**********

Create tickets
==============

Please use the `bugtracker`_ **before** starting some work:

* check if the bug or feature request has already been filed. It may have been
  answered too!
* else create a new ticket.
* if you plan to contribute, tell us, but don't wait for us! So that we are
  given an opportunity to discuss, join forces or give feedback as soon as
  possible.

Fork and branch
===============

* Work in forks and branches.
* Prefix your branch with the ticket ID corresponding to the issue. As an
  example, if you are working on ticket #23 which is about headings convention,
  name your branch like ``23-headings``.

Download and install
====================

System requirements:

* `Python`_ version 2.6 or 2.7.
  
  .. note::

    The provided Makefile uses ``python`` command. So you may use
    `Virtualenv`_ to make sure the active ``python`` is the adequate one.

* Access to the Internet.

Execute:

.. code:: sh

  git clone git@github.com/benoitbryon/documentation-style-guide-sphinx.git
  cd documentation-style-guide-sphinx/
  make install

If you cannot execute the Makefile, read it and adapt the few commands it
contains in the ``install`` section to your needs.

Hack
====

They said "Eat your own dog food", so follow `style guide for Sphinx-based
documentations`_.

In your commit messages, reference the ticket with some ``refs #TICKET-ID``
syntax.

Test and build
==============

Build the documentation and review your work before commit:

.. code:: sh

  make build-documentation

Share
=====

* Push your code
* Submit a pull request


**********
References
**********

.. target-notes::

.. _`Sphinx`: http://sphinx.pocoo.org
.. _`code repository`: 
   https://github.com/benoitbryon/documentation-style-guide-sphinx
.. _`bugtracker`: 
   https://github.com/benoitbryon/documentation-style-guide-sphinx/issues
.. _`online documentation`:
   http://documentation-style-guide-sphinx.readthedocs.org/
.. _`RestructuredText`: http://docutils.sourceforge.net/rst.html
.. _`Sphinx reStructuredText primer`: http://sphinx.pocoo.org/rest.html
.. _`docutils' reStructuredText documentation`:
   http://docutils.sourceforge.net/rst.html
.. _`PEP 8`: http://www.python.org/dev/peps/pep-0008/
.. _`Lettuce`: http://lettuce.it/
.. _`Read the docs`: http://readthedocs.org
.. _`Python`: http://python.org
.. _`style guide for Sphinx-based documentations`:
   http://documentation-style-guide-sphinx.readthedocs.org/
.. _`Virtualenv`: http://virtualenv.org
