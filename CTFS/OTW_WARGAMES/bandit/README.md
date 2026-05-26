This is overthewire wargemes passwords as of Tuesday May 2026 :

![wargames](wargames_1983.gif)

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


passwd for bandit5:

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
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
```

Bandit Level 9 → Level 10

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.


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

![img](bandit10.png)

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

![img](bandit12.png)

commands:
	xxd -r <data.txt> // to reverse it to binary
	
	bzip -d <file.bz>

	gzip -d <file.gz>
	
	tar -xf <file.tar>

password for bandit 14
	
	FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn


#	bandit 14


GOAL:

	Bandit Level 13 → Level 14
	The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.
	If you need help with this level: a hint file can be found in the home directory.
	Make sure to read the error messages as they are informative.

login command:

	 ssh -p 2220 bandit13@bandit.labs.overthewire.org

commands:

	scp -P 2220 bandit13@@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .

	// didn't really know that using scp you must specify port with -P 

	// login with the sshkey now

	// assign permission to the keysudo chmod 600 sshkey.private 

	ssh -p 2220 -i sshkey.private bandit14@bandit.labs.overthewire.org

	// cat /etc/bandit_pass/bandit14


![img](bandit13_fail.png)


![img](bandit13.png)


password for bandit 15:

	MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS


# bandit 15

GOAL:

	Bandit Level 14 → Level 15 ✅
	The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

login command:

	ssh -p 2220 bandit14@bandit.labs.overthewire.org

commands:
nc localhost 30000

// submit password for bandit15 here

password for bandit 16:
	8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

#	bandit 16

GOAL	
	Bandit Level 15 → Level 16 ✅
	The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption
	
login commands:

commands:

openssl s_client -connect localhost:30001

// issue the password for bandit 16 when prompted with "read R BLOCK"


![img](bandit15.png)


password for bandit17:
	kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
