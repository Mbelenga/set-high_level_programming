# 0x12. JavaScript - Warm Up

## Description

This project is part of the **JavaScript** curriculum and introduces the fundamentals of JavaScript programming.

The goal of this project is to learn how to use JavaScript for scripting, understand basic programming concepts, and become familiar with variables, data types, operators, functions, loops, and command-line arguments.

## Learning Objectives

At the end of this project, I should be able to explain:

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* The differences between `var`, `const`, and `let`
* The available data types in JavaScript
* How to use `if`, `if...else`, and `else if` statements
* How to use comments
* How to assign values to variables
* How to use `while` and `for` loops
* How to use `break` and `continue`
* What a function is and how to use it
* What a function that does not use a `return` statement returns
* How to use function parameters
* How to use strings and template literals
* How to manipulate objects and arrays
* How to import a file
* How to use `process.argv` to access command-line arguments
* How to use Node.js to execute JavaScript files

## Requirements

* Ubuntu 20.04 LTS
* Node.js
* JavaScript
* Semistandard

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd 0x12-javascript-warm_up
```

Check that Node.js is installed:

```bash
node --version
```

Check that Semistandard is installed:

```bash
semistandard --version
```

## Running JavaScript Files

JavaScript files can be executed using Node.js:

```bash
node filename.js
```

For example:

```bash
node 0-javascript_is_amazing.js
```

## Coding Style

This project follows the **Semistandard JavaScript style guide**.

To check the code for style errors:

```bash
semistandard *.js
```

## Tasks

The project contains several JavaScript exercises covering basic scripting concepts.

### 0. First constant, first print

Write a JavaScript script that prints:

```text
JavaScript is amazing
```

### 1. 3 languages

Print three different lines using JavaScript.

### 2. Arguments

Use `process.argv` to print a message depending on the number of arguments passed to the script.

### 3. Value of my argument

Print the first argument passed to the script.

### 4. Create a sentence

Print a sentence using two command-line arguments.

### 5. An Integer

Convert a command-line argument to an integer and print it.

### 6. Loop to languages

Use an array and a loop to print multiple languages.

### 7. I love C

Use a loop to print a sentence multiple times.

### 8. Square

Print a square using a character supplied through the command line.

### 9. Add

Create a function that adds two integers.

### 10. Factorial

Create a recursive function that calculates the factorial of an integer.

### 11. Second biggest!

Find and print the second largest integer in a list of arguments.

### 12. Object

Create an object and modify its properties.

### 13. Add file

Create a function that adds two integers and export it for use in another file.

## Key Concepts

### Variables

JavaScript provides different ways to declare variables:

```javascript
let name = 'Terrence'
const age = 20
```

### Functions

Functions allow reusable blocks of code to be created:

```javascript
function add (a, b) {
  return a + b
}
```

### Conditional Statements

```javascript
if (value > 0) {
  console.log('Positive')
} else {
  console.log('Not positive')
}
```

### Loops

A `for` loop can be used to iterate through an array:

```javascript
for (let i = 0; i < languages.length; i++) {
  console.log(languages[i])
}
```

### Command-Line Arguments

Node.js provides command-line arguments through `process.argv`:

```javascript
console.log(process.argv[2])
```

### Modules

Functions can be exported from one file and imported into another:

```javascript
module.exports = add
```

and:

```javascript
const add = require('./13-add')
```

## Testing

Run an individual script with:

```bash
node filename.js
```

Check JavaScript style with:

```bash
semistandard filename.js
```

## Author

**Mbelenga**

Frontier Institute of Technology
