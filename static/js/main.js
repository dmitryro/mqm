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























    });
})(jQuery);
