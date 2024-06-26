# Report for Assignment 1

## Project chosen

Name: pygame

URL: https://github.com/pygame/pygame

We used lizard in the terminal to count the number of lines of code (NLOC). NLOC: 113408. From these NLOC, ~48992 were in Python as 43% of this project consists of Python.

Programming language: Python

## Coverage measurement

### Existing tool

We used the tool Coverage.py.
Steps we took to do the test:
1. Enter the repository path in terminal.
2. Inside the repository directory, we went to path "/test" by using `cd test`.
3. Execute the coverage tool on the inbuild unit tester with the command: `coverage run .`.
4. After execution, the command `coverage report` is ran to get the coverage test results which will be shown below.

## Screenshot of coverage results:

### Screenshot part 1
![Screenshot part 1](https://github.com/Niteshns/pygame/blob/main/screenshot/coverage_deel1.png)
### Screenshot part 2
![Screenshot part 2](https://github.com/Niteshns/pygame/blob/main/screenshot/coverage_deel2.png)


### Your own coverage tool

<The following is supposed to be repeated for each group member>

Group member: Nitesh Shahatoe

Function 1: surfarray_tags.py

Link to instrumentation: https://github.com/pygame/pygame/commit/7ba08bded73317c1e37927489ade6f6a0e2bf23a 

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

### A screenshot of the coverage results output by the instrumentation
![Screenshot instrumentation](https://github.com/Niteshns/pygame/blob/main/screenshot/screenshot_instrumentation_coverageresult_surfarray_tags.py.png).

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

Group member: Nitesh Shahatoe

Test surfarray_tags.py

Link to the new/enhanced test: https://github.com/pygame/pygame/commit/9adcfca75f797a6c74a0c9a315b5220d75a9daee

## Screenshot before enhanced coverage improvement
![Screen before enhanced coverage](https://github.com/Niteshns/pygame/blob/main/screenshot/surfarray_tags_coverage_test_before.png)


## Screenshot of enhanced coverage improvement
![Screenshot enhanced coverage](https://github.com/Niteshns/pygame/blob/main/screenshot/surfarray_tags_coverage_test.png)


<State the coverage improvement with a number and elaborate on why the coverage is improved>
The tests show some overhead tests. In our case, we will skip the package tests and will only look at the surfarray_tags.py. The coverage was previously 58%. The enhanced test has a coverage of 83%. The coverage is improved because I added two advanced tests to test whether or not the imported libraries worked. 
These newly added tests did not branch out much. There is only a small branch in the second test for the exception handling. This improved the branch coverage significantly. 

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
