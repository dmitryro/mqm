define(['jquery', 'underscore'], function ($, _) {
    /*
     * implementation logic
     */

    var controllers = {},
        state = {
            _unload: [],
            onunload: function (func) {
                this._unload.push(func);
            }
        };

    var invokeController = function (name) {
        if (controllers[name] === undefined) {
            console.log('Error: Cannot find controller:', name);
            return;
        }

        var invoke = function (controller) { controller.call(state); };
        _.each(controllers[name], invoke);
    };

    var handleControllers = function () {
        var body_controllers = $('body').attr('data-controller');
        body_controllers = body_controllers.split(/\s+/);
        body_controllers = _.filter(body_controllers, function (name) { return !!name; });
        _.each(body_controllers, invokeController);
    };

    var unloadControllers = function () {
        if (state._unload) {
            $.each(state._unload, function (i, func) {
                func.call(state);
            });
            state._unload = [];
        }
    };

    var register = function (name, controller) {
        if (controllers[name] === undefined) {
            controllers[name] = [];
        }
        controllers[name].push(controller);
    };

    return {
        invoke: handleControllers,
        unload: unloadControllers,
        register: register
    };
});

