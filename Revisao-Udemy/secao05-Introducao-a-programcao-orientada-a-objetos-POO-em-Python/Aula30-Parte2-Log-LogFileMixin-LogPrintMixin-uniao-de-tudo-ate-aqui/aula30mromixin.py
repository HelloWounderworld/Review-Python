class MixinA:
    def close_log(self):
        print("Close log from MixinA")

class MixinB:
    def close_log(self):
        print("Close log from MixinB")

class Application(MixinA, MixinB):
    def close(self):
        self.close_log()

app = Application()
app.close()  # Isso imprimirá "Close log from MixinA"