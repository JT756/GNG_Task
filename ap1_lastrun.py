#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.1),
    on April 18, 2020, at 18:22
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
expName = 'ap1'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Josef Haydn\\Desktop\\SemesterVI\\AP\\ap1_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "Type_G"
Type_GClock = core.Clock()
Input_Group = keyboard.Keyboard()
Fed_Text = visual.TextStim(win=win, name='Fed_Text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Trial_Instructions"
Trial_InstructionsClock = core.Clock()
TR_Instructions = visual.TextStim(win=win, name='TR_Instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "TR"
TRClock = core.Clock()
TR_Key = keyboard.Keyboard()
TR_Image = visual.ImageStim(
    win=win,
    name='TR_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "TR_W"
TR_WClock = core.Clock()
TR_Wait = visual.ImageStim(
    win=win,
    name='TR_Wait', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Actual_Instructions"
Actual_InstructionsClock = core.Clock()
AR_Instructions = visual.TextStim(win=win, name='AR_Instructions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "AR"
ARClock = core.Clock()
AR_Image = visual.ImageStim(
    win=win,
    name='AR_Image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.25, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
AR_Key = keyboard.Keyboard()

# Initialize components for Routine "AR_W"
AR_WClock = core.Clock()
AR_Wait = visual.ImageStim(
    win=win,
    name='AR_Wait', 
    image='plus.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
    text='The Experiment has ended\nPress Space Bar to Exit',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EndKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Type_G"-------
continueRoutine = True
# update component parameters for each repeat
Input_Group.keys = []
Input_Group.rt = []
_Input_Group_allKeys = []
screen_text=""
inst="Choose your group it is either a,b or c"
event.clearEvents('keyboard')
# keep track of which components have finished
Type_GComponents = [Input_Group, Fed_Text]
for thisComponent in Type_GComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Type_GClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Type_G"-------
while continueRoutine:
    # get current time
    t = Type_GClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Type_GClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Input_Group* updates
    waitOnFlip = False
    if Input_Group.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Input_Group.frameNStart = frameN  # exact frame index
        Input_Group.tStart = t  # local t and not account for scr refresh
        Input_Group.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Input_Group, 'tStartRefresh')  # time at next scr refresh
        Input_Group.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Input_Group.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Input_Group.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Input_Group.status == STARTED and not waitOnFlip:
        theseKeys = Input_Group.getKeys(keyList=['A', 'a', 'B', 'b', 'C', 'c', 'return', 'backspace', 'space'], waitRelease=False)
        _Input_Group_allKeys.extend(theseKeys)
        if len(_Input_Group_allKeys):
            Input_Group.keys = [key.name for key in _Input_Group_allKeys]  # storing all keys
            Input_Group.rt = [key.rt for key in _Input_Group_allKeys]
    
    # *Fed_Text* updates
    if Fed_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fed_Text.frameNStart = frameN  # exact frame index
        Fed_Text.tStart = t  # local t and not account for scr refresh
        Fed_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fed_Text, 'tStartRefresh')  # time at next scr refresh
        Fed_Text.setAutoDraw(True)
    if Fed_Text.status == STARTED:  # only update if drawing
        Fed_Text.setText(inst+"\n"+screen_text+"\n"+"Press spacebar to continue", log=False)
    
    keys = event.getKeys()
    print(keys)
    if("backspace" in keys):
        if(len(screen_text)>0):
            screen_text=screen_text[:-1]
    elif("space" in keys):
        continueRoutine=False
    else:
        if(len(keys)>0):
            if(keys[-1]=="A" or keys[-1]=="B" or keys[-1]=="C" or keys[-1]=="a" or keys[-1]=="b" or keys[-1]=="c"):
                screen_text=keys[-1]
            
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Type_GComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Type_G"-------
for thisComponent in Type_GComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Input_Group.keys in ['', [], None]:  # No response was made
    Input_Group.keys = None
thisExp.addData('Input_Group.keys',Input_Group.keys)
if Input_Group.keys != None:  # we had a response
    thisExp.addData('Input_Group.rt', Input_Group.rt)
thisExp.addData('Input_Group.started', Input_Group.tStartRefresh)
thisExp.addData('Input_Group.stopped', Input_Group.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Fed_Text.started', Fed_Text.tStartRefresh)
thisExp.addData('Fed_Text.stopped', Fed_Text.tStopRefresh)
if(len(screen_text)!=1):
    screen_text="A"
else:
    if(not(screen_text=="A" or screen_text=="B" or screen_text=="C" or screen_text=="a" or screen_text=="b" or screen_text=="c")):
        screen_text="A"
        
        
  
# the Routine "Type_G" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("Group"+screen_text+".xlsx"),
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
    
    # ------Prepare to start Routine "Trial_Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    TR_Instructions.setText(TInstructions)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    Trial_InstructionsComponents = [TR_Instructions, key_resp]
    for thisComponent in Trial_InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_Instructions"-------
    while continueRoutine:
        # get current time
        t = Trial_InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TR_Instructions* updates
        if TR_Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_Instructions.frameNStart = frameN  # exact frame index
            TR_Instructions.tStart = t  # local t and not account for scr refresh
            TR_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_Instructions, 'tStartRefresh')  # time at next scr refresh
            TR_Instructions.setAutoDraw(True)
        
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
        for thisComponent in Trial_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_Instructions"-------
    for thisComponent in Trial_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('TR_Instructions.started', TR_Instructions.tStartRefresh)
    trials.addData('TR_Instructions.stopped', TR_Instructions.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "Trial_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Trial_Name),
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
        
        # ------Prepare to start Routine "TR"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        TR_Key.keys = []
        TR_Key.rt = []
        _TR_Key_allKeys = []
        TR_Image.setImage(Image_Name)
        # keep track of which components have finished
        TRComponents = [TR_Key, TR_Image]
        for thisComponent in TRComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TR"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TRClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TRClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TR_Key* updates
            waitOnFlip = False
            if TR_Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TR_Key.frameNStart = frameN  # exact frame index
                TR_Key.tStart = t  # local t and not account for scr refresh
                TR_Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TR_Key, 'tStartRefresh')  # time at next scr refresh
                TR_Key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TR_Key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TR_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TR_Key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TR_Key.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    TR_Key.tStop = t  # not accounting for scr refresh
                    TR_Key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TR_Key, 'tStopRefresh')  # time at next scr refresh
                    TR_Key.status = FINISHED
            if TR_Key.status == STARTED and not waitOnFlip:
                theseKeys = TR_Key.getKeys(keyList=['space'], waitRelease=False)
                _TR_Key_allKeys.extend(theseKeys)
                if len(_TR_Key_allKeys):
                    TR_Key.keys = _TR_Key_allKeys[-1].name  # just the last key pressed
                    TR_Key.rt = _TR_Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *TR_Image* updates
            if TR_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TR_Image.frameNStart = frameN  # exact frame index
                TR_Image.tStart = t  # local t and not account for scr refresh
                TR_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TR_Image, 'tStartRefresh')  # time at next scr refresh
                TR_Image.setAutoDraw(True)
            if TR_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TR_Image.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    TR_Image.tStop = t  # not accounting for scr refresh
                    TR_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TR_Image, 'tStopRefresh')  # time at next scr refresh
                    TR_Image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TRComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TR"-------
        for thisComponent in TRComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if TR_Key.keys in ['', [], None]:  # No response was made
            TR_Key.keys = None
        trials_3.addData('TR_Key.keys',TR_Key.keys)
        if TR_Key.keys != None:  # we had a response
            trials_3.addData('TR_Key.rt', TR_Key.rt)
        trials_3.addData('TR_Key.started', TR_Key.tStartRefresh)
        trials_3.addData('TR_Key.stopped', TR_Key.tStopRefresh)
        trials_3.addData('TR_Image.started', TR_Image.tStartRefresh)
        trials_3.addData('TR_Image.stopped', TR_Image.tStopRefresh)
        
        # ------Prepare to start Routine "TR_W"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        TR_WComponents = [TR_Wait]
        for thisComponent in TR_WComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TR_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TR_W"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TR_WClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TR_WClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TR_Wait* updates
            if TR_Wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TR_Wait.frameNStart = frameN  # exact frame index
                TR_Wait.tStart = t  # local t and not account for scr refresh
                TR_Wait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TR_Wait, 'tStartRefresh')  # time at next scr refresh
                TR_Wait.setAutoDraw(True)
            if TR_Wait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TR_Wait.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    TR_Wait.tStop = t  # not accounting for scr refresh
                    TR_Wait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TR_Wait, 'tStopRefresh')  # time at next scr refresh
                    TR_Wait.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TR_WComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TR_W"-------
        for thisComponent in TR_WComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_3.addData('TR_Wait.started', TR_Wait.tStartRefresh)
        trials_3.addData('TR_Wait.stopped', TR_Wait.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_3'
    
    
    # ------Prepare to start Routine "Actual_Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    AR_Instructions.setText(AInstructions
)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Actual_InstructionsComponents = [AR_Instructions, key_resp_2]
    for thisComponent in Actual_InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Actual_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Actual_Instructions"-------
    while continueRoutine:
        # get current time
        t = Actual_InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Actual_InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AR_Instructions* updates
        if AR_Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AR_Instructions.frameNStart = frameN  # exact frame index
            AR_Instructions.tStart = t  # local t and not account for scr refresh
            AR_Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AR_Instructions, 'tStartRefresh')  # time at next scr refresh
            AR_Instructions.setAutoDraw(True)
        
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
        for thisComponent in Actual_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Actual_Instructions"-------
    for thisComponent in Actual_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('AR_Instructions.started', AR_Instructions.tStartRefresh)
    trials.addData('AR_Instructions.stopped', AR_Instructions.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Actual_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(Actual_Name),
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
        
        # ------Prepare to start Routine "AR"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        AR_Image.setImage(Image_Name)
        AR_Key.keys = []
        AR_Key.rt = []
        _AR_Key_allKeys = []
        # keep track of which components have finished
        ARComponents = [AR_Image, AR_Key]
        for thisComponent in ARComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ARClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AR"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ARClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ARClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AR_Image* updates
            if AR_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AR_Image.frameNStart = frameN  # exact frame index
                AR_Image.tStart = t  # local t and not account for scr refresh
                AR_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AR_Image, 'tStartRefresh')  # time at next scr refresh
                AR_Image.setAutoDraw(True)
            if AR_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AR_Image.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    AR_Image.tStop = t  # not accounting for scr refresh
                    AR_Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AR_Image, 'tStopRefresh')  # time at next scr refresh
                    AR_Image.setAutoDraw(False)
            
            # *AR_Key* updates
            waitOnFlip = False
            if AR_Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AR_Key.frameNStart = frameN  # exact frame index
                AR_Key.tStart = t  # local t and not account for scr refresh
                AR_Key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AR_Key, 'tStartRefresh')  # time at next scr refresh
                AR_Key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(AR_Key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(AR_Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if AR_Key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AR_Key.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    AR_Key.tStop = t  # not accounting for scr refresh
                    AR_Key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AR_Key, 'tStopRefresh')  # time at next scr refresh
                    AR_Key.status = FINISHED
            if AR_Key.status == STARTED and not waitOnFlip:
                theseKeys = AR_Key.getKeys(keyList=['space'], waitRelease=False)
                _AR_Key_allKeys.extend(theseKeys)
                if len(_AR_Key_allKeys):
                    AR_Key.keys = _AR_Key_allKeys[-1].name  # just the last key pressed
                    AR_Key.rt = _AR_Key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ARComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AR"-------
        for thisComponent in ARComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('AR_Image.started', AR_Image.tStartRefresh)
        trials_2.addData('AR_Image.stopped', AR_Image.tStopRefresh)
        # check responses
        if AR_Key.keys in ['', [], None]:  # No response was made
            AR_Key.keys = None
        trials_2.addData('AR_Key.keys',AR_Key.keys)
        if AR_Key.keys != None:  # we had a response
            trials_2.addData('AR_Key.rt', AR_Key.rt)
        trials_2.addData('AR_Key.started', AR_Key.tStartRefresh)
        trials_2.addData('AR_Key.stopped', AR_Key.tStopRefresh)
        
        # ------Prepare to start Routine "AR_W"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        AR_WComponents = [AR_Wait]
        for thisComponent in AR_WComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AR_WClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AR_W"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AR_WClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AR_WClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AR_Wait* updates
            if AR_Wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AR_Wait.frameNStart = frameN  # exact frame index
                AR_Wait.tStart = t  # local t and not account for scr refresh
                AR_Wait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AR_Wait, 'tStartRefresh')  # time at next scr refresh
                AR_Wait.setAutoDraw(True)
            if AR_Wait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > AR_Wait.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    AR_Wait.tStop = t  # not accounting for scr refresh
                    AR_Wait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AR_Wait, 'tStopRefresh')  # time at next scr refresh
                    AR_Wait.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AR_WComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AR_W"-------
        for thisComponent in AR_WComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('AR_Wait.started', AR_Wait.tStartRefresh)
        trials_2.addData('AR_Wait.stopped', AR_Wait.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
EndKey.keys = []
EndKey.rt = []
_EndKey_allKeys = []
# keep track of which components have finished
EndComponents = [EndText, EndKey]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndText* updates
    if EndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndText.frameNStart = frameN  # exact frame index
        EndText.tStart = t  # local t and not account for scr refresh
        EndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndText, 'tStartRefresh')  # time at next scr refresh
        EndText.setAutoDraw(True)
    
    # *EndKey* updates
    waitOnFlip = False
    if EndKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndKey.frameNStart = frameN  # exact frame index
        EndKey.tStart = t  # local t and not account for scr refresh
        EndKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndKey, 'tStartRefresh')  # time at next scr refresh
        EndKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EndKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EndKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EndKey.status == STARTED and not waitOnFlip:
        theseKeys = EndKey.getKeys(keyList=['space'], waitRelease=False)
        _EndKey_allKeys.extend(theseKeys)
        if len(_EndKey_allKeys):
            EndKey.keys = _EndKey_allKeys[-1].name  # just the last key pressed
            EndKey.rt = _EndKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndText.started', EndText.tStartRefresh)
thisExp.addData('EndText.stopped', EndText.tStopRefresh)
# check responses
if EndKey.keys in ['', [], None]:  # No response was made
    EndKey.keys = None
thisExp.addData('EndKey.keys',EndKey.keys)
if EndKey.keys != None:  # we had a response
    thisExp.addData('EndKey.rt', EndKey.rt)
thisExp.addData('EndKey.started', EndKey.tStartRefresh)
thisExp.addData('EndKey.stopped', EndKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
