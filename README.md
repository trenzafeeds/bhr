# Usage Instructions

Right now the program is only configured to use Dihedral Groups
when run directly from the command line. You will have to import
the functions into Sage and use them at the prompt (and I'll show you
how below) in order to use other groups.

The syntax for a command is:
```
sage bhr.py [N or N_LOW N_HIGH] [OPTIONS]
```
For the given N-Group or all N-Groups from N_LOW to N_HIGH - 1,
bhr.py will write all "failing" multisets to a corresponding `.log`
file in the `log` directory.

### Options

You can use a couple of optional arguments after the one or two
integer arguments provided.

##### `-t` or `--type`

Follow this with an argument denoting the type of group that should be
calculated. If this option is not set the program defaults to
Dihedral Groups.

##### `-v` or `--verbose`

Runs the program verbosely, printing a status update to stdout at each
new step of computation.

##### `-s` or `--silent`

Runs the program silently, with almost no printing to stdout.