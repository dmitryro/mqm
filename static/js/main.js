requirejs.config({
    shim: {
        'ajaxify-html5': {
            deps: ['jquery', 'history']
        },
        'history': {
            deps: ['jquery']
        },
        'isotope': {
            deps: ['jquery']
        },
        'jquery': {
            exports: 'jQuery'
        },
        'modernizr': {
            exports: 'Modernizr'
        },
        'underscore': {
            exports: '_'
        }
    },
    paths: {
        history: 'libs/history.js/scripts/bundled-uncompressed/html4+html5/jquery.history',
        isotope: 'libs/jquery.isotope.min',
        jquery: 'libs/jquery/jquery',
        modernizr: 'libs/modernizr/modernizr',
        underscore: 'libs/underscore/underscore'
    }
});


requirejs([
    'modernizr',
    'jquery',
    'underscore',
    'app',
    'navigation',
    'controller'],
    function (
        Modernizr,
        $,
        _,
        app,
        navigation,
        controller) {

    $(document).ready(function () {
        controller.invoke();
    });

    // make controllers work with ajaxify as well
    $(window).bind('ajaxify-ready', function () {
        controller.invoke();
    });
    $(window).bind('ajaxify-leave', function () {
        controller.unload();
    });
});
