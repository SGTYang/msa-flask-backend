import urllib.request
import json
from flask import Flask

app = Flask(__name__)

@app.route('/details/<string:movie_code>', methods=['GET'])

def get_movie_details(movie_code):
    key_num = '7a5569340435ebbf7c32fbfa54d229a9'
    url_get_details = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    url = f'{url_get_details}?key={key_num}&movieCd={movie_code}'
    
    req = urllib.request.Request(url)
    data_get = urllib.request.urlopen(req).read()
    data_json = json.loads(data_get)
    
    return json.dumps(data_json)

if __name__=="__main__":
   app.run(host="0.0.0.0", port="80", debug=True)
