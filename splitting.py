import re

sentence = "ما هى الجرائم الإلكترونية ؟ انواعها ؟ كيفية تنفيذها ! وطرق مواجهتها"
splits1 = sentence.split('!')
print(splits1)
for spl in splits1:
 print(spl)
 splits2 = spl.split('؟')
 print(splits2)