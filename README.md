# Scrapping Drop

## Modules used:

### MechanicalSoup: 
A Python library for automating interaction with websites. MechanicalSoup automatically stores and sends cookies, follows redirects, and can follow links and submit forms.
MechanicalSoup provides a similar API, built on Python giants Requests (for HTTP sessions) and BeautifulSoup (for document navigation).

### os: 
Python OS module provides the facility to establish the interaction between the user and the operating system. It offers many useful OS functions that are used to perform OS-based tasks and get related information about the operating system.
It is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.

### wget: 
Wget is a convenient solution for downloading files over HTTP and FTP protocols. It works well with Python in recursively downloading multiple files, and the process can easily be automated to save you time.Using the proper parameters, Wget can operate as a web crawler. Instead of downloading a single file, it can recursively download files linked from a specific web page until all the links have been exhausted or until it reaches a user-specified recursion depth. In this scenario, Wget saves the downloaded files in a directory structure that resembles the server they have been downloaded from.

# Working:
* First the program takes the input from the user in the console
* Then it stores it in search_item
* Now the Search_item is queried to the browser with the help of the Mechanical Soup Module
* The browser will provide the information and appropriate images with respect to the searched item
* Mechanical Soup module will scrap the HTML code from the results
* That code is filtered with the image links followed by the tag “img” 
* The links of the images are stored in the list image_source
* User is promoted to enter the image format that needs to downloaded
* os module uses the given input format and downloads in that format
* Now os module is used to create a folder to store the downloaded images
* wget module downloads all the image links one by one  in the desired path
