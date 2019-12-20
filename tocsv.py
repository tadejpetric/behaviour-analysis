# import glob_vars
import sys
import csv
import os

executed = False


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
        global executed
        executed = True
        row = [self.frameid, self.fps, self.people_cnt, self.bodyid]

        def unpack(pos):
            return [pos.x, pos.y, pos.z]
        for pos in self.positions:
            row.append(unpack(pos))
        self.handler.writerow(row)


def create_patterns():
    def c_bflag(state, endevent):
        state.bodyflag = not state.bodyflag
        if endevent:
            state.write_state()
        return state

    def c_timerflag(state):
        state.timerflag = not state.timerflag
        return state

    def c_type(state, newtype):
        state.typenum = newtype
        return state

    def c_x_coor(state, newx):
        curtype = state.typenum
        state.positions[curtype].x = newx
        return state

    def c_y_coor(state, newy):
        curtype = state.typenum
        state.positions[curtype].y = newy
        return state

    def c_z_coor(state, newz):
        curtype = state.typenum
        state.positions[curtype].z = newz
        return state

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


def dispatch(fin, fout):
    global executed
    executed = False
    patterns = create_patterns()

    with open(fin, "r") as fread, open(fout, "w") as fwrite:
        header_row = ["frameid", "fps", "people_cnt", "bodyid",
                      "Head", "ShoulderSpine", "LeftShoulder", "LeftElbow",
                      "LeftHand", "RightShoulder", "RightElbow", "RightHand",
                      "MidSpine", "BaseSpine", "LeftHip", "LeftKnee", "LeftFoot",
                      "RightHip", "RightKnee", "RightFoot", "LeftWrist",
                      "RightWrist", "Neck", "Unknown"]
        csv.writer(fwrite).writerow(header_row)
        state = State(csv.writer(fwrite))
        for line in fread:
            while line != "":
                head, data, line = extract(line)
                # We get a function that takes the value and sets the correct
                # parameter. Also returns the correct function for
                # casting the data to the needed type
                action = patterns[head](state)
                state = action(data)
    if not executed:
        os.remove(fout)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Prilozi datoteko za pretvorbo v csv in izhod")
        sys.exit()
    dispatch(sys.argv[1], sys.argv[2])
