from fastapi import FastAPI

from .api import (hello_router)

app = FastAPI(title='Astrolens API',
              description='This is the first FastAPI example for the Astrolens project.',
              version='0.1.0',
              contact={
                  'name': 'Steven Karbjinsky',
                  'url': 'https://github.com/xKabbe/astrolens',
                  'email': 'steven.karbjinsky@web.de',
              },
              license_info={
                  'name': 'MIT License',
                  'url': 'https://github.com/xKabbe/astrolens/blob/master/LICENSE',
              })

# Include routers from endpoints
app.include_router(hello_router)
