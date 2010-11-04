# readMat
# Reads a directory full of matlab files. Creates corresponding
#   python pickles to be picked up by another program
# 
# Copyright 2010 Russ Ferriday November 2009, russf@topia.com
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
import os
import pickle
import scipy.io as sio

root = './data_in'
out = './data_out'
dirList = os.listdir(root)
for fname in dirList:
    path = os.path.join(root, fname)
    print path
    mat_contents = sio.loadmat(path)
    f = open(os.path.join(out,fname), 'w')
    pickle.dump(mat_contents, f)
    f.close()
