import configparser

config = configparser.ConfigParser()
config['hyperparameters'] = {
    'batch_sizes' : [64, 128],
    'num_epochs' : 20,
    'learning_rate' : 0.001,
    'embed_dims' : 512,
    'num_lstm_units' : 512,
    'num_lstm_layers' : 2,
    'num_output_classes' : 5
}

path = r"D:\\Data\\Documents\\Rafi\\Python Scripts\\Corona_Tweets_BiLSTM\\"
filename = 'config.ini'
with open(path + filename, 'w') as conf:
    config.write(conf)
