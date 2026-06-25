s = "A man, a plan, a canal: Panama"
avoid = "!@#$%^&*(){}[]\\|:;\"'<,>.?/"

res = ""

for ch in s:
    if ch not in avoid and ch != " ":
        ch=ch.lower()
        res+=ch

if res == res[::-1]:
    print(f"Sentance \"{s}\" is Palindrome")
else:
    print(f"Sentance \"{s}\" is Not Palindrome")
