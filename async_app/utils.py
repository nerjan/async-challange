import asyncio

from asgiref.sync import async_to_sync
from django.conf import settings
from googlesearch import search
from search_engine_parser.core.engines.aol import Search as AolSearch
from search_engine_parser.core.engines.ask import Search as AskSearch
from search_engine_parser.core.engines.baidu import Search as BaiduSearch
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.coursera import Search as CourseraSearch
from search_engine_parser.core.engines.duckduckgo import \
    Search as DuckDuckGoSearch
from search_engine_parser.core.engines.github import Search as GitHubSearch
from search_engine_parser.core.engines.myanimelist import Search as MALSearch
from search_engine_parser.core.engines.stackoverflow import \
    Search as StackOverflowSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch
from search_engine_parser.core.engines.yandex import Search as YandexSearch


def search_engine(name):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            if settings.DEBUG:
                print(name)
            try:
                return await func(*args, **kwargs)
            except:
                return ""

        return wrapper

    return decorator


@search_engine(name="Coursera")
async def get_coursera_first_page(search_term):
    courserasearch = CourseraSearch()
    coursera_first_page = await courserasearch.async_search(
        query=search_term, page=1, cache=False
    )
    return coursera_first_page["links"][0]


@search_engine("My Anime List")
async def get_mal_first_page(search_term):
    malsearch = MALSearch()
    mal_first_page = await malsearch.async_search(
        query=search_term, page=1, cache=False
    )
    return mal_first_page["links"][0]


@search_engine("Ask")
async def get_ask_first_page(search_term):
    asksearch = AskSearch()
    ask_first_page = await asksearch.async_search(
        query=search_term, page=1, cache=False
    )
    return ask_first_page["links"][0]


@search_engine("Aol")
async def get_aol_first_page(search_term):
    aolsearch = AolSearch()
    aol_first_page = await aolsearch.async_search(
        query=search_term, page=1, cache=False
    )
    return aol_first_page["links"][0]


@search_engine("Yandex")
async def get_yandex_first_page(search_term):
    yandexsearch = YandexSearch()
    yandex_first_page = await yandexsearch.async_search(
        query=search_term, page=1, cache=False
    )
    return yandex_first_page["links"][0]


@search_engine("Yahoo")
async def get_yahoo_first_page(search_term):
    if search_term == "yahoo":
        return "yahoo.com"
    yahoosearch = YahooSearch()
    yahoo_first_page = await yahoosearch.async_search(
        query=search_term, page=1, cache=False
    )
    return yahoo_first_page["links"][0]


@search_engine("StackOverflow")
async def get_stackoverflow_first_page(search_term):
    stackoverflowsearch = StackOverflowSearch()
    stackoverflow_first_page = await stackoverflowsearch.async_search(
        query=search_term, page=1, cache=False
    )
    return stackoverflow_first_page["links"][0]


@search_engine("Baidu")
async def get_baidu_first_page(search_term):
    baidusearch = BaiduSearch()
    baidu_first_page = await baidusearch.async_search(
        query=search_term, page=1, cache=False
    )
    return baidu_first_page["links"][0]


@search_engine("DuckDuckGo")
async def get_duckduckgo_first_page(search_term):
    duckduckgosearch = DuckDuckGoSearch()
    duckduckgo_first_page = await duckduckgosearch.async_search(
        query=search_term, page=1, cache=False
    )
    return duckduckgo_first_page["links"][0]


@search_engine("Bing")
async def get_bing_first_page(search_term):
    bingsearch = BingSearch()
    bing_first_page = await bingsearch.async_search(
        query=search_term, page=1, cache=False
    )
    return bing_first_page["links"][0]


@search_engine("GitHub")
async def get_github_first_page(search_term):
    githubsearch = GitHubSearch()
    github_first_page = await githubsearch.async_search(
        query=search_term, page=1, cache=False
    )
    return github_first_page["links"][0]


async def get_google_first_page(search_term):
    if search_term == "google":
        google_first_page = "google.com"
    else:
        if settings.DEBUG:
            print("GOOGLE")
        try:
            google_first_page = await next(
            google_first_page = next(
                search(search_term, tld="co.in", num=1, start=1, stop=1)
            )
        except:
            google_first_page = "Error: They are robot proof!"
    return google_first_page


async def search_everywhere(search_terms):
    tasks = []
    for search_term in search_terms:
        tasks += [
            asyncio.ensure_future(get_yahoo_first_page(search_term)),
            asyncio.ensure_future(get_bing_first_page(search_term)),
            asyncio.ensure_future(get_aol_first_page(search_term)),
            asyncio.ensure_future(get_ask_first_page(search_term)),
            asyncio.ensure_future(get_mal_first_page(search_term)),
        ]
    responses = await asyncio.gather(*tasks)
    return responses


def search_everywhere_sync(search_term):
    tasks = [
        async_to_sync(get_yahoo_first_page)(search_term),
        async_to_sync(get_bing_first_page)(search_term),
        async_to_sync(get_aol_first_page)(search_term),
        async_to_sync(get_ask_first_page)(search_term),
        async_to_sync(get_mal_first_page)(search_term),
    ]
    return tasks


def run_sync(search_term):
    search_results = search_everywhere_sync(search_term)
    return get_search_dict(search_results)


def run_async(search_terms):
    search_dict = {}
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    search_results = loop.run_until_complete(search_everywhere(search_terms))
    loop.close()
    for search_term in search_terms:
        search_dict[search_term] = get_search_dict(search_results)
    return search_dict


def get_search_dict(search_results):
    i = 0
    search_dict = {
        "Yahoo": search_results[i+0],
        "Bing": search_results[i+1],
        "Aol": search_results[i+2],
        "Ask": search_results[i+3],
        "MyAnimeList": search_results[i+4],
    }
    return {k: v for k, v in search_dict.items() if v}
