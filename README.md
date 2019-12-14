## A Database of European's state capitals 🇪🇺
Welcome to the repository 'capitals'.

Team NMTP is pleased to have You here!

Downloading this repository, you have the chance to obtain an EU member state's capital instantly! 

But, before starting using the program, please follow the instructions. 

The first thing you should do is to download the repository and populate the database with your username and password. 

1. From your terminal, go into the ```'exam'```directory and then go to the ```'scripts'```one and run dbmanager.py.  Here you can add a username with the relative password. The arguments you must use are  ```-a```, followed by your username, and 
```-p``` followed by the password. 


```
[12/14/19]seed@VM:~/exam$
[12/14/19]seed@VM:~/.../scripts$ python3 dbmanager.py -a Paolo -p Zp7$.dag.rem97?
User Paolo succesfully added to data.db

```
   Note well: you must remember your password by heart, later it is necessary to authenticate yourself before starting using      the main.py module. By the way, after you have run the dbmanager.py module, your username and password are stored in a        database called data.db. ```Here your password is salted and the salted password is hashed one hundred thousands              times.``` 
   If you have successfully run ```dbmanger.py```, e.g. ```python3 dbmanager.py a-  .... -p .... ```you receive a message. This    message tells you have successfully added a new user to the database ```data.db```. Note well: you can authenticate            yourself, in the ```main.py module``` only with a user present in the ```data.db```. 


The next step involves running the ```main.py module```, where the core of the application resides, briefly, if the program detects the existence of your username and password in the database ```data.db``` you are allowed to receive the capital of the EU's state you have decided to known. Let's come back to the steps to follow. 

2. You were in the ```'scripts'``` directory. You can now exit it, and return to the ```'exam'``` one.  Here you can execute ```main.py``` but before doing so, read carefully the arguments that you can and those that you must use. The required            arguments are the following: 

    ```-c``` to check that your username is correct and to know if it is present in the data.db database. Note well: this           argument is required. 
 
    ```-p``` to check that your password is correct and to know if it is present in the data.db database. Note well: this           argument is required. 

   ```'state'``` (positional argument)  to know the EU's capital of the state you have entered, i.e. Italy or France. Note        well: this argument is required. 
 
 Here, an example. 
 
 ```
[12/14/19]seed@VM:~/.../scripts$  
[12/14/19]seed@VM:~/exam$ -c Paolo -p Zp7$.dag.rem97? Spain
Username Correct.
Password Correct.
You are allowed to access the program!
Madrid
 ```
   
## Interlude: Error messages and optional arguments.

If you have successfully authenticated yourself and you have inserted a valid EU state, you receive a positive message. Your username is correct, your password is correct, you have access to the program,  and a primary output for your typed EU state, in this case, ```Rome``` is printed. 

If you have misplaced your username or password, you receive an error message that invites you to solve the issue accordingly, whether it is a problem with the username or the password. Note well: if you try to insert a username or password that have not been registered to the database, you have no access to the program. In the same way, till your username and password are not correct, you do not receive the EU capital of the state typed in the command line.  
If you typed a state that is not in the EU, you would receive an error message, which invites to insert a valid EU state. 

  Note well: the name of the state should start with a capital letter, ```i.e. Italy or France, not italy or france.``` Wrong   misspelt states are not considered valid. In this case, an error message manifests again.

Example, with mispelled username or password, and state name with first lower case letter.  

 ```
[12/14/19]seed@VM:~/exam$ python main.py -c paolo  -p Zp7$.dag.rem97? Spain 
Invalid Username
Please, Check Your Username...

[12/14/19]seed@VM:~/exam$ python main.py -c Paolo  -p ZP7?$.dag.rex97 Spain 
Invalid Password.
Please, Check Your Password...

[12/14/19]seed@VM:~/exam$ python main.py -c Paolo  -p Zp7$.dag.rem97? spain 
Username Correct.
Password Correct.
You are allowed to access the program!
Sorry, spain does not seem to be an European state.

[12/14/19]seed@VM:~/exam$ python main.py -c Paolo  -p Zp7$.dag.rem97? Egypt 
Username Correct.
Password Correct.
You are allowed to access the program!
Sorry, Egypt does not seem to be an European state.

 ```

For more information, you can increase the output verbosity of the program, adding the (not required) optional argument, i.e., ```-v or -vv``` according to the more or less info you want. 
    
## Optional arguments: 

    - v to increase the output verbosity. 
    -vv to obtain more debug information. 

With the -v option, you obtain extra information about the positional argument, namely ```'the EU's state capital of Italy is Rome'```  instead of the mere output ``` Rome.``` 

``` 
[12/14/19]seed@VM:~/capitals$ python main.py -c Paolo  -p Zp7$.dag.rem97? Spain -v  
Username Correct.
Password Correct.
You are allowed to access the program!
The Eu state's capital of Spain is Madrid

``` 
With the -vv option, you obtain more debug information about what the program is currently doing. When finished with debug information, the capital of the EU' state, it is also displayed. 

``` 
[12/14/19]seed@VM:~/capitals$ python main.py -c Paolo  -p Zp7$.dag.rem97?7 Spain -vv
Username Correct.
Password Correct.
You are allowed to access the program!
Running main.py...
100% 
Extracting your input from csv file...
100%
Fiding matching value...
100%
Obtainng the name of the capital...
100%
Returning matched value...
100%
The Eu state's capital of Spain is Madrid

``` 

If you follow the instructions, everything works fine. 

Thanks for your attention.

Team NMTP


