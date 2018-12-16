# Influencer Scraper

Generalizable tools to scrape Influencer blogs and extract patterns in illuminate advertisements.

## Usage

Start by copying `template_scraper.py` , naming it according to the blog you want to scrap, and filling in the configurable variables at the top of the file. From the terminal, run `python NEW_NAME_scraper.py URL_OF_INTEREST`. For example, I used `python styleheroine_scraper.py styleheroine.com` to create the Style Heroine corpus (which can be found in the `styleheroine` folder).

To analyze the content, run `python blog_analysis.py OUTPUTFILE` where the `OUTPUTFILE` is the output from running the scraper. The `blog_analysis.py` tool will generate the following metrics: Corpus size, Vocab size, Lexical diversity, Number of sponsor occurrences, Number of ad occurrences, Frequency Distribution, High Frequency Pronouns, and Product Frequency. 