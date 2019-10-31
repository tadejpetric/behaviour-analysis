import glob_vars
import sys
import csv


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


class State:
    def __init__(self, handler):
        self.handler = handler
        
        self.bodyflag = False
        self.timerflag = False
        
        self.delay = 33.0
        self.frameid = 0
        
        self.typenum = 0
        self.positions = [world_position() for _ in range(20)]
        self.bodyid = 0
        self.fps = 30
        self.people_cnt = 0

    def write_state(self):
        row = [self.frameid, self.delay, self.people_cnt, self.bodyid]

        def unpack(pos):
            return [pos.x, pos.y, pos.z]
        for pos in self.positions:
            row.append(unpack(pos))
        self.handler.writerow(row)


def create_patterns():
    def c_bflag(x, endevent):
        x.bodyflag = not x.bodyflag
        if endevent:
            x.write_state()
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
    def c_ppl_cnt(state, newppl):
        state.people_cnt = newppl
        return state

    def to_float(x):
        return float(x)
    def to_int(x):
        return int(x)

    patterns = {
        "###": lambda state: (lambda _: c_timerflag(state)),
        "---": lambda state: (lambda data: c_bflag(state, bool(int(data)))),
        "ms": lambda state: (lambda data: c_delay(state, float(data))),
        "fps": lambda state: (lambda data: c_fps(state, float(data))),
        "type": lambda state: (lambda data: c_type(state, int(data))),
        "x:": lambda state: (lambda data: c_x_coor(state, float(data))),
        "y:": lambda state: (lambda data: c_y_coor(state, float(data))),
        "z:": lambda state: (lambda data: c_z_coor(state, float(data))),
        "frame": lambda state: (lambda data: c_frameid(state, int(data))),
        "body_id": lambda state: (lambda data: c_bodyid(state, int(data))),
        "people": lambda state: (lambda data: c_ppl_cnt(state, int(data))),
    }
    return patterns


def extract(line):
    data = line.split(" ", 2)
    x = data[0]
    xs = data[1]
    xss = "" if len(data) == 2 else data[2]
    return (x, xs, xss)


def dispatch(filename):
    newfilename = csv_filename(filename)

    patterns = create_patterns()

    with open(filename, "r") as fread, open(newfilename, "w") as fwrite:
        state = State(csv.writer(fwrite))

        for line in fread:
            while line != "":
                head, data, line = extract(line)
                # We get a function that takes the value and sets the correct
                # parameter. Also returns the correct function for
                # casting the data to the needed type
                action = patterns[head](state)
                state = action(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Priloži datoteko za pretvorbo v csv")
        sys.exit()
    dispatch(filename)
