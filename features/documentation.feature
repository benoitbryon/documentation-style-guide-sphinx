Feature: Build documentation
    In order to publish documentation as HTML files
    As a developer
    I build documentation

    Scenario: Build documentation command
        Given I am at project's root path
	And ``docs/_build`` directory doesn't exist
	When I run ``make documentation-build``
	Then I don't get errors or warnings
	And I get documentation in ``docs/_build/html/`` folder
