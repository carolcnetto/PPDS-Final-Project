# A Python script containing at least 1 one well documented function (.py file) that you will use on my data
# flake8: noqa

import pandas as pd


def movie_cleaner_str(df):
    """
    Given a dataframe df = 'disney_movies_total_gross.csv':
    1-Remove any extra whitespace on columns 'movie_title' and 'genre'.
    2-Adjust the names in the columns 'movie_title' and 'genre' so that the first character in every word is upper case. # noqa: E501
    2-Fix dtype of Currency columns 'total_gross' and 'inflation_adjusted_gross' into 'int64' so we can perfom calculations. # noqa: E501
    3-Return a cleaner dataframe ready for analysis.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        The dataframe to be cleaned

    Returns
    -------
    pandas.core.frame.DataFrame
        The new cleaned dataframe

    Raises
    ------
    TypeError
        If the input argument df is not of type DataFrame

    Examples
    --------
    >>> movie_cleaner_str(movies)
        movie_title   release_date      genre  MPAA_rating  total_gross  inflation_adjusted_gross # noqa: E501
    0   Snow White..    1937-12-21    Musical            G    184925485                5228953251 # noqa: E501
    1   Pinocchio       1940-02-09  Adventure            G     84300000                2188229052 # noqa: E501
    """
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    df = df.assign(
        movie_title=df["movie_title"].str.strip().str.title(),
        genre=df["genre"].str.strip().str.title(),
    )

    df["total_gross"] = df["total_gross"].replace("[$,]", "", regex=True).astype(int)
    df["inflation_adjusted_gross"] = (
        df["inflation_adjusted_gross"].replace("[$,]", "", regex=True).astype(int)
    )  # noqa: E501
    return df


# -------------------------------------------


def list_repeted(seq):
    """
    Given a column with potential repeated items:
    1-Compare each item in the series to see if they are unique.
    2-Keek the ones that are not unique into a list.
    3-Return the list of the repeated items.

    Parameters
    ----------
    seq : pandas.core.series.Series
        The column to be verified
    df : pandas.core.frame.DataFrame
        The dataframe source

    Returns
    -------
    list
        A list with the repeated items

    Examples
    --------
    >>> list_repeated(df['col1'])
        ['Item X',
         'Item Y',
         'Item Z']
    """
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    return list(seen_twice)


# -------------------------------------------


def director_cleaner_str(df):
    """
    Given a dataframe df = 'disney-director.csv':
    1-Remove any extra whitespace on columns 'name' and 'director'.
    2-Adjust the names in the columns 'name' and 'director' so that the first character in every word is upper case. # noqa: E501
    3-Return a cleaner dataframe ready for analysis.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        The dataframe to be cleaned

    Returns
    -------
    pandas.core.frame.DataFrame
        The new cleaned dataframe

    Raises
    ------
    TypeError
        If the input argument df is not of type DataFrame

    Examples
    --------
    >>> director_cleaner_str(directors)
                                  name            director
    0  Snow White and the Seven Dwarfs          David Hand
    1                        Pinocchio      Ben Sharpsteen
    """
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Data is not a dataframe")

    df = df.assign(
        name=df["name"].str.strip().str.title(),
        director=df["director"].str.strip().str.title(),
    )
    return df


# -------------------------------------------
