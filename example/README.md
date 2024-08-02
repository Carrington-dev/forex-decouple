Running tests on a Python package is an important step in ensuring that your code works correctly. You can use a testing framework like `unittest` or `pytest` to execute your tests. Here's a guide on how to set up and run tests for your Python package using both frameworks.

### Using `unittest`

1. **Organize Your Tests:**

   Ensure that your test files are located in the `tests/` directory and follow a naming convention such as `test_*.py`.

2. **Write a Test Case:**

   Here is an example of a test file using `unittest`:

   ```python
   # tests/test_module1.py

   import unittest
   from my_package.module1 import hello_world

   class TestModule1(unittest.TestCase):
       def test_hello_world(self):
           self.assertEqual(hello_world(), "Hello, world!")

   if __name__ == '__main__':
       unittest.main()
   ```

3. **Run Tests:**

   You can run all tests in the `tests/` directory by executing the following command in your terminal:

   ```bash
   python -m unittest discover -s tests
   ```

   This command uses the `unittest` module to discover and run all test cases in the specified directory.

### Using `pytest`

1. **Install `pytest`:**

   If you haven't already installed `pytest`, you can do so using pip:

   ```bash
   pip install pytest
   ```

2. **Write a Test Case:**

   You can use the same test structure, but `pytest` can work without classes. Here's how you might write a test:

   ```python
   # tests/test_module1.py

   from my_package.module1 import hello_world

   def test_hello_world():
       assert hello_world() == "Hello, world!"
   ```

3. **Run Tests:**

   To run all tests with `pytest`, simply execute the following command in your terminal:

   ```bash
   pytest tests/
   ```

   `pytest` will automatically discover and execute all test functions in the specified directory.

### Running Tests Automatically

For automated testing, you can integrate these tests into a continuous integration (CI) system like GitHub Actions, Travis CI, or Jenkins. This will ensure your tests run whenever you make changes to your code.

### Additional Tips

- **Test Coverage**: Use tools like `coverage.py` to measure how much of your code is covered by tests.
- **Test Fixtures**: Utilize setup and teardown methods (or `pytest` fixtures) to manage test state and resources.

By following these steps, you can effectively run and manage tests for your Python package, helping to maintain code quality and reliability. Let me know if you have any further questions!