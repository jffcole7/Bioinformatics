def unique_count(thing):

    uniq_char_string=''.join(set(thing))
    uniq_char_count = len(uniq_char_string)
    return uniq_char_count


print unique_count("AAAAB")

print unique_count("AAAAAAAAAAAAAAAA")

print unique_count("AAAANNNNNNNNNNNNNNB")
