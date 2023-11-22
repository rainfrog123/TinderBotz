'''
Created by Frederikme (TeetiFM)
'''

from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import *

if __name__ == "__main__":
    session = Session()

    # session.set_custom_location(random_location()[0], random_location()[1])
    
    # session.set_custom_location(latitude=50.879829, longitude=4.700540)

    session.like(amount=5000000, ratio="90%", sleep=5)

