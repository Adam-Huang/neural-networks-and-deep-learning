import network
import mnist_loader

def exchange_data(traning_data):
    new_one = []
    for i in range(len(traning_data[0])):
        new_one.append([traning_data[0][i],traning_data[1][i]])
    return new_one

if __name__=="__main__":
    training,validation,test = mnist_loader.load_data()
    training = list(training)
    validation = list(validation)
    test = list(test)
