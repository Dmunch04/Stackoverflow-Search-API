# Stackoverflow-Search-API
Search Stackoverflow posts with this Python API

# Integrate
Wanna use this API? Add this to your `requirements.txt`: (https://pip.pypa.io/en/stable/user_guide/#requirements-files)
```
git://github.com/Dmunch04/Stackoverflow-Search-API.git
```
Does it not work? Try this:
```
git+git://github.com/Dmunch04/Stackoverflow-Search-API.git
```

# Stackoverflow Search API:
This is the attributes you can get from the class, StackOverflow:
- title ; The title of the post
- sender ; The author/sender of the post
- tags ; The tag(s) on the post
- url ; The URL for the post
- answers ; The amount of answers posted to the post
- answered ; A bool (True or False), of if the post/question has been answered

Example of use:
```python
import stackoverflow as so

def mySearch (searchItem):
  result = so.search("Python: How to match a string with generic date in middle")

  print(result.title)           # Prints the title of the result post
  print(result.sender)          # Prints the author's name of the result post
  print(result.tags)            # Prints the tag(s) of the result post
  print(result.url)             # Prints the URL of the result post
  print(result.answers)         # Prints the amount of answers to the result post
  print(result.answered)        # Prints a bool whether the post has been answered
```
