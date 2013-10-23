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

import os, sys, platform

def version_check():
    python_version = platform.python_version_tuple()
    if (python_version[0] != '2') or ((python_version[0] == '2') and (python_version[1] < '6')):
        print "This script requires Python 2 version 2.6 or greater. If you are running Python 3, then use version 2.x.x of this script."
        sys.exit(1)

class DefaultValues:
    showVersion = False
    filename = '.keep'
    dryrun = False
    verbose = False
    verbosecheck = False
    verboseignore = False
    skipdir = 'CVS:.git:.hg:.svn'
    remove = False
    pathlist = ['.']

def main():
    import argparse

    versionString = 'keep-empty-dirs.py 1.0.0'

    defaultValues = DefaultValues()

    parser = argparse.ArgumentParser(description=__doc__.strip())

    parser.add_argument('--version', action='store_true', dest='showVersion',
                      default=defaultValues.showVersion,
                      help="Print the script version information.")
    parser.add_argument('-f', '--filename', action='store', dest='filename',
                      default=defaultValues.filename,
                      help="Name of the file to create. (Default: "+defaultValues.filename+")")
    parser.add_argument('-n', '--dryrun', action='store_true', dest='dryrun',
                      default=defaultValues.dryrun,
                      help="Perform a dry run (don't create or remove the file). If not specified, then the file is created (or removed if the --remove option is specified).")
    parser.add_argument('-s', '--skipdir', action='store', dest='skipdir',
                      default=defaultValues.skipdir,
                      help="A list of one or more directories to skip, separated by colons (e.g. \"-s .git:.svn:CVS\"). (Default: "+defaultValues.skipdir+")")
    parser.add_argument('-r', '--remove', action='store_true', dest='remove',
                      default=defaultValues.remove,
                      help="Remove the file instead of creating it. If not specified, then the file is created.")
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                      default=defaultValues.verbose,
                      help="Print information about directories being inspected, and possibly additional information.")
    parser.add_argument('-vc', '--verbose-check', action='store_true', dest='verbosecheck',
                      default=defaultValues.verbosecheck,
                      help="Print the name of the directory being checked. If the --verbose option is specified then this information is also printed.")
    parser.add_argument('-vi', '--verbose-ignore', action='store_true', dest='verboseignore',
                      default=defaultValues.verboseignore,
                      help="Print the name of the directory being ignored. If the --verbose option is specified, then this information is also printed.")
    parser.add_argument('pathlist', action='store',
                      nargs='*',
                      default=defaultValues.pathlist,
                      help="One or more directory paths on which to act. (Default: act on the current directory)")

    opts = parser.parse_args()

    if opts.showVersion:
        print versionString
        sys.exit()

    skipdir = opts.skipdir.split(':')

    actionsAttempted=0
    dirsIgnored=0
    pathitemError = False

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
        if (not os.path.exists(pathitem)):
            print '\nERROR: The specified directory name does not exist: "'+pathitem+'"'
            pathitemError = True
        elif (not os.path.isdir(pathitem)):
            print '\nERROR: The path specified is not a directory (possibly a file?): "'+pathitem+'"'
            pathitemError = True

    if pathitemError:
        print
        parser.print_help()
        sys.exit()

    for pathitem in opts.pathlist:
        for root, dirs, files in os.walk(pathitem):
            if (opts.verbose | opts.verbosecheck):
                print "Checking: " + root

            for thisskipdir in skipdir:
                if thisskipdir in dirs:
                    dirs.remove(thisskipdir)
                    dirsIgnored += 1
                    if (opts.verbose | opts.verboseignore):
                        print "Ignoring: " + os.path.join(root, thisskipdir)

            if (not opts.remove) and (not files) and (not dirs):
                fn = os.path.join(root, opts.filename)
                print actionDesc, fn
                actionsAttempted += 1
                if not opts.dryrun:
                    open(fn, 'w')

            elif opts.remove and (opts.filename in files):
                fn = os.path.join(root, opts.filename)
                print actionDesc, fn
                actionsAttempted += 1
                if not opts.dryrun:
                    os.remove(fn)

        print
        print 'Starting path:', os.path.abspath(pathitem)
        print 'Directories ignored: ', dirsIgnored
        print actionSummary, actionsAttempted

if __name__ == '__main__':
    version_check()
    main()