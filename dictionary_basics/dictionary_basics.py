#Dictionary basics

model_config = {'model_name':'GPT-4', 'layers':48, 'parameters':'175B'}
print(model_config)

print(type(model_config))

hyperparameter = {
    'learning_rate':0.0001,
    'dropout_rate':0.3,
    'optimizer':'Adam'
}
print(type(hyperparameter))

#Adding a new value

hyperparameter['batch_size'] = 64
print(hyperparameter)

print(hyperparameter['learning_rate'])

print(hyperparameter.get('momentum', 'Not specified'))

#Nested dictionaries

pipeline_config={'GPT-4':{'layers': 48, 'parameters':'175B', 'attention_heads':96
          },
'BERT': {'layers':24,'parameters':'345M', 'attention_heads':16
      }
}
print(pipeline_config['GPT-4']['attention_heads'])