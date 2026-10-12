#!/usr/bin/env python3
"""Local dev server: like `python3 -m http.server`, but a path with no file extension that doesn't exist
(/explore, /faq ...) serves index.html, the same as the nginx rule `try_files $uri $uri/ /index.html;`.
Usage: python3 serve.py [port]"""
import http.server, os, sys

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')  # always show the latest edits
        super().end_headers()

    def send_head(self):
        name = self.path.split('?')[0].split('#')[0]
        if not os.path.exists(self.translate_path(name)) and '.' not in os.path.basename(name):
            self.path = '/index.html'
        return super().send_head()

http.server.test(HandlerClass=Handler, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
