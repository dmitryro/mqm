define(['jquery', 'ajaxify-html5'], function ($, __) {
    var navigation = {
        leaveAnimation: 'fadeout',
        enterAnimation: 'fadein',
        animations: {
            _animations: [],
            get: function (name) {
                return this._animations[name];
            },
            call: function (name, $content, callback) {
                this.get(name)($content, callback);
            },
            register: function (name, animation) {
                this._animations[name] = animation;
            }
        }
    };

    // hook into ajaxify to make animations work
    $(window).bind('ajaxify-leave', function (event, data) {
        var animation = data.$dataBody.data('leave-animation') || navigation.leaveAnimation;
        navigation.animations.call(animation, data.$content, data.callback);
    });

    $(window).bind('ajaxify-enter', function (event, data) {
        var animation = data.$dataBody.data('enter-animation') || navigation.enterAnimation;
        navigation.animations.call(animation, data.$content, data.callback);
    });

    // animations!

    navigation.animations.register('hide', function ($content, callback) {
        $content.animate({opacity: 0}, 0, callback);
    });

    navigation.animations.register('show', function ($content, callback) {
        $content.animate({opacity: 1}, 0, callback);
    });

    navigation.animations.register('fadeout', function ($content, callback) {
        $content.animate({opacity: 0}, 800, callback);
    });

    navigation.animations.register('fadein', function ($content, callback) {
        $content.animate({opacity: 1}, 800, callback);
    });

    // init ajaxify
    $(document).ready(function () {
        $('body').ajaxify();
    });

    return navigation;
});

