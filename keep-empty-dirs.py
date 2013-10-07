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

class DefaultValues:
    filename = '.keep'
    dryrun = False
    remove = False
    pathlist = ['.']

def main():
    import argparse

    defaultValues = DefaultValues()

    parser = argparse.ArgumentParser(description=__doc__.strip())

    parser.add_argument('-f', '--filename', action='store', dest='filename',
                      default=defaultValues.filename,
                      help="Name of the file to create. (Default: "+defaultValues.filename+")")
    parser.add_argument('-n', '--dryrun', action='store_true', dest='dryrun',
                      default=defaultValues.dryrun,
                      help="Perform a dry run (don't create or remove the file). If not specified, then the file is created (or removed if the --remove option is specified).")
    parser.add_argument('-r', '--remove', action='store_true', dest='remove',
                      default=defaultValues.remove,
                      help="Remove the file instead of creating it. If not specified, then the file is created.")
    parser.add_argument('pathlist', action='store',
                      nargs='*',
                      default=defaultValues.pathlist,
                      help="One or more directory paths on which to act. (Default: act on the current directory)")

    opts = parser.parse_args()

    actionsAttempted=0

    if (opts.remove):
        if (opts.dryrun):
            actionDesc = 'Would Remove: '
            actionSummary = 'Files to remove: '
        else:
            actionDesc = 'Remove: '
            actionSummary = 'Files removed: '
    else:
        if (opts.dryrun):
            actionDesc = 'Would Create: '
            actionSummary = 'Files to create: '
        else:
            actionDesc = 'Create: '
            actionSummary = 'Files created: '

    for pathitem in opts.pathlist:
        for root, dirs, files in os.walk(pathitem):
            if (not opts.remove) and (not files) and (not dirs):
                fn = os.path.join(root, opts.filename)
                print(actionDesc, fn)
                actionsAttempted += 1
                if not opts.dryrun:
                    open(fn, 'w')

            elif opts.remove and (opts.filename in files):
                fn = os.path.join(root, opts.filename)
                print(actionDesc, fn)
                actionsAttempted += 1
                if not opts.dryrun:
                    os.remove(fn)

        print()
        print('Starting path:', os.path.abspath(pathitem))
        print(actionSummary, actionsAttempted)

if __name__ == '__main__':
    main()