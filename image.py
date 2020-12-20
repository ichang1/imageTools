from PIL import Image, ImageFilter
from math import ceil
import os
from utils import camel

class ImageWrap:
    def __init__(self, path):
        self.path = path
        self.file_name, self.ext = os.path.basename(path).split(".")
        self.img = Image.open(path)
        self.final = None
        self.filter = ""
        self.final_dir = None
    
    def save(self, path):
        dir = "{}{}_{}.{}".format(path,self.file_name,self.filter,self.ext)
        self.final.save(dir)
        self.final_dir = dir

    def grayscale(self):
        self.final = self.img.convert("L")
        self.filter = 'grayscale'

    def blur(self):
        self.final = self.img.filter(ImageFilter.BLUR)
        self.filter = 'blur'

    def contour(self):
        self.final = self.img.filter(ImageFilter.CONTOUR)
        self.filter = 'contour'
    
    def detail(self):
        self.final = self.img.filter(ImageFilter.DETAIL)
        self.filter = 'detail'

    def edge_enhance(self):
        self.final = self.img.filter(ImageFilter.EDGE_ENHANCE)
        self.filter = 'edge_enchance'
    
    def edge_enhance_more(self):
        self.final = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.filter = 'edge_enchance_more'
    
    def emboss(self):
        self.final = self.img.filter(ImageFilter.EMBOSS)
        self.filter = 'emboss'

    def find_edges(self):
        self.final = self.img.convert("L").filter(ImageFilter.FIND_EDGES)
        self.filter = 'find_edges'
    
    def sharpen(self):
        self.final = self.img.filter(ImageFilter.SHARPEN)
        self.filter = 'sharpen'
    
    def smooth(self):
        self.final = self.img.filter(ImageFilter.SMOOTH)
        self.filter = 'smooth'
    
    def smooth_more(self):
        self.final = self.img.filter(ImageFilter.SMOOTH_MORE)
        self.filter = 'smooth_more'

    def gaussian_blur(self, radius):
        if radius < 0:
            radius = 0
        self.final = self.img.filter(ImageFilter.GaussianBlur(radius))
        self.filter = 'gaussian_blur_r'
    
    def box_blur(self, radius):
        self.final = self.img.filter(ImageFilter.BoxBlur(radius))
        self.filter = 'box_blur_r'.format(int(ceil(radius)))
    
    def unsharp_mask(self, radius, percent, threshold):
        self.final = self.img.filter(ImageFilter.UnsharpMask(radius, percent, threshold))
        self.filter = 'unsharp_mask'

    def kernel(self, kernel:tuple):
        n = int(len(kernel)**0.5)
        f = ImageFilter.Kernel((n, n), kernel, 1, 0)
        self.final = img.filter(f)
        self.filter = "kernel"

    def resize(self, dim):
        self.final = self.img.resize(dim)
        self.filter = "resized"

    
