# Your job is simple, if (x) squared is more than 1000, return 'It's hotter than the sun!!', else, return 'Help yourself to a honeycomb Yorkie for the glovebox.'.

# variation 1
def apple(x):
    if pow(int(x), 2) > 1000:
        return 'It\'s hotter than the sun!!'
    return 'Help yourself to a honeycomb Yorkie for the glovebox.'
  
 # variation 2
def apple(x):
    return "It's hotter than the sun!!" if pow(int(x), 2) > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."
  
 # variation 3
def apple(x):
    return ("Help yourself to a honeycomb Yorkie for the glovebox.","It's hotter than the sun!!")[int(x)**2>1000]
