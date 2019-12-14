## Test

As last step we test our code implementing three different functions in order to check three different aspect of our program.

To activate the test phase, it is necessary to use this command:

``` 
[12/14/19]seed@VM:~/exam$ python3 -m unittest -v -b tests/test_csv.py 
test_empty_datafile (tests.test_csv.TestMain) ... ok
test_no_datafile (tests.test_csv.TestMain) ... ok
test_valid_extension (tests.test_csv.TestMain) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

``` 

Through the module ```test_csv.py``` we check the ```test.py``` module in which there is our function that read the csv file. We are going to check the following conditions: 

1. The existence of the CSV file containing all the EU state with the matching capital;
2. The presence of data inside of the CSV file in order not to work on an empty file;
3. The extension of the file we want to use in order to handle only CSV files (that is the only format allowed by our code).

Note Well: Since we found some problmes, in order to run correctly this piece of program it is necessary to insert the path of the CSV according to your terminal files' collocation. More specifically you have to modify the path in two different point of the code:

1. In the file ```test_csv.py```, inside ```tests```, in line 3.

2. In the file ```test.py```, inside ```myfolder```, in line 18.

If you follow the instructions, everything works fine.

Thanks for your attention.

Team NMTP
