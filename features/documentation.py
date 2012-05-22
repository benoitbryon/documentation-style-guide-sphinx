# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

from lettuce import step, world


current_dir = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
root_dir = os.path.dirname(current_dir)


@step(u'Given I am at project\'s root path')
def given_i_am_at_project_s_root_path(step):
    """Cd to project's root."""
    os.chdir(root_dir)


@step(u'And ``docs/_build`` directory doesn\'t exist')
def and_docs__build_directory_doesn_t_exist(step):
    """Remove docs/_build folder."""
    if os.path.exists('docs/_build'):
        shutil.rmtree('docs/_build')


@step(u'When I run ``make documentation-build``')
def when_i_run_make_documentation_build(step):
    """Build documentation."""
    command = ['make', 'documentation-build']
    process = subprocess.Popen(command, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    world.return_code = process.wait()
    world.stderr = process.communicate()[1]
    world.stderr = world.stderr[len('Making output directory...\n'):]


@step(u'Then I don\'t get errors or warnings')
def and_i_don_t_get_errors_or_warnings(step):
    """Assert no errors were raised."""
    assert world.return_code is 0
    if world.stderr is not '':
        print world.stderr
    assert world.stderr is ''


@step(u'And I get documentation in ``docs/_build/html/`` folder')
def then_i_get_documentation_in_docs__build_html_folder(step):
    """Check that docs/_build/html and docs/_build/html/index.html exist."""
    assert os.path.isdir('docs/_build/html')
    assert os.path.isfile('docs/_build/html/index.html')


@step(u'When I run ``make README-build``')
def when_i_run_make_readme_build(step):
    """Build README."""
    command = ['make', 'README-build']
    process = subprocess.Popen(command, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    world.return_code = process.wait()
    world.stderr = process.communicate()[1]


@step(u'And I ``docs/_build/README/README.html`` file is generated')
def and_i_docs__build_readme_readme_html_file_is_generated(step):
    """Assert no errors were raised."""
    assert world.return_code is 0
    if world.stderr is not '':
        print world.stderr
    assert world.stderr is ''
