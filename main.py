from image import ImageWrap
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os
import tempfile

app = FastAPI()
STATIC_DIR = 'static/'
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")

methods = [method_name for method_name in dir(ImageWrap)
                  if callable(getattr(ImageWrap, method_name)) 
                  and not method_name.startswith('__')
                  and method_name != "save"]

def clean():
    filelist = [ f for f in os.listdir(STATIC_DIR)]
    for f in filelist:
        os.remove(os.path.join(STATIC_DIR, f))

@app.get("/", response_class=HTMLResponse)
async def filter_post(request: Request):
    context = {'request':request}
    return templates.TemplateResponse('home.html', context)

# filename — Name of the file. It is based on the original file name uploaded.
# content_type — Content type of the file. For example, an JPEG image file should be image/jpeg.
# file — Python file object.
@app.post("/", response_class=FileResponse)
async def filter_post(request: Request):
    clean()
    # try:
    form_data = await request.form()
    f = form_data['filter']
    params = {}
    if 'radius' in form_data.keys():
        params['radius'] = form_data['radius']
    if 'percent' in form_data.keys():
        params['percent'] = form_data['percent']
    if 'threshold' in form_data.keys():
        params['threshold'] = form_data['threshold']
    if 'kernel' in form_data.keys():
        params['kernel'] = form_data['kernel']
    name = form_data['image'].filename
    file = form_data['image'].file
    file_path = '{}{}'.format(STATIC_DIR, name)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file, buffer)
    img = ImageWrap(file_path)
    getattr(img, f)(params=params)
    img.save(STATIC_DIR)
    return FileResponse(getattr(img, 'final_dir'))
    # except:
    #     raise HTTPException(status_code=404, detail="Error")
    
