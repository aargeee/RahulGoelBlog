import os
import time

Title = input("Enter the blog title here : ")
TitleWords = Title.split()
Title = "-".join(TitleWords)

os.mkdir(path="_posts/"+Title)
date = time.localtime()
fileName = f"{date.tm_year}-{date.tm_mon}-{date.tm_mday}-{Title}.md"
f = open(f"_posts/{Title}/{fileName}", "w")
f.writelines([
    "---\n",
    f"title: {' '.join(TitleWords)}\n",
    f"date: {date.tm_year}-{date.tm_mon}-{date.tm_mday} {date.tm_hour}:{date.tm_min}:{date.tm_sec} {time.timezone}\n",
    "tags: []\n",
    f"description: {input('Enter Blog Description : ')}\n",
    "---\n",
])
f.close()