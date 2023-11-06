# inheritance + extended + overriding + super()

class LoggingDict(dict):

    def __setitem__(self, key, value):
        print(f'set key: {key};value: {value}')
        super().__setitem__(key, value)


ld = LoggingDict()
ld['a'] = 'b'
print(ld)
