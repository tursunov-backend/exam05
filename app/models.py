# from sqlalchemy import String, Integer, Float
# from sqlalchemy.orm import Mapped, mapped_column
# from .database import Base


# class Book(Base):
#     __tablename__ = "books"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String(100), nullable=False)
#     author: Mapped[str] = mapped_column(String(100), nullable=False)
#     genre: Mapped[str] = mapped_column(String(50), nullable=False)
#     year: Mapped[int] = mapped_column(Integer, nullable=False)
#     rating: Mapped[float] = mapped_column(Float, nullable=False)

#     def __repr__(self):
#         return (
#             f"<Book(id={self.id}, title='{self.title}', "
#             f"author='{self.author}', year={self.year}, rating={self.rating})>"
#         )
