'''
Created by Frederikme (TeetiFM)
'''

from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import *

if __name__ == "__main__":
    session = Session()
    session.like(amount=5000000, ratio="91%", sleep=3)