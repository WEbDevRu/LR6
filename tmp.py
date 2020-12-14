class MenuScreen(Screen):
    Texture_acc = ObjectProperty()
    NickName = StringProperty()
    Description = StringProperty()

    def __init__(self, **kwargs):
        if ERRORVALUE == 1:
            cursor.execute("Select * FROM dbo.Users where ID_User = '" + '3' + "'")
            res = cursor.fetchone()
            self.NickName = res[1]
            self.Description = res[4]
            raw_texture_acc = res[3]
            data = io.BytesIO(raw_texture_acc)
            self.Texture_acc = CoreImage(data, ext='jpg').texture
        else:
            self.NickName = 'Putin'
            self.Description = 'PUTINNNN'
        super(MenuScreen, self).__init__(**kwargs)

    def on_touch_move(self, touch):
        if touch.ox - touch.x > 50:
            TamadaApp().change_to_tape()

    @staticmethod
    def exit_app():
        MyTamada.stop()
        print('App close')
