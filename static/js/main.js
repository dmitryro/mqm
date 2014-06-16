(function ($) {
    $(document).ready(function () {

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


        // Label tooltips
        $("label[data-content], .titlePopOver").popover({
            trigger: "hover"
        });

        /* Ismail */

        $("#action_addNewVideo").click(function (e) {
            $('#myModal').modal();


        });

        var openModal = function ($element) {
            $element.modal({

            });
        };

        $('body').on("click", ".action_addNew", function (e) {
            e.preventDefault();

            var modalSelector = $(this).attr('data-target');
            var $modalContent = $(modalSelector);

            openModal($modalContent);

            //$(".widget-bar ul").hide(); //you want to hide the dropdown menu here
        });

        // Open up modals on load if they have the ``data-open`` attribute.
        $('body').find('.action_addNew[data-open]').each(function () {
            var $that = $(this);
            $($that.attr('data-target')).modal({

            });
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
