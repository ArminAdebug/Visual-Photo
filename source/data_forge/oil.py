r"""import numpy as np
from PIL import Image


def main(Image, radius: int):  # --> RGB, [x, y, c]

    array = np.array(Image)
    array_h, array_w = array.shape[:2]

    array_out = array.copy()

    for x in np.arange(1, array_w):
        for y in np.arange(1, array_h):

            r_sum = 0
            g_sum = 0
            b_sum = 0

            colors = {}

            area_x = [max(0, x - radius), min(array_w, x + radius)]
            area_y = [max(0, y - radius), min(array_h, y + radius)]
            
            r_sum = array[area_x[0]:area_x[1], area_y[0]:area_y[1], 0].sum()
            g_sum = array[area_x[0]:area_x[1], area_y[0]:area_y[1], 1].sum()
            b_sum = array[area_x[0]:area_x[1], area_y[0]:area_y[1], 2].sum()
                        
            
            print("x :", x ,"y :", y)
            
            area_pixels_count = (area_x[1] - area_x[0]) * (area_y[1] - area_y[0])
            for w in range(area_x[0], area_x[1]):
                for h in range(area_y[0], area_y[1]):
                    
                    if w > array_w or h > array_h:
                        print("w, h:", (w, h))
                        raise IndexError
                    color_rounded = (round(array[w, h][0] / 10) * 10,
                                    round(array[w, h][1] / 10) * 10,
                                    round(array[w, h][2] / 10) * 10
                                    )
                    if not color_rounded in colors:
                        colors[color_rounded] = 1
                    else:
                        colors[color_rounded] += 1
                        
            average_pixels = (r_sum / area_pixels_count,
                              g_sum / area_pixels_count,
                              b_sum / area_pixels_count)

            most_frequent = sorted(colors, key=lambda x: x[1])[0]
            print("most_frequent :", most_frequent)
            colors.clear()
                
            array_out[x, y] = ((most_frequent[0] + (average_pixels[0])) / 2,
                               (most_frequent[1] + (average_pixels[1])) / 2,
                               (most_frequent[2] + (average_pixels[2])) / 2
                               ) # average

    return array_out


path = r"F:\docc\armin\+GAME'S\Dev\Code\Python\Portfolio\image test folder\test2.png"
PIL_image = Image.open(path)

out_image = Image.fromarray(main(PIL_image, 3))
print("finished")

out_image.save(r"F:\docc\armin\+GAME'S\Dev\Code\Python\Portfolio\image test folder\out.png")
"""
"█"
import numpy as np
from PIL import Image
from process_bar import ProcessBar

def oil_painting_effect(image, radius=3, bin_size=10):
    array = np.array(image)
    height, width = array.shape[:2]
    total_pixels = height * width
    
    output = np.zeros_like(array)

    process_bar = ProcessBar(total_pixels, True, True)
    
    for y in range(height):
        for x in range(width):
            process_bar.next(y * x)
            
            y_start = max(0, y - radius)
            y_end = min(height, y + radius + 1)
            x_start = max(0, x - radius)
            x_end = min(width, x + radius + 1)
            
            window = array[y_start:y_end, x_start:x_end]
            
            bins = {}
            for i in range(window.shape[0]):
                for j in range(window.shape[1]):
                    r, g, b = window[i, j]
                    quantized = (
                        (r // bin_size) * bin_size,
                        (g // bin_size) * bin_size,
                        (b // bin_size) * bin_size
                    )
                    bins[quantized] = bins.get(quantized, 0) + 1
            
            dominant_color = max(bins.items(), key=lambda item: item[1])[0]
            
            output[y, x] = dominant_color
    
    print()
    return output

input_path = "F:\\docc\\armin\\+GAME'S\\Dev\\Code\\Python\\Portfolio\\image test folder\\test.png"
output_path = "F:\\docc\\armin\\+GAME'S\\Dev\\Code\\Python\\Portfolio\\image test folder\\out_oil_painting.png"

original_image = Image.open(input_path)
result_array = oil_painting_effect(original_image, radius=5)
result_image = Image.fromarray(result_array)
result_image.save(output_path)

print(f"\nپردازش با موفقیت انجام شد! تصویر در {output_path} ذخیره گردید.")