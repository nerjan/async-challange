# Async web engine searcher
App made to learn a little bit more of python asynchronous. 
It use a various search engines to get 1st result of each search with imput phrase.

## API
### /firstone
POST request


```
curl -X POST \
  http://0.0.0.0:8000/validate \
  -H 'Content-Type: application/json' \
  -d '{"one serach", "second search"}
```

Response:
```
{
    "Google": "1st result found by google",
    "Youtube": "1st result found by Youtube",
    "StackOverflow": "1st result found by StackOverflow",
    "Yahoo": "1st result found by Yahoo",
    "Baidu": "1st result found by Baidu",
    "DuckDuckGo": etc.,
    "Bing": etc.,
    "GitHub": etc.,
    "Yandex": etc.,
    "Aol": etc.,
    "Ask": etc.,
    "MyAnimeList": etc.,
    "Coursera": etc.,
    "It took": "How much time it took",
}
```