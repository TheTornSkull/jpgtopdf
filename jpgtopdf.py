from PIL import Image, ExifTags
import os
import shutil

# make a folder named Q2 and Q3 on your desktop
# put images of question 2 and 3 in appropriate folders and make sure all of them are in portrait mode (vertical)
#make changes here :
pcname = ""
seatno = ""
admissionno = ""

# run this python script
# Enter the subject name accordingly


def jpgtopdf(q,sub):
    directory = "C:/Users/" + pcname + "/Desktop/"+q+"/"
    pdf_path = directory+ seatno +"_"+ sub +"_"+ admissionno + "_"+ q + ".pdf"
    dest = directory+"temp/"
    os.mkdir(dest)
    for file_name in os.listdir(directory):
        if file_name.endswith(".jpg"):
            full_file_name = os.path.join(directory, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest)

    img_list = []
    one = 0
    for filename in os.listdir(dest):
        if filename.endswith(".jpg"):

            img = Image.open(directory+filename)
            for orientation in ExifTags.TAGS.keys() :
                if ExifTags.TAGS[orientation]=='Orientation' : break
            exif=dict(img._getexif().items())

            if   exif[orientation] == 3 :
                img=img.rotate(180, expand=True)
            elif exif[orientation] == 6 :
                img=img.rotate(270, expand=True)
            elif exif[orientation] == 8 :
                img=img.rotate(90, expand=True)

            img.thumbnail((3120 , 4160), Image.ANTIALIAS)
            img.save(os.path.join(dest,filename))

            if(one == 0):
                im1 = Image.open(dest+filename)
                one = 1
            else:
                img_list.append(img)

            continue
        else:
            continue

    im1.save(pdf_path, "PDF" ,resolution=300, save_all=True, append_images=img_list)
    shutil.rmtree(dest)

#main
sub = input("Enter the subject: ")
jpgtopdf("Q2",sub)
jpgtopdf("Q3",sub)
print("Files converted successfully")
