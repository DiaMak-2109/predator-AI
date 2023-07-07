import jetson.inference
import jetson.utils
import argparse




#parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()

#load the image (placeholder)
img = jetson.utils.loadImage(opt.filename)

#load the image classification/recognition network (pre-trained)
net = jetson.inference.imageNet(opt.network)

#classify the image
class_idx, confidence = net.Classify(img)

#find and store the object description
object_class = net.GetClassDesc(class_idx)





print("")
print("*______________________________________________________________________________________________________________-*")
if object_class == "cougar, puma, catamount, mountain lion, painter, panther, Felis concolor":
    print("Threat identified: Cougar")
elif object_class == "coyote, prairie wolf, brush wolf, Canis latrans":
     print("Threat identified: Coyote")
elif object_class == "red fox, Vulpes vulpes":
    print("Threat identified: Fox")
elif object_class == "kit fox, Vulpes macrotis":
    print("Threat identified: Fox")
elif object_class == "grey fox, gray fox, Urocyon cinereoargenteus":
    print("Threat identified: Fox")
elif object_class == "American alligator, Alligator mississipiensis":
    print("Threat identified: Alligator")
elif object_class == "diamondback, diamondback rattlesnake, Crotalus adamanteus":
    print("Threat identified: Rattlesnake")
else:
    print("No threat identified")
