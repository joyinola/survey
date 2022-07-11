from import_export import resources,fields
from .models import HeadLines,Vote

class HeadlineResource(resources.ModelResource):
    upvote = fields.Field(attribute="upvote_total", column_name="Upvote_Total")
    downvote =fields.Field(attribute='downvote_total',column_name='Downvote_Total')
    class Meta:
        model=HeadLines
        fields=('id','headLine','description','img','upvote','downvote')


class VoteResource(resources.ModelResource):


    class Meta:
        model = Vote
        fields = (
            'user__prolificId','user__puceTest','user__gender','user__ipAddress','user__age','user__qualification','user__politicalInterest',
            'user__party','user__presidentialCandidate',
            'headline__id','headline__headLine','headline__description',
            'headline__img','vote','createdAt','updatedAt'
            )