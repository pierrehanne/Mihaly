ECHO "Start";
cd ../..
cd "Blender Foundation"
cd "Blender 2.81"
blender.exe "C:\Users\jacky\Desktop\Mihally Project\Mihaly-master\Figures Tests\test.blend" -b -P "C:\Users\jacky\Desktop\Mihally Project\Mihaly-master\Reorientation.py" -o //result -f +1
ECHO "Finish";
PAUSE