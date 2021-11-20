# Twitter bot

This is a Twitter bot made for the purpose of testing Twitter's API

## Setup
1. Clone the repo
2. Create a config.json file and place it in `twitterbot/src` folder
with the syntax of
```
{
  "api_key": "<insert api key here>",
  "api_key_secret": "<insert api key secret here>",
  "access_token": "<insert access token here>",
  "access_token_secret": "<insert access token secret here>",
  "bearer_token": "<insert bearer token here>"
}
```
3. Create a virtual environment
```
python3 -m venv <name of environment>
```

4. Run requirements.txt
```
pip install -r requirements.txt
```

## Future Ideas
1. Make this into a Flask or FastAPI app to perform actions through implemented API

## Contribution guidelines
1. Each contribution should be in a separate branch
2. A Pull Request (PR) will be created to merge changes into the master branch
3. Each Pull Request (PR) title will need to have the one of the
following prefix
```
- feat:     A new feature
- fix:      A bug fix
- docs:     Documentation only changes
- style:    Formatting, missing semi-colons, white-space, etc
- refactor: A code change that neither fixes a bug nor adds a feature
- perf:     A code change that improves performance
- test:     Adding missing tests
- chore:    Maintain. Changes to the build process or auxiliary tools/libraries/documentation
``` 