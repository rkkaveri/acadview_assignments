#Q1.Extract the user id, domain name and suffix from the following email addresses. 
#emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com" 
#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')] 

import re
emails = ["zuck26@facebook.com", "page33@google.com",
"jeff42@amazon.com"]
desired_output=[]
for e in emails:
    desired_output.append(tuple(re.split('[@.]',e)))

print(desired_output)



#Q2.Retrieve all the words starting with ‘b’ or ‘B’ from the following text.

import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better." 
desired_output=re.findall('[bB]\S*',text)
print(desired_output)



#Q3. Split the following irregular sentence into words
import re
sentence = "A, very very; irregular_sentence"
desired_output=re.sub('[\W_]',' ',sentence)
print(desired_output)



