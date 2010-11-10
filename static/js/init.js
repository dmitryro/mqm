(function ($) {
    $(function() {

    });
})(jQuery);

// usage: log('inside coolFunc',this,arguments);
// http://paulirish.com/2009/log-a-lightweight-wrapper-for-consolelog/
window.log = function(){
    // store logs to an array for reference
    log.history = log.history || [];
    log.history.push(arguments);
    if(this.console){
        console.log( Array.prototype.slice.call(arguments) );
    }
};
