# Scraping Drop Project By Shravan

# Importing Libraries
import mechanicalsoup
import os
import wget

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"

browser.open(url)
# get HTML
browser.get_current_page()

# target the search input
browser.select_form()

# searching for a term
search_term = input("Enter a search term: ")
browser["q"] = search_term

# submitting the search
response = browser.submit_selected()

# opening of URL
new_url = browser.get_url()
browser.open(new_url)
print(new_url, "\n")

# get HTML code
page = browser.get_current_page()
all_images = page.find_all('img')

# target the source attributes of image
image_source = []
for image in all_images:
    image = image.get('src')
    image_source.append(image)

image_source[5:25]
image_source = [image for image in image_source if image.startswith('https')]
image_source[5:]

path = os.getcwd()
# just adding s to the end of the path name
path = os.path.join(path, search_term + "s")

typechoice = input("Enter the type of image you want to download (jpg or png): ")
if typechoice == "jpg":
    imgtype = ".jpg"
elif typechoice == "png":
    imgtype = ".png"
else:
    print("Invalid type")

# creating the directory
os.mkdir(path)
print('Your Query images are stored here: ', path)

# Saving the images according to type of image
counter = 0
for image in image_source:
    save_as = os.path.join(path, search_term + str(counter) + imgtype)
    wget.download(image, save_as)
    counter += 1
