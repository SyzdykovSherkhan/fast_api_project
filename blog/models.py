from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from fast_api_project import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), nullable=False)
    description = Column(String)
    main_image = Column(String(100))
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', backref=backref('blog', uselist=False))


class BlogText(Base):
    __tablename__ = 'blog_texts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    blog_id = Column(Integer, ForeignKey('blogs.id'))

    blog = relationship('Blog', backref='texts')


class BlogImage(Base):
    __tablename__ = 'blog_images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String(100), nullable=False)
    blog_id = Column(Integer, ForeignKey('blogs.id'))

    blog = relationship('Blog', backref='images')
