from image import ImageWrap
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
STATIC_DIR = '/static'
app.mount(STATIC_DIR, StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")

methods = [method_name for method_name in dir(ImageWrap)
                  if callable(getattr(ImageWrap, method_name)) 
                  and not method_name.startswith('__')
                  and method_name != "save"]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context= {}
    return templates.TemplateResponse("home.html", context)

@app.get("/{filter}", response_class=HTMLResponse)
async def filter(request: Request):
    if filter not in methods:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        context= {}
        return templates.TemplateResponse("filter_get.html", context)

@app.post("/{filter}", response_class=HTMLResponse)
async def filter(request: Request):
    context= {}
    return templates.TemplateResponse("filter_post.html", context)  

@app.get("/api", response_class=HTMLResponse)
async def filter(request: Request):
    context= {}
    return templates.TemplateResponse("api.html", context) 

@app.post("/api/{filter}", response_class=FileResponse)
async def filter(request: Request):
    return FileResponse("")

# img = ImageWrap("images/glass.jpg")
# img.find_edges()
# img.save(STATIC_DIR)