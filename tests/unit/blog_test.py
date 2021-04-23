from unittest import TestCase
from blog import Blog



class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('My Day ', 'Rolf')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1post)')
        self.assertEqual(b2.__repr__(), 'My Day  by Rolf (2posts)')


    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }



