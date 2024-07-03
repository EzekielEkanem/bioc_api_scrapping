import json
import pickle
from post import Post
from get_input_args import get_input_args
import types

posts = {}

# Load data from filepath
def load_file(filepath):
    if ".pkl" in filepath:
        with open(filepath, "rb") as f:
            posts = pickle.load(f)
    else:
        with open(filepath, "r") as f:
            posts = json.load(f)
    return posts

# Get arguments passed from get_input_args
in_args = get_input_args()
if in_args.load_file:
    posts = load_file(in_args.load_file)

# Abstract out all the questions in posts
qs_posts = [p for k, p in posts.items() if p.get_type() == "Question"]

# Only filter out all the questions that have a thread score of 10 and above
# qs_posts = [p for k, p in posts.items() if p.get_thread_score() >= 10]

# Sort the list in order of top vote_count
qs_posts = sorted(qs_posts, key=lambda post: post.get_thread_score(), reverse=True)

# Serialize post object
class PostEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return obj.to_summary_dict()
        return json.JSONEncoder.default(self, obj)
    
# dump posts in json format
def serialize_posts(posts, filename):
    with open(filename, "w") as f:
        json.dump(posts, f, cls=PostEncoder, indent=4)

serialize_posts(qs_posts, in_args.dump_file)