#!/usr/bin/env bash

cd "$(dirname "$0")"

set -o errexit
set -o pipefail
set -o nounset

mkdir -p data/favorites

page=1
while true; do
    echo "page=${page}"
    curl "https://news.ycombinator.com/upvoted?id=jaytaylor&p=${page}" \
        -H 'accept-encoding: gzip, deflate, sdch, br' \
        -H 'accept-language: en-US,en;q=0.8' \
        -H 'upgrade-insecure-requests: 1' \
        -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36' \
        -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
        -H 'cache-control: max-age=0' \
        -H 'authority: news.ycombinator.com' \
        -H "cookie: $(cat .cookie)" \
        --compressed \
        --silent \
        --fail \
        --show-error > "data/favorites/${page}.html"
    page=$(("${page}" + 1))
done

