# Async web engine searcher
App made to learn a little bit more of python asynchronous. 
It use a various search engines to get 1st result of each search with imput phrase.

## Setup

Copy `.env-template` into `.env` and fill with secrets
```
cp .env-template .env && nano .env
```

## API
### /firstone
POST request


```
curl --location --request POST '0.0.0.0:8000/firstone/' \
--header 'Content-Type: application/json' \
--data-raw '{"body": ["first search", "second search"]}'
```

Response:
```
[
    {
        "first search": {
            "Google": "google first page",
            "Youtube": "youtube first video",
            "StackOverflow": "etc.",
            "Yahoo": "etc.",
            "Baidu": "etc.",
            "DuckDuckGo": "etc.",
            "Bing": "etc.",
            "GitHub": "etc.",
            "Yandex": "etc.",
            "Aol": "etc.",
            "Ask": "etc.","etc.",
            "Coursera": "etc.",
        },
        "second search": {
            "Google": "google first page",
            "Youtube": "youtube first video",
            "StackOverflow": "etc.",
            "Yahoo": "etc.",
            "Baidu": "etc.",
            "DuckDuckGo": "etc.",
            "Bing": "etc.",
            "GitHub": "etc.",
            "Yandex": "etc.",
            "Aol": "etc.",
            "Ask": "etc.","etc.",
            "Coursera": "etc.",
        },
    }
]
```
