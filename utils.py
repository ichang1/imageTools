def camel(s):
    words = s.split("_")
    s_raw = [words[i].lower() if i == 0 else words[i].lower().capitalize() for i in range(len(words))]
    s_camel = "".join(s_raw)
    return s_camel