# Book Scraper Tool

So3-Py-team-1

* ## Project Summary
*A tool to collect the book data asynchronously from a bookstore website, then to sort this data based on given 
keys, dedicated to http://books.toscrape.com/. Used and developped technologies are aplicable for scrapping to most conteporary websites with certain updates*

* ## Requirements
Python 2.7+ (This script is written for Python 2.7, but could be run on all newer versions of Python)*

*Packages used:*

*bs4 BeautifulSoup - (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)*

*grequests - (requests + gevent, including urllib3 - https://github.com/spyoungtech/grequests)*

*for now...*
* ### All packages should be installed for the proper Python version
* 
* ## Usage

*The script is used to gather data from http://books.toscrape.com/.
You can write the following command in your terminal:*
  ```
    *still in working process*
  ```
*About the optional arguments:*

 *b - number of books(should be n?) - already done*

 *g - list of genres to search through*

 *s - list of sortings (for the output, ascending or descending)*

 *f - list of priority filters for which books to exclude from the scrape*

 *d - list of keywords to be searched from the description*

 *t - title of a book to search for*

 *F - list of book titles to search for (from given json)*

  
* ## Tests
*coming soon...*
  
* ## Technical Details

*To get data from http://books.toscrape.com/, the script uses class RequestHandler,
which uses request response functions from urlparse package.RequestsHandler is used by the
LinkParser class to obtain each page URL.LinkParser is used by BookLinkParser class
to obtain each book URL, traversing through every page URL.The books URLs are then used to extract the
data for the books title, price, in stock availability, description, star rating and genre. 
A full list of the genres is obtained from the main page URL by search in 'div', class_="side_categories"
All the books ing\formation is stored in DataBase class in a dictionary format*

  
### Workflow:
*coming soon...*
*Describe the workflow, step by step, of the script.*  
*This includes all the technical details!*  
*When and how is an input and output expected? When and how is data transfered or saved? When and how are any alghoritms used?*

*For example*  
1\. When you start the script you will be asked for an input...\
2\. Based on the input it will...\
3\. Then it will sort the gathered data based on...\
  ...\
*\. At the end an output is given that shows...

