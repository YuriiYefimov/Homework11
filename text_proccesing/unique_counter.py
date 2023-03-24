story = 'DOWN THE RABBIT HOLE. Alice had sat on the bank by her sis-ter till she was tired.' \
        'Once or twice she had looked at the book her sis-ter held in her hand,' \
        'but there were no pict-ures in it, "and what is the use of a book," thought Alice,' \
        '"with-out pict-ures?" She asked her-self as well as she could,' \
        'for the hot day made her feel quite dull, if it would be worth while' \
        'to get up and pick some dai-sies to make a chain.' \
        'Just then a white rab-bit with pink eyes ran close by her.'

print(story)


def how_many_uniq_words(story):
    new_story = story.replace("-", "")
    new_story = new_story.replace('"', "")
    new_story = new_story.upper()
    new_story = new_story.replace(".", ". ")
    new_story = new_story.replace(",", " ")
    new_story = new_story.replace("?", "")
    new_story = new_story.replace(".", " ")
    new_story = new_story.replace("-", "")
    new_story = " ".join(new_story.split())
    new_story_list = new_story.split()
    set_new_story_words = set(new_story_list)  # convert list to set
    unique_new_story_words = (list(set_new_story_words))  # convert set to list
    counts = []
    b = 0
    for i in unique_new_story_words:
        b = new_story_list.count(i)
        counts.append(b)

    result_in_dict = dict(zip(unique_new_story_words, counts))
    return (result_in_dict)


how_many_uniq_words(story)
