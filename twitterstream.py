import cherrypy
import pandas as pd
import myprocessor
import os

p = myprocessor.MyProcessor()
consumer_key = os.environ['CONSUMERKEY']


class MyWebService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self):
        print(f'Consumer Key {consumer_key}')
        data = cherrypy.request.json
        df = pd.DataFrame(data)
        output = p.run(df)
        return output.to_json()
