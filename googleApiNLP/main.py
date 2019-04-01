#!/usr/bin/env python3
"""Main file of the google api fetcher module."""
import httplib2
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys

class NLPFetcher(object):

    """Application of the project."""

    def __init__(self):
        """Initiliaze the language fetcher."""
        self.client = language.LanguageServiceClient()


    def fetch_sentiment(self, data: str):
        """Fetch document information from google cloud."""
        document = types.Document(
            content=data,
            type=enums.Document.Type.PLAIN_TEXT
        )
        return self.client.analyze_sentiment(document=document)

    def fetch_entities(self, data: str):
        """Fetch document syntax information from google cloud."""
        document = types.Document(
            content=data,
            type=enums.Document.Type.PLAIN_TEXT
        )
        return self.client.analyze_syntax(document=document)

    def _parse_args(self, argv) -> str:
        """Parse program argument if it's fail exit with error."""
        try:
            self.data = argv[1]
            try:
                self.fetch_type = argv[2]
            except IndexError:
                self.fetch_type = "--entities"
        except IndexError:
            sys.stderr.write("You need to have at least one argument.")
            sys.exit(1)

    def run(self, argv):
        """Run the fetcher as a program."""
        self._parse_args(sys.argv)
        if "--sentiment" == self.fetch_type:
            print("Launching sentiments: \n", self.fetch_sentiment(self.data))
        else:
            print("Launching entities: \n", self.fetch_entities(self.data))

if __name__ == "__main__":
    fetcher = NLPFetcher()
    fetcher.run(sys.argv)
