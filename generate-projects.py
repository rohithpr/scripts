from bs4 import BeautifulSoup as bs4

# deltax = [
#     (

#     )
# ]

otherprojects = [
    (
        'https://github.com/rohithpr/ipc-messenger',
        'ipc-messenger',
        'JavaScript',
        'A package that simplifies communication between workers in a node.js application'
    ),
    (
        'https://github.com/rohithpr/timeout-async/',
        'timeout-async',
        'JavaScript',
        'A node.js package that calls the callback function with default arguments if the async function takes too long'
    ),
    (
        'https://github.com/rohithpr/py-web-search/',
        'py-web-search',
        'Python (Requests, BeautifulSoup)',
        'A Python package to fetch results from different search engines'
    ),
    (
        'https://github.com/rohithpr/vhci/',
        'vhci',
        'Python (Flask), JavaScript (jQuery), HTML-CSS (Bootstrap)',
        'An application to communicate with a Ubuntu laptop using voice commands'
    ),
    (
        'https://github.com/rohithpr/bookmark-manager/',
        'Bookmark Manager',
        'Python (Django), JavaScript (jQuery), HTML-CSS (Bootstrap)',
        'A responsive site that stores bookmarks in an easily accessible way and makes efficient use of screen space'
    ),
    (
        'https://github.com/rohithpr/clouder-lite/',
        'Clouder-lite',
        'Python (Flask), JavaScript (jQuery), HTML-CSS (Bootstrap)',
        'A Flask app that helps transfer files to and from your computer through a browser'
    ),
    (
        'https://github.com/rohithpr/py-timed-dialog/',
        'py-timed-dialog',
        'Python (Tk)',
        'A Python package that helps create dialog boxes that self-destruct after a timeout'
    ),
    (
        'https://github.com/rohithpr/reactive/',
        'reactive',
        'Python',
        'A Python package to write functional reactive programs'
    ),
    (
        'https://github.com/rohithpr/search-api/',
        'search-api',
        'Python (Flask)',
        'An API to fetch results from different search engines in JSON format<br/>Hosted on Heroku'
    ),
    (
        'https://github.com/rohithpr/pyquora/',
        'pyquora',
        'Python (Requests)',
        'Contributed to the development of the scraper on which the unofficial quora-api is built'
    ),
]

projects = otherprojects
result = ''
count = 1
offset = ''

for project in projects:
    # if count == 0:
    #     offset = ' col-lg-offset-1 '
    # else:
    #     offset = ''

    item = [
        '<div class="col-lg-4 col-sm-6 col-xs-12',
        offset,
        '">',
        '<h2><a href="',
        project[0],
        '" target="_blank">',
        project[1],
        '</a></h2>',
        '<p class="lead">',
        project[2],
        '</p>',
        '<p class="description">',
        project[3],
        '</p>',
        '</div>'
    ]
    result += ''.join(item)

    if count == 0:
        count += 1
        continue

    if count % 2 == 0:
        result += '<div class="clearfix visible-sm-block visible-md-block"></div>'

    if count % 3 == 0:
        result += '<div class="clearfix visible-lg-block"></div>'

    count += 1

    # if count == 0:
    #     count = 1
    # elif count == 1:
    #     count = 2
    #     result += '<div class="clearfix visible-sm-block visible-md-block"></div>'
    # else:
    #     count = 0
    #     result += '<div class="clearfix visible-lg-block"></div>'

print(result)
# soup = bs4(result)
# output = bs4.prettify(soup)
# print(output)
