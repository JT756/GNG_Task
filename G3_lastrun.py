#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.1),
    on April 18, 2020, at 02:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.1'
expName = 'try1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Josef Haydn\\Desktop\\SemesterVI\\AP\\G3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instructions_Text = visual.TextStim(win=win, name='Instructions_Text',
    text='Experiment: Influence of emotional information in biasing performance\n\nTask: Go and Nogo Tasks\n\nInstructions:\n1.Press Space Bar when Target stimuli appears\n2.Do not press a key when Non-Target stimuli appears\n\n3.There will be three runs in the experiment\n\nPress Space Bar to continue',
    font='Arial',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Instructions_Key_Next = keyboard.Keyboard()

# Initialize components for Routine "Instructions_TR1"
Instructions_TR1Clock = core.Clock()
ITR1 = visual.TextStim(win=win, name='ITR1',
    text="This is the first practise run.\n8 images will be shown for 500 milli second and the \ninter-stimulus time will be 2000 milli second\n\nTargets: Happy and Angry facial expressions\nNon-Targets: Neutral facial expressions\n\nPress Space Bar for target using your dominant\nhand's thumb.\nRespond as fast as possible without making mistakes\n\nPress space bar to continue\n",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "TR1_Image"
TR1_ImageClock = core.Clock()
Image_TR1 = visual.ImageStim(
    win=win,
    name='Image_TR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Key_TR1 = keyboard.Keyboard()

# Initialize components for Routine "TR1_W"
TR1_WClock = core.Clock()
Wait_TR1 = visual.ImageStim(
    win=win,
    name='Wait_TR1', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Instructions_AR1"
Instructions_AR1Clock = core.Clock()
IR1 = visual.TextStim(win=win, name='IR1',
    text="This is the first actual run.\n60 images will be shown for 500 milli second and the \ninter-stimulus time will be 2000 milli second\n\nTargets: Happy and Angry facial expressions\nNon-Targets: Neutral facial expressions\n\nPress Space Bar for target using your dominant\nhand's thumb.\nRespond as fast as possible without making mistakes\n\nPress space bar to continue",
    font='Arial',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "AR1_Image"
AR1_ImageClock = core.Clock()
Image_AR1 = visual.ImageStim(
    win=win,
    name='Image_AR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Key_AR1 = keyboard.Keyboard()

# Initialize components for Routine "AR1_W"
AR1_WClock = core.Clock()
Wait_AR1 = visual.ImageStim(
    win=win,
    name='Wait_AR1', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Instructions_TR2"
Instructions_TR2Clock = core.Clock()
ITR2 = visual.TextStim(win=win, name='ITR2',
    text="This is the first practise run.\n8 images will be shown for 500 milli second and the \ninter-stimulus time will be 2000 milli second\n\nTargets: Angry and Neutral facial expressions\nNon-Targets: Happy facial expressions\n\nPress Space Bar for target using your dominant\nhand's thumb.\nRespond as fast as possible without making mistakes\n\nPress space bar to continue\n",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "TR2_Image"
TR2_ImageClock = core.Clock()
Image_TR2 = visual.ImageStim(
    win=win,
    name='Image_TR2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Key_TR2 = keyboard.Keyboard()

# Initialize components for Routine "TR2_W"
TR2_WClock = core.Clock()
Wait_TR2 = visual.ImageStim(
    win=win,
    name='Wait_TR2', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Instructions_AR2"
Instructions_AR2Clock = core.Clock()
IRA2 = visual.TextStim(win=win, name='IRA2',
    text="This is the first actual run.\n60 images will be shown for 500 milli second and the \ninter-stimulus time will be 2000 milli second\n\nTargets: Angry and Neutral facial expressions\nNon-Targets: Happy facial expressions\n\nPress Space Bar for target using your dominant\nhand's thumb.\nRespond as fast as possible without making mistakes\n\nPress space bar to continue",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "AR2_Image"
AR2_ImageClock = core.Clock()
Image_AR2 = visual.ImageStim(
    win=win,
    name='Image_AR2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Key_AR2 = keyboard.Keyboard()

# Initialize components for Routine "AR2_W"
AR2_WClock = core.Clock()
Wait_AR2 = visual.ImageStim(
    win=win,
    name='Wait_AR2', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Instructions_TR3"
Instructions_TR3Clock = core.Clock()
ITR3 = visual.TextStim(win=win, name='ITR3',
    text="This is the first practise run.\n8 images will be shown for 500 milli second and the \ninter-stimulus time will be 2000 milli second\n\nTargets: Happy and Neutral facial expressions\nNon-Targets: Angry facial expressions\n\nPress Space Bar for target using your dominant\nhand's thumb.\nRespond as fast as possible without making mistakes\n\nPress space bar to continue\n",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "TR3_Image"
TR3_ImageClock = core.Clock()
Image_TR3 = visual.ImageStim(
    win=win,
    name='Image_TR3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Key_TR3 = keyboard.Keyboard()

# Initialize components for Routine "TR3_W"
TR3_WClock = core.Clock()
Wait_TR3 = visual.ImageStim(
    win=win,
    name='Wait_TR3', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Instructions_AR3"
Instructions_AR3Clock = core.Clock()
IAR3 = visual.TextStim(win=win, name='IAR3',
    text="This is the first practise run.\n60 images will be shown for 500 milli second and the \ninter-stimulus time will be 2000 milli second\n\nTargets: Happy and Neutral facial expressions\nNon-Targets: Angry facial expressions\n\nPress Space Bar for target using your dominant\nhand's thumb.\nRespond as fast as possible without making mistakes\n\nPress space bar to continue\n",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "AR3_Image"
AR3_ImageClock = core.Clock()
Image_AR3 = visual.ImageStim(
    win=win,
    name='Image_AR3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Key_AR3 = keyboard.Keyboard()

# Initialize components for Routine "AR3_W"
AR3_WClock = core.Clock()
Wait_AR3 = visual.ImageStim(
    win=win,
    name='Wait_AR3', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "End_Instructions"
End_InstructionsClock = core.Clock()
EI = visual.TextStim(win=win, name='EI',
    text='End of the experiment\n',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
Instructions_Key_Next.keys = []
Instructions_Key_Next.rt = []
_Instructions_Key_Next_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Instructions_Text, Instructions_Key_Next]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_Text* updates
    if Instructions_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Text.frameNStart = frameN  # exact frame index
        Instructions_Text.tStart = t  # local t and not account for scr refresh
        Instructions_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Text, 'tStartRefresh')  # time at next scr refresh
        Instructions_Text.setAutoDraw(True)
    
    # *Instructions_Key_Next* updates
    waitOnFlip = False
    if Instructions_Key_Next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_Key_Next.frameNStart = frameN  # exact frame index
        Instructions_Key_Next.tStart = t  # local t and not account for scr refresh
        Instructions_Key_Next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_Key_Next, 'tStartRefresh')  # time at next scr refresh
        Instructions_Key_Next.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Instructions_Key_Next.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Instructions_Key_Next.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Instructions_Key_Next.status == STARTED and not waitOnFlip:
        theseKeys = Instructions_Key_Next.getKeys(keyList=['space'], waitRelease=False)
        _Instructions_Key_Next_allKeys.extend(theseKeys)
        if len(_Instructions_Key_Next_allKeys):
            Instructions_Key_Next.keys = _Instructions_Key_Next_allKeys[-1].name  # just the last key pressed
            Instructions_Key_Next.rt = _Instructions_Key_Next_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions_Text.started', Instructions_Text.tStartRefresh)
thisExp.addData('Instructions_Text.stopped', Instructions_Text.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --------Prepare to start Staircase "trials_7" --------
# set up handler to look after next chosen value etc
trials_7 = data.StairHandler(startVal=0.5, extraInfo=expInfo,
    stepSizes=[0.8,0.8,0.4,0.4,0.2], stepType='log',
    nReversals=0, nTrials=2, 
    nUp=1, nDown=2,
    minVal=0, maxVal=1,
    originPath=-1, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
level = thisTrial_7 = 0.5  # initialise some vals

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    level = thisTrial_7
    
    # set up handler to look after randomisation of conditions etc
    trials_8 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_8')
    thisExp.addLoop(trials_8)  # add the loop to the experiment
    thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    for thisTrial_8 in trials_8:
        currentLoop = trials_8
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
        if thisTrial_8 != None:
            for paramName in thisTrial_8:
                exec('{} = thisTrial_8[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Instructions_TR1"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        Instructions_TR1Components = [ITR1, key_resp_3]
        for thisComponent in Instructions_TR1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instructions_TR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instructions_TR1"-------
        while continueRoutine:
            # get current time
            t = Instructions_TR1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instructions_TR1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITR1* updates
            if ITR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITR1.frameNStart = frameN  # exact frame index
                ITR1.tStart = t  # local t and not account for scr refresh
                ITR1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITR1, 'tStartRefresh')  # time at next scr refresh
                ITR1.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions_TR1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions_TR1"-------
        for thisComponent in Instructions_TR1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_8.addData('ITR1.started', ITR1.tStartRefresh)
        trials_8.addData('ITR1.stopped', ITR1.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials_8.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials_8.addData('key_resp_3.rt', key_resp_3.rt)
        trials_8.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        trials_8.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        # the Routine "Instructions_TR1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Trial1.xlsx'),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "TR1_Image"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            Image_TR1.setImage(Image_Name)
            Key_TR1.keys = []
            Key_TR1.rt = []
            _Key_TR1_allKeys = []
            # keep track of which components have finished
            TR1_ImageComponents = [Image_TR1, Key_TR1]
            for thisComponent in TR1_ImageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TR1_ImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TR1_Image"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TR1_ImageClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TR1_ImageClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Image_TR1* updates
                if Image_TR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Image_TR1.frameNStart = frameN  # exact frame index
                    Image_TR1.tStart = t  # local t and not account for scr refresh
                    Image_TR1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Image_TR1, 'tStartRefresh')  # time at next scr refresh
                    Image_TR1.setAutoDraw(True)
                if Image_TR1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Image_TR1.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Image_TR1.tStop = t  # not accounting for scr refresh
                        Image_TR1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Image_TR1, 'tStopRefresh')  # time at next scr refresh
                        Image_TR1.setAutoDraw(False)
                
                # *Key_TR1* updates
                waitOnFlip = False
                if Key_TR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_TR1.frameNStart = frameN  # exact frame index
                    Key_TR1.tStart = t  # local t and not account for scr refresh
                    Key_TR1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_TR1, 'tStartRefresh')  # time at next scr refresh
                    Key_TR1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_TR1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_TR1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_TR1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_TR1.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_TR1.tStop = t  # not accounting for scr refresh
                        Key_TR1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_TR1, 'tStopRefresh')  # time at next scr refresh
                        Key_TR1.status = FINISHED
                if Key_TR1.status == STARTED and not waitOnFlip:
                    theseKeys = Key_TR1.getKeys(keyList=['space'], waitRelease=False)
                    _Key_TR1_allKeys.extend(theseKeys)
                    if len(_Key_TR1_allKeys):
                        Key_TR1.keys = _Key_TR1_allKeys[-1].name  # just the last key pressed
                        Key_TR1.rt = _Key_TR1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TR1_ImageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TR1_Image"-------
            for thisComponent in TR1_ImageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('Image_TR1.started', Image_TR1.tStartRefresh)
            trials.addData('Image_TR1.stopped', Image_TR1.tStopRefresh)
            # check responses
            if Key_TR1.keys in ['', [], None]:  # No response was made
                Key_TR1.keys = None
            trials.addData('Key_TR1.keys',Key_TR1.keys)
            if Key_TR1.keys != None:  # we had a response
                trials.addData('Key_TR1.rt', Key_TR1.rt)
            trials.addData('Key_TR1.started', Key_TR1.tStartRefresh)
            trials.addData('Key_TR1.stopped', Key_TR1.tStopRefresh)
            
            # ------Prepare to start Routine "TR1_W"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            TR1_WComponents = [Wait_TR1]
            for thisComponent in TR1_WComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TR1_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TR1_W"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TR1_WClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TR1_WClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Wait_TR1* updates
                if Wait_TR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Wait_TR1.frameNStart = frameN  # exact frame index
                    Wait_TR1.tStart = t  # local t and not account for scr refresh
                    Wait_TR1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wait_TR1, 'tStartRefresh')  # time at next scr refresh
                    Wait_TR1.setAutoDraw(True)
                if Wait_TR1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wait_TR1.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Wait_TR1.tStop = t  # not accounting for scr refresh
                        Wait_TR1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Wait_TR1, 'tStopRefresh')  # time at next scr refresh
                        Wait_TR1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TR1_WComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TR1_W"-------
            for thisComponent in TR1_WComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('Wait_TR1.started', Wait_TR1.tStartRefresh)
            trials.addData('Wait_TR1.stopped', Wait_TR1.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
        
        # ------Prepare to start Routine "Instructions_AR1"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        Instructions_AR1Components = [IR1, key_resp_4]
        for thisComponent in Instructions_AR1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instructions_AR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instructions_AR1"-------
        while continueRoutine:
            # get current time
            t = Instructions_AR1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instructions_AR1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *IR1* updates
            if IR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IR1.frameNStart = frameN  # exact frame index
                IR1.tStart = t  # local t and not account for scr refresh
                IR1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IR1, 'tStartRefresh')  # time at next scr refresh
                IR1.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions_AR1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions_AR1"-------
        for thisComponent in Instructions_AR1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_8.addData('IR1.started', IR1.tStartRefresh)
        trials_8.addData('IR1.stopped', IR1.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials_8.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials_8.addData('key_resp_4.rt', key_resp_4.rt)
        trials_8.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        trials_8.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        # the Routine "Instructions_AR1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Actual1.xlsx'),
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "AR1_Image"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            Image_AR1.setImage(Image_Name)
            Key_AR1.keys = []
            Key_AR1.rt = []
            _Key_AR1_allKeys = []
            # keep track of which components have finished
            AR1_ImageComponents = [Image_AR1, Key_AR1]
            for thisComponent in AR1_ImageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AR1_ImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AR1_Image"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AR1_ImageClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AR1_ImageClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Image_AR1* updates
                if Image_AR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Image_AR1.frameNStart = frameN  # exact frame index
                    Image_AR1.tStart = t  # local t and not account for scr refresh
                    Image_AR1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Image_AR1, 'tStartRefresh')  # time at next scr refresh
                    Image_AR1.setAutoDraw(True)
                if Image_AR1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Image_AR1.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Image_AR1.tStop = t  # not accounting for scr refresh
                        Image_AR1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Image_AR1, 'tStopRefresh')  # time at next scr refresh
                        Image_AR1.setAutoDraw(False)
                
                # *Key_AR1* updates
                waitOnFlip = False
                if Key_AR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_AR1.frameNStart = frameN  # exact frame index
                    Key_AR1.tStart = t  # local t and not account for scr refresh
                    Key_AR1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_AR1, 'tStartRefresh')  # time at next scr refresh
                    Key_AR1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_AR1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_AR1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_AR1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_AR1.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_AR1.tStop = t  # not accounting for scr refresh
                        Key_AR1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_AR1, 'tStopRefresh')  # time at next scr refresh
                        Key_AR1.status = FINISHED
                if Key_AR1.status == STARTED and not waitOnFlip:
                    theseKeys = Key_AR1.getKeys(keyList=['space'], waitRelease=False)
                    _Key_AR1_allKeys.extend(theseKeys)
                    if len(_Key_AR1_allKeys):
                        Key_AR1.keys = _Key_AR1_allKeys[-1].name  # just the last key pressed
                        Key_AR1.rt = _Key_AR1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AR1_ImageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AR1_Image"-------
            for thisComponent in AR1_ImageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('Image_AR1.started', Image_AR1.tStartRefresh)
            trials_2.addData('Image_AR1.stopped', Image_AR1.tStopRefresh)
            # check responses
            if Key_AR1.keys in ['', [], None]:  # No response was made
                Key_AR1.keys = None
            trials_2.addData('Key_AR1.keys',Key_AR1.keys)
            if Key_AR1.keys != None:  # we had a response
                trials_2.addData('Key_AR1.rt', Key_AR1.rt)
            trials_2.addData('Key_AR1.started', Key_AR1.tStartRefresh)
            trials_2.addData('Key_AR1.stopped', Key_AR1.tStopRefresh)
            
            # ------Prepare to start Routine "AR1_W"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            AR1_WComponents = [Wait_AR1]
            for thisComponent in AR1_WComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AR1_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AR1_W"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AR1_WClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AR1_WClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Wait_AR1* updates
                if Wait_AR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Wait_AR1.frameNStart = frameN  # exact frame index
                    Wait_AR1.tStart = t  # local t and not account for scr refresh
                    Wait_AR1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wait_AR1, 'tStartRefresh')  # time at next scr refresh
                    Wait_AR1.setAutoDraw(True)
                if Wait_AR1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wait_AR1.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Wait_AR1.tStop = t  # not accounting for scr refresh
                        Wait_AR1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Wait_AR1, 'tStopRefresh')  # time at next scr refresh
                        Wait_AR1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AR1_WComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AR1_W"-------
            for thisComponent in AR1_WComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('Wait_AR1.started', Wait_AR1.tStartRefresh)
            trials_2.addData('Wait_AR1.stopped', Wait_AR1.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_2'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_8'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_9 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_9')
    thisExp.addLoop(trials_9)  # add the loop to the experiment
    thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))
    
    for thisTrial_9 in trials_9:
        currentLoop = trials_9
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
        if thisTrial_9 != None:
            for paramName in thisTrial_9:
                exec('{} = thisTrial_9[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Instructions_TR2"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        Instructions_TR2Components = [ITR2, key_resp_5]
        for thisComponent in Instructions_TR2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instructions_TR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instructions_TR2"-------
        while continueRoutine:
            # get current time
            t = Instructions_TR2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instructions_TR2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITR2* updates
            if ITR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITR2.frameNStart = frameN  # exact frame index
                ITR2.tStart = t  # local t and not account for scr refresh
                ITR2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITR2, 'tStartRefresh')  # time at next scr refresh
                ITR2.setAutoDraw(True)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions_TR2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions_TR2"-------
        for thisComponent in Instructions_TR2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_9.addData('ITR2.started', ITR2.tStartRefresh)
        trials_9.addData('ITR2.stopped', ITR2.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials_9.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials_9.addData('key_resp_5.rt', key_resp_5.rt)
        trials_9.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        trials_9.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        # the Routine "Instructions_TR2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Trial2.xlsx'),
            seed=None, name='trials_3')
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    exec('{} = thisTrial_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "TR2_Image"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            Image_TR2.setImage(Image_Name)
            Key_TR2.keys = []
            Key_TR2.rt = []
            _Key_TR2_allKeys = []
            # keep track of which components have finished
            TR2_ImageComponents = [Image_TR2, Key_TR2]
            for thisComponent in TR2_ImageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TR2_ImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TR2_Image"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TR2_ImageClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TR2_ImageClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Image_TR2* updates
                if Image_TR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Image_TR2.frameNStart = frameN  # exact frame index
                    Image_TR2.tStart = t  # local t and not account for scr refresh
                    Image_TR2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Image_TR2, 'tStartRefresh')  # time at next scr refresh
                    Image_TR2.setAutoDraw(True)
                if Image_TR2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Image_TR2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Image_TR2.tStop = t  # not accounting for scr refresh
                        Image_TR2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Image_TR2, 'tStopRefresh')  # time at next scr refresh
                        Image_TR2.setAutoDraw(False)
                
                # *Key_TR2* updates
                waitOnFlip = False
                if Key_TR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_TR2.frameNStart = frameN  # exact frame index
                    Key_TR2.tStart = t  # local t and not account for scr refresh
                    Key_TR2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_TR2, 'tStartRefresh')  # time at next scr refresh
                    Key_TR2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_TR2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_TR2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_TR2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_TR2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_TR2.tStop = t  # not accounting for scr refresh
                        Key_TR2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_TR2, 'tStopRefresh')  # time at next scr refresh
                        Key_TR2.status = FINISHED
                if Key_TR2.status == STARTED and not waitOnFlip:
                    theseKeys = Key_TR2.getKeys(keyList=['space'], waitRelease=False)
                    _Key_TR2_allKeys.extend(theseKeys)
                    if len(_Key_TR2_allKeys):
                        Key_TR2.keys = _Key_TR2_allKeys[-1].name  # just the last key pressed
                        Key_TR2.rt = _Key_TR2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TR2_ImageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TR2_Image"-------
            for thisComponent in TR2_ImageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_3.addData('Image_TR2.started', Image_TR2.tStartRefresh)
            trials_3.addData('Image_TR2.stopped', Image_TR2.tStopRefresh)
            # check responses
            if Key_TR2.keys in ['', [], None]:  # No response was made
                Key_TR2.keys = None
            trials_3.addData('Key_TR2.keys',Key_TR2.keys)
            if Key_TR2.keys != None:  # we had a response
                trials_3.addData('Key_TR2.rt', Key_TR2.rt)
            trials_3.addData('Key_TR2.started', Key_TR2.tStartRefresh)
            trials_3.addData('Key_TR2.stopped', Key_TR2.tStopRefresh)
            
            # ------Prepare to start Routine "TR2_W"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            TR2_WComponents = [Wait_TR2]
            for thisComponent in TR2_WComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TR2_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TR2_W"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TR2_WClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TR2_WClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Wait_TR2* updates
                if Wait_TR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Wait_TR2.frameNStart = frameN  # exact frame index
                    Wait_TR2.tStart = t  # local t and not account for scr refresh
                    Wait_TR2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wait_TR2, 'tStartRefresh')  # time at next scr refresh
                    Wait_TR2.setAutoDraw(True)
                if Wait_TR2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wait_TR2.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Wait_TR2.tStop = t  # not accounting for scr refresh
                        Wait_TR2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Wait_TR2, 'tStopRefresh')  # time at next scr refresh
                        Wait_TR2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TR2_WComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TR2_W"-------
            for thisComponent in TR2_WComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_3.addData('Wait_TR2.started', Wait_TR2.tStartRefresh)
            trials_3.addData('Wait_TR2.stopped', Wait_TR2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_3'
        
        
        # ------Prepare to start Routine "Instructions_AR2"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # keep track of which components have finished
        Instructions_AR2Components = [IRA2, key_resp_7]
        for thisComponent in Instructions_AR2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instructions_AR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instructions_AR2"-------
        while continueRoutine:
            # get current time
            t = Instructions_AR2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instructions_AR2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *IRA2* updates
            if IRA2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IRA2.frameNStart = frameN  # exact frame index
                IRA2.tStart = t  # local t and not account for scr refresh
                IRA2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IRA2, 'tStartRefresh')  # time at next scr refresh
                IRA2.setAutoDraw(True)
            
            # *key_resp_7* updates
            waitOnFlip = False
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions_AR2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions_AR2"-------
        for thisComponent in Instructions_AR2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_9.addData('IRA2.started', IRA2.tStartRefresh)
        trials_9.addData('IRA2.stopped', IRA2.tStopRefresh)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials_9.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials_9.addData('key_resp_7.rt', key_resp_7.rt)
        trials_9.addData('key_resp_7.started', key_resp_7.tStartRefresh)
        trials_9.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
        # the Routine "Instructions_AR2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Actual2.xlsx'),
            seed=None, name='trials_4')
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        for thisTrial_4 in trials_4:
            currentLoop = trials_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    exec('{} = thisTrial_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "AR2_Image"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            Image_AR2.setImage(Image_Name)
            Key_AR2.keys = []
            Key_AR2.rt = []
            _Key_AR2_allKeys = []
            # keep track of which components have finished
            AR2_ImageComponents = [Image_AR2, Key_AR2]
            for thisComponent in AR2_ImageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AR2_ImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AR2_Image"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AR2_ImageClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AR2_ImageClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Image_AR2* updates
                if Image_AR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Image_AR2.frameNStart = frameN  # exact frame index
                    Image_AR2.tStart = t  # local t and not account for scr refresh
                    Image_AR2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Image_AR2, 'tStartRefresh')  # time at next scr refresh
                    Image_AR2.setAutoDraw(True)
                if Image_AR2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Image_AR2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Image_AR2.tStop = t  # not accounting for scr refresh
                        Image_AR2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Image_AR2, 'tStopRefresh')  # time at next scr refresh
                        Image_AR2.setAutoDraw(False)
                
                # *Key_AR2* updates
                waitOnFlip = False
                if Key_AR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_AR2.frameNStart = frameN  # exact frame index
                    Key_AR2.tStart = t  # local t and not account for scr refresh
                    Key_AR2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_AR2, 'tStartRefresh')  # time at next scr refresh
                    Key_AR2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_AR2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_AR2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_AR2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_AR2.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_AR2.tStop = t  # not accounting for scr refresh
                        Key_AR2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_AR2, 'tStopRefresh')  # time at next scr refresh
                        Key_AR2.status = FINISHED
                if Key_AR2.status == STARTED and not waitOnFlip:
                    theseKeys = Key_AR2.getKeys(keyList=['space'], waitRelease=False)
                    _Key_AR2_allKeys.extend(theseKeys)
                    if len(_Key_AR2_allKeys):
                        Key_AR2.keys = _Key_AR2_allKeys[-1].name  # just the last key pressed
                        Key_AR2.rt = _Key_AR2_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AR2_ImageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AR2_Image"-------
            for thisComponent in AR2_ImageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_4.addData('Image_AR2.started', Image_AR2.tStartRefresh)
            trials_4.addData('Image_AR2.stopped', Image_AR2.tStopRefresh)
            # check responses
            if Key_AR2.keys in ['', [], None]:  # No response was made
                Key_AR2.keys = None
            trials_4.addData('Key_AR2.keys',Key_AR2.keys)
            if Key_AR2.keys != None:  # we had a response
                trials_4.addData('Key_AR2.rt', Key_AR2.rt)
            trials_4.addData('Key_AR2.started', Key_AR2.tStartRefresh)
            trials_4.addData('Key_AR2.stopped', Key_AR2.tStopRefresh)
            
            # ------Prepare to start Routine "AR2_W"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            AR2_WComponents = [Wait_AR2]
            for thisComponent in AR2_WComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AR2_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AR2_W"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AR2_WClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AR2_WClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Wait_AR2* updates
                if Wait_AR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Wait_AR2.frameNStart = frameN  # exact frame index
                    Wait_AR2.tStart = t  # local t and not account for scr refresh
                    Wait_AR2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wait_AR2, 'tStartRefresh')  # time at next scr refresh
                    Wait_AR2.setAutoDraw(True)
                if Wait_AR2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wait_AR2.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Wait_AR2.tStop = t  # not accounting for scr refresh
                        Wait_AR2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Wait_AR2, 'tStopRefresh')  # time at next scr refresh
                        Wait_AR2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AR2_WComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AR2_W"-------
            for thisComponent in AR2_WComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_4.addData('Wait_AR2.started', Wait_AR2.tStartRefresh)
            trials_4.addData('Wait_AR2.stopped', Wait_AR2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_4'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_9'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_10 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_10')
    thisExp.addLoop(trials_10)  # add the loop to the experiment
    thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            exec('{} = thisTrial_10[paramName]'.format(paramName))
    
    for thisTrial_10 in trials_10:
        currentLoop = trials_10
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
        if thisTrial_10 != None:
            for paramName in thisTrial_10:
                exec('{} = thisTrial_10[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Instructions_TR3"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        Instructions_TR3Components = [ITR3, key_resp]
        for thisComponent in Instructions_TR3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instructions_TR3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instructions_TR3"-------
        while continueRoutine:
            # get current time
            t = Instructions_TR3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instructions_TR3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITR3* updates
            if ITR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITR3.frameNStart = frameN  # exact frame index
                ITR3.tStart = t  # local t and not account for scr refresh
                ITR3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITR3, 'tStartRefresh')  # time at next scr refresh
                ITR3.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions_TR3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions_TR3"-------
        for thisComponent in Instructions_TR3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_10.addData('ITR3.started', ITR3.tStartRefresh)
        trials_10.addData('ITR3.stopped', ITR3.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials_10.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials_10.addData('key_resp.rt', key_resp.rt)
        trials_10.addData('key_resp.started', key_resp.tStartRefresh)
        trials_10.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "Instructions_TR3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_5 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Trial3.xlsx'),
            seed=None, name='trials_5')
        thisExp.addLoop(trials_5)  # add the loop to the experiment
        thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        for thisTrial_5 in trials_5:
            currentLoop = trials_5
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
            if thisTrial_5 != None:
                for paramName in thisTrial_5:
                    exec('{} = thisTrial_5[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "TR3_Image"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            Image_TR3.setImage(Image_Name)
            Key_TR3.keys = []
            Key_TR3.rt = []
            _Key_TR3_allKeys = []
            # keep track of which components have finished
            TR3_ImageComponents = [Image_TR3, Key_TR3]
            for thisComponent in TR3_ImageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TR3_ImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TR3_Image"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TR3_ImageClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TR3_ImageClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Image_TR3* updates
                if Image_TR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Image_TR3.frameNStart = frameN  # exact frame index
                    Image_TR3.tStart = t  # local t and not account for scr refresh
                    Image_TR3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Image_TR3, 'tStartRefresh')  # time at next scr refresh
                    Image_TR3.setAutoDraw(True)
                if Image_TR3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Image_TR3.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Image_TR3.tStop = t  # not accounting for scr refresh
                        Image_TR3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Image_TR3, 'tStopRefresh')  # time at next scr refresh
                        Image_TR3.setAutoDraw(False)
                
                # *Key_TR3* updates
                waitOnFlip = False
                if Key_TR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_TR3.frameNStart = frameN  # exact frame index
                    Key_TR3.tStart = t  # local t and not account for scr refresh
                    Key_TR3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_TR3, 'tStartRefresh')  # time at next scr refresh
                    Key_TR3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_TR3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_TR3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_TR3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_TR3.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_TR3.tStop = t  # not accounting for scr refresh
                        Key_TR3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_TR3, 'tStopRefresh')  # time at next scr refresh
                        Key_TR3.status = FINISHED
                if Key_TR3.status == STARTED and not waitOnFlip:
                    theseKeys = Key_TR3.getKeys(keyList=['space'], waitRelease=False)
                    _Key_TR3_allKeys.extend(theseKeys)
                    if len(_Key_TR3_allKeys):
                        Key_TR3.keys = _Key_TR3_allKeys[-1].name  # just the last key pressed
                        Key_TR3.rt = _Key_TR3_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TR3_ImageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TR3_Image"-------
            for thisComponent in TR3_ImageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_5.addData('Image_TR3.started', Image_TR3.tStartRefresh)
            trials_5.addData('Image_TR3.stopped', Image_TR3.tStopRefresh)
            # check responses
            if Key_TR3.keys in ['', [], None]:  # No response was made
                Key_TR3.keys = None
            trials_5.addData('Key_TR3.keys',Key_TR3.keys)
            if Key_TR3.keys != None:  # we had a response
                trials_5.addData('Key_TR3.rt', Key_TR3.rt)
            trials_5.addData('Key_TR3.started', Key_TR3.tStartRefresh)
            trials_5.addData('Key_TR3.stopped', Key_TR3.tStopRefresh)
            
            # ------Prepare to start Routine "TR3_W"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            TR3_WComponents = [Wait_TR3]
            for thisComponent in TR3_WComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TR3_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TR3_W"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TR3_WClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TR3_WClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Wait_TR3* updates
                if Wait_TR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Wait_TR3.frameNStart = frameN  # exact frame index
                    Wait_TR3.tStart = t  # local t and not account for scr refresh
                    Wait_TR3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wait_TR3, 'tStartRefresh')  # time at next scr refresh
                    Wait_TR3.setAutoDraw(True)
                if Wait_TR3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wait_TR3.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Wait_TR3.tStop = t  # not accounting for scr refresh
                        Wait_TR3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Wait_TR3, 'tStopRefresh')  # time at next scr refresh
                        Wait_TR3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TR3_WComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TR3_W"-------
            for thisComponent in TR3_WComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_5.addData('Wait_TR3.started', Wait_TR3.tStartRefresh)
            trials_5.addData('Wait_TR3.stopped', Wait_TR3.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_5'
        
        
        # ------Prepare to start Routine "Instructions_AR3"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # keep track of which components have finished
        Instructions_AR3Components = [IAR3, key_resp_2]
        for thisComponent in Instructions_AR3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Instructions_AR3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Instructions_AR3"-------
        while continueRoutine:
            # get current time
            t = Instructions_AR3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Instructions_AR3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *IAR3* updates
            if IAR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IAR3.frameNStart = frameN  # exact frame index
                IAR3.tStart = t  # local t and not account for scr refresh
                IAR3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IAR3, 'tStartRefresh')  # time at next scr refresh
                IAR3.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions_AR3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions_AR3"-------
        for thisComponent in Instructions_AR3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_10.addData('IAR3.started', IAR3.tStartRefresh)
        trials_10.addData('IAR3.stopped', IAR3.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials_10.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials_10.addData('key_resp_2.rt', key_resp_2.rt)
        trials_10.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_10.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "Instructions_AR3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_6 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Actual3.xlsx'),
            seed=None, name='trials_6')
        thisExp.addLoop(trials_6)  # add the loop to the experiment
        thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisTrial_6 != None:
            for paramName in thisTrial_6:
                exec('{} = thisTrial_6[paramName]'.format(paramName))
        
        for thisTrial_6 in trials_6:
            currentLoop = trials_6
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
            if thisTrial_6 != None:
                for paramName in thisTrial_6:
                    exec('{} = thisTrial_6[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "AR3_Image"-------
            continueRoutine = True
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            Image_AR3.setImage(Image_Name)
            Key_AR3.keys = []
            Key_AR3.rt = []
            _Key_AR3_allKeys = []
            # keep track of which components have finished
            AR3_ImageComponents = [Image_AR3, Key_AR3]
            for thisComponent in AR3_ImageComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AR3_ImageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AR3_Image"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AR3_ImageClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AR3_ImageClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Image_AR3* updates
                if Image_AR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Image_AR3.frameNStart = frameN  # exact frame index
                    Image_AR3.tStart = t  # local t and not account for scr refresh
                    Image_AR3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Image_AR3, 'tStartRefresh')  # time at next scr refresh
                    Image_AR3.setAutoDraw(True)
                if Image_AR3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Image_AR3.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Image_AR3.tStop = t  # not accounting for scr refresh
                        Image_AR3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Image_AR3, 'tStopRefresh')  # time at next scr refresh
                        Image_AR3.setAutoDraw(False)
                
                # *Key_AR3* updates
                waitOnFlip = False
                if Key_AR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Key_AR3.frameNStart = frameN  # exact frame index
                    Key_AR3.tStart = t  # local t and not account for scr refresh
                    Key_AR3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Key_AR3, 'tStartRefresh')  # time at next scr refresh
                    Key_AR3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Key_AR3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Key_AR3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Key_AR3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Key_AR3.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Key_AR3.tStop = t  # not accounting for scr refresh
                        Key_AR3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Key_AR3, 'tStopRefresh')  # time at next scr refresh
                        Key_AR3.status = FINISHED
                if Key_AR3.status == STARTED and not waitOnFlip:
                    theseKeys = Key_AR3.getKeys(keyList=['space'], waitRelease=False)
                    _Key_AR3_allKeys.extend(theseKeys)
                    if len(_Key_AR3_allKeys):
                        Key_AR3.keys = _Key_AR3_allKeys[-1].name  # just the last key pressed
                        Key_AR3.rt = _Key_AR3_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AR3_ImageComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AR3_Image"-------
            for thisComponent in AR3_ImageComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_6.addData('Image_AR3.started', Image_AR3.tStartRefresh)
            trials_6.addData('Image_AR3.stopped', Image_AR3.tStopRefresh)
            # check responses
            if Key_AR3.keys in ['', [], None]:  # No response was made
                Key_AR3.keys = None
            trials_6.addData('Key_AR3.keys',Key_AR3.keys)
            if Key_AR3.keys != None:  # we had a response
                trials_6.addData('Key_AR3.rt', Key_AR3.rt)
            trials_6.addData('Key_AR3.started', Key_AR3.tStartRefresh)
            trials_6.addData('Key_AR3.stopped', Key_AR3.tStopRefresh)
            
            # ------Prepare to start Routine "AR3_W"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            AR3_WComponents = [Wait_AR3]
            for thisComponent in AR3_WComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AR3_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AR3_W"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AR3_WClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AR3_WClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Wait_AR3* updates
                if Wait_AR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Wait_AR3.frameNStart = frameN  # exact frame index
                    Wait_AR3.tStart = t  # local t and not account for scr refresh
                    Wait_AR3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Wait_AR3, 'tStartRefresh')  # time at next scr refresh
                    Wait_AR3.setAutoDraw(True)
                if Wait_AR3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Wait_AR3.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Wait_AR3.tStop = t  # not accounting for scr refresh
                        Wait_AR3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Wait_AR3, 'tStopRefresh')  # time at next scr refresh
                        Wait_AR3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AR3_WComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AR3_W"-------
            for thisComponent in AR3_WComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_6.addData('Wait_AR3.started', Wait_AR3.tStartRefresh)
            trials_6.addData('Wait_AR3.stopped', Wait_AR3.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_6'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_10'
    
    thisExp.nextEntry()
    
# staircase completed


# ------Prepare to start Routine "End_Instructions"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
End_InstructionsComponents = [EI]
for thisComponent in End_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End_Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = End_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EI* updates
    if EI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EI.frameNStart = frameN  # exact frame index
        EI.tStart = t  # local t and not account for scr refresh
        EI.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EI, 'tStartRefresh')  # time at next scr refresh
        EI.setAutoDraw(True)
    if EI.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EI.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            EI.tStop = t  # not accounting for scr refresh
            EI.frameNStop = frameN  # exact frame index
            win.timeOnFlip(EI, 'tStopRefresh')  # time at next scr refresh
            EI.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End_Instructions"-------
for thisComponent in End_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EI.started', EI.tStartRefresh)
thisExp.addData('EI.stopped', EI.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
