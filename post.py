class Post:
    def __init__(self, post_json, answers=[], comments=[]):
        self._raw_json = post_json
        self._comments = comments
        self._answers = answers
    
    def get_id(self):
        return self._raw_json.get("id")
    
    def get_uid(self):
        return self._raw_json.get("uid")

    def get_content(self):
        return self._raw_json.get("content")

    def get_vote_count(self):
        return self._raw_json.get("vote_count")
    
    def get_thread_score(self):
        return self._raw_json.get("thread_score")

    def get_type(self):
        return self._raw_json.get("type")

    def get_parent_id(self):
        return self._raw_json.get("parent_id")

    def get_author_uid(self):
        return self._raw_json.get("author_id")

    def get_comments(self):
        return self._comments

    def add_comment(self, comment):
        self._comments.append(comment)

    def get_comment(self, index):
        if 0 <= index < len(self._comments):
            return self._comments[index]
        else:
            raise IndexError("Index out of range")

    def get_answers(self):
        return self._answers

    def add_answer(self, answer):
        self._answers.append(answer)

    def get_answer(self, index):
        if 0 <= index < len(self._answers):
            return self._answers[index]
        else:
            raise IndexError("Index out of range")
        
    def to_dict(self):
        return {
            "raw_json": self._raw_json,
            "comments": [comment.to_dict() if isinstance(comment, Post) else comment for comment in self._comments],
            "answers": [answer.to_dict() if isinstance(answer, Post) else answer for answer in self._answers]
        }
    
    def to_summary_dict(self):
        return {
            "id": self.get_id(),
            "uid": self.get_uid(),
            "content": self.get_content(),
            "thread_score": self.get_thread_score(),
            "vote_count": self.get_vote_count(),
            "type": self.get_type(),
            "comments": [comment.to_summary_dict() if isinstance(comment, Post) else comment for comment in self._comments],
            "answers": [answer.to_summary_dict() if isinstance(answer, Post) else answer for answer in self._answers]
        }