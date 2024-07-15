# Bioconductor API Scrapping

This package makes api calls to the Bioconductor support site, processes the response, and dumps the processed response in a pickle file. This pickle file is then serialized in json
format. 

## Scripts
**get_input_args.py**
- [ ] Retrieves command line inputs from the user using the ArgParse module
- [ ] The arguments to be parsed in the command line depends on the script that the user wants to run

**api_scrapping.py**
- [ ] Makes api calls to the bioconductor support site, processes the response, and dumps it into a pickle file
- [ ] Command line inputs:
- ***Necessary inputs***
  - Input one of the following
    - --single_index num (where num is the id number whose post is to be requested) *or*
    - --double_index num1 num2 (where num1 and num2 are the two id numbers corresponding to the range of posts to be requested. For example, if requesting for the posts
      from index numbers 1 to 25, input 1 25)
  - --dump_file file (where file is the the filepath/filename to which 'posts' will be dumped to- should be a pickle file)
- ***Optional input***
  - --load_file file (where file is the filepath from which 'posts' is to be loaded from). This is very useful if some api calls had been made earlier and dumped in a pickle file.
    The script will load this pickle file and add more posts to this file. The file to be loaded must be a pickle file.
- [ ] Each **post** (from the api call) is added to a **posts** dictionary with the post id number as the key and the post object as the value
- [ ] If an api call is not successful, the program makes two retries, waiting for five seconds before each retry, before continuing to the next api call

**format_pickle.py**
- [ ] Loads the stored pickle file, formats the file and serializes it in a json format
- [ ] Command line inputs:
- ***Inputs***
  - --dump_file file (where file is the the filepath/filename to which 'posts' will be dumped to- should be a json file)
  - --load_file file (where file is the filepath from which 'posts' is to be loaded from). 
- [ ] The script will load the pickle file, keep only posts with type "Question", and sort the posts in decreasing order based on their thread_score
- [ ] The posts are then converted to a json serialized format and dumped in a json file

**post.py**
- [ ] This is the post class and contains all the methods used to access the post object
- [ ] It also contains a *to_summary_dict()* method that encodes the object in a json serialized format
