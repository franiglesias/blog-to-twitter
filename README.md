# Blog-to-twitter

This is a simple script to check RSS from a blog and publish new posts to twitter.

## Configuration

Copy `config.yaml.dist` to `config.yml`

```
cp config.yaml.dist config.yml
```

Replace placeholders with your data. They should be self-explanatory, but you can read some explanations in a moment.

```
twitter:
    consumer_key: twitter_api_consumer_key
    consumer_secret: twitter_api_consumer_secret
    access_token: twitter_api_access_token
    access_token_secret: twitter_api_access_token_secret

feed:
    name: name_of_the_site
    uri: absolute_uri_to_feed
    days: 1
```

`twitter.*`: credentials for your registered app in twitter.

`feed.name`: the name of the site you are publishing.
`feed.uri`: absolute uri of the feed. For example: `'https://franiglesias.github.io/feed.xml'`
`feed.days`: number of days before today since you want to retrieve posts from the RSS. Typical setup is `1`, allowing the announcement of post published the same day the script runs.

The script will publish all posts found.

## Basic usage

Run:

```
./blog-to-twitter
```