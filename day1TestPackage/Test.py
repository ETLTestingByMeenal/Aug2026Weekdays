# Import the functions from the PythonPackageDemo package
from day1PythonPackageDemo.Greetings import hello,bye

# Now, use the functions in Test.py
def test_call():
    hello("Rakesh")
    bye("Meenal")

if __name__ == "__main__":
    test_call()





