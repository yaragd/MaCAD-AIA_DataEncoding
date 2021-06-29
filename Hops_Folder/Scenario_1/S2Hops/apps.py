from flask import Flask
from logging import debug
import rhinoinside
import ghhops_server as hs
import runPythonapp as myML
import rhino3dm as r
rhinoinside.load(str())
import Rhino 
import Rhino.Geometry as rg


app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/directSunE",  #this is what we have to write in hops address, like http://127.0.0.1:5000/pointat
    name="predict direct sun access",
    description="predict direct sun acceses",
    inputs=[
        hs.HopsNumber("h", "h", "Building height"),
        hs.HopsNumber("w", "w", "Building width"),
        hs.HopsNumber("l", "l", "Building length"),
        hs.HopsNumber("s", "s", "hoys")
        
        
    ],
    outputs=[
        hs.HopsNumber("prediction", "DSH", "prediction", hs.HopsParamAccess.LIST )
    ]
)

def predictions(h, w, l, s):

    pred = myML.predictions(h,w,l,s)
    return pred

if __name__ == "__main__":
    app.run(debug=True)
