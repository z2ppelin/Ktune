import Ktune

t = Ktune.Sequential()
t.network("fully connected")
t.layersize(3)
t.add(784)
t.add(120)
t.add(10)
t.activation("sigmoid")
t.loss("mean_squared_error")
t.optimizer("sgd")
t.data("mnist")
t.show();
t.fit(64,10,0.8);
