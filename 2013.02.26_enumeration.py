# From psychopy import visual, core #import some libraries from PsychoPy.
from psychopy import core, visual, gui, data, misc, event
import time, numpy, random

allKeys=event.getKeys()
for thisKey in allKeys:
    if thisKey in ['q', 'escape']:
        core.quit()
event.clearEvents() 

# Create window.
mywin = visual.Window([1280,1042],monitor="testMonitor", units="deg", color = 'black')

# Write File.
file= open('enum' + '.csv', 'w')
file.write('position,correct,rt\n')

string_num_list = ['1','2','3','4','5','6','7','8','9','0','minus','equal']

# Create square number list.
sq_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Create square position list.
sq_pos_list = [[0,0], [0.6,0], [0,0.6], [-0.6,0], [0,-0.6], [1.2,0], [0,1.2], [1.2,1.2], [-1.2,-1.2], [-1.2,1.2], [1.2,-1.2], [-1.2,0], [0,-1.2], [-1.2,0.6], [-1.2,-0.6], [1.2,-0.6], [1.2,0.6], [0.6,0.6], [0.6,-0.6], [-0.6,0.6], [-0.6,-0.6], [-0.6,1.2], [0.6,1.2], [-0.6,-1.2], [0.6,-1.2]]

# Create trial list.
trial_list = data.TrialHandler(sq_num_list, nReps=1, method='random')

# Write instructions.
instructions = visual.TextStim(mywin, text = "In this task, a number of white boxes will be presented to you briefly.  Your goal is to correctly report the number of white boxes by pressing the number(s) on the keyboard.\n\nPress the A key when you are ready to start.", color = 'white', height = 1, pos = [0, 0])

# Write message to prompt user input.
message = visual.TextStim(mywin, text = "Please report the number of boxes using the keyboard.", color = 'white', height = 1, pos = [0, 0])

# Create clock.
clock = core.Clock()

# Make mouse invisible.
mouse = event.Mouse(visible = 0)

# Create unfilled rectangle.
square=visual.ShapeStim(mywin, lineWidth=1, lineColor='white', vertices=((-2, 2), (2, 2), (2, -2),(-2,-2)), closeShape=True)
#Q3 how do I make this square 5 x 5 degrees? maybe solved by function thru psychopy or matlab

# Create fixation cross.
vertical_line=visual.ShapeStim(mywin, lineWidth=2, lineColor='white', vertices=((0,.3),(0,-.3)), closeShape=True)
horiz_line=visual.ShapeStim(mywin, lineWidth=2, lineColor='white', vertices=((-.3,0),(.3,0)), closeShape=True)

# Grab the starting time.
startclock = clock.getTime()

# Grab the end time.
endclock = clock.getTime()

# Calculate completion time.
rt = endclock - startclock



# Present instructions until the 'a' key is pressed.
while 'a' not in event.getKeys():
    # Draw and present instructions.
    instructions.draw()
    mywin.flip()
    
# Go through trial list.
for trial in trial_list:
    mouse.setVisible(0)
    # Reset clock and clear events for trial.
    clock.reset()
    event.clearEvents()
    # Set stimuli presentation time.
    pres_time = 1.0
    # Set square size.
    sq_size = 0.5
    # Create square for current trial.
    pos_list = random.sample(sq_pos_list, trial) #random.choice for single item
    vertical_line.draw()
    horiz_line.draw()
    mywin.flip()
    core.wait(.5)
    for pos in pos_list:
        visual.PatchStim(win=mywin, size=sq_size, pos=pos, sf = 0, color='white').draw()
    square.draw()
    mywin.flip()
    core.wait(pres_time)
    message.draw()
    mywin.flip()
    startclock = clock.getTime() 
    if string_num_list[trial-1] in event.waitKeys(): 
        correct = 1
    else: 
        correct = 0
    endclock = clock.getTime()
    rt = endclock - startclock
    print rt
    file.write(str(trial) + '\t' + str(correct) + '\t' + str(rt) + '\n')