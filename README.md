# search-query-performance-analysis
Scripts for scraping customer search results for future analysis.  The POC script is specific to Bloomingdales and is design to:
1. Open a headless chrome browser and navigate to the BLM search page with a given search term
2. take a screenshot of the pages results
3. scrape the UTAG data set on the page by Bloomingdales which contains lots of meta data about the search result page (productids, categories, etc.) and save it to a JSON file for analysis
## Prerequisites
1. You must have a working local python set up with the appropriate modules installed (all can be installed with pip)
2. You have the latest version of [chromedriver](https://chromedriver.chromium.org/) set up and running
3. Install Selenium pip3 install selenium or pip install selenium if using python2
## Run script 
1. If you simply invoke the script `python blm_test.py`there is one default search term that the script will use.  This is good for testing during local setup
2. Alternatively you can pass the name of a .csv file `python blm_test.py search_terms.csv` that contains multiple search terms that the script will iterate through.  File structure must be `search term, /n` for each search term
3. The script will create a new directory with a unix time stamp for each invocation of the script and all artifacts from that run of the script will be added to that new sub-directory with the same unix time stamp appended
## TODO's
- Add error handling when looping through search terms (just gobble up any errors for now and continue the for loop).  Getting baseline data is the goal, not complete data quite yet
- Auto upload result runs to S3, for now manual upload from each run is fine, but if this starts to be useful auto uploading will be nice
- If this does become valuale enough for any retailers dockerize and move to "The Cloud™" to run.
