# Import useful libraries and packages
import requests
from post import Post 
from get_input_args import get_input_args
import pickle
import time
import json 

# function that takes in the a query, calls the query, and returns the response in a json format 
def call_api(query, num_of_retries=3, wait_len=5):
    retries = 0
    while retries <= num_of_retries:
        try: 
            # Get the response
            response = requests.get(query)

            # raises an error if there is one
            response.raise_for_status()

            # returns the value of the request in a json format if response is successful
            response_dict = response.json()
            return response_dict
        except requests.exceptions as e:
            print(f"The request wasn't successful: {e}") 
            retries += 1
            print(f"Sleeping for {wait_len} seconds")
            if retries <= num_of_retries:
                time.sleep(wait_len)  
            else:
                raise Exception(f"Number of trials exceeded for call_api ({num_of_retries}). Request still unsuccessful")

# make_query calls the call_api function on a query, adds them to the posts dictionary, and
# return the posts dictionary
def add_post(posts, index):
    pre_query = "https://support.bioconductor.org/api/post/"
    # For now, I am just putting all posts into this dictionary where the keys are the post's 
    # id and the value of each key is the post, but this can change later
    """
    I'm suggesting that, to make the for loop dynamic, we could make a variable or function
    that gets the ID of the latest post and the for loop runs based on that number, so that 
    we won't hard code the number of times the for loop runs
    """
    # if a post is a comment or an answer, add the content of that post to the parent_id of the post
    query = pre_query + f"{index}/"
    query_response = call_api(query)
    post = Post(query_response)        
    posts[post.get_id()] = post
    if post.get_type() != "Question":
        parent_id = post.get_parent_id()
        if parent_id in posts:
            if post.get_type() == "Comment":
                posts[parent_id].add_comment(post.get_content)  
            else:
                posts[parent_id].add_answer(post.get_content)
        else:
            raise Exception(f"Post does not have the parent id {parent_id} available")
    return post

# bulk_query takes in posts and the range of indices whose url is to be called, calls make_query on 
# each index and returns the posts dictionary
def bulk_query(posts, first_index, last_index):
    for i in range(first_index, last_index+1):
        add_post(posts, i)
    return posts

posts = {}

# Get arguments passed from get_input_args   
in_args = get_input_args()
if in_args.single_index:
    add_post(posts, in_args.single_index)
elif in_args.double_index:
    bulk_query(posts, in_args.double_index[0], in_args.double_index[1])
else:
    raise Exception(f"No argument has been passed. You must set either a single index or a double \
                    index in the command line")

# Serialize data to filepath
def dump_to_file(filepath, object):
    with open(filepath, "wb") as f:
        pickle.dump(object, f)
    return filepath 

# Load data from filepath
def load_file(filepath):
    with open(filepath, "rb") as f:
        posts = pickle.load(f)
    return posts 

# dump and load files if a filepath is given
if in_args.dump_file:
    dump_to_file(in_args.dump_file, posts)
if in_args.load_file:
    load_file(in_args.load_file)
