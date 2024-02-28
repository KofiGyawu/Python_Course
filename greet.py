def greet(name):
    return f"Hello, {name}!"
# The editor is an incomplete code.
# Update the function greet_and_capitalize by calling the above defined functions inside it to get expected output
# Expected Results : Final Result: HELLO, ALICE!


def capitalize(text):
    return text.upper()


def greet_and_capitalize(name):
    # Update the code below this line
    return f"Hello, {name}!".upper()


# Call the functions
name = "Alice"
final_result = greet_and_capitalize(name)

# Display the results
print("Final Result:", final_result)
