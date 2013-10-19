import sys
sys.path.append('systemetric')

from systemetric import LifterBot
from sr2013.vision import MARKER_ARENA, MARKER_ROBOT, MARKER_PEDESTAL, MARKER_TOKEN

r = LifterBot("comp")

f = r.see()

print(f)
