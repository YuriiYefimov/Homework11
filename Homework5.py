story_title = 'THE BOY WHO LIVED'
story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were \
        proud to say that they were perfectly normal, thank \
        you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t \
        hold with such nonsense. \
        Mr. Dursley was the director of a fi rm called Grunnings, which \
        made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin \
        and blonde and had nearly twice the usual amount of neck, which \
        came in very useful as she spent so much of her time craning over \
        garden fences, spying on the neighbors. The Dursleys had a small \
        son called Dudley and in their opinion there was no fi ner boy \
        anywhere."

#all relpaces are SEPARATELY
story = story.replace("Mr.", "Mr")
story = story.replace("Mrs.", "Mrs")
story = " ".join(story.split())#убрал пробелы
story_list=story.split('.')
del story_list[-1]#тут есть вопрос. Последним элементом было постуо предложение, не понимаю, откуда оно появлялось
print(story_list)

#all relpaces in cycle for
REPLACEMENTS = [
    (".", ""),
    (",", ""),
]

for old, new in REPLACEMENTS:
  story = story.replace(old, new)
print(story)

story_words=story.split()
print(story_words)

wordscount_story_words = len(story_words)
print("Words count:",wordscount_story_words)
sentencescount_story_list = len(story_list)
print("Sentences count:",sentencescount_story_list)

story_title_len=len(story_title)
story_title_list=story_title[0:story_title_len].split('.')
full_text_list=story_list+story_title_list
print(full_text_list)

Dursley_count = story.count("Dursley")
print(Dursley_count)

print(story_words)
set_story_words=set(story_words)#convert list to set
print("The unique elements in story_words:\n")
unique_story_words=(list(set_story_words))#convert set to list
print(unique_story_words)
