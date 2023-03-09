# createObjectURL-XSS-Test
This repo contains a PoC that shows how `createObjectURL()` can be vulnerable to XSS. To test it yourself, you simply have to install and run the Python backend, and then open `xss-createObjectUrl.html`, and an alert will show up. To prevent XSS, `// a.download = true;` needs to be uncommented in `xss-createObjectUrl.html`.

In order to prevent `XSS` to happen, `a.download = true;` must be set!

# How to Install the Backend
- Simply run `pipenv shell` followed by `pipenv install`

# How to Run the Backend
- `python3 main.py`
