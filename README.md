# Coding challenges solution
## Back-end Challenge

Imagine you are writing a function within a Django application to parse JSON data. In the Python file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/json-cleaning and then clean the object according to the following rules: Remove all keys that have values of N/A, -, or empty strings. If one of these values appear in an array, remove that single item from the array. Then print the modified object as a string.

Example Input
> {"name":{"first":"Penguin","middle":"N/A","last":"MR."},"age":27}

Example Output
> {"name":{"first":"Penguin","last":"Mr."},"age":27}
