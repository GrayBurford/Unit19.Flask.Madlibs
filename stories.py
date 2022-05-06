"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    # init is auto called (like constructor). Story([words], "text")
    # words = list of parts of a sentence, i.e. verb, noun.
    # text = String of text with [words] list in {braces}
    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words # list of words
        self.template = text # String of text w/ {noun}, {verb}, etc.

    def generate(self, answers):
        """Substitute answers into text."""
        # answers is a dictonary to replace noun, verb, etc. with vals
        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" +key+ "}", val)

        return text

# Here's a story to get you started. Story([words], "text")
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

grays_story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """I'm a {noun}, I'm some {plural_noun} in a {place} that {verb} a {adjective} tofu."""
)

tinas_story = Story(
    ['verb', 'noun'],
    """I {verb} {noun}."""
)