glossary = {
            'function': 'A series of statements which returns some value to a caller. ',
            'list': 'A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).',
            'object': 'Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.',
            'PEP': 'Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.',
            'Zen of Python': 'Listing of Python design principles and philosophies that are helpful in understanding and using the language.',
            'lambda': 'keyword that lets you create lambda functions. These are anonymous functions used to perform simple computations.',
            'literals': 'Literals are data items that have a fixed value. Python allows several kinds of literals like string, numeric, boolean etc.',
            'loader': 'A loader is an object that loads a module that is being imported.',
            'loop': 'A loop is used for iterating over a sequence (like list, tuple, string, dictionary, set). Python offers two loops: for and while.',
            'module': 'A module is a file consisting of Python code. This module can be imported and the code within can be reused in another Python program.',
            'mutable': 'A mutable data type is one that can change its value during the program execution.',
            'pass': 'Pass keyword is used to write a pass statement. Pass statement is used when there is a syntactical need of a statement but your program’s logic doesn’t need one.',
            }
for key, value in glossary.items():
    print(f'\n {key.title()}')
    print(f'\t{value}')