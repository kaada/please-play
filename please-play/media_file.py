class MediaFile():

    def __init__(self, name, source, icon='☁ '):
        self.name = name
        self.source = source
        self.icon = icon

    def get_name(self):
        return self.name

    def get_source(self):
        return self.source

    def __repr__(self):
        return (f' {self.icon} : {self.name}')#\n\t ({self.source})')
