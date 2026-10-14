# How Does an AI Actually Work?

A plain-English, no-jargon guide to how AI chatbots work, with things to click and play with along the way.

**Live site: [ai-for-dummies.info](https://ai-for-dummies.info)**

## What's on the site

- **Chat**: a pretend chatbot, plus a pop-the-hood view that animates what really happens when you press Send: the notebook, the model, the cache, tools and thinking.
- **Explore**: each part of a chatbot explained piece by piece (tokens, the model, the context window, thinking, tools and agents).
- **In the News**: scary AI headlines taken apart one question at a time.
- **FAQ**: the questions people ask most about chatbots.
- **Resources**: where to go next.

## Run it locally

It's a single static page, so there's nothing to build or install:

```sh
python3 serve.py        # then open http://localhost:8000 (or pass a port: python3 serve.py 8765)
```

`serve.py` is like `python3 -m http.server`, except that paths with no file extension (`/explore`, `/faq`, ...) serve `index.html`, the same as an nginx `try_files $uri $uri/ /index.html;` rule would.

## What's in the repo

```text
index.html     the whole site: HTML, CSS and JavaScript
serve.py       local dev server (see above)
sitemap.xml    sitemap for search engines
robots.txt     crawler rules
og-image.png   social sharing image
apple-touch-icon.png
docs/          notes and ideas
CLAUDE.md      notes on how the code is organised
```

## Support the site

If you found it useful, you can [buy me a coffee ☕](https://buymeacoffee.com/teknocat). You can find more about me at [peter-epp.dev](https://peter-epp.dev).
