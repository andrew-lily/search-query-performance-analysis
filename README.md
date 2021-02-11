# search-query-performance-analysis
Scripts for scraping customer search results for future analysis.  The POC script is specific to Bloomingdales and is design to:
1. Open a headless chrome browser and navigate to the BLM search page with a given search term
2. take a screenshot of the pages results
3. scrape the UTAG data set on the page by Bloomingdales which contains lots of meta data about the search result page (productids, categories, etc.) and save it to a JSON file for analysis
## Prerequisites
1. You must have a working local python set up with the appropriate modules installed (all can be installed with pip)
2. You have the latest version of [chromedriver](https://chromedriver.chromium.org/) set up and running
## Run script 
1. If you simply invoke the script `python blm_test.py`there is one default search term that the script will use.  This is good for testing during local setup
2. Alternatively you can pass the name of a .csv file `python blm_test.py search_terms.csv` that contains multiple search terms that the script will iterate through.  File structure must be `search term, /n` for each search term
3. The script will create a new directory with a unix time stamp for each invocation of the script and all artifacts from that run of the script will be added to that new sub-directory
