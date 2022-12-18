# :mag_right: Textrac
---

#### :bulb: Features
---

- Stand-alone Word Detection
- Stand-alone Digit Detection
- Real-time Webcam Text Detection
- Screen Capture Text Detection
---
#### :wrench: Pre-requisites before running
---
##### :books: Libraries (you may check the requirements.txt)

- opencv - `pip install opencv-python`
- pytesseract - `pip install pytesseract`
- Pillow - `pip install pytesseract`
- re - comes with Python
- os - comes with Python
- numpy - `pip install numpy`
- tempfile - comes with Python

##### :open_file_folder: Others (you may choose any of these methods to download and install Tesseract)

- [Tesseract Installation(Binaries) on Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- [Tesseract Installation(Binaries) on Ubuntu](https://launchpad.net/~alex-p/+archive/ubuntu/tesseract-ocr-devel)
- [Tesseract Installation(Binaries) on Debian](https://notesalexp.org/tesseract-ocr/#tesseract_5.x)
- [Source Code and Other Ways to Download and Install](https://github.com/tesseract-ocr/tessdoc/blob/main/Downloads.md)

:page_facing_up: Note: You may find the documentation for Tesseract here: [Tesseract Documentation on GitHub](https://github.com/tesseract-ocr/tesseract)

---
#### :question: How to run?
---

1. Make sure **tesseract** is installed. You can check if it is installed probably in your `C:\Program Files\Tesseract-OCR` directory if you're using Windows.
2. Make sure all the necessary **libraries** are installed. To make sure, you can run all the `pip install` commands or you can manually check them with `pip list` command which lists all your currently installed libraries.
3. Ready your assets (e.g. clear images with text, clear images with number/digits).

##### :question: How to run words_detection.py?
1. Drag your assets(clear images with some text) to the `img_words` directory.
2. Run the `words_detection.py` file.
3. The program will ask you to enter the filename that you want use. Make sure that the file is in the `img_words directory`.
4. The results will be shown. You may click the window and the Press the `X` key to exit.

##### :question: How to run digits_detection.py?
1. Drag your assets(clear images with some numbers/digits) to the `img_digits` directory.
2. Run the `digits_detection.py` file.
3. The program will ask you to enter the filename that you want use. Make sure that the file is in the `digits directory`.
4. The results will be shown. You may click the window and the Press the `X` key to exit.

##### :question: How to run webcam_text_detection.py?
1. Prepare something readable with some text such as a book,
2. Run the `webcam_text_detection.py` file.
3. Put it closer to the camera/webcam once the webcam turns on.
4. See the real-time text detection in the terminal/console.
5. If you want to screencapture, you may Press the `S` key to save the image.
6. The screencaptured image would then be saved in the root directory of this app.
7. The results will be shown. You may click the window and the Press the `X` key to exit.