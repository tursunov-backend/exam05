# from pydantic import BaseModel, Field


# class BookBase(BaseModel):
#     title: str
#     author: str
#     genre: str
#     year: int
#     rating: float = Field(ge=0, le=5)


# class BookCreate(BookBase):
#     pass


# class BookRead(BookBase):
#     id: int

#     class Config:
#         orm_mode = True



# class BookUpdate(BaseModel):
#     title: str | None = None
#     author: str | None = None
#     genre: str | None = None
#     year: int | None = None
#     rating: float | None = Field(default=None, ge=0, le=5)