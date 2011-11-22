#import datetime
#from haystack.indexes import *
#from haystack import site
#from myapp.models import Note


#class NoteIndex(SearchIndex):
#    text = CharField(document=True, use_template=True)
#    author = CharField(model_attr='user')
#    pub_date = DateTimeField(model_attr='pub_date')

#    def index_queryset(self):
#        """Used when the entire index for model is updated."""
#        return Note.objects.filter(pub_date__lte=datetime.datetime.now())


#site.register(Note, NoteIndex)

