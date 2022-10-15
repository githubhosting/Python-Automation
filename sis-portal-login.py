import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = 'http://parents.msrit.edu/parents_even2022/'
username = input('Enter your USN: ')
browser.open(url)
print(browser.get_url())
# print(browser.get_current_page())
# browser.select_form('form[class="cn-landing-login"]')
# print(browser.get_current_form().print_summary())
form = browser.select_form('form[class="cn-landing-login"]')
form.set_input({"username": username})

birthday = input("Enter your date of birth: ")

day, month, year = birthday.split('/')
months = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}
month = months[month]
form.set_select({"dd": day})
form.set_select({"mm": month})
form.set_select({"yyyy": year})
# launch browser
browser.launch_browser()

# submit form
print(browser.get_current_form().print_summary())
submit = browser.page.find('input', onclick='return check1()')
print(submit)
form.choose_submit(submit)
response = browser.submit_selected()
print(response.text)
