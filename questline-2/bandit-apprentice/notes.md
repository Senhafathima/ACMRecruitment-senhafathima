 ## Bandit Apprentice Notes

 This file contains my notes and commands for solvig OverTheWire Bandit levels 0 to 10
 
## Level 00
Command to connect:ssh bandit0@bandit.labs.overthewire.org -p 2220

Password:bandit0

Solution steps:Listed the files using 'ls'.
Found the file named 'readme'.
Used 'cat readme' to read the file content.
Retrieved the password for level 1

## Level 01

Command to connect :ssh bandit1@bandit.labs.overthewire.org -p 2220

Password:ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

Solution steps:-Listed all files using 'ls -la'.
-Found a file named '_'.
-Used 'cat./-' to read the file contents.
-Retreived the password for level 2.

## Level 2
Command to connect:ssh bandit2@bandit.labs.overthewire.org -p 2220

Password:263JGJPfgU6LtdEvgfWU1XP5yac29mFx

Solution steps:-Listed all files using 'l'.
-Found a file named '--spaces in this filename--'.
-Used 'cat -- "--spaces in this filename--" to read the file contents.
-Retreived the password for level 3.

## Level 3
Command to connect:ssh bandit3@bandit.labs.overthewire.org -p 2220

Password:MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

Solution steps:-Listed all files using 'ls -la'.
-Found output 'inhere'.
-entered into inhere using 'cd inhere'.
-Listed all files using 'ls -la' in inhere.
-Found a file named '...Hiding-From-You.
-Used 'cat ...Hiding-From-You' to read the file contents.
-Retreived the password for level 4.

## Level 4
Command to connect:ssh bandit4@bandit.labs.overthewire.org -p 2220

Password:2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

Solution steps:-Listed all files using 'ls'.
-Found 'inhere'.
-Entered in to inhere using 'cd inhere'.
-List all file using 'ls -la' in inhere.
-Got files named 'file00,file01,file02,file03,file04,file05,file06,file07,file08,file09'.
-Used "cat./- 'filename'" for each to read the file contents.
-Retreived password for level 5 from file07.

## Level 5
**Goal:**Find password for level 6 hidden in one of the directories in 'inhere'.

Command to connect:ssh bandit5@bandit.labs.overthewire.org -p 2220

Password:4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

**Steps and commands:'''bash
                       cd inhere
                       ls -la
-lists all directories like maybehere00,maybehere01,etc
check inside each directory
 '''bash
      find . -type f -size 1033c -exec cat {} \;
-Retreived password for level 6.

## Level 6
**Goal:**Find the password for level 7
 Command to connect:ssh bandit6@bandit.labs.overthewire.org -p 2220

 Password:HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
**Hints / Proprties of password:
 1.Owned by user bandit7
 2.owned by group bandit6
 3.size in 33bytes

***Commands used:
 Search the entire server for the password file with given property.
command:'find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null'.

Display the contents of the password file
got '/var/lib/dpkg/info/bandit7.password'.
-Used 'cat /var/lib/dpkg/info/bandit7.password'.
-Retreived password for level 7.
