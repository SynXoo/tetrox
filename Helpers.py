import pygame as py


class HelpingMethods:
    @staticmethod
    def ratioRetainer(rect, wratio, hratio):
        w, h = py.display.get_window_size()
        centW = w // wratio
        centH = h // hratio

        rect.center = (centW, centH)
        print(f"These are the coordinates:\n Width = {centW} pixels \n Height = {centH}")
        return rect

    @staticmethod
    def imageScaler(imageo, scale):
        originalWidth, originalHeight = imageo.get_size()
        newWidth = int(originalWidth // scale)
        newHeight = int(originalHeight // scale)
        return py.transform.scale(imageo, (newWidth, newHeight))
