# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x*x*x

def factorial(x):
    assert(x >= 0)
    ans = 1
    while x > 0:
        ans = ans*x
        x-=1
    return ans

def count_pattern(pattern, lst):
    i = ans = 0
    l = len(pattern)
    while i < len(lst):
	if pattern == lst[i:i+l]:
        	ans+=1
        i+=1
    return ans


# Problem 2.2: Expression depth

def depth(expr):
    currentLists = None
    depth = 0
    def hasLists(ls):
	return len([item for item in ls if isinstance(item,(list,tuple))]) > 0
	 
	 
    def getSublists(ls):
	 result = []
	 for sublist in ls:
		 if isinstance(sublist,(list,tuple)):
			 result+= [item for item in sublist if isinstance(item,(list,tuple))]
	 return result

    if isinstance(expr,(list,tuple)):
	    depth+=1
	    currentLists = expr
            while hasLists(currentLists):
		 depth+=1
	         currentLists = getSublists(currentLists)
	         #print currentLists
            return depth
    else:
        return 0
                  

# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    subtree = tree
    for i in index:
        subtree = subtree[i]
    return subtree



# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = "never"

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = "0"

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = "not at all"

# How many hours did this lab take?
HOURS = "3"
