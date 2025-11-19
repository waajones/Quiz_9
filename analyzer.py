def convert(text: str):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = []
    current = []

    for ch in text:
        if ch.isalnum() or ch == "_":
            current.append(ch.lower())
        else:
            if current:
                words.append("".join(current))
                current = []

    # If text ended with a word
    if current:
        words.append("".join(current))

    return words


def count_words(text: str) -> int:
    return len(convert(text))


def count_chars(text: str, include_spaces: bool = False) -> int:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if include_spaces:
        return len(text)

    count = 0
    for ch in text:
        if ch != " ":
            count += 1
    return count


def find_most_common_word(text: str):
    words = convert(text)
    if not words:
        return None

    freq = {}

    # Count manually
    for w in words:
        if w not in freq:
            freq[w] = 1
        else:
            freq[w] += 1

    # Determine the highest
    max_count = 0
    for count in freq.values():
        if count > max_count:
            max_count = count

    # Collect tied words
    candidates = []
    for w, c in freq.items():
        if c == max_count:
            candidates.append(w)

    return sorted(candidates)[0]


def count_unique_words(text: str) -> int:
    words = convert(text)
    seen = {}
    for w in words:
        seen[w] = True
    return len(seen)


def average_word_length(text: str) -> float:
    words = convert(text)
    if not words:
        return 0.0

    total_length = 0
    count = 0
    for w in words:
        total_length += len(w)
        count += 1

    return total_length / count
