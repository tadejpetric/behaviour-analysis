import glob_vars
import sys
from collections import defaultdict as ddick


class world_position:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


def csv_filename(filename):
    newfilename = ""
    for char in filename:
        if char != ".":
            newfilename += char
        else:
            break
    return newfilename + ".csv"


class state:
    def __init__(self):
        self.bodyflag = False
        self.timerflag = False
        
        self.delay = None
        self.frameid = None
        
        self.typenum = None
        self.positions = [world_position() for _ in range(20)]
        self.bodyid = None
        self.fps = None


def create_patterns():
    def c_bflag(x):
        x.bodyflag = not x.bodyflag
        return x
    def c_timerflag(x):
        x.timerflag = not x.timerflag
        return x
    def c_type(x, newtype):
        x.typenum = newtype
        return x
    def c_x_coor(state, newx):
        curtype = state.typenum
        state.positions[curtype].x = newx
    def c_y_coor(state, newy):
        curtype = state.typenum
        state.positions[curtype].y = newy
    def c_z_coor(state, newz):
        curtype = state.typenum
        state.positions[curtype].z = newz
    def c_delay(state, newdelay):
        state.delay = newdelay
        return state
    def c_frameid(state, newid):
        state.frameid = newid
        return state
    def c_bodyid(state, newid):
        state.bodyid = newid
        return state
    def c_fps(state, newfps):
        state.fps = newfps
        return state

    patterns = {
        "###": lambda state: (lambda _: c_timerflag(state)),
        "---": lambda state: (lambda _: c_bflag(state)),
        "ms": lambda state: (lambda data: c_delay(state, data)),
        "fps": lambda state: (lambda data: c_fps(state, data)),
        "type": lambda state: (lambda data: c_type(state, data)),
        "x:": lambda state: (lambda data: c_x_coor(state, data)),
        "y:": lambda state: (lambda data: c_y_coor(state, data)),
        "z:": lambda state: (lambda data: c_z_coor(state, data)),
        "body_id": lambda state: (lambda data: c_bodyid(state, data)),
    }
    return patterns


def dispatch(filename):
    newfilename = csv_filename(filename)

    delay = 0
    frameid = 0
    
    with open(filename, "r") as fread, open(newfilename, "w") as fwrite:
        bodyflag = False
        timerflag = False

        patterns = {
            "###": lambda state: (not tf, bf, "", lambda x: x),
            "---": lambda tf, bf, line: (tf, not bf, "", lambda x: x)
        }
        
        for line in fread:
            while line != "":
                action = patterns[line]
                timerflag, bodyflag, line, func = action(timerflag, bodyflag, line)
                state = func(state)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Priloži datoteko za pretvorbo v csv")
        sys.exit()
    dispatch(filename)
