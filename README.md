# coderbyte-json-solution
##Back-end Challenge
Imagine you are writing a function within a Django application to parse JSON data. In the Python file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/json-cleaning and then clean the object according to the following rules: Remove all keys that have values of N/A, -, or empty strings. If one of these values appear in an array, remove that single item from the array. Then print the modified object as a string.

Example Input
{"name":{"first":"Daniel","middle":"N/A","last":"Smith"},"age":45}

Example Output
{"name":{"first":"Daniel","last":"Smith"},"age":45}
Browse Resources
Search for any help or documentation you might need for this problem. For example: array indexing, Ruby hash tables, etc.
