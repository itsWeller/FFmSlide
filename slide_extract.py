from PIL import Image
import os,sys,getopt,imagehash

def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(str(s1)) != len(str(s2)):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str(s1), str(s2)))

input_f  = 'lect1.mp4'
output_f = 'foo-'
output_d = 'slides'

os.system('rm -r ' + output_d)
os.system('mkdir ' + output_d)
os.system('ffmpeg -i '+input_f+' -vsync 0 -vf select="eq(pict_type\,PICT_TYPE_I)" -f image2 '+output_d + '/' + output_f+'%03d.jpeg')

file_list = os.listdir('./'+output_d)
file_list = file_list[::-1]

comparison_file = None
current_file = None

comparison_file = file_list[0]
comparison_hash = imagehash.dhash(Image.open(output_d + '/' + comparison_file))

for filename in file_list[1:]:
    #print filename
    f_hash = imagehash.dhash(Image.open(output_d + '/' + filename)) 

    print f_hash,comparison_hash
    jamon = hamming_distance(f_hash, comparison_hash)

    #if f_hash == comparison_hash:
    if jamon < 5: # 5 is magical
        os.system('rm ' + output_d + '/' + filename)
    else:
        comparison_hash = imagehash.dhash(Image.open(output_d + '/' + filename))
    #pass

