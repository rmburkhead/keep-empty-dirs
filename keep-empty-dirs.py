#!/usr/bin/env python

# This program is licensed under the GNU General Public License v2 (http://www.gnu.org/licenses/gpl-2.0.html)
# See the accompanying LICENSE file.
#
# GPL Modification Notice:
# This program is modified, beginning in October 2013, from the original. See the accompanying README.md file for information on,
# and access to the original author and source.
#
# Compatibility:
# This script has been tested with Python 3.3.2. Your mileage may vary.

"""
This script recurses through the given directories (or the current directory, by default),
finds the empty subdirectories, and adds a file in each. This is used to mark all existing
empty subdirectories in a hierarchy to be kept from deletion, or for the sentinels to be
used to insure the directories are added to a version control repository that does not normally
retain empty directories (e.g., Mecurial, Git).
"""

import os

def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.strip())

    parser.add_argument('-f', '--filename', action='store', dest='filename',
                      default='.keep',
                      help="Name of the file to create. (Default: .keep)")

    parser.add_argument('pathlist', action='store',
                      nargs='*',
                      default=['.'],
                      help="One or more directory paths on which to act. (Default: act on the current directory)")

    opts = parser.parse_args()

    for pathitem in opts.pathlist:
        for root, dirs, files in os.walk(pathitem):
            if not files:
                fn = os.path.join(root, opts.filename)
                print(fn)
                open(fn, 'w')

if __name__ == '__main__':
    main()