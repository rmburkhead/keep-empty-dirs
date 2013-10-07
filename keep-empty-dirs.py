#!/usr/bin/env python

# This program is licensed under the GNU General Public License v2 (http://www.gnu.org/licenses/gpl-2.0.html)
# See the accompanying LICENSE file.
#
# GPL Modification Notice:
# This program is modified, beginning in October 2013, from the original. See the accompanying README.md file for information on,
# and access to the original author and source.

"""
Recurse through the given directories, find the empty subdirectories and add a
.keep file in each. This is used to mark all existing empty subdirectories in a
hierarchy to be kept from deletion, or for the sentinels to be used to insure
the directories are added to a Mercurial repository.
"""

import os
from os.path import join


def main():
    import optparse
    parser = optparse.OptionParser(__doc__.strip())

    parser.add_option('-f', '--filename', action='store',
                      default='.keep',
                      help="Default name of file to create.")

    opts, args = parser.parse_args()

    for arg in args:
        for root, dirs, files in os.walk(arg):
            if not files:
                fn =join(root, opts.filename)
                print fn
                open(fn, 'w')

if __name__ == '__main__':
    main()