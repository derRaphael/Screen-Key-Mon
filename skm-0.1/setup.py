#!/usr/bin/env python
#
# Copyright (c) 2011 derRaphael <screenKeyMon@itholic.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup
import gettext


NAME = 'screen-key-mon'
DIR = 'src/skm'
gettext.install(NAME, DIR + '/locale')
VER = '1.7'
PY_NAME = 'screen_key_mon'
DEB_NAME = NAME.replace('-', '')
RELEASE_FILE = 'RELEASE'
VCS = ''

PY_SRC = '%s.py' % PY_NAME
DEPENDS = ['python-xlib', 'python-gtk2']
DEPENDS_STR = ' '.join(DEPENDS)

MENU_SUBSECTION = 'Graphics'
AUTHOR_NAME = 'derRaphael'
COPYRIGHT_NAME = ''
GOOGLE_CODE_EMAIL = 'screenKeyMon@itholic.org'
MAILING_LIST = ''
KEYWORDS = ['keyboard', 'status', 'monitor', 'education']
MAN_FILE = ''
DESKTOP_FILE = ''
ICON = ''
COMMAND = '/usr/bin/%s' % NAME
LANGS = ['en_US']

SETUP = dict(
  name=NAME,
  version=VER,
  packages=['screenkeymon'],
  package_dir={
      'screenkeymon': 'src/skm'},
  package_data = {
      'screenkeymon': [
          'themes/**/*', '*.kbd',
          'icons/key-mon.desktop', 'locale/**/*/*.mo'],
  },
  scripts=['src/screen-key-mon'],
  author=AUTHOR_NAME,
  author_email='screenKeyMon@itholic.org',
  platforms=['POSIX'],
  license='GPL v3',
  keywords=' '.join(KEYWORDS),
  url='',
  download_url='',
  description=_('Fork of key-mon 1.7 and screenkey 0.2'),
  long_description=_("""See included README for details"""),
  classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'Environment :: X11 Applications',
      'Intended Audience :: Education',
      'License :: OSI Approved :: GPL v3',
      'Operating System :: POSIX :: Linux',
      'Topic :: Education :: Computer Aided Instruction (CAI)',
  ],
)

if __name__ == '__main__':
  setup(**SETUP)
