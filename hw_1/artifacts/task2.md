```bash
amir@amir-TM1701:~/source/python-practice/hw_1$ python3 tail.py
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
amir@amir-TM1701:~/source/python-practice/hw_1$ cat file.txt 
first line

second line
third line

amir@amir-TM1701:~/source/python-practice/hw_1$ python3 tail.py file.txt
first line

second line
third line

amir@amir-TM1701:~/source/python-practice/hw_1$ cat file1.txt
line 1
line 2
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
line 11
line 12
amir@amir-TM1701:~/source/python-practice/hw_1$ cat file2.txt
line A
line B
line C
line D
amir@amir-TM1701:~/source/python-practice/hw_1$ python3 tail.py file1.txt file2.txt
==> file1.txt <==
line 3
line 4
line 5
line 6
line 7
line 8
line 9
line 10
line 11
line 12

==> file2.txt <==
line A
line B
line C
line D
amir@amir-TM1701:~/source/python-practice/hw_1$
```
