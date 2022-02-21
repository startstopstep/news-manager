sources_response_successful = {'status': 'ok', 'sources': [
    {'id': 'abc-news', 'name': 'ABC News',
     'description': 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',
     'url': 'https://abcnews.go.com', 'category': 'general', 'language': 'en',
     'country': 'us'},
    {'id': 'abc-news-au', 'name': 'ABC News (AU)',
     'description': "Australia's most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.",
     'url': 'http://www.abc.net.au/news', 'category': 'general',
     'language': 'en', 'country': 'au'},
]}

sources_response_error = {'status': 'error', 'code': 'apiKeyInvalid',
                          'message': 'Your API key is invalid or incorrect. Check your key, or go to https://newsapi.org to create a free API key.'}

top_headlines_response_successful = {'status': 'ok', 'totalResults': 211, 'articles': [
    {'source': {'id': 'news24', 'name': 'News24'}, 'author': 'Jeanette Chabalala',
     'title': 'I have made a lot of enemies through State Capture Inquiry work, Zondo tells Chief Justice panel',
     'description': '"Through the work of this commission, I have made a lot of enemies for myself, but it is not as if I did not know that taking this kind of job will land me in that situation. I knew," Justice Raymond Zondo has said during his JSC interview.',
     'url': 'https://www.news24.com/news24/SouthAfrica/News/i-have-made-a-lot-of-enemies-through-state-capture-inquiry-work-zondo-tells-chief-justice-panel-20220204',
     'urlToImage': 'https://cdn.24.co.za/files/Cms/General/d/2857/1681debe06634f46bba3d54cba6efeac.jpg',
     'publishedAt': '2022-02-04T15:28:08+00:00',
     'content': '<ul><li>Justice Raymond Zondo is vying for the position of chief justice.\xa0\xa0</li><li>Zondo said he had "made enemies" through his work on the State Capture Inquiry.\xa0</li><li>Zondo said that when he wa… [+4578 chars]'},
    {'source': {'id': 'news24', 'name': 'News24'}, 'author': 'Juniour Khumalo',
     'title': 'Mashatile says Mervyn Dirks was out of line, but latter insists he was just doing his job',
     'description': "Mervyn Dirks was placed on precautionary suspension after calling for Parliament's Standing Committee on Public Accounts to investigate President Cyril Ramaphosa.",
     'url': 'https://www.news24.com/news24/SouthAfrica/News/mashatile-says-mervyn-dirks-was-out-of-line-but-latter-insists-he-was-just-doing-his-job-20220204',
     'urlToImage': 'https://cdn.24.co.za/files/Cms/General/d/7417/54472526794b43288578cd5056e7a898.jpg',
     'publishedAt': '2022-02-04T15:28:08+00:00',
     'content': "<ul><li>Paul Mashatile insists Mervyn Dirks should have had the party's permission before he tried to hold Cyril Ramaphosa accountable.\xa0</li><li>Dirks disputes this, saying he was only doing his job … [+6193 chars]"},
]}

top_headlines_result_successful = [['name', 'author', 'title'],
                                   ['News24', 'Jeanette Chabalala',
                                    'I have made a lot of enemies through State Capture Inquiry work, Zondo tells Chief Justice panel'],
                                   ['News24', 'Juniour Khumalo',
                                    'Mashatile says Mervyn Dirks was out of line, but latter insists he was just doing his job'],
                                   ]
