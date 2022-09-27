import function
function.make_sandwich('bread', 'cheese', 'butter', 'salt and pepper')

from function import make_sandwich
make_sandwich('bread', 'cheese')

from function import make_sandwich as ms
ms('bread', 'cheese', 'butter', 'cucumber', 'fresh herbs', 'lemon juice', 'salt and pepper')

import function as f
f.make_sandwich('butter', 'salt and pepper')

from function import *
make_sandwich('bread', 'cucumber', 'fresh herbs', 'lemon juice')