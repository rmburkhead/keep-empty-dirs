keep-empty-dirs
===============

A Python script to add or remove a file to empty directories so that various version control systems retain them.

This script recurses through the given directories (or the current directory, by default), finds the empty subdirectories, and adds a file in each. This is used to mark all existing empty subdirectories in a hierarchy to be kept from deletion, or for the sentinels to be used to insure the directories are added to a version control repository that does not normally retain empty directories (e.g., Mecurial, Git).

For help and usage information specify the `--help` option on the command line:

    keep-empty-dirs.py --help

License and Copyright
=====================

In accordance with the original author's licensing, this is licensed under the [GNU General Public License v2 (GPL v2)](http://www.gnu.org/licenses/gpl-2.0.html). Please see the referenced web page, or the `LICENSE` file contained in this repostiory.

This work is Copyright &copy; Robert M Burkhead, 2013.
Portions of this work are Copyright &copy; Martin Blais, 2001-2008.

GPL v2 Modification Notice
==========================

The script found in this repository has been **MODIFIED** from the original, begining in October 2013, by Robert Burkhead.

* Original Author: Martin Blais (b _at_ furius _dot_ ca)
* Original Copyright: Copyright &copy; 2001-2008 Martin Blais. All Rights Reserved.
* Original License: This code is distributed under the GNU General Public License (assumed to be GPL v2)
* Original project page: http://furius.ca/pubcode/pub/conf/bin/keep-empty-dirs.html [(archive)](http://www.webcitation.org/6KBQMQ1zr)
* Original source: http://furius.ca/pubcode/pub/conf/bin/keep-empty-dirs [(archive)](http://www.webcitation.org/6KBQWif4g)
