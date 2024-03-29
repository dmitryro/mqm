(function ($) {
    $(document).ready(function () {

        //Login tabs

        $("#loginTabs a").click(function(){
            $("#loginTabs a").each(function( index ) {
                $(this).removeClass("active");
            });

            $(this).addClass("active");
        });

        $('#settings-icon, #logout, #write, #add-icon').tooltip();

        //makes the dashboard switcher width correct
        $("#top-bar #person ul li").css("width", $("#search-bar").position().left-54);
        //might also need to do this on resize, probably...


        // DROP DOWNS
        $('body').on('click', '.drop', function () {
            if ($(this).hasClass('dropped')) {
                $(this).parent().find('ul').css('display', 'none');
                $(this).removeClass('dropped');
            } else {
                $(this).parent().find('ul').css('display', 'block');
                $(this).addClass('dropped');
            }
        });


        $('.add-another').addanother();

        // Init skills widgets.
        $('select[name=skill], select[name=skills], select[name$=-skills], select[name=categories]').addClass('chosen-select');

        // Make this global.
        window.initChosen = function ($element) {
            $element.find('.chosen-select').each(function () {
                if ($(this).next().hasClass('chosen-container')) {
                    $(this).next().remove();
                }
                $(this).chosen({
                    search_contains: true
                });
                $(this).next().css('width', $(this).parent().width() + 'px');
            });
        };

        window.initTextformat = function ($element) {
            $element.find('.textformat').each(function () {
                if ($(this).hasClass('markItUpEditor') === false) {
                    $(this).markItUp({
                        previewParserPath: '',
                        markupSet: [
                            {name:'Bold', key:'B', openWith:'[b]', closeWith:'[/b]'},
                            {name:'Italic', key:'I', openWith:'[i]', closeWith:'[/i]'},
                            {name:'Underline', key:'U', openWith:'[u]', closeWith:'[/u]'},
                            {name:'List', key:'R', openWith:'[ul]\n[li]', closeWith:'[/li]\n[/ul]'},
                            {name:'List item', key:'O', openWith:'[li]', closeWith:'[/li]'},
                            {name:'Link', key:'L', openWith:'[url=[![Url]!]]', closeWith:'[/url]', placeHolder:'Your text to link here …'}
                        ]
                    });
                }
            });
        };

        initChosen($('body'));
        initTextformat($('body'));


        // Label tooltips
        $("label[data-content], .titlePopOver").popover({
            trigger: "hover"
        });

        // Tasks do/undo

        $('.tasks-active, .tasks-completed').find('input[type=checkbox]').change(function () {
            var  url = '/todos/' + $(this).val() + '/';
            url += $(this).is(':checked') ? 'done/' : 'undone/';

            $.post(url, function (data) {
                window.location.href = window.location.href;
            });
        });

        // Instant submit forms, for example filter in call-out.
        $('body').on('change', '.instant-submit :input', function () {
            $(this).parents('form:first').submit();
        });

        /* Ismail */

        $("#action_addNewVideo").click(function (e) {
            $('#myModal').modal();
        });

        var openModal = function ($element) {
            $element.modal();

            $element.on('shown.bs.modal', function () {
                // Init document categories widget.
                initChosen($element);
                initTextformat($element);
            });
        };

        $('body').on("click", ".action_addNew", function (e) {
            e.preventDefault();

            var modalSelector = $(this).attr('data-target');
            var action = $(this).attr('data-action');
            var $modalContent = $(modalSelector);

            if (action) {
                $modalContent.find('form').attr('action', action);
            }

            openModal($modalContent);

            //$(".widget-bar ul").hide(); //you want to hide the dropdown menu here
        });

        // Open up modals on load if they have the ``data-open`` attribute.
        $('body').find('.action_addNew[data-open]').each(function () {
            var $that = $(this);
            openModal($($that.attr('data-target')));
        });

        $('body').find('.modal.auto-open').each(function () {
            openModal($(this));
        });

        $('body').on('hidden.bs.modal', '.modal', function () {
            $(this).removeData('bs.modal'); //very important so that new modals are loaded
        });

        /* End of Ismail*/

        if ($('#video-content').length) {
            if ($('#video-content').height() < $('#sidebar').height()) {
                $('#content').css('min-height', $('#sidebar').height() + 70)
            }
        }

        if ($('#content').length) {
            if ($('#content').height() < $(window).height()) {
                $('#content').css('min-height', $(window).height())
            }
        }





        //POP UP

        $('#write').click(function () {
            $('.overlay').fadeIn(400);
        });

        $('.overlay-close').bind('click', function () {
            overlayClose();
        });

        $('.pop-up-close').bind('click', function () {
            overlayClose();
        });

        function overlayClose() {
            $('.overlay').fadeOut(400);
        }

        $('body').on("click", ".smallIcon.openAccordion", function (e) {
            $(this).removeClass("openAccordion").addClass("closeAccordion");
        });


        $('body').on("click", ".smallIcon.closeAccordion", function (e) {
            $(this).removeClass("closeAccordion").addClass("openAccordion");
        });




    });
})(jQuery);
