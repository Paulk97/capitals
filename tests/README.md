## Tests
As last step we test our code implementing three different functions in order to check three different aspect of our program.

To activate the test phase, it is necessary to use this command:

``` 
python3 -m unittest -v -b tests/test_csv.py


``` 

In the module ```TestMain1``` we check:

1. The existence of the CSV file containing all the EU state with the matching capital;
2. The presence of data inside of the CSV file in order not to work on an empty file;
3. The extension of the file we want to use in order to handle only CSV files (that is the only format allowed by our code).

In order to run correctly this piece of program it is necessary to insert the directory of the CSV file in two different point of the code:

1. In the file ```test_csv.py```, inside ```tests```, in line 3;
2 . In the file ```test.py```, inside ```myfolder```, in line 18;
3. In the file ```capitals.py```, inside ```myfolder```, in line 7.

If you follow the instructions, everything works fine.

Thanks for your attention.
Team NMTP
