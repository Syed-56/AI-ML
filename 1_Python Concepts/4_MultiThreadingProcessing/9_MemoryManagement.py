import sys
a = [1, 2, 3]
print(sys.getrefcount(a))  # 2
b = a
print(sys.getrefcount(a))  # 3
del b
print(sys.getrefcount(a))  # 2

#Cyclic GC
import gc

gc.enable()       # on by default
gc.disable()      # turn off automatic cyclic collection
gc.collect()      # manually run a full collection, returns count of objects collected
print(gc.get_stats())     # per-generation stats (collections, collected, uncollectable)
print(gc.garbage)         # objects GC couldn't free (uncollectable), usually empty

#Circular Reference
import gc

class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} deleted")

obj1 = MyObject("obj1")
obj2 = MyObject("obj2")

obj1.reference = obj2
obj2.reference = obj1

del obj1
del obj2

gc.collect()  # needed — without this, __del__ won't fire (cycle keeps refcount > 0)

#Avoid Cycles in First Place
import weakref

class MyObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Object {self.name} deleted")

obj1 = MyObject("obj1")
obj2 = MyObject("obj2")

obj1.reference = weakref.ref(obj2)  # doesn't increase obj2's refcount
obj2.reference = weakref.ref(obj1)

del obj1
del obj2
# Both get deleted immediately via reference counting — no gc.collect() needed