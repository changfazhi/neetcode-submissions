class LRUCache:
    # need to find a way to find out which is the least used, i am thinking of using stack


    def __init__(self, capacity: int):
        # initialise capacity
        self.capacity = capacity
        self.mapping = {}
        

    def get(self, key: int) -> int:
        # if key exist return its value
        if key in self.mapping.keys():
            # save the value of the key 
            # del the pair then insert it back as it maintains insertion order
            value = self.mapping.get(key)
            del self.mapping[key]
            self.mapping[key] = value
            # this ensures that the last pair of the dict is the least used
            return self.mapping[key]
            # else return -1 if the key does not exist
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # if key, update value of key
        if key in self.mapping.keys():
            # replace the outdated value with the new value 
            del self.mapping[key]
            self.mapping[key] = value
        # if the key does not exist, we need to add the pair
        else:
            # we need to check the length of the mapping
            n = len(self.mapping)
            # if my current length, n is the same as the cap, i need to remove the least used
            if n == self.capacity:
                # remove the least used - which is the first pair in the dict
                # in order to remove i need to pop it
                for keyz in self.mapping.keys():
                    self.mapping.pop(keyz)
                    break
                # add the new key-value pair
                self.mapping[key] = value
                # i removed one and added one such that n is still n
            elif n < self.capacity:
                # if my current length is less than the pair, i have space to add one nore key-value pair
                self.mapping[key] = value

        
