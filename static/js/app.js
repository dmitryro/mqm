define(['jquery', 'controller'], function ($, controller, gallery) {

// ==================================================================
// GLOBAL


    controller.register('page', function () {
        console.log('the "page" controller is executed on every page load.');
    });


// ==================================================================
// HOMEPAGE


    controller.register('homepage', function () {
        console.log('main loaded');
    });


// ==================================================================

});
