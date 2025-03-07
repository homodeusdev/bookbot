def count_words(text):
    return len(text.split())

def count_chars(text):
    result = {}
    text = text.lower()
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_char_counts(counts):
    sorted_list = [{"character": char, "count": count} for char, count in counts.items()]
    sorted_list.sort(key=lambda item: item["count"], reverse=True)
    return sorted_list

