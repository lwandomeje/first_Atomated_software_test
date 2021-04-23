
from  blog import  Blog

MENU_PROMPT = 'Enter "c" to create a blog,"l" to list blags,"r" to read one, "p" to create a post, or "q" to quit:'

POST_TEMPATE = ''' 
___{}___

{}

'''

blogs = dict()

def menu():

    print_blogs()
    selectoin = input(MENU_PROMPT)
    while selectoin != 'q':
        if selectoin == 'c':
            ask_create_blog()
        elif selectoin == 'l':
            print_blogs()
        elif selectoin == 'r':
            ask_read_blog()
        elif selectoin == 'p':
            ask_create_post()
        selectoin = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('-{}'.format(blog))

def ask_create_blog():
    title = input('Enter your blog title:')
    author = input('Enter your name:')

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter the blog title you want to to read ')
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post[post]

def print_post(post):
    print(POST_TEMPATE.format(post.title, post.content))

def ask_create_post():
    pass




