branch_coverage = {     
    "except_import_numpy": False,       
    "import_numpy_succes": False,         
    "except_import_pygame.pixelcopy": False,      
    "imports_failed": False                 
}

__tags__ = ["array"]

exclude = False

try:
    import numpy
except ImportError:
    branch_coverage["except_import_numpy"] = True
    exclude = True
else:
    branch_coverage["import_numpy_succes"] = True
    try:
        import pygame.pixelcopy
    except ImportError:
        branch_coverage["except_import_pygame.pixelcopy"] = True
        exclude = True

if exclude:
    branch_coverage["imports_failed"] = True
    __tags__.extend(("ignore", "subprocess_ignore"))

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")

print_coverage()