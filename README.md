# Couch Potato

This TV Boxset Review site is an interactive webpage designed to allow users to share and review their favourite tv boxsets.
The webpage allows the user to create, read, update and delete boxsets(CRUD).
My inspiration for this project came from the current Pandemic and the country being on lockdown. Friends and family would gather together
for video calls and talk about what they were watching on TV and the likes of Netflix and Amazon Prime were releasing more boxsets due to people being restricted
to the indoors. Upon my research I found websites that reviewed movies, and movies and boxsets, however there did not appear to be many websites that solely
focused on TV boxsets. I chose this idea because I thought it would be extremely suitable given pandemic and allow people to share and review what they are watching.

# UX:
## User Stories
### As a user of this platform I will be able to:
 - View all boxsets listed on the website in ascending order.
 - I will be able to search the title of a boxset and locate that boxset if it is already on the webpage.
 - I will be able to add a boxset and upload an image of this boxset.
 - I will be able to add a rating and review of a boxset which will then be displayed on the boxset page.
 - I will be able to edit an existing boxset and update it.
 - I will be able to delete a boxset.
 - I will be able to access and view the webpage from other devices eg. mobile and ipad.

## Wireframes
Located in my github repo for desktop and mobile

## Design
To assist with the design of the website I used grids, nav, carousel and cards from Materialize. The aim of this website
was to have a colourful and bold website that would be pleasing to user eye. I attempted to keep the design simple and not
overcrowd the page with too much information. My aim was to create a fun and casual looking website whilst looking clean and spacious.

I used resources available to me on Slack by the tutors and used the following document a guide:
https://code-institute-room.slack.com/archives/C7J2ZAVHB/p1556827813043100 
- I maintained website conventions to allow a user to find what they want easily eg. navbar at the top, 
clearly labelled buttons, search field at the top of the page.
- I used subtle but effective user actions for example hover effects for buttons and navbar.
- I provided bite size information and ensured not to overload the user with information.
- I have attempted to create a simple design which does not force the user to "go looking" for what they want.
- I have used colours which provide comfortable viewing for individuals with learning disabilities such as Dyslexia. i.e minimal use of white.
- I used styling commonly found on modern websites (see PDF above) such as border radius for buttons, box shadows with colour and borders.

## Colours
- Due to using alot of images which provide alot of colour, I chose a simple background colour which would not clash with the colours of the images.
- As someone who is Dyslexic, the use of white is extremely challenging to read from due to being sensitive to brightness.
White also makes words and images "swirl" making it difficult focus, I therefore chose black.
- According to information on the web, black provides a sophisticated and powerful look and when used against colour, can look modern.
    https://www.toptal.com/designers/ux/color-in-ux
    https://uxplanet.org/how-color-can-effect-emotion-ccab0431b1d
- I used a lighter colour inside bordered boxes to make it easier on the eye for the viewer and prevent it from being too dark.
- I looked at movie review websites such as Rotten Tomatoes, IMDb, Flixster and saw that they used simple colour backgrounds i.e. white, gray or black,
with the use of bold colours and lots of images to create additional colour and I therefore attempted to use a similar colour scheme.

### Colour Palettes I took inspiration from:
http://lowdi.com/
https://i.pinimg.com/736x/6d/66/e6/6d66e6d2e07577cacb7a3382a86b090d.jpg

## Typography
- I chose Barlow for my main font as I felt this was simple and easy to read and display.
- For my main title and the navbar I used Righteous as I thought this was a fun and relaxed looking font but still easy to read.

## Icons
- I made use of the icons from the Materialize icons library to help create a fun feel when the user visits the website.


# Features
## Base   
All pages contain a navigation bar at the top of the page on desktop. The navbar becomes a side-nav when the user
uses a mobile or ipad device. This navbar allows the user to jump to the following pages:
- Home page - this is the landing page which includes an image carousel, cards which contain ratings for selected boxsets,
and 4 boxset cards of boxsets which have just released a new season. The items on the home page are there to tell the user what the website is about,
and to create something that is simple but visually appealing.
- All Boxsets - paginates pages that lists all the boxsets on the website in ascending order. This page also contains a 'search'
function which allows the user to search the title of any boxset, and their search is filtered. The page is displayed with 9 boxsets per page, in a row of 3. Each
boxset is presented as a simple card providing the user with a bitesize of information and a button leading them to a page with full details of that boxset.
- Add Boxset - this page allows the user to add a boxset as well as have the ability to upload a link for an image.

## Other pages
- View page - the user can view each boxset on an individual page which will provide more information about that boxset as well as
user ratings and reviews. This page is reached by pressing the 'read more' button on the 'All Boxsets' page. 
The view page allows the user to use the following functions:
    - Edit boxset - once updated takes the user back to the view page
    - Delete boxset - once deleted the page redirects to 'All Boxsets'
    - Add Review - Once a review is added it redirects the user to the view page.
- Search page - this page is linked to the search function. The user can search for a boxset title on 'All Boxsets' and their results
are listed in the search page.

## Features left to implement
    - I would like to add a login/register function to allow the user to create a username which can then
    be displayed when they write a review.

### Technologies used
## Front End
- [HTML](https://en.wikipedia.org/wiki/HTML) -  Used as the base for project code.
- [CSS](https://www.w3schools.com/css/) - Used as the base for cascading styles.
- [JQuery](https://jquery.com/) - Used for initialising side nav and image carousel and to set timing of the image carousel
- [Materialize](https://materializecss.com/) - Used for the design framework.

## Back End
- [Flask 1.0.2](https://flask.palletsprojects.com/en/1.1.x/quickstart/) - Used as templating language to display data in HTML templates.
- [Python 3](https://www.python.org/) - Used as the programming language at the back-end
- [MongoDB Atlas](https://www.mongodb.com/) - Used as the database to manage the data for this website. 
- [Jinja 2.10](https://en.wikipedia.org/wiki/Jinja_(template_engine)) - Used for displaying elements from back-end to front-end.
- [Heroku](https://www.heroku.com/) - Used for hosting the deployed website.

# Testing

## Desktop 
### Functions and outcomes:
Navbar:
- Click navbar 'All Boxsets' > directs user to 'All Boxsets' > Outcome: Pass
- Click navbar 'Add Boxset' > directs user to 'Add Boxset' > Outcome: Pass
- Click navbar 'Home' > directs user to Home > Outcome: Pass 

Buttons:
- Click 'Read more' button on home page > directs user to view page > Outcome: Pass
- Click ' Read more' button on 'All Boxsets' > directs user to view page > Outcome: Pass
- Click 'Add Review' button on 'View' > directs user to 'Add Review' page > Outcome: Pass
- Click 'Add Review' button on 'Add Review' page > redirects user to 'View' > Outcome: Pass
- Click 'Edit Boxset' button on 'View' > directs user to 'Edit Boxset' page > Outcome: Pass
- Click 'Update Boxset' button on 'Edit Review' > directs user to 'View' page > Outcome: Pass
- Click 'Delete Boxset' button on 'View' page > deletes boxset and redirects user to 'All Boxsets' > Outcome: Pass

Search Bar: 
- Type title or letters of a boxset into search bar > click submit > directs user to 'Search' template listing results > Outcome: Pass

## Mobile and Ipad 
### Functions and outcomes:
Navbar:
- Click navbar 'All Boxsets' > directs user to 'All Boxsets' > Outcome: Pass
- Click navbar 'Add Boxset' > directs user to 'Add Boxset' > Outcome: Pass
- Click navbar 'Home' > directs user to Home > Outcome: Pass 

Buttons:
- Click 'Read more' button on home page > directs user to view page > Outcome: Pass
- Click ' Read more' button on 'All Boxsets' > directs user to view page > Outcome: Pass
- Click 'Add Review' button on 'View' > directs user to 'Add Review' page > Outcome: Pass
- Click 'Add Review' button on 'Add Review' page > redirects user to 'View' > Outcome: Pass
- Click 'Edit Boxset' button on 'View' > directs user to 'Edit Boxset' page > Outcome: Pass
- Click 'Update Boxset' button on 'Edit Review' > directs user to 'View' page > Outcome: Pass
- Click 'Delete Boxset' button on 'View' page > deletes boxset and redirects user to 'All Boxsets' > Outcome: Pass

Search Bar: 
- Type title or letters of a boxset into search bar > click submit > directs user to 'Search' template listing results > Outcome: Pass

## Code Validators
HTML - https://validator.w3.org/ 
I ran each HTML template through the validators. Each page presented with a number of errors that related to
the Jinja templating. I discussed this with the Tutors on the support tab who informed me that this is to be expected
and I do not need to make any amendments to the code.

CSS - https://jigsaw.w3.org/css-validator/ 
I ran my style.css through the validator and I recieved no errors.

Python - http://pep8online.com/ 
I ran my app.py through the validator and I received 3 errors:
- Lines were too login
- White space  
- Additional line space
I fixed these errors and ran my code again which recieved no errors.

## Testing devices
- Desktop - passed
- Mobile device - passed
- Ipad - passed

## Testing Browsers
- Chrome - passed
- Internet Explorer - passed

#Deployment to Heroku
To deploy this project to Heroku required the following steps:
1. Register for Heroku and once signed in click the "New" button on the dashboard to create a new app.
2. In Heroku Name the app and specify the region.
3. Create a requirement.txt file to allow Heroku to install the required dependencies to run the app. The CLI text to input is as follows pip3 freeze --local > requirements.txt.
4. Create a Procfile to inform Heroku what type of app is being deployed echo web: python run.py > Procfile.
5. In the CLI of you IDE input the following:
    $ heroku login
    $ heroku git:remote -a <tvboxset-reviews>
    $ git push heroku master


#Credits
- All Image links taken from Google Searches 
- Information for each boxset was taken from a number of different websites including; IMDb, Rotten Tomatoes and Wikipedia
- I used Netflix, Amazon and NOWtv to choose popular boxsets.
- I reviewed a number of peer code that I used to gather ideas and help me:
    https://github.com/Bumper0417/Milestone-project-3-Python 
    https://github.com/DarrenCoppinger/milestone-project-3
    https://github.com/rodrigoneumann/third-milestone-project
- I used Slack (data-centric dev channel) to assist with my pagination
- I used the following code example to assist with pagination: https://github.com/DarilliGames/flaskpaginate/blob/master/app.py
- I used the mini project lessons provided by CI to put together my functions

#Acknowledgments
- I would like to thank my mentor, Anthony Ngene who as always has been amazing. I was really struggling with
a couple of functions and he kindly gave me alot of his time to show me what to do and then talked me through each
line of code so I understood it and knew what to do for next time. He was reassuring, non-judgemental and I really
don't think I would have got there without his help.





