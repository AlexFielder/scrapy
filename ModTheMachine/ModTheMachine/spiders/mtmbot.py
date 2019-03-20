# -*- coding: utf-8 -*-
import scrapy


class MtmbotSpider(scrapy.Spider):
    name = 'mtmbot'

    def start_requests(self):
        urls = [
            'https://modthemachine.typepad.com/my_weblog/2008/10/converting-vba-auto-macros-to-an-add-in.html',
            'https://modthemachine.typepad.com/my_weblog/2008/10/program-prototyping.html',
            'https://modthemachine.typepad.com/my_weblog/2008/11/creating-buttons-for-vba-macros.html',
            'https://modthemachine.typepad.com/my_weblog/2009/01/removing-vba-document-projects-from-inventor-files.html',
            'https://modthemachine.typepad.com/my_weblog/2009/01/translating-files-with-the-api.html',
            'https://modthemachine.typepad.com/my_weblog/2009/02/controlling-part-colors.html',
            'https://modthemachine.typepad.com/my_weblog/2009/02/saving-image-files.html',
            'https://modthemachine.typepad.com/my_weblog/2009/02/setting-the-weight-for-ipart-members.html',
            'https://modthemachine.typepad.com/my_weblog/2009/03/accessing-assembly-components.html',
            'https://modthemachine.typepad.com/my_weblog/2009/03/combining-multiple-actions-into-a-single-undo.html',
            'https://modthemachine.typepad.com/my_weblog/2009/03/running-commands-using-the-api.html',
            'https://modthemachine.typepad.com/my_weblog/2009/04/controlling-layers-in-your-flat-pattern-export.html',
            'https://modthemachine.typepad.com/my_weblog/2009/04/extracting-a-specific-size-icon-from-a-ico-file.html',
            'https://modthemachine.typepad.com/my_weblog/2009/04/positioning-assembly-occurrences.html',
            'https://modthemachine.typepad.com/my_weblog/2009/07/introduction-to-attributes.html',
            'https://modthemachine.typepad.com/my_weblog/2009/10/visual-basic-6-add-ins-and-64-bit.html',
            'https://modthemachine.typepad.com/my_weblog/2010/01/exporting-assembly-structure-to-excel.html',
            'https://modthemachine.typepad.com/my_weblog/2010/02/accessing-iproperties.html',
            'https://modthemachine.typepad.com/my_weblog/2010/02/custom-iproperties.html',
            'https://modthemachine.typepad.com/my_weblog/2010/03/document-thumbnails-and-button-icons.html',
            'https://modthemachine.typepad.com/my_weblog/2010/03/flattening-an-assembly.html',
            'https://modthemachine.typepad.com/my_weblog/2010/03/iproperties-without-inventor-apprentice.html',
            'https://modthemachine.typepad.com/my_weblog/2010/04/creating-custom-property-sets-and-iproperties.html',
            'https://modthemachine.typepad.com/my_weblog/2010/04/iproperties-and-dates.html',
            'https://modthemachine.typepad.com/my_weblog/2010/04/iproperty-expressions.html',
            'https://modthemachine.typepad.com/my_weblog/2010/04/parameters-as-iproperties.html',
            'https://modthemachine.typepad.com/my_weblog/2010/05/working-with-filenames.html',
            'https://modthemachine.typepad.com/my_weblog/2010/05/working-with-files-and-directories.html',
            'https://modthemachine.typepad.com/my_weblog/2010/06/accessing-thumbnail-images.html',
            'https://modthemachine.typepad.com/my_weblog/2010/06/how-to-time-an-operation.html',
            'https://modthemachine.typepad.com/my_weblog/2010/07/approximating-a-sketch-curve-with-line-segments.html',
            'https://modthemachine.typepad.com/my_weblog/2010/07/saving-files-as-an-image-bmp-jpg-png-tiff-gif.html',
            'https://modthemachine.typepad.com/my_weblog/2010/07/sketch-curve-as-line-segments-in-vbnet-and-c.html',
            'https://modthemachine.typepad.com/my_weblog/2010/07/using-c-with-the-inventor-api-part-1.html',
            'https://modthemachine.typepad.com/my_weblog/2010/08/using-c-with-the-inventor-api-part-2.html',
            'https://modthemachine.typepad.com/my_weblog/2010/08/using-c-with-the-inventor-api-part-3.html',
            'https://modthemachine.typepad.com/my_weblog/2010/09/balloon-reporting-macro.html',
            'https://modthemachine.typepad.com/my_weblog/2010/09/totaling-the-length-of-parts-in-an-assembly.html',
            'https://modthemachine.typepad.com/my_weblog/2010/10/changing-drawing-curves-to-match-assembly-color.html',
            'https://modthemachine.typepad.com/my_weblog/2011/02/balloon-renumbering-across-sheets.html',
            'https://modthemachine.typepad.com/my_weblog/2011/02/importing-non-native-models-into-inventor.html',
            'https://modthemachine.typepad.com/my_weblog/2011/05/saving-3d-dwg-using-the-dwg-translator.html',
            'https://modthemachine.typepad.com/my_weblog/2011/06/moving-a-part-in-a-flexible-assembly.html',
            'https://modthemachine.typepad.com/my_weblog/2011/06/stepping-through-the-features-of-a-model.html',
            'https://modthemachine.typepad.com/my_weblog/2011/06/writing-work-points-to-an-excel-file.html',
            'https://modthemachine.typepad.com/my_weblog/2012/02/bitmaps-without-vb6-icontoipicture.html',
            'https://modthemachine.typepad.com/my_weblog/2012/02/getting-data-from-content-center.html',
            'https://modthemachine.typepad.com/my_weblog/2012/02/xml-ribbon-builder-design-pattern.html',
            'https://modthemachine.typepad.com/my_weblog/2012/03/clientgraphics-text-on-each-planar-face.html',
            'https://modthemachine.typepad.com/my_weblog/2012/03/create-a-mini-toolbar.html',
            'https://modthemachine.typepad.com/my_weblog/2012/03/create-an-ipart.html',
            'https://modthemachine.typepad.com/my_weblog/2012/03/customizing-marking-menus.html',
            'https://modthemachine.typepad.com/my_weblog/2012/03/surfacegraphics-select-primitives.html',
            'https://modthemachine.typepad.com/my_weblog/2012/04/creating-and-setting-up-your-project.html',
            'https://modthemachine.typepad.com/my_weblog/2012/04/drawing-in-a-sketch.html',
            'https://modthemachine.typepad.com/my_weblog/2012/04/objects-in-the-api.html',
            'https://modthemachine.typepad.com/my_weblog/2012/04/working-with-sketches.html',
            'https://modthemachine.typepad.com/my_weblog/2012/05/creating-geometric-constraints-in-a-sketch.html',
            'https://modthemachine.typepad.com/my_weblog/2012/05/get-strokes-for-2d-and-3d-transient-wireframe-geometry.html',
            'https://modthemachine.typepad.com/my_weblog/2012/05/thumbnail-viewer-component-on-a-64-bit-system.html',
            'https://modthemachine.typepad.com/my_weblog/2012/05/transient-wire-body-create-ruled-surface.html',
            'https://modthemachine.typepad.com/my_weblog/2012/06/3d-equivalent-of-a-2d-curve-on-a-surface.html',
            'https://modthemachine.typepad.com/my_weblog/2012/06/extract-partial-curves-from-2d-and-3d-transient-geometry.html',
            'https://modthemachine.typepad.com/my_weblog/2012/07/api-support-for-the-creation-and-edit-of-a-move-body-feature.html',
            'https://modthemachine.typepad.com/my_weblog/2012/08/discussion-on-client-graphics-segment-2.html',
            'https://modthemachine.typepad.com/my_weblog/2012/08/discussion-on-client-graphics-segment-3.html',
            'https://modthemachine.typepad.com/my_weblog/2012/08/discussion-on-client-graphics-segment-4.html',
            'https://modthemachine.typepad.com/my_weblog/2012/08/discussion-on-client-graphics.html',
            'https://modthemachine.typepad.com/my_weblog/2012/09/c-help-examples-for-parts-general.html',
            'https://modthemachine.typepad.com/my_weblog/2012/09/eto-override-getnewpartnumber-to-update-iproperties.html',
            'https://modthemachine.typepad.com/my_weblog/2012/09/eto-use-inventor-api-to-create-a-rendered-image-from-a-design.html',
            'https://modthemachine.typepad.com/my_weblog/2012/11/c-help-examples-for-drawing-annotations-part-one.html',
            'https://modthemachine.typepad.com/my_weblog/2012/11/c-help-examples-for-drawing-annotations-part-two.html',
            'https://modthemachine.typepad.com/my_weblog/2013/01/eto-potlatch-recordings.html',
            'https://modthemachine.typepad.com/my_weblog/2013/02/inventor-api-training-lesson-1.html',
            'https://modthemachine.typepad.com/my_weblog/2013/02/inventor-api-training-lesson-11.html',
            'https://modthemachine.typepad.com/my_weblog/2013/02/inventor-api-training-lesson-2.html',
            'https://modthemachine.typepad.com/my_weblog/2013/03/control-feature-creation-based-on-user-defined-boundary.html',
            'https://modthemachine.typepad.com/my_weblog/2013/03/inventor-2014-api-enhancements.html',
            'https://modthemachine.typepad.com/my_weblog/2013/03/inventor-api-training-lesson-12.html',
            'https://modthemachine.typepad.com/my_weblog/2013/07/add-in-with-event-example-to-replace-auto-run-macros-in-2014.html',
            'https://modthemachine.typepad.com/my_weblog/2013/07/inventor-events-using-net-3-examples.html',
            'https://modthemachine.typepad.com/my_weblog/2013/08/comparing-floating-point-numbers.html',
            'https://modthemachine.typepad.com/my_weblog/2013/08/updating-parts-through-an-assembly.html',
            'https://modthemachine.typepad.com/my_weblog/2013/09/processing-a-directory-of-files.html',
            'https://modthemachine.typepad.com/my_weblog/2013/09/working-with-cameras-part-2.html',
            'https://modthemachine.typepad.com/my_weblog/2014/09/fast-booleans-using-the-api.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/09/improving-your-programs-performance.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/09/understanding-reference-keys-in-inventor.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/12/placing-a-part-in-inventor-with-user-interaction.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/01/open-drawing-from-a-part-or-assembly.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/06/projecting-points-onto-a-solid.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/09/creating-construction-geometry-in-assemblies-in-inventor.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/01/store-and-restore-occurrence-position.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/04/units-and-parameters-in-inventor.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/06/getting-the-overall-size-of-parts.html',
            # 'https://modthemachine.typepad.com/my_weblog/2018/10/troubleshooting-debugging.html',
            # 'https://modthemachine.typepad.com/my_weblog/2019/03/accessing-iproperties.html',
            # 'https://modthemachine.typepad.com/my_weblog/2019/03/automate-creation-of-named-geometry.html',
            #recent posts:
            # 'https://modthemachine.typepad.com/my_weblog/2015/09/add-control-to-toolbar-panel.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/09/extrude-profile-with-hole.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/09/fusion-360-hackathon-qa-1-2.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/10/fusion-360-hackathon-qa-7-8-9-10.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/10/use-entitlement-api-from-fusion.html',
            # 'https://modthemachine.typepad.com/my_weblog/2015/11/fusion-add-in-path.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/01/run-fusion-commands.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/01/selection-object-properties-become-invalid.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/02/fusion-add-in-with-mfc.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/04/fusion-meetups-and-melting-butter.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/05/appearance-properties.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/05/is-point-on-face.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/08/drive-robot-arm-in-fusion-update.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/08/drive-robot-arm-in-fusion.html',
            # 'https://modthemachine.typepad.com/my_weblog/2016/12/parameter-io-issues.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/01/store-and-restore-occurrence-position.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/02/connect-to-fusion-lifecycle-from-fusion-360-add-in.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/04/units-and-parameters-in-inventor.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/06/getting-the-overall-size-of-parts.html',
            # 'https://modthemachine.typepad.com/my_weblog/2017/06/use-chromiumwebbrowser-from-inventor.html',
            # 'https://modthemachine.typepad.com/my_weblog/2018/10/troubleshooting-debugging.html',
            # 'https://modthemachine.typepad.com/my_weblog/2018/12/prepare-add-in-for-ui-preview.html',
            # 'https://modthemachine.typepad.com/my_weblog/2019/03/accessing-iproperties.html',
            # 'https://modthemachine.typepad.com/my_weblog/2019/03/automate-creation-of-named-geometry.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    # allowed_domains = ['https://modthemachine.typepad.com/']
    start_urls = ['https://modthemachine.typepad.com//my_weblog'] #//2019//03//automate-creation-of-named-geometry.html']
    #works but only for recent posts:
    # def parse(self, response):
    #     #Extracting the content using css selectors
    #     yield {
    #         'created_at' : response.css('.date-header::text').extract(),
    #         'footers' : ", ".join(a.strip() for a in response.css('.post-footers a::text').extract()),
    #         'title' : response.css('.entry-header::text').extract(),
    #         'codeSample' : response.css('pre::text').extract(),
    #     }
    #common theme for both posts below is background is set to #eeeeee
#xpath from this 2009 post: https://modthemachine.typepad.com/my_weblog/2009/02/setting-the-weight-for-ipart-members.html/
# //*[@id="entry-62662269"]/div/div[1]/div/div[1] & //*[@id="entry-62662269"]/div/div[1]/div/div[2]

#xpath from this 2013 post: https://modthemachine.typepad.com/my_weblog/2012/05/creating-geometric-constraints-in-a-sketch.html
# //*[@id="entry-6a00e553fcbfc688340163057bb06a970d"]/div/div[1]/div/p[11]
    def parse(self, response):
        #Extracting the content using css selectors
        yield {
            'created_at' : response.css('.date-header::text').extract(),
            'footers' : ", ".join(a.strip() for a in response.css('.post-footers a::text').extract()),
            'title' : response.css('.entry-header::text').extract(),
            'codeSample' : response.css('pre::text').extract(),
        }
