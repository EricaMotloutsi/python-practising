#smart looping technique: continue, pass, braeak

sentence = 'AI is the future of technology.'
for word in sentence.split():
    if word in ['the', 'in', 'of']:
        continue #skip this current iteration and move to the next one
    print(word, end=' ')


while True:
    prompt = input('Enter a prompt for the model:')
    if len(prompt)<5:
        print('Prompt too short. Try again!')
        continue 
    print(f'Processing your prompt {prompt}')
    break 

#pass #ToDo
for model in range(5):
    pass #placeholder while you finanlize the setup