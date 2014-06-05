(function ($) {

    var replacePrefix = function (element, attrName, newValue) {
        $(element).attr(attrName, function (index, value) {
            return value.replace(/__prefix__/, newValue);
        });
    };

    $.fn.addanother = function () {
        return $(this).each(function () {
            var self = $(this);

            $(this).click(function () {
                var destination = self.attr('data-destination');
                var formset = self.parents('[data-formset-prefix]');
                var templateSelector = formset.attr('data-template') || '.template';
                var prefix = formset.attr('data-formset-prefix');

                var template = formset.find(templateSelector).clone(),
                    totalForms = $('#id_' + prefix + '-TOTAL_FORMS');

                template.removeClass('template');
                template.find(':input').each(function () {
                    replacePrefix(this, 'name', totalForms.val());
                    replacePrefix(this, 'id', totalForms.val());
                });
                template.find('label').each(function () {
                    replacePrefix(this, 'for', totalForms.val());
                });

                totalForms.val(function (index, val) {
                    return parseInt(val) + 1;
                });

                template.find('.form-counter').text(totalForms.val());

                self.before(template);
            });

            return this;
        });
    };

})(jQuery);