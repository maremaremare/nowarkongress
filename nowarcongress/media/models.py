# -*- coding: utf-8 -*-
from django.db import models
from embed_video.fields import EmbedVideoField
#from imagekit.models import ImageSpecField
from content.models import ContentItem
#from imagekit.processors import ResizeToFill, ResizeToFit, Anchor

import logging
from filebrowser.base import FileObject
from filebrowser.fields import FileBrowseField


# Get an instance of a logger
logger = logging.getLogger('my')


class Photo(models.Model):
    image = FileBrowseField("Image", max_length=200, directory="photos/", extensions=[".jpg",".jpeg",".png"], blank=True, null=True)


    #photo = models.ImageField(upload_to='photos', null=True, blank=True, verbose_name=u'Фотография', help_text=u'Фотография в jpg. Не менее 850 на 350 пикселов.')
    title = models.CharField(max_length=100,
                             verbose_name=u'Название', help_text=u'Название фотографии')
    content = models.ForeignKey(ContentItem, related_name='photos')
    # photo_content_type = models.ForeignKey(
    #     ContentType, related_name="photo")
    # photo_object_id = models.PositiveIntegerField()
    # photo_content_object = generic.GenericForeignKey(
    #     'photo_content_type', 'photo_object_id')
    # list_thumbnail = ImageSpecField(source='photo',
    #                                 processors=[ResizeToFill(340, 240)],
    #                                 format='JPEG',
    #                                 options={'quality': 60})
    # slmin_thumbnail = ImageSpecField(source='photo',
    #                                  processors=[ResizeToFill(96, 60)],
    #                                  format='JPEG',
    #                                  options={'quality': 60})
    # slmax_thumbnail = ImageSpecField(source='image',
    #                                  processors=[ResizeToFill(848, 350)],
    #                                  format='JPEG',
    #                                  options={'quality': 60})
    # sidebar_thumbnail = ImageSpecField(source='photo',
    #                                    processors=[ResizeToFill(50, 50)],
    #                                    format='JPEG',
    #                                    options={'quality': 70})
    # adv_thumbnail = ImageSpecField(source='photo',
    #                                processors=[
    #                                    ResizeToFill(247, 175, anchor=Anchor.TOP)],
    #                                format='JPEG',
    #                                options={'quality': 60})
    # adv_thumbnail_detail = ImageSpecField(source='photo',
    #                                       processors=[
    #                                           ResizeToFit(247, anchor=Anchor.TOP)],
    #                                       format='JPEG',
    #                                       options={'quality': 60})
    # owlcarousel_thumbnail = ImageSpecField(source='photo',
    #                                        processors=[ResizeToFill(848, 485)],
    #                                        format='JPEG',
    #                                        options={'quality': 70})

    class Meta:
        verbose_name = ('Фото')
        verbose_name_plural = ('Фото')

    def __unicode__(self):
        if not self.title:
            return u'Без названия' 
        return self.title+' '+'.'


    def image_thumbnail(self):
        if self.image:
            image = FileObject(self.image.path)
            if image.filetype == "Image":
                return '<img src="%s" />' % image.version_generate('admin_thumbnail').url
        else:
            return ""
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Thumbnail"


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Видео')
    video = EmbedVideoField()
    content = models.ForeignKey(ContentItem, related_name='videos')
    # video_content_type = models.ForeignKey(
    #     ContentType, related_name="video")
    # video_object_id = models.PositiveIntegerField()
    # video_content_object = generic.GenericForeignKey(
    #     'video_content_type', 'video_object_id')

    class Meta:
        verbose_name = ('Видео')
        verbose_name_plural = ('Видео')

    def __unicode__(self):
        return self.title

# class PhotoMixin(object):
#   @property
#   def relatedphotos(self):
#     ctype = ContentType \
#       .objects \
#       .get_for_model(self.__class__)
#     try:
#       photos = Photo \
#         .objects \
#         .filter(
#           photo_content_type = ctype.id,
#           photo_object_id=self.id)
#     except Photo.DoesNotExist:
#       return None

#     return photos

# class VideoMixin(object):
#   @property
#   def relatedvideos(self):
#     ctype = ContentType \
#       .objects \
#       .get_for_model(self.__class__)
#     try:
#       videos = Video \
#         .objects \
#         .filter(
#           photo_content_type = ctype.id,
#           photo_object_id=self.id)
#     except Video.DoesNotExist:
#       return None

#     return videos
