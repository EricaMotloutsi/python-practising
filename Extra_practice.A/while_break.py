#The break statement
keywords= ['innovation', 'deep learning', 'AI revolution','neutral network', 'machine learning' ]
for word in keywords:
    print(f'Checking word {word}')
    if word == 'AI revolution':
        break 

while True: 
    user_input = input('Say the magic word to start:')
    if user_input.lower()=='launch':
        print('Starting the AI-powered chatbot!')
        break
    print("Hmm, that's not the magic word. Try again!")

