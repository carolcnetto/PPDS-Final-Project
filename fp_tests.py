"""
Created on Sun Mar 19 2023

@author: Maria Carolina C. Netto

This function creates a helper data to test the sample script created for 
the sample solution to the Python Programmign for Data Science project.
"""

# A Python script containing  at least 2 unit tests that checks my function
# Testing my own functions with pytest

import pandas as pd
from fp_functions import movie_cleaner_str

def test_movie_cleaner_str1():
    raw = {'movie_title': ["Snow White and the Seven Dwarfs", "Pinocchio", "Fantasia"], 
           'release_date': ['1937-12-21', '1940-02-09', '1940-11-13'], 
            'genre': ['Musical','Adventure','Musical'],
            'MPAA_rating': ['G', 'G', 'G'],
            'total_gross': ['$184,925,485','$84,300,000','$83,320,000'],
            'inflation_adjusted_gross': ['$5,228,953,251','$2,188,229,052','$2,187,090,808']}
    helper_data = pd.DataFrame.from_dict(raw)
    
    clean_str = movie_cleaner_str(helper_data)
    
    # Tests the shape of the dataframe. There are only 3 rows and 6 columns 
    assert clean_str.shape == (3, 6), "The dataframe is not of the expected dimensions"
    return

def test_movie_cleaner_str2():
    raw = {'movie_title': ["Snow White and the Seven Dwarfs", "Pinocchio", "Fantasia"], 
           'release_date': ['1937-12-21', '1940-02-09', '1940-11-13'], 
            'genre': ['Musical','Adventure','Musical'],
            'MPAA_rating': ['G', 'G', 'G'],
            'total_gross': ['$184,925,485','$84,300,000','$83,320,000'],
            'inflation_adjusted_gross': ['$5,228,953,251','$2,188,229,052','$2,187,090,808']}
    helper_data = pd.DataFrame.from_dict(raw)
    
    clean_str = movie_cleaner_str(helper_data)
    
    # A dataframe is the type of object being passed into the data argument
    assert True
    if not isinstance(helper_data, pd.DataFrame):
        raise TypeError("Data is not a dataframe")
    return
