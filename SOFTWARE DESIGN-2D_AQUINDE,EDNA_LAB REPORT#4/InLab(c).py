a="pots&pans"
b=a.split("&")

def reverse(word):

    if not word:
        return ""

    return reverse(word[1:]) + word[0]

result = reverse(b[1]) + "&" + reverse(b[0])

print(result)
