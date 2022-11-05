# Simple Task Tracker

#### Brief: takes a task description, a categor (topic), and stores it in a .csv file for recording.

#### Full Description

Does what it says on the tin, it tracks tasks, simply.

I made this program to use at work. I needed to solve for a problem, in my job I perform dozens of tasks a day with a variety of different areas. Recently as I progressed in the company it became clear that I need a better time management system than what I already have, which is nothing. Specifically I wanted to know exactly what eats up my time at the office, and see if any reoganization is required. There actually isn't a single task tracking software that's used by us at the company (at least in my department) and all the ones I tried from the internet (e.g. Monday.com, clickup) were good, but they had a lot of non-optional features that I didn't really need and in the end using them became a task of its own. So I decided to build mine.

It needed to be:

1. Simple, I can log a task in barely more than the amount of time it takes me to write a description for it.

2. At a glance I could see what I have done.

This accomplished by a simple duo of functions, one to write (or rather, append) the task to a .csv file, and the other to extract it. Those 2 along with main() are what makes up my program.

## main()

Main starts a "While True" infinite loop then displays instructions for the program usage. The user is then prompted for an input. Anything outside 2 designated keywords (actually 3 but more on the third one in a bit) will be treated as a task to be logged.

If the user enters a task, they will then be prompted for the "Topic" which would be the category the task would be filed under. The program then takes the "task" and the "topic" and calls the function "track_this()" with them. Then the program loops again.

If the user inputs **Display**, case insensitive, using the function display() the program will display the tasts already in the .csv file + a summary by Topic.

If the user inputs **Exit**, case insensitive, the program will exit

If the user inputs **GlUrck**, case sensitive, this is the "hidden" input. It's only there because I was testing different ways of erasing tasks, something I might implement in the future, and ended up leaving it there as a placeholder for such a time.


## track_this()


This function takes the two inputs: task (called "action" in the function because naming conventions are hard) and "topic", and put them in a Dictionary called "line". Using open() in append mode the program opens the file 'lists.csv' (in case this is the first time the program is used it creates the file). Then csv.DictWriter() appends the dictionary "line" onto lists.csv.




## display()

Display uses open() in "r" mode, and then using csv.DictReader() it iterates over all the rows in the file lists.csv, for each row a dictionary is created with the key being the Action and the value being the Topic, each dictionary is then appended onto a list called "dicting".

At the same time, a list of "topics" is compiled and each occurence is counted. That is accomplished by creating a dictionary called "counts", for the first occurence the topic is entered as a key, with value 1. Each iteration the program checks if the topic is already in the dictionary, if it is the value is incremented, if not it's entered with value 1.

Both "dicting" and "counts" are then passed back to main where they are displayed using Tabulate and normal print() respectively.


## Future plans

1. Input validation, I want to make it so only specific values can be entered under Topic. I have to use the program for a while to know which possible values there are.

2. Implement a clear way to delete tasks or even clear the file.

3. Using NumPy, implement some actual analytics to the program.

I DO NOT plan to add any features that will making using the program any more complicated, nothing that will rely on extra input from the user. Knowing my ADHD brain if it takes more than a few seconds to input a task I will not be using it at all.
