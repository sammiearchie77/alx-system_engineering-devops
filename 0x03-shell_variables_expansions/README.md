# 0x03. Shell, init files, variables and expansions


## Learning Objectives
> At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
1. What happens when you type $ ls -l *.txt

## Shell Initialization Files
1. What are the /etc/profile file and the /etc/profile.d directory
2. What is the ~/.bashrc file

## Variables
1. What is the difference between a local and a global variable
2. What is a reserved variable
3. How to create, update and delete shell variables
4. What are the roles of the following reserved variables: HOME, PATH, PS1
5. What are special parameters
6. What is the special parameter $??

## Expansions
1. What is expansion and how to use them
2. What is the difference between single and double quotes and how to use them properly
3. How to do command substitution with $() and backticks
4. Shell Arithmetic
5. How to perform arithmetic operations with the shell

## The alias Command
1. How to create an alias
2. How to list aliases
3. How to temporarily disable an alias


# 200~Requirements

> ## General
> Allowed editors: vi, vim, emacs
> All your scripts will be tested on Ubuntu 20.04 LTS
> All your scripts should be exactly two lines long ($ wc -l file should print 2)
> All your files should end with a new line (why?)
> The first line of all your files should be exactly #!/bin/bash
> A README.md file, at the root of the folder of the project, describing what each script is doing
> You are not allowed to use &&, || or ;
> You are not allowed to use bc, sed or awk
> All your files must be executable

# Tasks
> 0-alias is a script that creates an alias.
> 1-hello_you is a script that prints hello user, where user is the current Linux user.
> 2-path is a script that adds /action to the PATH.
> 3-paths is a script that counts the number of directories in the PATH.
> 4-global_variables is a script that lists environment variables.
> 5-local_variables is a script that lists all local variables and environment variables, and functions.
> 6-create_local_variable is a script that creates a new local variable.
> 7-create_global_variable is a script that creates a new global variable.
> 8-true_knowledge is a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
> 9-divide_and_rule is a script that prints the result of POWER divided by DIVIDE, followed by a new line.
> 10-love_exponent_breath is a script that displays the result of BREATH to the power LOVE.
> 11-binary_to_decimal is a script that converts a number from base 2 to base 10.
> 12-combinations is a script that prints all possible combinations of two letters, except oo.
> 13-print_float is a script that prints a number with two decimal places.
> 14-decimal_to_hexadecimal is a script that converts a number from base 10 to base 16.
> 100-rot13 is a script that encodes and decodes text using the rot13 encryption.
> 101-odd is a script that prints every other line from the input, starting with the first line.
> 102-water_and_stir is a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.
