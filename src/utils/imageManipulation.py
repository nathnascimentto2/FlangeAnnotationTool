import cv2, os
import shutil

class imageManipulation():

    def rgbToGrayscale(self, filePath, saveAs = ''):
        
        image = cv2.imread(filePath)
        grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        self.saveImage(filePath, saveAs) 

        return 1

    def cropImage(self, filePath, heigth, width, startPixelX = 0, startPixelY = 0, saveAs = ''):

        image = cv2.imread(filePath)
        cropImage = image[startPixelY:startPixelY+heigth, startPixelX:startPixelX+width]
        
        self.saveImage(filePath, saveAs)

        return 1

    def resizeImage(self, filePath, heigth, width, saveAs = ''):
        
        image = cv2.imread(filePath)

        resizedImg = cv2.resize(image, (heigth, width))
        self.saveImage(filePath, saveAs)
        
        return 1
        
    def saveImage(self, image, filePathToRewrite, saveAs = ''):

        if saveAs != '': 
            cv2.imwrite(saveAs, image)
        else:
            cv2.imwrite(filePathToRewrite, image)

        return 1

    def toBitmap(self, filePath, saveAs = ''):

        image = cv2.imread(filePath)
        grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        bitmap = grayscale.reshape([img.shape[0], img.shape[1]])
        bitmap = np.dot((bitmap > 128).astype(float),255)

        bitmap = bitmap.astype(np.uint8)

        self.saveImage(filePath, saveAs)

        return 1

    def adjustContrast(self, factor, filePath, saveAs = ''):

        image = cv2.imread(filePath)
        factor = np.ones(image.shape)*100
        contrast = np.add(image, factor) 

        self.saveImage(filePath, saveAs)

        return 1
    
