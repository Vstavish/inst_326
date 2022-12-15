import re

def get_word(s):
    """Extract a list of words from string s
    
    Args: 
    s (str): a string containing one or more words
    
    Returns:
    list of str: a list of words from s converted to lower case
    
    """

    words = list 
    s = re.sub(r"--+", " ", s)
    for word in re.findall