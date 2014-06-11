(function ($) {
    $(document).ready(function () {
        $('.add-another').addanother();



/* Ismail */

$("#action_addNewVideo").click(function(e){
	$('#myModal').modal();
	

});

$('body').on("click", ".action_addNew", function(e){
	//global for dashboard
	// get type from button -> load remote URL in modal window
	var type = $(this).attr('data-type');
	if(type != "") {
		$("#sharedModal").modal({
			remote: "/_add" + type + "/"
		});
	}
	
	//$(".widget-bar ul").hide(); //you want to hide the dropdown menu here
});

$('body').on('hidden.bs.modal', '.modal', function () {
    $(this).removeData('bs.modal'); //very important so that new modals are loaded
});

/* End of Ismail*/

if($('#video-content').length) {
    	if($('#video-content').height() < $('#sidebar').height()) {
    		$('#content').css('min-height',$('#sidebar').height() + 70)
    	}
    }

    if($('#content').length) {
    	if($('#content').height() < $(window).height()) {
    		$('#content').css('min-height',$(window).height())
    	}
    }



    // DROP DOWNS 

    $('.drop').bind('click',function() {
        if ($(this).hasClass('dropped')) {
            $(this).parent().find('ul').css('display','none');
            $(this).removeClass('dropped');
        }else{
            $(this).parent().find('ul').css('display','block');
            $(this).addClass('dropped');
        }
    });

    //POP UP

    $('#write').click(function() {
        $('.overlay').fadeIn(400);
    });

    $('.overlay-close').bind('click', function() {
        overlayClose();
    });

    $('.pop-up-close').bind('click', function() {
        overlayClose();
    });

    function overlayClose() {
        $('.overlay').fadeOut(400);
    }
















    });
})(jQuery);
