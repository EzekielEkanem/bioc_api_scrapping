class Post:
    def __init__(self, post_json):
        self._id = post_json["id"]
        self._content = post_json["content"]
        self._vote_count = post_json["vote_count"]
        self._type = post_json["type"]
        self._parent_id = post_json["parent_id"]
        self._comments = []
        self._answers = []
    """
    I think getter and setter methods are more widely known in other programming
    languages, so I decided to use that instead of @property methods. I can change 
    to using property methods if that is better
    """
    
    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    def get_content(self):
        return self._content

    def set_content(self, new_content):
        self._content = new_content

    def get_vote_count(self):
        return self._vote_count

    def set_vote_count(self, new_vote_count):
        self._vote_count = new_vote_count

    def get_type(self):
        return self._type

    def set_type(self, new_type):
        self._type = new_type

    def get_parent_id(self):
        return self._parent_id

    def set_parent_id(self, new_parent_id):
        self._parent_id = new_parent_id

    def get_comments(self):
        return self._comments

    def set_comments(self, new_comments):
        self._comments = new_comments

    def add_comment(self, comment):
        self._comments.append(comment)

    def get_comment(self, index):
        if 0 <= index < len(self._comments):
            return self._comments[index]
        else:
            raise IndexError("Index out of range")

    def get_answers(self):
        return self._answers

    def set_answers(self, new_answers):
        self._answers = new_answers

    def add_answer(self, answer):
        self._answers.append(answer)

    def get_answer(self, index):
        if 0 <= index < len(self._answers):
            return self._answers[index]
        else:
            raise IndexError("Index out of range")