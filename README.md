# IMDB-List-Generator

Tool to add items to IMDB list, be it Movies or TV-Shows, by name or by IMDB id.

## How to use the tool.

You will need the following Python 3 dependancies for this to work (installed using pip)
- requests
- urllib

You will also need to edit the Python file to add your browser cookies (this is used to authenticate the API requests). This is found at the top of the file, and the following must be edited.
```
webInfo = {

    'Id': listID, # Leave this alone, it gets the listID when you enter it into the program
    'x-imdb-parent-id': '????', # Add this.
    'Referer': 'https://www.imdb.com/list/' + listID + '/edit?inProgress=true', # Leave this alone, it gets the listID when you enter it into the program
    'Cookie': '??????', # Add this.
    'Data': '????c=????' # Add this.
}
```

You can get this information through the chrome developer tools (F12) when you create an IMDB list and add an item. See steps below.
- Create new IMDB List
- Press F12 in Chrome to open developer tools.
- Select 'Network' tab along the top menu bar. Make sure that it is recording (red button, top left)
- Go back to your IMDB list window and search for, and add a new item (don't worry, we will remove after).
- After adding your new item, return to the developer window and in the list of items, select the one with the name 'add'.
- Then on the right hand side, scroll down to the 'Request Headers' section.
- Copy the entire cooke information ('cookie: session-id=......')
- Copy the x-imdb-parent-id information ('x-imdb-parent-id: BS1J.....')
- Then under 'Form Data', copy the information, and replace the colon and space with the equals sign (49xxc: e3xx -> 49xxc=e3xx)
- Place this information into the python file, and make sure you have each item in single quotes.



### How to add items using IMDB id.

By default, this is how the python file is setup. You just need to append the 'list.txt' file with your list of movies, one line for each. See example below.
```
tt2527338
tt7975244
tt7131622
tt2527336
tt0112442
```

To get the list from the file, the program runs the following.
```python
getLocalListWithIDs("list.txt")
```

To add all the items, the program runs the following function using the data retrieved.
```python
getLocalListWithIDs(data)
```

Final line.
```
addListByIDs(getLocalListWithIDs("list.txt"))
```

### How to add items using name and year.

By default, this is not how the program is set to run, so it must be edited to do so. For this method, the items are stored in the following formats in the 'list.txt' file.
```
Quincy 2018
Neruda 2016
The Salvation 2014
```

To get the list from the file, the program runs the following.
```python
getLocalListWithTitleYears("list.txt","movies") # 'movies' can be changed to 'tvSeries' to search for them instead.
```

To add all the items, the program runs the following function using the data retrieved.
```python
addListByTitleYear(data)
```

Final line.
```
addListByTitleYear(getLocalListWithTitleYears("list.txt","movie"))
```


