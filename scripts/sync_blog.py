"""Copy posts over from _posts to _blog."""

from glob import glob
import os
import shutil
from stat import S_IREAD, S_IRGRP, S_IROTH

def get_posts():
    return glob("./_posts/*.markdown") + glob("./posts/*.md")

def duplicate():
    shutil.rmtree("_blog")

    os.makedirs("_blog")

    for post in get_posts():
        fname = os.path.basename(post)
        blog_path = os.path.join("_blog", fname)
        post_path = os.path.join("_posts", fname)
        print(f"copy {post_path} to {blog_path}")
        shutil.copy2(post_path, blog_path)
        
        # Make read-only so I don't accidentally edit them
        os.chmod(blog_path, S_IREAD|S_IRGRP|S_IROTH)


if __name__ == "__main__":
    duplicate()