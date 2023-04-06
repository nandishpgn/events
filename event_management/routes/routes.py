from pydantic import BaseModel
from fastapi import HTTPException, status, Depends, APIRouter
from config.database import get_database
from typing import Optional, Tuple, List
from datetime import datetime
from databases import Database
from models.api_logs import posts

router=APIRouter()


class Event(BaseModel):
    id: int
    event_name:str
    event_date:datetime
    # event_time:time
    location:str
    event_organiser:str
    chief_guest:Optional[str]=None
    total_guests:Optional[str]=None
    # created_date:datetime
    # updated_date:datetime

def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
    return (skip, limit)


async def get_post_or_404(
    id: int, database: Database = Depends(get_database)
) -> Event:
    select_query = posts.select().where(posts.c.id == id)
    raw_post = await database.fetch_all(select_query)
    print(raw_post)

    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Event(**raw_post)



@router.post("/posts", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: Event, database: Database = Depends(get_database)
 ) -> Event:
    insert_query = posts.insert().values(post.dict())
    post_id = await database.execute(insert_query)
    print(post_id)
    post_db = await get_post_or_404(post_id, database)
    return post_db


# @router.get("/posts")
# async def list_posts(
#     pagination: Tuple[int, int] = Depends(pagination),
#     database: Database = Depends(get_database),
# ) -> List[Event]:
#     skip, limit = pagination
#     select_query = posts.select().offset(skip).limit(limit)
#     rows = await database.fetch_all(select_query)
#     results = [Event(**row) for row in rows]
#     return results
@router.get("/posts")
async def sorted_info(sort_by: str = None, database: Database=Depends(get_database)):
    select_query = posts.select()
    rows = await database.fetch_all(select_query)
    print(rows, type(rows))
    if sort_by:
        sorted_info = sorted(rows, key=lambda x: x[sort_by])
        return sorted_info
    return rows

@router.patch("/posts/{id}", response_model=Event)
async def update_post(
    post_update: Event,
    post: Event = Depends(get_post_or_404),
    database: Database = Depends(get_database),
) -> EnvironmentError:
    update_query = (
        posts.update()
        .where(posts.c.id == post.id)
        .values(post_update.dict(exclude_unset=True))
    )
    await database.execute(update_query)
    post_db = await get_post_or_404(post.id, database)
    return post_db


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post: Event= Depends(get_post_or_404), database: Database = Depends(get_database)
):
    delete_query = posts.delete().where(posts.c.id == post.id)
    await database.execute(delete_query)


@router.get("/posts/{id}", status_code=status.HTTP_200_OK)
async def get_individual_post(
    id: int,
    database: Database = Depends(get_database)
):
    select_query = posts.select().where(posts.c.id == id)
    raw_post = await database.fetch_one(select_query)
    print(raw_post)

    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Event(**raw_post)

