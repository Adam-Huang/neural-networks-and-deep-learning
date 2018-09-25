import network
import mnist_loader

def exchange_data(traning_data):
    new_one = []
    for i in range(len(traning_data[0])):
        temp=[0,0,0,0,0,0,0,0,0,0]
        temp[traning_data[1][i]] = 1
        new_one.append([traning_data[0][i],temp])
    return new_one

if __name__=="__main__":
    training,validation,test = mnist_loader.load_data()
    training = list(training)
    validation = list(validation)
    test = list(test)
    tra = exchange_data(training)
    val = exchange_data(validation)
    tet = exchange_data(test)
    ne = network.Network([784,30,10])
    ne.SGD(tra,30,10,3.0,test_data=tet)