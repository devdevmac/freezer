#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# This file is execfile()d with the current directory set
# to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# NOTE(dims): monkey patch subprocess to prevent failures in latest eventlet
# See https://github.com/eventlet/eventlet/issues/398


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('../../'))
# sys.path.insert(0, os.path.abspath('../'))
# sys.path.insert(0, os.path.abspath('./'))

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*')
# or your custom ones.

extensions = ['sphinx.ext.autodoc',
              'openstackdocstheme',
              'oslo_config.sphinxconfiggen',
              'oslo_config.sphinxext'
              ]

config_generator_config_file = (
    '../../config-generator/scheduler.conf')
sample_config_basename = '_static/freezer'

# autodoc generation is a bit aggressive and a nuisance
# when doing heavy text edit cycles. Execute "export SPHINX_DEBUG=1"
# in your terminal to disable
#if not os.getenv('SPHINX_DEBUG'):
#    extensions += ['ext.freezer_autodoc']

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = []

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
repository_name = 'openstack/freezer'
bug_project = 'freezer'
bug_tag = 'doc'
# project = u'Freezer'
# copyright = u'2010-present, OpenStack Foundation'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# from freezer import version_info
# # The full version, including alpha/beta/rc tags.
# release = version_info.release_string()
# # The short X.Y version.
# version = version_info.version_string()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.

# # List of directories, relative to source directory, that shouldn't be searched
# # for source files.
# exclude_trees = []

# A list of glob-style patterns that should be excluded when looking for
# source files. They are matched against the source file names relative to the
# source directory, using slashes as directory separators on all platforms.
exclude_patterns = [
    # Missing win32serviceutil module on linux
    #'api/freezer.scheduler.win_daemon*',
]

#
# # The reST default role (used for this markup: `text`) to use
# # for all documents.
# # default_role = None
#
# # If true, '()' will be appended to :func: etc. cross-reference text.
# # add_function_parentheses = True
#
# # If true, the current module name will be prepended to all description
# # unit titles (such as .. function::).
# add_module_names = False
#
# # If true, sectionauthor and moduleauthor directives will be shown in the
# # output. They are ignored by default.
# show_authors = False
#
# # The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['freezer.']

# -- Options for man page output ----------------------------------------------

# Grouping the document tree for man pages.
# List of tuples 'sourcefile', 'target', u'title', u'Authors name', 'manual'

man_pages = [
    ('man/freezer-manage', 'freezer-manage', u'Cloud controller fabric',
     [u'OpenStack'], 1)
]

# -- Options for HTML output --------------------------------------------------

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
html_theme = 'openstackdocs'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d %H:%M'

