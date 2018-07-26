# codeforces-example-automatic-testing

After writing code for problems on codeforces.com, we generally test it out on the examples available on the problem page, this script automates that task.

How to use:

* First write your code 
* At the top of your your code file, add a single line comment with the link to the problem that you are solving.

![image](https://user-images.githubusercontent.com/36476228/43288642-237baa72-9146-11e8-84a6-b37c0f60c055.png)

* Run the code in terminal giving the path to file with code as command line arguements.

``` python3 automatic-testing.py A.cpp ```


![image](https://user-images.githubusercontent.com/36476228/43288762-7d857c96-9146-11e8-88ca-9ec008d38dd3.png)

The script first checks the example inputs and outputs and the allows you to further enter your own test data for testing.

More about the script: the script uses BeautifulSoup4 library in Python3

> Disclaimer: This is currently supported for C++, support for other languages maybe rolled out later on.



