import os

def cls():
    """To clear screen after ending the run"""
    os.system('cls' if os.name == 'nt' else 'clear')

def temp():
    print(__name__)