from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import *

if __name__ == "__main__":
    while True:
        try:
            # Create a new session
            session = Session()

            # Perform the 'like' action with specified parameters
            session.like(amount=5000000, ratio="95%", sleep=5)

        except Exception as e:
            # Print the exception details
            print(f"An exception occurred: {e}")

