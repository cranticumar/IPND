import json
import urllib2

def get_json_response(url):
    """
    Input: URL to an thirdparty website API
    Output: JSON object in dictionary format
    """
    return json.loads(urllib2.urlopen(url).read())

def json_dump(dictionary):
    """
    packages data as JSON object to be passed between different locations/nodes or frameworks
    """
    return json.dumps(dictionary)