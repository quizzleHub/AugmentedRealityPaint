# **AugmentedRealityPaint**
 Drawing by gesture control, respectively an object <br /> 

---
## *Description*
AugmentedRealityPaint is a tool that offers the user the possibility to draw on the screen via object recognition and object tracking. To do this, simply hold an object up to the camera (preferably one color and round) and briefly calibrate it, and you can start drawing by pressing the space bar.

**Why all this?** <br /> 
It should not only be a small alternative to the classic pen and paper, but also animate us to move more in everyday life. Unfortunately, we sit too often and too long, so the focus is on gesture-controlled drawing. And children can draw playfully and increase their own creativity. 


---
## *Working environment* (Requirement)
- Python                            3.8.10
- numpy                             1.21.4
- opencv_python                     4.5.4.58
- Pillow                            8.4.0
- PyQt5                             5.15.4
- scipy                             1.7.2
- pyinstaller                       4.7  (Only for creating **executable File**)
- Webcam
---
## *Created executable file*
- **pyinstaller --onefile --windowed Start.spec** <br /> 
  **Important** : The executable File should be copied/moved to folder "executable _File". <br /> The Reason is the necessary folder structure like this: <br />

  > executable_File/Start <br /> 
  > icons_mac/\*.PNG <br /> 
  > icons_win/\*.PNG <br /> 
---
## *Installing pip* (package manager)
- Windows:
  **python3 -m pip install -r path/to/requirements.txt**
- Unix/macOS: 
  **py -m pip install -r path/to/requirements.txt**
- Source: (Virtuelle environment)
  https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
  
create requirements.txt: pipreqs /path/to/your/project/
install requirements: install pip install -r requirements.txt


## *Structure and Functional description*

- Screenshot vom UML ? 

**Beispiel ??**
### class Start
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
    - Text

### class MainController
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
    - \_\_init_\_
    - registerEvents
      -  Text
    - connectSignals
    - registerCommands
    - actionPerformed
    - undo
    - redo
    - keyPressEvent
    - keyReleaseEvent
    - quitApp
    - windowResize
    - windowHide
    - windowActivate
  
**Views**

### class GraphicsView
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
    - \_\_init_\_
    - updateCanvas
      -  Text
    - drawImage
    - drawFigures
    - getCanvas
    - getScaledImage
    - getStrokeColor
    - getStrokeWidth
    - getStrokePattern
    - getBrushStyle
    - getPenCapStyle
    - setCanvas
    - setStrokeColor
    - setStrokeWidth
    - setStrokePattern
    - setBrushStyle
    - setPenCapStyle

### class MainView
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
    - \_\_init_\_
    - keyPressEvent
      -  Text
    - keyReleaseEvent
    - canvasPressedEvent
    - closeEvent
    - resizeEvent
    - hideEvent
    - undoEvent
    - redoEvent
    - getGraphicsView
    - getbtnFile
    - getbtnClear_all
    - getbtnOpen
    - getbtnSave
    - getbtnCalibrate
    - getbtnHelp
    - getbtnPaint
    - getbtnErase
    - getbtnRed
    - getbtnBlue
    - getbtnYellow
    - getbtnThick
    - getbtnMedium
    - getbtnThin
    - getbtnUndo
    - getbtnRedo
    - getbtnColorPicker
    - getbtnStrokeWidthPicker
  
### class View_ui_rcs
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
    - \_\_init_\_
    - retranslateUi
      -  Text

**models**

### class GraphicsModel
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
    - \_\_init_\_
    - addFigure
    - recPoint
    - getLastFigure
    - deleteLastFigure
    - deleteFigure
    - clearFigures
    - safeFigures
    - openFigures
    - exportDrawing
    - bSpline
    - findFigure
    - getFigures
    - getMode
    - setMode

### class Figure
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
    - \_\_init_\_
    - addPoint
    - getPoints
    - getStrokeColor
    - getStrokeWidth
    - getStrokePattern
    - getBrushStyle
    - getPenCapStyle
  
### class CVModel
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - getHeight
  - getWidth
  - run

**commands**

### class CmdCalibrateCVCol
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable
  - alertUser
  - canvasClick

### class CmdClearFigures
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable
  
### class CmdDrawingMode
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable

### class CmdErasingMode
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable

### class CmdExportDwgNB
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable
  
### class CmdHelp
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable

### class CmdOpenFigures
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable

### class CmdSafeFigures
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable
  
### class CmdSetStrokeColor
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable 

### class CmdSetStrokeWidth
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable
  - getPenProperties
  - setPenProperties
  
### class CommandInterface
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - execute
  - redo
  - undo
  - isUndoable

### class CommandInvoker
- description: <br /> 
  Text
- attribute <br /> 
  - Text
- methods <br /> 
  - \_\_init_\_
  - addCommand
  - executeCommand
  - undoCommand
  - redoCommand 
