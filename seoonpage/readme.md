# SEO - OnPage

This script uses the [Natural Language Toolkit](http://www.nltk.org/) to extract entities from a docs.microsoft markdown file. And then it scores the entities using the SEO guidelines in the _Developer Relations Contributor Guide_. It then pulls the top 10 keywords.

The script grabs nouns. The majority of organic searches (85%) use two or three nouns to find content on the web through Google and Bing. This script will do a good job of aligning these keywords.

However, the script will not identify verb. For instance, "Create storage account" would not show up with this script, but may be a perfectly valid keyword optimization.


## General usage notes

There are two versions of the script. The CLI script and the Repo script. The script will return a JSON object such as for each page:

```JSON
{
    1: {
        "score rank": 1,
        "keyword": "Azure Stack",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    2: {
        "score rank": 2,
        "keyword": "Topic test",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    3: {
        "score rank": 3,
        "keyword": "racing season",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    4: {
        "score rank": 4,
        "keyword": "Kentucky boys",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    5: {
        "score rank": 5,
        "keyword": "Hanley Turner",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    6: {
        "score rank": 6,
        "keyword": "freight train",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    7: {
        "score rank": 7,
        "keyword": "livery barn",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    8: {
        "score rank": 8,
        "keyword": "Churchhill Downs",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    9: {
        "score rank": 9,
        "keyword": "winter meeting",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    },
    10: {
        "score rank": 10,
        "keyword": "New Orleans",
        "page": "https://docs.microsoft.com/en-us/azure//dummy-text"
    }
}
```

You will need to have the Natural Language Toolkit and the training data installed.

### CLI Script

```bash
Run Python <path>\seoonpagecli.py
```

### Repo Script

1. Create or update a configuration file named `config.json` with the following properties:

    ```json
        {   "repoinput" :       "<path to the repo>", 
            "reportoutput" :    "<output of the lint report" }
    ```

2.  Run the script.

    ```bash
    Run Python <path>\seoonpagerepo.py
    ```

3. Open the output to review issues.