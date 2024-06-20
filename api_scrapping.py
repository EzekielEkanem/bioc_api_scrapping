# Import useful libraries and packages
import requests
from post import Post 
import json
        
# function that takes in the a query, calls the query, and returns the response in a json format 
def call_api(query):
    # Get the response
    response = requests.get(query)

    # returns the value of the request in a json format if response is successful
    if response:
        response_dict = response.json()
        return response_dict
    else: 
        raise Exception(f"The request wasn't successful: {response.status_code}")

# make_query calls the call_api function on a query, adds them to the posts dictionary, and
# return the posts dictionary
def make_query(posts, index):
    pre_query = "https://support.bioconductor.org/api/post/"
    # For now, I am just putting all posts into this dictionary where the keys are the post's 
    # id and the value of each key is the post, but this can change later
    posts = posts
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
    return posts

# bulk_query takes in posts and the range of indices whose url is to be called, calls make_query on 
# each index and returns the posts dictionary
def bulk_query(posts, first_index, last_index):
    posts = posts
    for i in range(first_index, last_index+1):
        posts = make_query(posts, i)
    return posts



# Call the make_query() function
print(bulk_query({}, 1, 25))