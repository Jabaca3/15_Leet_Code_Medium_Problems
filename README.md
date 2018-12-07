# 15_Leet_Code_Medium_Problems
School: Here is my IDEAL definition and Duke 7 steps for 15 medium leet code problems


15 LeetCode Medium Difficulty Problems



Problem 1.

https://leetcode.com/problems/range-sum-of-bst/
Range sum BST.

Questions: No question Problem Was very descriptive

I - The problem is to accumulate the data inside of a node with boundaries
D- Sum the tree and traverse the nodes.
E - Some options may be iterative of recursive
A – I started to create different smaller scenarios in order to adjust my idea
L – Creating a separate method, and create a variable to hold the accumulated value.

Duke 7
1.	The first example I had created was a single tree with 2 leaves, to accumulate the sums of them within the boundaries.
2.	For the second step I had diagramed the exact execution of solving this problem. To simplify it.
3.	The main issue I generalized was finding out how to store the solution.
4.	I had diagrammed my solution and sketched out edge cases
5.	I ran a few inputs of my own to make sure that nothing can go wrong
6.	I tested the solution but it had failed due to syntax
7.	Once I had debugged the syntax the solution worked perfectly fine


Problem 2.
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
Max Increase to Keep City Skyline
	
Questions: 
I had an overwhelming amount of questions to this problem when it came to understanding the actual question. I wouldn’t like to go through each question, but the majority of them where like: I don’t get it? Or I’m not sure what you’re asking for? But rereading the problem multiple times I was able to understand the concept

I – The problem is to update values in the grid without messing up the skyline limit
D – The way to solve this problem is to get the max value of the rows and the col
E – The best exploration would’ve probably been how to save values in the row/col.
A – I decided to write and n solution that seemed obvious at first glance.
L – There probably was a better solution to the problem but for the sake of solving it,  
       I was please

Duke 7 
1.	I created a smaller grid of the problem and ran for Loops to extract max elements
2.	I had taken note of the for loops demonstrated to apply them elsewhere
3.	Using these for loops I began assuming they will simply work on these kind of larger problem
4.	I made sure to test out possible edge cases like jagged arrays and negative integers
5.	Translating the loops to code was fairly simple, there were no issues in doing so.
6.	There was a syntax error in the program that I had to debug, but was successful
7.	The solution worked just as planned 


Problem 3
https://leetcode.com/problems/encode-and-decode-tinyurl/
Encode and Decode TinyURL

Question:
I wasn’t sure how they wanted me to hash the actual URL. I had a bunch of questions on what they wanted, if they wanted me to shrink it and exclude all the information. I was actually confused of the logic behind shrinking and replicating. I started to assume using some kind of compression algorithm that can be decompressed, but was confused.

I – The problem was to compress a URL into a decompressable URL
D – To solve this problem I needed to come up with a compression algorithm
E – I spent around 30 minutes decided how I can compress an entire String
A – I began writing ascii value conversions and maybe % the values
L – I felt I spent too much time writing a compression that I didn’t value how compressed it should be

Duke 7
1.	I wrote a string : “cars are cool” Then I figured I would parse to ascii and compress somehow
2.	With doing 1. I then asked questions with how far do I have to shrink my url? On paper
3.	I wrote down some ascii value compressions to see what the outcome would be
4.	I tested edge cases like getting ascii value of a number which was odd. 
5.	I through in some inputs but always found a way to break my code
6.	Compression failed on inputs
7.	Attempted to debug but realized I was spending too much time on the problem


Problem 4
https://leetcode.com/problems/maximum-binary-tree/
Maximum Binary Tree

Question:
This problem was very descriptive and I did not have any questions.

I – The problem is to return a tree given an array, but it is a max tree
D – Some trick may be that larger inputs are later in the array
E – I didn’t really explore different solutions because I felt the one I had satisfied my expectations
A – I created the algorithm pretty quickly with success
L – Maybe I could’ve taken my time solving this problem and explore solutions


Duke 7
1.	I decided to take the smallest problem first, and slowly expand it.
2.	With writing down this information on paper, I found very simple solutions with just grabbing the max of the entire array     and starting with that value first
3.	With getting the max value the problem became very simple, because I was just to build off of that
4.	I didn’t really have much edge cases to test because the base case would catch almost everything
5.	I threw in some input and everything worked out well
6.	The inputs came out correct and I was satisfied with the answer. However it can be improved.
7.	There was not really any debugging, because the solution was fairly simple


Problem 5
https://leetcode.com/problems/insert-into-a-binary-search-tree/
Insert into a Binary Search Tree
	
Questions:
There were no questions everything was straight forward and understandable.

I – going into this question it seemed very simple, I thought there might be a trick laying ahead, but nope.
D – The problem was the insert a new node into a BST
E  - I didn’t really explore any solution because it was fairly simple
A – I wrote the code very quickly and I had a syntax error in the base case, but fixed it rather quickly.
L – Maybe I solved this problem too fast, but I’m still sure there isn’t a more optimal solution to the problem.

Duke 7
1.	With most problem dealing with BST’s I normally Start with the most simple problem that way I can create my base case to       handle None value and such.
2.	I got the information down on paper and everything went as planned.
3.	The base case was probably the ‘trick’ in this problem but It didn’t distract me by much.
4.	The inputs I used worked perfectly fine on paper because of almost no edge cases in trees.
5.	Inputs worked fine
6.	Everything checked out with no bugs so I submitted the problem and ignored 7.


Problem 6.
	https://leetcode.com/problems/find-and-replace-pattern/
	Find and Replace Pattern

Questions:
Can there be different types of patterns that I Need to look out for?
	
I – The problem was to detect a pattern in the strings of the array.
D – Writing an algorithm to detect the patter was quite odd
E – I tried exploring as many possibilities as I can like, Tracking repeats and such. But the 
	  The code started to become very messy and complex which I did not enjoy.
A – The acting part of this code really threw me off
L – I feel like I had spent too much time attempting to figure out the solution, I probably should’ve checked the discussion       tab to understand the logic behind solving this problem.

Duke 7
1.	I created an example and decided that the problem can have many different patters and I wouldn’t be able to keep track of     all those, and there must be a built in function for this.
2.	I had written down the things I did to check for patters.
3.	At this point in the problem I had used up too much of my time and decided to check the answer.


Problem 7.
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid
Minimum Add to Make Parentheses
	
Questions:
At the beginning of this problem I was unsure if I can do this with N space or maybe recursively. If this was an interview I would’ve probably asked what the interviewer would prefer for a solution.

I – The problem Is to return an Int of the number of needed parenthesis to make it value
D – I needed to count the parenthesis that were left out.
E – I tried to implement the answer without using a stack, but I became sort of confused, so I went back to the traditional       solution.
A – I coded everything on paper to make sure it check out, and it did.
L – I kind of rushed this problem and probably could’ve came up with a better solution

Duke7
1.	I took a very small example where there was one open parenthesis and made a count for it. Then If it needed its opposing       side, I would just return the count, else I would remove the count.
4.	Doing this by hand I started to run into errors, so I changed my form of solving this problem with instead using a stack.
5.	Putting this information into code there were an enormous amount of syntax errors that needed debugging
6.	I debugged all the syntax and then there was a logic error when checking if the parenthesis was actually correct already.
7.	I debugged this issue and finished the solution


Problem 8
	https://leetcode.com/problems/binary-tree-pruning/
	Binary Tree Pruning
	
Questions:
The question was descriptive and I didn’t have any clarifying questions.

I – The problem is to remove nodes from the binary tree without actually breaking the tree
D – How to solve this problem was quite interesting. First you need to check the value of the Node and act on it.
E – There didn’t seem much different exploration when it comes to trees.
A – I decided to act on this problem by writing the base cases to give me a clear understanding of what I need to do.
L - looking back on this problem I began to enter the depths of recursion and confuse myself. I should avoid doing that at all     cost, but sometimes it happens.

Duke 7
1.	Always for trees I start with the smallest problem to solve. This normally helps my make the proper base cases.
2.	I wrote down my solutions
3.	I started to make sure I didn’t miss any base cases 
4.	I tested my code by hand and found that I actually had an issue of there im checking my values.
5.	N/a
6.	My testing also suggested that the logic I was using with my base cases was incorrect
7.	All bugs fixed (They were logic bugs)


Problem 9
https://leetcode.com/problems/find-all-duplicates-in-an-array
Find All Duplicates in an Array

Questions:
There were not questions for this problem for it was very straight forward

I – The problem is to find the duplicates and return them in a list
D – The way I wanted to solve this problem was using a set the check for duplicates
E – I’m sure there were better was to do this without O(N) space
A – I coded the set first try and everything worked out
L – Given enough time I can make a better solution

Duke 7
To be honest I didn’t really follow Duke 7 for this example. I felt that I had solved this particular problem multiple times and solution has never changed for me. I felt I had this set checker as a tool under my belt.


Problem 10
	https://leetcode.com/problems/teemo-attacking/
	Teemo Attacking

Questions: Because I am a big Lol player there were a few questions I did have to ask, but the questions instead seemed to be suggestions to add more complexity so I ignored the whole idea on its own.

I – The problem is given two inputs which is a list and an Int I have to calculate the total poison time condition
D – To solve this problem all I had to do was simple calculations
E – I didn’t really explore other solutions
A – I coded the problem very quickly but ran into an issue of what I wanted to return
L – I felt I could’ve solved this problem faster if I took time to think.

Duke 7:
1.	I took a very basic example with two very small inputs [1] , 2
2.	I solved it simply on paper with no code, just my brain
3.	I thought with complication there needs to be more checks of this problem
4.	I tried coding a solution but it came out a little flawed
5.	N/a
6.	Testing the code there was small issue in my calculation, it turns out I wasn’t getting the min correctly
7.	After debugging the code there were no more logic/bug issues.


Problem 11
https://leetcode.com/problems/flip-equivalent-binary-trees/
Flip Equivalent Binary Trees

Questions:
I had a few questions of determining whether the tree is a flipEquivalent. I don’t actually know what the question Is asking, I’ve written code to flip trees, but flip equivalent seems very bizarre to me. How many nodes, or trees would I need to flip to know that it’s not flip equivalent. What if I were to flip nodes with not its equivalent, but the parent of the opposing tree. 

I – The problem is to identify if a tree is flip equivalent
D – If you keep flipping a tree x at some point you can make it equal to tree y
E – I could not even think of a simple solution to this problem, I was very confused and lost
A – I tried to break the solution down into smaller quantities but still seemed confused
L – Looking back at this problem, I feel that I should’ve gone to the discussion tab to seek an understanding of the problem.

Duke 7 :

1.	I wrote down only 3 nodes and moved values around to determine if flipping would give me an answer, but I only had more       questions.
2.	I wrote down examples, but still had no understanding of the question.


Problem 12:
	https://leetcode.com/problems/sort-characters-by-frequency/
	Sort Characters By Frequency
	
I – Sort the string by frequency as oppose to a alphabetical sort
D – the problem is that storing the information when passing through the string is the Issue
E – I did happen to explore other solutions, but most of them where making my own object to store the information
A – I started coding my idea which was throwing everything in a dictionary and then sorting the dictionary.
L – Looking back I’m sure there is a better solution to this problem.

Duke 7 :
5. For this problem I was confident my solution was accurate and would solve all possible instances of the problem
6. I tested out the code and had some syntax errors, but where simple to cure.
7. The output after debugging was as expected.


Problem 13.
	https://leetcode.com/problems/single-element-in-a-sorted-array
	Single Element in a Sorted Array

Questions: 
A huge question I had was to make sure that the elements where not appearing more than twice, because if that was the case my ideal solution would not work for this problem.

I – there is a single element in the array that doesn’t have a duplicate
D – it Is my job to find that element and return it
E – I’m sure there is an O(n) solution to this problem. That I did attempt to discover, but didn’t have much luck
A – I coded my ideal solution and everything worked without any errors
L – Looking back I feel like I’m trying too hard to speed through these 15 problems and not actually exploring how I should

Duke 7:
5. I felt the solution I had was very logical and worked perfectly given the constraints of the duplicates only having a single partner.
6. Tested and worked!

Problem 14:
https://leetcode.com/problems/find-the-duplicate-number

	Find the Duplicate Number
	
Question:
I understood the question pretty well, there isn’t too much complication to this problem.

I – For this problem I’m looking for the number who does have a duplicate
D – This problem is the inverse of the previous one
E – Again I’m sure there is an o(n) solution that I could not discover for this problem
A – I coded the problem and it worked perfectly as planned first try!
L – Again I’m speeding through the Exploration part of Ideal and give up too fast.

Duke 7:
5. For this problem I was confident my solution was accurate and would solve all possible instances of the problem
6. I tested out the code and had some syntax errors, but where simple to cure.
7. The output after debugging was as expected.

Problem 15:
	https://leetcode.com/problems/edit-distance/
Edit Distance

Question:
The first time this problem was shown to me was quite confusing. My questions consisted of: What happened if I’m comparing to an empty string? What if a string is very identical and removal of lets say the middle character gave a solution? How is it possible to even solve for that?

I - The problem is calculating the lesser amount of moves to make one string identical to 	another
D – The issue is differentiating whether or not a simple replacement or deletion will help 	you in the future
E - The first approach I took to solve this problem was a mathematical approach. I believe 	that It may be possible to get an    answer by just looking at the sizes and what they have in 	common for deleting and inserting both take one step
A – After taking a course that tackled dynamic programing, they had mentioned this 	problem and how it can be solved using DP.     I understood the logic and decided to start 	coding it
L – Looking back I don’t think I would’ve solved this problem if it was never introduced 	to my eyes in a classroom, the logic     was incredible and the solution even more so.

Duke7:
1.	The example I had done was two strings – ‘cars’ and ‘carts’ even though they aren’t words This is a really good example because of how identical they are.
2.	I set up the matrix ready for dynamic programming and began understanding the logic of how to ensure I don’t make a mistake by calculating
3.	N/a
4.	I had solved many test cases by hand using a grid and believed I was ready to code
5.	Once coding I ran into a few issues such as comparisons and such, but easily debuggable
6.	I ran a test on my string that I created and they worked!
7.	There were a few instances where I needed to debug my for loop and such, but everything went well.
