/*

=========================================================
* AppSeed - Simple SCSS compiler via Gulp
=========================================================

*/

var browserSync = require('browser-sync').create();
var cleanCss = require('gulp-clean-css');
var gulp = require('gulp');
const npmDist = require('gulp-npm-dist');
var wait = require('gulp-wait');
var sourcemaps = require('gulp-sourcemaps');
var rename = require("gulp-rename");

// Define COMMON paths

const paths = {
    src: {
        base: './',
        css: './css',
        scss: './scss',
        node_modules: './node_modules/',
        vendor: './vendor'
    }
};

// Minify CSS
gulp.task('minify:css', function() {
    return gulp.src([
            paths.src.css + '/styles.min.css'
        ])
        .pipe(cleanCss())
        .pipe(rename(function(path) {
            // Updates the object in-place
            path.extname = ".min.css";
        }))
        .pipe(gulp.dest(paths.src.css))
});

// Default Task: Compile SCSS and minify the result
gulp.task('default', gulp.series('scss', 'minify:css'));
