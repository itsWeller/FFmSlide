from PIL import Image
import os,sys,imagehash,platform,subprocess,shutil

output_d = 'slides'

output_folder_path = os.getcwd() + '/' + output_d

if platform.system() == 'Windows':
    FFMPEG_BIN = 'ffmpeg.exe'
else:
    FFMPEG_BIN = 'ffmpeg'

def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(str(s1)) != len(str(s2)):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str(s1), str(s2)))

for input_f in os.listdir(os.getcwd() + '/' + 'lecture_videos'):
    sub_dir = input_f[0:input_f.find('.')]
    sub_dir_path = output_folder_path + '/' + sub_dir

    if not os.path.exists(sub_dir_path):
        os.makedirs(sub_dir_path)

    command = [FFMPEG_BIN,'-i',os.getcwd() + '/lecture_videos/' + input_f,'-vsync','0','-vf','select=eq(pict_type\,PICT_TYPE_I)','-f','image2',output_d + '/' + sub_dir + '/slide-'+'%03d.jpeg']

    try:
        subprocess.check_call(command)
    except:
        print '\n\tFFmpeg raised error. Check output for details. Exiting.'
        sys.exit()

    file_list = os.listdir(sub_dir_path)
    file_list = file_list[::-1]

    comparison_file = None
    current_file = None

    comparison_file = file_list[0]
    comparison_hash = imagehash.dhash(Image.open(sub_dir_path + '/' + comparison_file))

    for filename in file_list[1:]:
        f_hash = imagehash.dhash(Image.open(sub_dir_path + '/' + filename)) 

        jamon = hamming_distance(f_hash, comparison_hash)

        if jamon < 5: # 5 is magical
            os.remove(sub_dir_path + '/' + filename)
        else:
            comparison_hash = imagehash.dhash(Image.open(sub_dir_path + '/' + filename))

