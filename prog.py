import argparse

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
'''
Example 8
        Conflicting options

'''
