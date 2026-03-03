# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message

# short_texts = ['message1','message2','message3',]

# def messages(short_texts):
#     for short_text in short_texts:
#         print(short_text)


# messages(short_texts)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.



short_texts = ['message1','message2','message3',]
sent_messages = []

def send_message(short_texts):
   while short_texts:
    current_message = short_texts.pop()
    print(current_message)
    sent_messages.append(current_message)

send_message(short_texts[:])
print(f"lists are : {sent_messages} for sent messsages and \n{short_texts} for texts which were present in original ")



