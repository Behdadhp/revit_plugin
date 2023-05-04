# Revit Plugin
This script makes it possible to create a JSON from 3D model in Revit using [PyRevit](https://github.com/eirannejad/pyRevit). The JSON should
contain infos about the wall, roof and floor and also their material thickness.
To add this plugin to Revit, you need to copy the content of [JSON.pushbutton](JSON.pushbutton)
to this path:


**Users\User\AppData\Roaming\pyRevit-Master\extensions\pyRevitJSON.extension\JSON.pushbutton\ModelToJSON.tab\Convertor.panel\JSON.pushbutton**


<br />
Then it is necessary to reload the PyRevit in Revit. To open the plugin in its path, you need hold the ALT while clicking on the icon.

The Icon is taken from [ichon8](https://icons8.com/).

# Revit API Autocomplete in PyCharm 
It can be set up using [ironpython-stubs](https://github.com/gtalarico/ironpython-stubs). In order to that, you Just need to download the project and go to release folder and copy the [stub.min](https://github.com/gtalarico/ironpython-stubs/tree/master/release/stubs.min)
and paste it to the folder of virtual environment. Finally you need to add this foolder to the interpreter path in PyCharm. 

# Attention
This code is customized for my need, so it may not be working in your case. But if you are new in using PyRevit, it can inspire and give you a mindset how to develop your own script.
