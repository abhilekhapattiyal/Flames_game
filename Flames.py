import streamlit as st
st.title("Welcome to the game")
a=st.text_input("Enter first name-")
b=st.text_input("Enter second name-")
a=list(a)
b=list(b)
count=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            a[i]='0'
            b[j]='0' 
            break
count=0
for i in a+b:
    if i!=0:
        count+=1
res=["Friends","Lovers","Attraction","Marriage","Enemies","Siblings"]
while len(res)>1:
    splitIndex=(count%len(res)-1)
    if splitIndex>=0:
        right=res[splitIndex+1:]
        left=res[:splitIndex]
        res=right+left
    else:
        res=res[:len(res)-1]
if st.button('submit'):
    st.success(res[0])