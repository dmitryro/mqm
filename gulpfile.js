var gulp = require('gulp'),
    autoprefixer = require('gulp-autoprefixer'),
    livereload = require('gulp-livereload'),
    sass = require('gulp-sass');


var paths = {
  scripts: ['static/js/**/*.js'],
  sass: ['static/sass/**/*.scss'],
  sassLibs: [],
  cssOutput: 'static/dist/css/',
  templates: ['templates/**/*.*'],
};


gulp.task('sass', function () {
    return gulp.src(paths.sass)
        .pipe(sass({
            includePaths: paths.sassLib
        }))
        .pipe(autoprefixer("last 1 version", "> 1%", "ie 8", "ie 7"))
        .pipe(gulp.dest(paths.cssOutput));
});


gulp.task('watch', ['sass'], function () {
    var server = livereload();

    var reloadPaths = []
        .concat([paths.cssOutput])
        .concat(paths.scripts)
        .concat(paths.templates);

    // Recompile SASS files when they have changed.
    gulp.watch(paths.sass, ['sass']);

    // Notify livereload server when files have changed.
    gulp.watch(reloadPaths).on('change', function(file) {
        server.changed(file.path);
    });
});


/*
 * Make a complete build.
 */
gulp.task('default', ['sass'], function () {

});
