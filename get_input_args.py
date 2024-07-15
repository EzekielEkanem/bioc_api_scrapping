# Import the necessary libraries
import argparse

# function that retrieves command line inputs from the user using the ArgParse
# Python Module
def get_input_args():
    parser = argparse.ArgumentParser(description="Takes in input arguments needed to run api_scrapping.py smoothly")
    parser.add_argument("--single_index", type=int, help="Set an id number whose post is to be requested")
    parser.add_argument("--double_index", type=int, nargs=2, help="Set two id numbers corresponding \
                        to the range of posts to be requested. For example, if requesting for the posts \
                         from index numbers 1 to 25, input 1 25")
    parser.add_argument("--load_file", type=str, default="", required=False, help="Set the filepath from \
                        which 'posts' is to be loaded from")
    parser.add_argument("--dump_file", type=str, default="", required=False, help="Set the filepath to \
                        which 'posts' will be dumped to")
    return parser.parse_args()