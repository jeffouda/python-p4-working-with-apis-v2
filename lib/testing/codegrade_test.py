
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from open_library_api import Search

def test_get_search_results():
    search = Search()
    result = search.get_search_results()
    assert isinstance(result, bytes)
    assert b'title' in result

def test_get_search_results_json():
    search = Search()
    result = search.get_search_results_json()
    assert isinstance(result, dict)
    assert 'docs' in result
    assert len(result['docs']) == 1
    assert 'title' in result['docs'][0]
    assert 'author_name' in result['docs'][0]

def test_get_user_search_results():
    search = Search()
    result = search.get_user_search_results("the lord of the rings")
    assert isinstance(result, str)
    assert 'Title:' in result
    assert 'Author:' in result