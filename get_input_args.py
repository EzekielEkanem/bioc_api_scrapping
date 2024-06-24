# Import the necessary libraries
import argparse

# function that retrieves command line inputs from the user using the ArgParse
# Python Module
def get_input_args():
    parser = argparse.ArgumentParser(description="Takes in id numbers of posts: to search for a single post, choose \
                                     --single_index; for a range of posts, choose --double_index")
    parser.add_argument("--single_index", type=int, help="Set an id number whose post is to be requested")
    parser.add_argument("--double_index", type=int, nargs=2, help="Set two id numbers corresponding \
                        to the range of posts to be requested. For example, if requesting for the posts between index \
                        numbers 1 and 25, input 1 25")
    return parser.parse_args()