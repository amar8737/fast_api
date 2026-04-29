from fastapi import APIRouter, HTTPException

from storeapi.models.post import (
    Comment,
    CommentIn,
    UserPost,
    UserPostIn,
    UserPostWithComments,
)

router = APIRouter()

post_table = {}

comment_table = {}


def find_post(post_id: int) -> UserPost:
    if post_id not in post_table:
        raise HTTPException(status_code=404, detail="Post not found")
    return post_table[post_id]


@router.post("/", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.dict()
    new_id = len(post_table) + 1
    post_with_id = UserPost(id=new_id, **data)
    post_table[new_id] = post_with_id
    return post_with_id


@router.get("/get/{post_id}", response_model=UserPost)
async def read_post(post_id: int):
    if post_id not in post_table:
        raise HTTPException(status_code=404, detail="Post not found")
    return post_table[post_id]


@router.get("/posts", response_model=list[UserPost])
async def read_posts():
    return list(post_table.values())


@router.post("/comments", response_model=Comment)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    data = comment.dict()
    new_id = len(comment_table) + 1
    comment_with_id = Comment(id=new_id, **data)
    comment_table[new_id] = comment_with_id
    return comment_with_id


@router.get("/post/{post_id}/comments", response_model=list[Comment])
async def read_comments_for_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return [comment for comment in comment_table.values() if comment.post_id == post_id]


@router.get("/post/{post_id}/with_comments", response_model=UserPostWithComments)
async def read_post_with_comments(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"post": post, "comments": await read_comments_for_post(post_id)}
