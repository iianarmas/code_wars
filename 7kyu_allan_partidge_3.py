# Description
'''Ever the learned traveller, Alan Partridge has pretty strong views on London:

"Go to London. I guarantee you'll either be mugged or not appreciated.
Catch the train to London, stopping at Rejection, Disappointment, Backstabbing Central and Shattered Dreams Parkway."
Your job is to check that the provided list of stations contains all of the stops Alan mentions. There will be other stations in the array. Example:

['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
If the stations all appear, return 'Smell my cheese you mother!', if not, return 'No, seriously, run. You will miss it. '.'''


# solution
def alan(arr):
    lst = ['London', 'Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
    return ('No, seriously, run. You will miss it.', 'Smell my cheese you mother!')[all(i.strip() in arr for i in lst)]
  
  
# variation 1
def alan(arr):
    s = {'Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway'}
    return "Smell my cheese you mother!" if s.issubset(arr) else "No, seriously, run. You will miss it."
