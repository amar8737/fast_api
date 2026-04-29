from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int


class CommentIn(BaseModel):
    post_id: int
    body: str


class Comment(CommentIn):
    id: int


class UserPostWithComments(UserPost):
    comments: list[Comment] = []
    post: UserPost
