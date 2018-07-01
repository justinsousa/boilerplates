#!/usr/bin/env python2.7
"""
overall doc string
"""
import argparse

MAJOR_VERSION = "1"
MINOR_VERSION = "0"
PATCH_VERSION = "1"
VERSION_TUPLE = (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)
VERSION_STRING = "{0}.{1}.{2}".format(MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)


def _get_cl_args():
    """
    utility function to parse cli args
    """
    argument_parser = argparse.ArgumentParser(description="Description of program", usage="%(prog)s example cli call", add_help=True)

    # required args
    # argument_parser.add_argument("-r", "--arequired", action="store", required=True)

    # standard args
    argument_parser.add_argument("-t", "--test", help="help text for arg", action="store")
    argument_parser.add_argument("--boolflag", action="store_true", help="some bool flag")

    # Common flags for programs
    # 'count' - This counts the number of times a keyword argument occurs. For example, this is useful for increasing verbosity levels
    argument_parser.add_argument("-v", "--verbose", action="count", help="enable verbose output")
    argument_parser.add_argument("--debug", action="store_true", help="enable debug mode")
    argument_parser.add_argument('--version', action='version', version="{0}".format(VERSION_STRING))

    return argument_parser.parse_args()

def _check_args(parsed_args):
    """
    function used to perform program specific validation on cli args
    raises Exceptions if problems found
    """
    return

def main():
    """
    docstring for main function
    """
    cl_args = _get_cl_args()
    _check_args(cl_args)


if __name__ == '__main__':
    main()
