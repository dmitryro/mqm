var gridster;
$(document).ready(function() {



	//Draggable Grid 


	// var $window = $(window);
    
 //    $window.resize(function() {
 //      var wwidth = $window.width();
 //      if (wwidth < 768) {
	//         for (var i = 0; i < gridster.$widgets.length; i++) {
 //          gridster.resize_widget($(gridster.$widgets[i]), 1, 1);
 //        }

 //          gridster.generate_grid_and_stylesheet();
 //      	}
 //    });

		


	
	var widget = '<li class="widget"><div class="widget-bar"></div></li>'
 	
	
	var widgets = [
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1],
		[widget, 1, 1]
	];

/*
	{"col":1,"row":1,"size_x":1,"size_y":1, "name":"collectiveimpact"},
	{"col":2,"row":1,"size_x":1,"size_y":1, "name":"areasofgrowth"},
*/

	var serialization = [
	{"col":1,"row":1,"size_x":1,"size_y":1, "name":"callout"}
	];
	

    gridster = $(".gridster > ul").gridster({
        widget_margins: [20, 20],
        widget_base_dimensions: [294, 300],
        widget_selector: 'li',
        avoid_overlapped_widgets: true,
        autogrow_cols: true,
        autogenerate_stylesheet: true,
        resize: {
        	enabled: true
      	}
    }).data('gridster');

    $.each(serialization, function() {
            gridster.add_widget($('.'+this.name).html(), this.size_x, this.size_y, this.col, this.row);
    });

    function makeGrid(state, gr) {

		if (state == 'opn') {

			var width = $(window).width() - 485;
			console.log('yo')

		} else {

			var width = $(window).width() - 40;

		}

		var cols = Math.floor((width - 120) / $('.widget').width());

		$('.gridster ul').css('width', width);

		console.log(cols)

		var colCounter = 1;
		var rowCounter = 1;

		//gridster.serialize();

		// gridster.options.min_cols = cols;
		

		for (var i = 0; i < $('.widget').length; i++){
			if (colCounter <= cols) {
				$('.widget').eq(i).attr('data-col', colCounter);
				colCounter = colCounter + 1;
			} else {
				$('.widget').eq(i).attr('data-col', 1);
				colCounter = 1;
				rowCounter = rowCounter + 1;
			}
			$('.widget').eq(i).attr('data-row', rowCounter);
		}

		var tooFar = $('.widget').filter(function () {
	  		return $(this).data('col') > cols;
		});

		$(tooFar).each(function () {
	  		$(this).attr('data-col', '1');
		});

		// gridster.serialize_changed();

		// gridster.generate_grid_and_stylesheet();

		// gridster.init()

		// for (var i = 0; i < gridster.$widgets.length; i++) {
  //   		gridster.resize_widget($(gridster.$widgets[i]), 1, 1);
		// }

	}

	//makeGrid('opn', gridster);

     //$('.widget').each(function(i, $('.widget')){
     //     gridster.apply(gridster, widget)
     // });

	// SIDEBAR TOGGLE


	var menuToggle;

	if($('.sidebar-colapse').length) {
		menuToggle = false;
	} else {
		menuToggle = true;
	}

	$('#sidebar-button').bind('click', function() {
		$("#sidebar").show();
		if(menuToggle == false) {
			menuToggle = true;
			$('#sidebar').removeClass('sidebar-colapse');
			$('#content').addClass('push');
			$(this).removeClass('closed');
			//makeGrid('opn', gridster);
		} else {
			menuToggle = false;
			$('#sidebar').addClass('sidebar-colapse');
			$('#content').removeClass('push');
			$(this).addClass('closed');
			$('head [generated-from="gridster"]:not(:last)').remove();
			//makeGrid('cls', gridster);
			
            
		}
	});

	// TOOLTIP 

	var tooltip = '<div class="s-tooltip"><div class="tt-arrow"></div><div class="tt-name"></div><div class="tt-text"></div></div>'

	$('.tt-icon').mouseenter(function(){
		var me = $(this);
		var ttText = $(this).parent().attr('data-tt');
		menuROver($(this).parent().find('.menu-button'));
		$('body').append(tooltip);
		$('.s-tooltip').css({'top': $(me).offset().top - (parseInt($('.s-tooltip').height()) / 2) - 8 + 'px', 'left': $(me).offset().left + 36 +'px'})
		$('.tt-text').html(ttText);
		$('.tt-name').html($(this).parent().find('.menu-name').html())
		$('.s-tooltip').stop().fadeIn(300);
	}).mouseleave(function(){
		menuROut($(this).parent().find('.menu-button'));
		$('.s-tooltip').stop().delay(100).fadeOut(300, function() {
			$('.tooltip').remove();
		});
	})

	// MENU

	$('.menu-button').mouseenter(function() {
		var iconName = $(this).attr('data-iconName');
		$(this).css('background-image','url(/static/assets/img/ui/icons/'+iconName+'_hover.svg)');
		$(this).parent().find('.tt-icon').css({'background-image':'url(/static//assets/img/ui/icons/info-hover.svg)', 'background-position':'center'});
	}).mouseleave(function() {
		var iconName = $(this).attr('data-iconName');
		$(this).css('background-image','url(/static//assets/img/ui/icons/'+iconName+'.svg)');
		$(this).parent().find('.tt-icon').css({'background-image':'url(/static//assets/img/ui/icons/info.svg)', 'background-position':'center'});
	});

	
	function menuROver(me) {
		var iconName = $(me).attr('data-iconName');
		$(me).addClass('goRed').css({'background-image':'url(/static//assets/img/ui/icons/'+iconName+'_hover.svg)', 'background-position':'center'})
	}

	function menuROut(me) {
		var iconName = $(me).attr('data-iconName');
		$(me).removeClass('goRed').css({'background-image':'url(/static//assets/img/ui/icons/'+iconName+'.svg)', 'background-position':'center'}).removeClass('goRed')
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

	//COLAPSE SIDEBAR DESCRIPTION

	$('#close-description').click(function() {
		// $('#description-wrap').animate({'height':'0px'}, 200, function() {
		// 	$(this).remove();
		// });
		$('#description-wrap').addClass('slideUp').delay(100).fadeOut(200);
		$(this).fadeOut(300);
	});

	

	//AUTO COMPLETE

	var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];
    $( "#search" ).autocomplete({
      source: availableTags
    });

    //HEIGHTS 
    
    if($('#video-content').length) {
    	if($('#video-content').height() < $('#sidebar').height()) {
    		$('#content').css('min-height',$('#sidebar').height() + 70)
    	}
    }

    if($('#content').length) {
    	if($('#content').height() < $('#sidebar').height()) {
    		$('#content').css('min-height',$('#sidebar').height() + 70)
    	}
    }

    // add widgets

    $('.menu-button').click(function() {
    	if ($(this).parent().attr('data-widg')) {
	    	var widgetName = $(this).parent().attr('data-widg');
	    	gridster.add_widget( $('.'+widgetName).html(), 1, 1, 1, 1 );
	    	if(widgetName == "fundingmap") {initializeFundingMap();}
	    	
	    	$('.drop').unbind('click');
	    	$('.drop').bind('click',function() {
				if ($(this).hasClass('dropped')) {
					$(this).parent().find('ul').css('display','none');
					$(this).removeClass('dropped');
				}else{
					$(this).parent().find('ul').css('display','block');
					$(this).addClass('dropped');
				}
			});
			$('.delete-node').bind('click');
			$('.delete-node').bind('click', function() {
		    	var widgetName = $(this).parent().parent().parent();
		    	gridster.remove_widget(widgetName);
		    });
    	}
    });

    // Delete Widgets

    $('.delete-node').bind('click', function() {
    	var widgetName = $(this).parent().parent().parent();
    	gridster.remove_widget(widgetName);
    });

});


















