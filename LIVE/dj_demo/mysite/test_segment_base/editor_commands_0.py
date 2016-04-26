# Qt client receives this message
def on_message_set_text(self, payload):
    self.set_text(payload['text'])
