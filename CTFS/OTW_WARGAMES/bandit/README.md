This is overthewire wargemes passwords as of 2026 May:
bandit0 password:
 bandit0
#	bandit1:
ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

#	bandit2:
command:
cat ./-

![img](bandit1.png)

passwd: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx

#	bandit3:
login:
	ssh -p 2220 bandit2@bandit.labs.overthewire.org
command for getting this password:
	cat ./"--spaces in this filename--"

![img](bandit2.png)

password obtained:
		MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

#	bandit4:
login:	 ssh -p 2220 bandit3@bandit.labs.overthewire.org

commands:
cat "...Hiding-From-You"	

![img](bandit3.png)

passwd:
	2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
# bandit 5
login:
	 ssh -p 2220 bandit4@bandit.labs.overthewire.org
commands:
	find . | xargs file | grep text 
// this command find any human readable file in the current directory

![img](bandit4.png)

password for bandit 6:
	4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
# 	bandit 6
login command:
	ssh -p 2220 bandit5@bandit.labs.overthewire.org
commands:
	find * -type f -size 1033c

![img](bandit5.png)

password for bandit7 :
	HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
# bandit 7

login commands:

	 ssh -p 2220 bandit6@bandit.labs.overthewire.org

commands:
find / -type f -user bandit7 -group bandit6

![img](bandit6.png)

password for bandit 8:
	morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

# bandit 8 
GOAL:
```
Bandit Level 8 → Level 9
```
The password for the next level is stored in the file data.txt next to the word millionth
```	
login:
 ssh -p 2220 bandit7@bandit.labs.overthewire.org

![img](bandit7.png)

commands:
cat data.txt | grep "millionth"

password for bandit9:
	 dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc



# bandit 9

GOAL:
```
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once
```

![img](bandit8.png)

commands:
cat data.txt | sort | uniq -u

password for bandit 10
	4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

#	bandit 10
login command:
	 ssh -p 2220 bandit9@bandit.labs.overthewire.org
GOAL
```
Bandit Level 9 → Level 10
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
```

![img](bandit9.png)

commands:
	 cat data.txt | strings | grep "=="

password for bandit 11:
	FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey


#	bandit 11

GOAL:
```
The password for the next level is stored in the file data.txt, which contains base64 encoded data
```
login command:

	ssh -p 2220 bandit10@bandit.labs.overthewire.org
commands:

echo "VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg" | base64 -d

password for bandit 12:
	dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

# bandit 12

GOAL:
```
Bandit Level 11 → Level 12
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
```
login command:
 ssh -p 2220 bandit11@bandit.labs.overthewire.org
commands:

![img](bandit11.png)

// site: https://www.dcode.fr/rot-13-cipher

rot-13
password for bandit 13:
	7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

#	bandit 13

GOAL:
```
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)
```
Login command:

 ssh -p 2220 bandit12@bandit.labs.overthewire.org

commands:


password for bandit 14



