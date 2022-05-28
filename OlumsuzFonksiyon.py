def olumsuzKarakter(String):
    if len(String)>0 and "degil" in String:
        return String
    else:
        return String+" degil"

print(olumsuzKarakter("mukemmel"))