# snipped_url
Given a long URL link, it generates a shorter link that works.


----
|  Endpoint  | HTTP Verb |   Request    |                   Body Action                    |
|:----------:|:---------:|:------------:|:------------------------------------------------:|
|     /      |    GET    |    :---:     |              Returns a Hello world               |
|   /`url`   |   POST    | `target_url` | shows the shortened url and some additional info |
| /{url_key} |    GET    |              |              goes to the target url              |
|   :---:    |   :---:   |    :---:     |                      :---:                       |
|            |           |              |                                                  |
|            |           |              |                                                  |


## How to Run

- First create a virtual environment and activate it.
- Run `pip install -r requirements.txt`
- Run `python run.py` to start the server.

`uvicorn snipped_url_app.main:app --reload`

If your browser doesn't open automatically, point it to [http://127.0.0.1:8521/](http://127.0.0.1:8521/). When the visualization loads, press Reset, then Run.
`pip install -r requirement.txt`
`npm i --save-dev typescript jest browser-sync rimraf @types/jest npm-run-all`
