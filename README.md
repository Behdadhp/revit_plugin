# Revit Plugin
This scripts make it possible to create a JSON from 3D model in Revit using [PyRevit](https://github.com/eirannejad/pyRevit). The JSON should
contain infos about the wall, roof and floor and also their thickness.
To add this plugin to Revit, you need to copy the content of [JSON.pushbutton](JSON.pushbutton)
to this path:


**Users\User\AppData\Roaming\pyRevit-Master\extensions\pyRevitJSON.extension\JSON.pushbutton\ModelToJSON.tab\Convertor.panel\JSON.pushbutton**


<br />
Then it is necessary to reload the PyRevit in Revit. After adding the plugin to Revit it can be open by clicking on the icon while pressing Alt.

The Icon is taken from [ichon8](https://icons8.com/).

# Revit API Autocomplete in PyCharm 
It can be set up using [ironpython-stubs](https://github.com/gtalarico/ironpython-stubs). In order to that, Just need to download the project and go to release folder anc copy the [stub.min](https://github.com/gtalarico/ironpython-stubs/tree/master/release/stubs.min)
and paste it to the folder of virtual environment. Finally you need to add this foolder to the interpreter path in PyCharm. 
