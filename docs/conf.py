# -*- coding: utf-8 -*-
#
# F5 OpenStack Documentation documentation build configuration file, created by
# sphinx-quickstart on Thu Feb 18 15:51:54 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import os.path

import f5_sphinx_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.4'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'cloud_sptheme.ext.table_styling',
    'sphinxjp.themes.basicstrap',
    'sphinx.ext.extlinks',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'F5 OpenStack Solutions'
copyright = u'2018, F5 Networks Inc'
author = u'F5 Networks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
# release = ''

# OpenStack release
openstack_release = "Pike"

#rst_prolog = '''
#'''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build',
                    'guides/includes',
                    'Thumbs.db',
                    '.DS_Store',
                    'drafts',
                    '_static/reuse'
                    ]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'f5_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
                        #'site_name': '',
                        'next_prev_link': False
                     }

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'F5 OpenStack Solutions'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'F5 OpenStack Home'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/f5-logo-solid-rgb_small.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = '_static/f5-logo.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'F5OpenStackDocumentationdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'F5OpenStackDocumentation.tex', u'F5 OpenStack Documentation',
     u'F5 Networks Inc', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'f5openstackdocumentation', u'F5 OpenStack Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'F5OpenStackDocumentation', u'F5 OpenStack Documentation',
     author, 'F5OpenStackDocumentation',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://docs.python.org/': None}

f5_lbaasv2_driver_shim_version = '10.0.0'
f5_lbaasv2_driver_shim_url = '\https://github.com/F5Networks/neutron-lbaas/releases/download/v%s/f5.tgz' % f5_lbaasv2_driver_shim_version
# F5 SDK release version should be set here
f5_sdk_version = '2.3.3'
# F5 icontrol REST version should be set here
f5_icontrol_version = '1.3.0'
agent_version = '9.6.0'
driver_version = '12.0.0'

rst_epilog = '''
.. |agent| replace:: F5 Agent
.. |dashboard| replace:: F5 Neutron LBaaS Dashboard
.. |agent-long| replace:: F5 Agent for OpenStack Neutron
.. |agent-versions| replace:: 9.0.x-9.5.x, 9.6+, 10.2.x
.. |config-file| replace:: :agent:`configuration file <config-file.html>`
.. |configs| replace:: :agent:`configuration parameters <config-file.html#configuration-parameters>`
.. |driver| replace:: F5 Driver
.. |driver-long| replace:: F5 Driver for OpenStack LBaaSv2
.. |driver-settings| replace:: :agent:`Device driver\/iControl Driver settings <device-driver-settings.html>`
.. |driver-versions| replace:: 9.x-12.x
.. |env-generator| replace:: :driver:`F5 environment generator <environment-generator.html>`
.. |f5_lbaasv2_driver_shim_url| replace:: %(f5_lbaasv2_driver_shim_url)s
.. |grm| replace:: :agent:`Global routed mode <global-routed-mode.html>`
.. |heat| replace:: `OpenStack Heat`_
.. |heat-t| replace:: F5 Heat template library
.. |heat-versions| replace:: 9.x, 10.x
.. |l2-seg| replace:: :agent:`L2 Segmentation Mode settings <config-file.html#l2-segmentation-mode-settings>`
.. |l3-seg| replace:: :agent:`L2 Segmentation Mode settings <config-file.html#l3-segmentation-mode-settings>`
.. |l2mode| replace:: :agent:`L2-adjacent mode <l2-adjacent-mode.html>`
.. |plugins-versions| replace:: 9.x, 10.x
.. |neutron| replace:: `OpenStack Neutron`_
.. |openstack| replace:: %(openstack_release)s
.. |oslbaas| replace:: F5 Integration for OpenStack Neutron LBaaS
.. |f5_agent_deb_url| replace:: \https://github.com/F5Networks/f5-openstack-agent/releases/download/v%(agent_version)s/python-f5-openstack-agent_%(agent_version)s-1_1404_all.deb
.. |f5_agent_rpm_url| replace:: \https://github.com/F5Networks/f5-openstack-agent/releases/download/v%(agent_version)s/f5-openstack-agent-%(agent_version)s-1.el7.noarch.rpm
.. |f5_agent_deb_package| replace:: python-f5-openstack-agent_%(agent_version)s-1_1404_all.deb
.. |f5_agent_rpm_package| replace:: f5-openstack-agent-%(agent_version)s-1.el7.noarch.rpm
.. |f5_lbaasv2_driver_deb_package| replace:: python-f5-openstack-lbaasv2-driver_%(driver_version)s-1_1404_all.deb
.. |f5_lbaasv2_driver_deb_url| replace:: \https://github.com/F5Networks/f5-openstack-lbaasv2-driver/releases/download/v%(driver_version)s/python-f5-openstack-lbaasv2-driver_%(driver_version)s-1_1404_all.deb
.. |f5_lbaasv2_driver_pip_url_branch| replace:: git+https:\//github.com/F5Networks/f5-openstack-lbaasv2-driver@%(openstack_release_l)s
.. |f5_lbaasv2_driver_rpm_package| replace:: f5-openstack-lbaasv2-driver-%(driver_version)s-1.el7.noarch.rpm
.. |f5_lbaasv2_driver_rpm_url| replace:: \https://github.com/F5Networks/f5-openstack-lbaasv2-driver/releases/download/v%(driver_version)s/f5-openstack-lbaasv2-driver-%(driver_version)s-1.el7.noarch.rpm
.. |f5_sdk_deb_package| replace:: python-f5-sdk_%(f5_sdk_version)s-1_1404_all.deb
.. |f5_sdk_deb_url| replace:: \https://github.com/F5Networks/f5-common-python/releases/download/v%(f5_sdk_version)s/python-f5-sdk_%(f5_sdk_version)s-1_1404_all.deb
.. |f5_agent_pip_url| replace:: git+https://github.com/F5Networks/f5-openstack-agent@v%(agent_version)s
.. |f5_driver_pip_url| replace:: git+https://github.com/F5Networks/f5-openstack-lbaasv2-driver@v%(driver_version)s
.. |f5_icontrol_deb_package| replace:: python-f5-icontrol-rest_%(f5_icontrol_version)s-1_1404_all.deb
.. |f5_icontrol_deb_url| replace:: \https://github.com/F5Networks/f5-icontrol-rest-python/releases/download/v%(f5_icontrol_version)s/python-f5-icontrol-rest_%(f5_icontrol_version)s-1_1404_all.deb
.. |f5_icontrol_rpm_package| replace:: f5-icontrol-rest-%(f5_icontrol_version)s-1.el7.noarch.rpm
.. |f5_icontrol_rpm_url| replace:: \https://github.com/F5Networks/f5-icontrol-rest-python/releases/download/v%(f5_icontrol_version)s/f5-icontrol-rest-%(f5_icontrol_version)s-1.el7.noarch.rpm
.. |f5_sdk_rpm_package| replace:: f5-sdk-%(f5_sdk_version)s-1.el7.noarch.rpm
.. |f5_sdk_rpm_url| replace:: \https://github.com/F5Networks/f5-common-python/releases/download/v%(f5_sdk_version)s/f5-sdk-%(f5_sdk_version)s-1.el7.noarch.rpm
.. |agent_version| replace:: %(agent_version)s
.. |driver_version| replace:: %(driver_version)s
.. |f5_agent_readme| raw:: html
   
   <a href="https://github.com/F5Networks/f5-openstack-agent/blob/master/README.rst" target="_blank">README</a>
.. |f5_lbaasv2_driver_readme| raw:: html

   <a href="https://github.com/F5Networks/f5-openstack-lbaasv2-driver/blob/master/README.rst" target="_blank">README</a>
.. |neutron-lbaas| raw:: html
   
   <a href="https://docs.openstack.org/latest/networking-guide/config-lbaas.html" target="_blank">Neutron LBaaS</a>
.. |os-deployment| raw:: html
   
   <a href="https://docs.openstack.org/latest/networking-guide/deploy.html" target="_blank">OpenStack Deployment</a>
.. |os-extnet| raw:: html

    <a href="https://docs.openstack.org/latest/install-guide-rdo/launch-instance-networks-provider.html" target+"_blank">external provider network</a>
.. |community_tempest_lbaasv2_tests| raw:: html

   <a href="https://github.com/openstack/neutron-lbaas/tree/stable/%(openstack_release_l)s">tests</a>
.. _Acknowledgements page: %(base_url)s/containers/latest/acknowledgements.html
.. _Agent configuration parameter: %(base_url)s/products/openstack/agent/latest/#configuration-parameters
.. _Barbican: https://docs.openstack.org/developer/barbican/
.. _Better or Best license: https://f5.com/products/how-to-buy/simplified-licensing
.. _BIG-IP device service clustering: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-device-service-clustering-administration-12-1-1.html
.. _BIG-IP Nova flavor: %(base_url)s/cloud/openstack/latest/support/openstack_big-ip_flavors.html
.. _BIG-IP onboarding Heat template: %(base_url)s/products/templates/openstack-heat/latest/f5_supported/f5-bigip-ve_image-patch-upload.html
.. _BIG-IP server-side SSL termination: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-ssl-administration-13-0-0/4.html#guid-45595e00-5179-4055-87f7-277eb7d922bd
.. _BIG-IP session persistence profile: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-13-0-0/4.html
.. _BIG-IP SSL profile: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-13-0-0/6.html
.. _BIG-IP TCP profile: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-13-0-0/1.html#guid-4b08badd-ccd9-4ddc-a4c3-1d8f788f38c3
.. _BIG-IP VE Standalone, 3-NIC Heat template: %(base_url)s/products/templates/openstack-heat/latest/f5_supported/f5-bigip-ve_standalone-3nic.html
.. _Certificate Manager settings: %(base_url)s/products/openstack/agent/latest/#cert-manager-settings
.. _configure access and security groups: https://docs.openstack.org/horizon/latest/user/configure-access-and-security-for-instances.html
.. _configuration synchronization: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-device-service-clustering-administration-12-1-1/5.html
.. _Client SSL: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-ssl-administration-13-0-0/5.html
.. _client SSL profile: https://support.f5.com/csp/article/K14783
.. _Create security groups using the OpenStack CLI: https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/security-group.html
.. _Create security group rules using the OpenStack CLI: https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/security-group-rule.html
.. _Configure the F5 Agent for OpenStack Neutron: %(base_url)s/products/openstack/agent/latest/index.html#configure-the-f5-openstack-agent
.. _Configuring the basic BIG-IP network: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-ecmp-mirrored-clustering-12-1-0/2.html?sr=56312127
.. _Create an LBaaSv2 HTTPS listener: https://docs.openstack.org/mitaka/networking-guide/config-lbaas.html#adding-an-https-listener
.. _Create a Neutron load balancer: https://docs.openstack.org/mitaka/networking-guide/config-lbaas.html#building-an-lbaas-v2-load-balancer
.. _Create a Neutron L7 policy: https://docs.openstack.org/cli-reference/neutron.html
.. _deprecated OpenStack LBaaS v1 project: https://docs.openstack.org/mitaka/networking-guide/config-lbaas.html#lbaas-v1
.. _Device driver/iControl Driver settings: %(base_url)s/products/openstack/agent/latest/device-driver-settings.html
.. _different sizes: https://support.f5.com/csp/article/K14946
.. _environment file: https://docs.openstack.org/heat/latest/template_guide/environment.html
.. _environment variables: https://docs.openstack.org/user-guide/common/cli-set-environment-variables-using-openstack-rc.html
.. _F5-Supported Heat Templates: %(base_url)s/products/templates/openstack-heat/latest/index.html#f5-supported-heat-templates
.. _F5 BIG-IP Active-Standby Pair: %(base_url)s/products/templates/openstack-heat/latest/f5_supported/f5-bigip-ve_active-standby-pair.html
.. _F5 iApps: https://devcentral.f5.com/wiki/iApp.HomePage.ashx
.. _F5 Python SDK: http://f5-sdk.readthedocs.io/
.. _F5 Unsupported HOT library: %(base_url)s/products/templates/openstack-heat/latest/#unsupported-heat-templates
.. _Heat: https://www.openstack.org/software/releases/%(openstack_release_l)s/components/heat
.. _heat orchestration template library: %(base_url)s/products/templates/openstack-heat/latest/#heat-orchestration-template-index
.. _Glance: https://www.openstack.org/software/releases/%(openstack_release_l)s/components/glance
.. _Horizon: https://www.openstack.org/software/releases/%(openstack_release_l)s/components/horizon
.. _High Availability mode: %(base_url)s/products/openstack/agent/latest/ha-mode.html
.. _HPE Helion OpenStack: https://www.openstack.org/foundation/companies/profile/hewlett-packard-enterprise
.. _iControl REST: https://devcentral.f5.com/wiki/iControlrest.HomePage.ashx
.. _Install the F5 Agent: %(base_url)s/products/openstack/agent/latest/#installation
.. _Install the F5 Plugins for Heat: %(base_url)s/products/openstack/heat-plugins/latest/#installation
.. _Install the F5 LBaaSv2 Driver: %(base_url)s/products/openstack/lbaasv2-driver/latest/#installation
.. _iRules: https://devcentral.f5.com/irules
.. _iRule: https://devcentral.f5.com/irules
.. _Keystone: https://docs.openstack.org/developer/keystone/
.. _L7 policy: https://wiki.openstack.org/wiki/Neutron/LBaaS/l7#L7_Policies
.. _L7 policy delete: https://docs.openstack.org/cli-reference/neutron.html#neutron-lbaas-l7policy-delete
.. _license: https://f5.com/products/how-to-buy/simplified-licensing
.. _Local Traffic Manager: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-basics-13-0-0.html
.. _Manage SSH keys using OpenStack Horizon: https://docs.openstack.org/horizon/latest/user/configure-access-and-security-for-instances.html#keypair-add
.. _Manage SSH keys using the OpenStack CLI: https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/keypair.html
.. _Mirantis OpenStack: https://www.mirantis.com/partners/f5-networks/
.. _Neutron: https://www.openstack.org/software/releases/%(openstack_release_l)s/components/neutron
.. _Nova: https://www.openstack.org/software/releases/%(openstack_release_l)s/components/nova
.. _OpenStack API: https://developer.openstack.org/api-guide/quick-start/index.html
.. _OpenStack CLI: https://docs.openstack.org/cli-reference/
.. _OpenStack Barbican: https://docs.openstack.org/barbican/latest
.. _OpenStack Heat: https://docs.openstack.org/heat/latest
.. _OpenStack Heat Orchestration Template: https://docs.openstack.org/heat/latest/template_guide/hot_spec.html
.. _OpenStack Horizon: https://www.openstack.org/software/releases/%(openstack_release_l)s/components/horizon
.. _OpenStack Networking Concepts: http://docs.openstack.org/liberty/networking-guide/
.. _OpenStack Neutron: https://docs.openstack.org/neutron/latest
.. _OpenStack Nova: https://docs.openstack.org/nova/latest
.. _OpenStack installation guides: https://docs.openstack.org/install-guide/
.. _policies: https://support.f5.com/csp/article/K15085
.. _policy: https://support.f5.com/csp/article/K15085
.. _profiles: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-12-0-0/2.html
.. _profile: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-profiles-reference-12-0-0/2.html
.. _python-openstackclient: https://docs.openstack.org/python-openstackclient/latest
.. _RedHat OpenStack Platform: https://access.redhat.com/ecosystem/software/1446683
.. _secrets: http://developer.openstack.org/api-guide/key-manager/secrets.html
.. _Server SSL: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-ssl-administration-13-0-0/5.html
.. _Set up Neutron to use the F5 service provider driver: %(base_url)s/products/openstack/lbaasv2-driver/latest/#neutron-setup
.. _Sync-Failover device group: https://support.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-system-device-service-clustering-administration-13-0-0/4.html
.. _Virtual Edition: https://f5.com/products/deployment-methods/virtual-editions
.. _OpenStack Neutron LBaaS Dashboard: https://docs.openstack.org/neutron-lbaas-dashboard/latest/usage.html
.. _Octavia Documentation: https://docs.openstack.org/octavia/latest/index.html
.. _Setting up Barbican: https://docs.openstack.org/barbican/latest/configuration/index.html
''' % {
  'openstack_release': openstack_release,
  'openstack_release_l': openstack_release.lower(),
  'f5_lbaasv2_driver_shim_url': f5_lbaasv2_driver_shim_url,
  'f5_sdk_version': f5_sdk_version,
  'f5_icontrol_version': f5_icontrol_version,
  'agent_version': agent_version,
  'driver_version': driver_version,
  'version': version,
  'base_url': 'http://clouddocs.f5.com'
}

# Markup to shorten links to external sites
extlinks = {'agent': ('http://clouddocs.f5.com/products/openstack/agent/latest/%s',
                      ''),
            'driver': ('http://clouddocs.f5.com/products/openstack/lbaasv2-driver/latest/%s',
            ''),
            'heat': ('http://clouddocs.f5.com/products/templates/openstack-heat/latest/%s',
            ''),
            'plugins': ('http://clouddocs.f5.com/products/openstack/heat-plugins/latest/%s',
            ''),
            'github': ('https://github.com/f5networks/%s',
            '')
}

# Ignore anchors when running linkcheck
linkcheck_anchors = False
