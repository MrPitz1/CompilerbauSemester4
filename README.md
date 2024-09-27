# Python Dialekt Compiler

This program compiles a custom Python dialect that uses `{ }` instead of `:` and indentation for block structures, and uses `;` to separate lines (similar to C-style languages).



  ### Example:
  ```plaintext
  def foo(x) {
      if x > 0 {
          print("Positive");
      } else {
          print("Non-positive");
      }
  };
````

### How to use:
```
python3 main.py <input_file> <output_file>
```
if that doesnt work install the antlr4-python3-runtime:
```
pip install antlr4-python3-runtime
````