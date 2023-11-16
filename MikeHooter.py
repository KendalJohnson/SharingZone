#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on November 16, 2023, at 20:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'sounddevice'
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'MikeHooter'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\kenda\\OneDrive - University of Canterbury\\Documents\\PhD\\MMCB\\Stimuli Applications\\PsychoPy\\MikeHooter\\MikeHooter.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='Black', fillColor='Black',
    opacity=None, depth=0.0, interpolate=True)
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome\n\nYou are about to listen to an audio story\n\nPress SPACE bar to begin',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
keyWelcome = keyboard.Keyboard()

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
polyBlank500 = visual.Rect(
    win=win, name='polyBlank500',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='Black', fillColor='Black',
    opacity=None, depth=0.0, interpolate=True)
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "WordStory"
WordStoryClock = core.Clock()
textWordStory = visual.TextStim(win=win, name='textWordStory',
    text='There are two kinds of bears - smart bears and foolish bears.\nFolks in Mississippi used to say Mississippi bears were the smartest in the whole U.S.A.\nThat\'s what Mike Hooter, the great Bear-Hunter and Preacher of the Magnolia State, used to say when he was alive, and he sure knew all anybody ever knew about bears. \nFact is, he was the greatest bear hunter ever was in Mississippi.\nSome folks called him Mike Shouter, for he was forever roaring louder than ten waterfalls when he was preaching sermons or when he was arguing about the smartness of the Mississippi bears. Whenever anyone tried to argue about bears, Mike would tell them about Ike Hamberlin and his\ntime with the smart bears.\nOne time Mike Hooter and Ike Hamberlin were talking about bears and they decided to go out hunting together. But Ike was monstrously jealous of Mike, so he thought he\'d get a head start and go out alone before him. He set out in the early morning, just he and his dogs.\nWell, Mike caught wind of this, so he got up early himself that morning, took his two-shooter, and went off looking for Ike. But Mike didn\'t take his dogs.\nAfter a time he spotted Ike and just followed him for a distance. Ike had gone pretty deep into the woods when his dogs started growling and barking. \nThey heard another kind of deep noise and their hairs stood straight up their backs like tomcats in a fight.\n"Run go get \'em," Ike shouted to the dogs. But the dogs wouldn\'t. \nThey just ran around Ike yapping and crying, as if they were scared to death.\n"Sic \'em! Sic \'em!" Ike kept on hollering to the dogs, but they minded him like birds in flight.\nMike was watching all the time, wondering what was going to happen next.\nIke was mad as a hornet, but he was trying to keep his temper, he just kept coaxing the dogs to stir up the bear that he knew was in there somewhere.\nThose dogs just weren\'t acting natural. \nMike was watching, and he even felt kind of sorry for Ike.\nAfter all, there was the man out hunting for bear. \nAnd there was a bear just waiting to be got. \nAnd there were the bear-hunting dogs who were supposed to be stirring up the bear. \nBut instead of doing their duty as good hunting dogs should, they just kept whining and standing there with their tails between their legs.\nIt sure wasn\'t right. \nYou\'d think a curse had been cast on them.\nIke was fit to be tied. \n"I\'ll teach you good-for-nothin\' critters to tend to your business as you ought to," he shouted. \nThen he took his single barrel, leaned it against a tree, and ran to the creek.\nThere he began picking up stones and throwing them at his dogs. \nThose dogs started howling to the heavens. \nJust then Ike ran out of stones so he turned around to gather some more. As his back was turned, and his dogs were still howling up a storm, there was a sudden crackling and breaking soundcoming from the woods. \nMike was watching and out came the biggest and most powerful bear he\'d\never seen. \nIke heard the sound too and figured he must have thrown enough rocks for his bewitched dogs to get on with their business.\nSo Ike started setting down the stones he wouldn\'t be needing. \nBut meanwhile this big mean bear had walked clear over to the tree where Ike had sat down his gun. \nThe bear picked it up with his front paws and looked at it. \nThen he blew into it with some powerful breaths.\nIke turned around just in time to see the bear with his paws on the gun. \nIke froze in his boots. \nHis hair stood up on his head, his mouth was wide open, and his eyes were ready to jump out of his head. \nAnd Mike, watching, was just as numb.\nThe bear looked at Ike with a bear grin, then he put the rifle back against the tree, turned around, and walked off.\nIke rushed up to the gun, grabbed it, aimed straight at the bear, and snapped the lock!...\nBut not a sound came from the trusty old piece. \nThough there was a sound of laughing afar off. \nJust then Ike looked down at his feet and sure enough he was standing in a pile of gunpowder.\nMike who had been laughing so hard decided it was time to give himself up. \nSo he went out from his hiding place and told his friend what that smart Mississippi bear had done to his gun. \nOld Ike didn\'t think it was quite so funny. \nBut after years of hearing Mike tell the story, Ike would laugh just\nas hard as any of the other listeners. \nAnd he\'d laugh particularly hard when Mike would tell the\npart about when the bear was walking off, and how he stopped to look back at Ike standing there with that good for nothing gun, with his good for nothing dogs, and how the bear then put one of\nhis front paws up to his face, and thumbed his nose at poor ole Ike.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='Black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Blank500"
Blank500Clock = core.Clock()
polyBlank500 = visual.Rect(
    win=win, name='polyBlank500',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='Black', fillColor='Black',
    opacity=None, depth=0.0, interpolate=True)
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
polygonEndScreen = visual.Rect(
    win=win, name='polygonEndScreen',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='Black', fillColor='Black',
    opacity=None, depth=0.0, interpolate=True)
textEndScreen = visual.TextStim(win=win, name='textEndScreen',
    text='Thank you for listening\nPlease see the researcher now\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
_keyWelcome_allKeys = []
# keep track of which components have finished
WelcomeScreenComponents = [polygon, textWelcome, keyWelcome]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['space'], waitRelease=False)
        _keyWelcome_allKeys.extend(theseKeys)
        if len(_keyWelcome_allKeys):
            keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
            keyWelcome.rt = _keyWelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.addData('keyWelcome.started', keyWelcome.tStartRefresh)
thisExp.addData('keyWelcome.stopped', keyWelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [polyBlank500, textBlank500]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polyBlank500* updates
    if polyBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polyBlank500.frameNStart = frameN  # exact frame index
        polyBlank500.tStart = t  # local t and not account for scr refresh
        polyBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polyBlank500, 'tStartRefresh')  # time at next scr refresh
        polyBlank500.setAutoDraw(True)
    if polyBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polyBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            polyBlank500.tStop = t  # not accounting for scr refresh
            polyBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polyBlank500, 'tStopRefresh')  # time at next scr refresh
            polyBlank500.setAutoDraw(False)
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polyBlank500.started', polyBlank500.tStartRefresh)
thisExp.addData('polyBlank500.stopped', polyBlank500.tStopRefresh)
thisExp.addData('textBlank500.started', textBlank500.tStartRefresh)
thisExp.addData('textBlank500.stopped', textBlank500.tStopRefresh)

# ------Prepare to start Routine "WordStory"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
WordStoryComponents = [textWordStory]
for thisComponent in WordStoryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WordStoryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WordStory"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WordStoryClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WordStoryClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWordStory* updates
    if textWordStory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWordStory.frameNStart = frameN  # exact frame index
        textWordStory.tStart = t  # local t and not account for scr refresh
        textWordStory.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWordStory, 'tStartRefresh')  # time at next scr refresh
        textWordStory.setAutoDraw(True)
    if textWordStory.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textWordStory.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            textWordStory.tStop = t  # not accounting for scr refresh
            textWordStory.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textWordStory, 'tStopRefresh')  # time at next scr refresh
            textWordStory.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WordStoryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WordStory"-------
for thisComponent in WordStoryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWordStory.started', textWordStory.tStartRefresh)
thisExp.addData('textWordStory.stopped', textWordStory.tStopRefresh)

# ------Prepare to start Routine "Blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
Blank500Components = [polyBlank500, textBlank500]
for thisComponent in Blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polyBlank500* updates
    if polyBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polyBlank500.frameNStart = frameN  # exact frame index
        polyBlank500.tStart = t  # local t and not account for scr refresh
        polyBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polyBlank500, 'tStartRefresh')  # time at next scr refresh
        polyBlank500.setAutoDraw(True)
    if polyBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polyBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            polyBlank500.tStop = t  # not accounting for scr refresh
            polyBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polyBlank500, 'tStopRefresh')  # time at next scr refresh
            polyBlank500.setAutoDraw(False)
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank500"-------
for thisComponent in Blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polyBlank500.started', polyBlank500.tStartRefresh)
thisExp.addData('polyBlank500.stopped', polyBlank500.tStopRefresh)
thisExp.addData('textBlank500.started', textBlank500.tStartRefresh)
thisExp.addData('textBlank500.stopped', textBlank500.tStopRefresh)

# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [polygonEndScreen, textEndScreen]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygonEndScreen* updates
    if polygonEndScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygonEndScreen.frameNStart = frameN  # exact frame index
        polygonEndScreen.tStart = t  # local t and not account for scr refresh
        polygonEndScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygonEndScreen, 'tStartRefresh')  # time at next scr refresh
        polygonEndScreen.setAutoDraw(True)
    if polygonEndScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygonEndScreen.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            polygonEndScreen.tStop = t  # not accounting for scr refresh
            polygonEndScreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygonEndScreen, 'tStopRefresh')  # time at next scr refresh
            polygonEndScreen.setAutoDraw(False)
    
    # *textEndScreen* updates
    if textEndScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndScreen.frameNStart = frameN  # exact frame index
        textEndScreen.tStart = t  # local t and not account for scr refresh
        textEndScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndScreen, 'tStartRefresh')  # time at next scr refresh
        textEndScreen.setAutoDraw(True)
    if textEndScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndScreen.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            textEndScreen.tStop = t  # not accounting for scr refresh
            textEndScreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEndScreen, 'tStopRefresh')  # time at next scr refresh
            textEndScreen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygonEndScreen.started', polygonEndScreen.tStartRefresh)
thisExp.addData('polygonEndScreen.stopped', polygonEndScreen.tStopRefresh)
thisExp.addData('textEndScreen.started', textEndScreen.tStartRefresh)
thisExp.addData('textEndScreen.stopped', textEndScreen.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
