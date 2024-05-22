import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

"""
#Example 1
def concepts():
    parser = argparse.ArgumentParser()
    parser.parse_args()

#Example 2
def the_basics():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    print(args.echo)

#Example 3
def positional_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number",
                    type=int)
    args = parser.parse_args()
    print(args.square**2)

#Example 4
def optional_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print("verbosity turned on")

#Example 5
def combining_pos_and_opt_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2

    # bugfix: replace == with >=
    if args.verbosity >= 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity >= 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)

#Example 6
def getting_more_advanced():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    answer = args.x**args.y
    if args.verbosity >= 2:
        print(f"Running '{__file__}'")
    if args.verbosity >= 1:
        print(f"{args.x}^{args.y} == ", end="")
    print(answer)
"""

'''
Example 7
                specifying_ambiguous_args
    When there is ambiguity in deciding whether an argument is 
    positional or for an argument, -- 
    can be used to tell parse_args() that everything after that 
    is a positional argument:

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('-n', nargs='+')
parser.add_argument('args', nargs='*')

# ambiguous, so parse_args assumes it's an option
parser.parse_args(['-f'])
usage: PROG [-h] [-n N [N ...]] [args ...]
PROG: error: unrecognized arguments: -f

parser.parse_args(['--', '-f'])
Namespace(args=['-f'], n=None)

# ambiguous, so the -n option greedily accepts arguments
parser.parse_args(['-n', '1', '2', '3'])
Namespace(args=[], n=['1', '2', '3'])

parser.parse_args(['-n', '1', '--', '2', '3'])
Namespace(args=['2', '3'], n=['1'])
'''

"""
Example 8
        Conflicting options
    So far, we have been working with two methods of an argparse.ArgumentParser instance. 
    Let’s introduce a third one, add_mutually_exclusive_group(). It allows for us to specify options that conflict with each other. 
    Let’s also change the rest of the program so that the new functionality makes more sense: 
    we’ll introduce the --quiet option, which will be the opposite of the --verbose one:

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

    That should be easy to follow. I’ve added that last output so you can see the sort of flexibility you get, i.e. 
    mixing long form options with short form ones.
    Before we conclude, you probably want to tell your users the main purpose of your program, 
    just in case they don’t know:

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")

    Note that slight difference in the usage text. 
    Note the [-v | -q], which tells us that we can either use -v or -q, 
    but not both at the same time:
"""

"""
Example 9
                How to translate the argparse output
    The output of the argparse module such as its help text and error messages are all made translatable using the get text module. 
    This allows applications to easily localize messages produced by argparse. See also Internationalizing your programs and modules.
    For instance, in this argparse output:

python prog.py --help
usage: prog.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

options:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet

    The strings usage:, positional arguments:, options: and show this help message and exit are all translatable.
    In order to translate these strings, they must first be extracted into a .po file. For example, using Babel, run this command:

pybabel extract -o messages.po /usr/lib/python3.12/argparse.py

    This command will extract all translatable strings from the argparse module and output them into a file named messages.po. 
    This command assumes that your Python installation is in /usr/lib.
    You can find out the location of the argparse module on your system using this script:

import argparse
print(argparse.__file__)

    Once the messages in the .po file are translated and the translations are installed using gettext, 
    argparse will be able to display the translated messages.
    To translate your own strings in the argparse output, use gettext.
"""
