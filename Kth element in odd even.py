# Python3 implementation of the approach

# Function to return the kth element
# in the modified array
def getNumber(n, k) :

	# Finding the index from where the
	# even numbers will be stored
	if (n % 2 == 0) :
		pos = n // 2;
	
	else :
		pos = (n // 2) + 1;

	# Return the kth element
	if (k <= pos) :
		return (k * 2 - 1);
		
	else :
		return ((k - pos) * 2);

# Driver code
if __name__ == "__main__" :
	n = 8; k = 5;
	
	print(getNumber(n, k));

# This code is contributed by AnkitRai01
