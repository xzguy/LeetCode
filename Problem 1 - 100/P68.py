def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    result = []
    line_start = 0
    cur_line_word_len = 0
    line_space_total = 0
    # all lines before the last line
    for i in range(len(words)):
        if cur_line_word_len + len(words[i]) + i - line_start > maxWidth:
            line_space_total = maxWidth - cur_line_word_len
            new_line = ''
            for j in range(line_start, i):
                new_line += words[j]
                if i - j - 1 > 0:
                    if line_space_total % (i - j - 1) > 0:
                        num_space = line_space_total // (i - j - 1) + 1
                    else:
                        num_space = line_space_total // (i - j - 1)
                    new_line += ' ' * num_space
                    line_space_total -= num_space
            # in case of only one word in the 'new_line', pad space
            if len(new_line) < maxWidth:
                new_line += ' ' * (maxWidth - len(new_line))
            result.append(new_line)
            cur_line_word_len = len(words[i])
            line_start = i
        else:
            cur_line_word_len += len(words[i])
    # the last line
    new_line = ''
    for j in range(line_start, len(words)):
        new_line += words[j]
        if j < len(words) - 1:
            new_line += ' '
    if len(new_line) < maxWidth:
        new_line += ' ' * (maxWidth - len(new_line))
    result.append(new_line)
    return result

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(fullJustify(words, maxWidth))