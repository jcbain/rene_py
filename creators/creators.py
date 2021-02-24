from itertools import product

def create_params(param_str, *opts):
    """
    Creates a list of explicit simulation parameter options for a single parameter.

    Parameters
    ----------
    param_str: str
       A string parameter option to be modified which will generally take on the for of "<param>". For example, to
       specify the rate of migration (m) you would input "m=".
    opts: str
       Any number of parameter values that you wish to run for any given parameter. For example, if you wanted to run a
       simulation with migrations rates of 1e-5 and 1e-3 then you would pass `"1e-5", "1e-3"` as arguments after the
       `param_str` option.

    Returns
    -------
    list
        A list of strings explicitly specifying the parameter to be run within the slim script.

    Examples
    --------
    To specify a simulation that runs migration rates (m) set to 1-e5 and 1-e4 you would:
    >>> create_params("m=", "1e-5", "1e-3")
    ["m=1e-5", "m=1e-6"]
    """
    return [param_str + "{}".format(opt) for opt in opts]

def create_permutations(*opts):
    """
    Creates a list of permutation from all possible unique combinations of parameters passed to it.

    Paramaters
    ----------
    opts: list
        Any number of lists that contain the parameter options to be combined together in a parameter set. See <create_params>.

    Returns
    -------
    list
        A list of tuples, where each tuple is a unique set of parameters.

    Examples
    --------
    >>> create_permutations(["m=1", "m=2"], ["r=6", "r=5"])
    [("m=1", "r=6"), ("m=1", "r=5"), ("m=2", "r=6"), ("m=2", "r=5")]
    """
    param_list = [x for x in product(*opts)]
    
    return param_list