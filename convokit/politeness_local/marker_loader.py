import os
import pkg_resources
import json
from collections import defaultdict


UNIGRAM_FILE = pkg_resources.resource_filename("convokit",
    os.path.join("politeness_local/lexicons", "unigram_strategies.json"))

NGRAM_FILE = pkg_resources.resource_filename("convokit",
    os.path.join("politeness_local/lexicons", "ngram_strategies.json"))


START_FILE = pkg_resources.resource_filename("convokit",
    os.path.join("politeness_local/lexicons", "start_strategies.json"))

# TODO not all are relevant
MODE_FILE = pkg_resources.resource_filename("convokit",
    os.path.join("politeness_local/lexicons", "marker_mode.json"))


############## LOADING MARKER INFO ####################

# Loading basic markers 
def load_basic_markers(unigram_path=None, ngram_path=None, start_path=None):
    
    # load unigram markers 
    if unigram_path is None:
        unigram_path = UNIGRAM_FILE
    
    if ngram_path is None:
        ngram_path = NGRAM_FILE
    
    if start_path is None:
        start_path = START_FILE
    
    with open(unigram_path, "r") as f:
        unigram_dict = json.load(f)

    with open(ngram_path, "r") as f:
        ngram_dict = json.load(f)

    # load phrase markers 
    with open(start_path, "r") as f:
        start_dict = json.load(f)
    
    return unigram_dict, start_dict, ngram_dict


def load_marker_mode(mode_path=None):
    
    if mode_path is None:
        mode_path = MODE_FILE
    
    with open(mode_path, "r") as f:
        marker_mode = json.load(f)
        
    return marker_mode