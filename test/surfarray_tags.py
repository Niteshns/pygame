__tags__ = ["array"]

exclude = False

try:
    import numpy
except ImportError:
    exclude = True
else:
    try:
        import pygame.pixelcopy
    except ImportError:
        exclude = True

if exclude:
    __tags__.extend(("ignore", "subprocess_ignore"))

assert 'numpy' in globals(), "numpy not imported correctly"
assert 'pygame' in globals() and 'pixelcopy' in dir(pygame), "pygame.pixelcopy not imported correctly"
print("Succesfully imported numpy and pygame.pixelcopy")

array = numpy.array([1, 2, 3])
assert array.ndim == 1, "Array dimension is not equal to 1"
assert array.size == 3, "Array size is not equal to 3"
assert numpy.sum(array) == 6, "The sum of array elements is not correct"
array_2 = numpy.array([3, 2, 1])
sum_array = array + array_2
mult_array = array * array_2
assert numpy.array_equal(sum_array, [4, 4, 4]), "Array addition did not work correct"
assert numpy.array_equal(mult_array, [3, 4, 3]), "Array multiplication did not work correct"
print("Advanced numpy test works correct")


try:
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    screen.fill((255, 255, 255))
    surface = pygame.Surface((10, 10))
    surface.fill((255, 0, 0))
    arr = pygame.surfarray.pixels2d(surface)
    new_surface = pygame.Surface(arr.shape)
    pygame.pixelcopy.array_to_surface(new_surface, arr)
    assert new_surface.get_size() == surface.get_size(), "Surface sizes do not match"
    assert new_surface.get_at((0, 0)) == surface.get_at((0, 0)), "Pixel copy did not work correctly"
    pygame.quit()
    print("Advanced pygame_pixelcopy test passed")
except AssertionError:
    print("Advanced pygame_pixelcopy test failed")
finally:
    pygame.quit()