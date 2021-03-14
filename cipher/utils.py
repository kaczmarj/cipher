"""Useful functions."""

import os


# TODO: Function to load tsv to dataframe

# TODO: function to save dataframe to tsv


def make_directory(dirpath, verbose=1):
    """make a directory.

    Parameters
    ----------
    dirpath : string
        String of path to directory.

    Returns
    -------


    Examples
    --------
    >>> dirpath = './results'
    >>> make_directory(dirpath)

    """
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
        print("making directory: " + dirpath)


def import_model(model_name):
    """Import a model from model_zoo. 

    Parameters
    ----------
    model_name : string
        Name of model in model_zoo to import.

    Returns
    -------
        imported model 

    Examples
    --------
    >>> model_name = 'deepbind'
    >>> model = import_model(model_name)

    """

    # Import model from the zoo as singular animal
    # Equivalent of `from model_zoo import model_name as animal` where model_name is evaluated at runtime
    animal = __import__("cipher.model_zoo." + model_name, globals(), locals(), [model_name], 0) 
    return animal
