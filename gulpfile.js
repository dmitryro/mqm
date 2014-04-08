var gulp = require('gulp'),
    autoprefixer = require('gulp-autoprefixer'),
    livereload = require('gulp-livereload'),
    sass = require('gulp-sass');


var paths = {
  scripts: ['static/app/**/*.js'],
  sass: ['static/styles/**/*.scss'],
  templates: ['templates/**/*.*'],
  partials: ['static/partials/**/*.html'],
  sassLib: ['static/libs/sass-bootstrap/lib'],
};


gulp.task('sass', function () {
    return gulp.src(paths.sass)
        .pipe(sass({
            includePaths: paths.sassLib
        }))
        .pipe(autoprefixer("last 1 version", "> 1%", "ie 8", "ie 7"))
        .pipe(gulp.dest('static/dist/styles/'));
});


gulp.task('watch', ['sass'], function () {
    var server = livereload();

    var all = []
        .concat(paths.scripts)
        .concat(paths.sass);

    // Recompile SASS files when they have changed.
    gulp.watch(paths.sass, ['sass']);

    // Notify livereload server when styles have changed.
    gulp.watch('static/dist/styles/**/*.*').on('change', function(file) {
        server.changed(file.path);
    });

    // Notify livereload server when scripts have changed.
    gulp.watch(paths.scripts).on('change', function(file) {
        server.changed(file.path);
    });

    // Notify livereload server when templates have changed.
    gulp.watch(paths.templates).on('change', function(file) {
        server.changed(file.path);
    });

    // Notify livereload server when partials have changed.
    gulp.watch(paths.partials).on('change', function(file) {
        server.changed(file.path);
    });
});


gulp.task('default', ['sass'], function(){

});
