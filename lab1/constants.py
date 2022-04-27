REGEX_WORDS = r"(?:(?:[^a-zA-Z]+')|(?:'[^a-zA-Z]+))|(?:[^a-zA-Z']+)"
REGEX_SENTENCES = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"